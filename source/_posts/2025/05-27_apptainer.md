---
title: 使用Apptainer构建NequIP容器，并在DRAC上运行
permalink: post/82/
excerpt: <!-- -->
date: 2025-05-27 13:52:27
tags:
---

DRAC（前身computecanada）的运行节点不能联网，也没有sudo权限，想要在DRAC上编译/使用自定义的程序，或使用对环境有苛刻要求的程序，一个稍微省心的办法是通过容器，把程序运行所需的所有文件（代码、库、依赖、配置等）打包起来。

Docker是最常用的容器工具，但DRAC只支持Apptainer。

<br>

### 编译Apptainer

因为DRAC是Linux环境，所以我们也要在Linux环境下编译Apptainer。

Windows用户可以使用WSL（Windows Subsystem for Linux）进入Linux环境。如果没有安装WSL，可以参考[这个网页](https://docs.microsoft.com/zh-cn/windows/wsl/install)自行安装。

在Windows中打开PowerShell，输入以下命令以进入WSL环境：

```bash
wsl
```

如果看到了类似于`yourname@hostname:~$`的彩色提示符，说明已经进入了WSL环境。

Mac用户可以使用multipass等工具进入Linux环境。

<br>

然后，输入以下命令以编译Apptainer：

```bash
cd ~
sudo apt-get install -y build-essential uidmap squashfs-tools \
    libseccomp-dev pkg-config git wget cryptsetup

# 安装 Go 语言
wget https://go.dev/dl/go1.22.2.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.22.2.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# 编译 Apptainer
git clone https://github.com/apptainer/apptainer.git
cd apptainer
./mconfig --without-seccomp   # 去掉seccomp可避免编译失败
make -C builddir
sudo make -C builddir install
apptainer --version
```

如果最后一行命令输出了类似
```
apptainer version 1.4.1+165-g49bb538c5
```
说明Apptainer编译成功。

注：gpt-o3说WSL2默认禁用seccomp，所以使用apt安装的Apptainer无法运行，只能手动编译无seccomp的版本。此外，安装的版本也可能不支持fakeroot。但我没有亲自试过。

<br>

### 安装CUDA 11.8

NequIP需要CUDA 11.8。我们可以在WSL环境中安装CUDA 11.8，然后将其打包到容器中。此安装不会影响Windows系统中的CUDA。

首先先检测CUDA是否已安装：

```bash
nvidia-smi
```

如果报错`command not found`，则说明CUDA未安装。跳过下一步。

如果其输出了一个表格，且表格中CUDA版本号不是`11.8`，则需要先清理现有的CUDA：

```bash
# 清理现有的CUDA
sudo apt-get remove --purge 'cuda-*' 'libcudnn*' 'nvidia-cuda-toolkit' || true
sudo apt-get autoremove -y
```

接下来安装CUDA 11.8。

```bash
# 添加WSL专用仓库
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/7fa2af80.pub
echo "deb https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/ /" | sudo tee /etc/apt/sources.list.d/cuda-wsl.list
sudo apt-get update

# 安装CUDA 11.8
sudo apt-get install cuda-toolkit-11-8
/usr/local/cuda-11.8/bin/nvcc --version
```

如果最后一行命令输出11.8.x，说明CUDA 11.8安装成功。

<br>

### 构建NequIP容器

接下来，我们可以使用Apptainer构建NequIP容器。建议新建一个文件夹用于存放容器相关的文件。

新建一个名为`nequip.def`的文件，内容如下：

```bash
Bootstrap: docker
From: nvidia/cuda:11.8.0-runtime-ubuntu22.04

%labels
    Author      Tennisatw

%environment
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export PATH=/opt/python311/bin:$PATH
    export PYTHONUNBUFFERED=1
    export WANDB_ANONYMOUS=must

%post
    # Install tools and packages for compile python
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential wget curl git ca-certificates unzip \
        libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev libffi-dev \
        libncursesw5-dev libgdbm-dev liblzma-dev \
        python3-venv && \
    rm -rf /var/lib/apt/lists/*

    # Compile Python 3.11.12
    cd /tmp && \
    wget https://www.python.org/ftp/python/3.11.12/Python-3.11.12.tgz && \
    tar -xzf Python-3.11.12.tgz && \
    cd Python-3.11.12 && \
    ./configure --prefix=/opt/python311 --enable-optimizations && \
    make -j$(nproc) && make install && \
    cd /
    rm -rf /tmp/Python-3.11.12 /tmp/Python-3.11.12.tgz

    # Upgrade pip
    /opt/python311/bin/python3 -m ensurepip
    /opt/python311/bin/python3 -m pip install --upgrade pip
    # export PATH=/opt/python311/bin:$PATH
    
    # Install nequip, allegro, and torch
    # i.e., cp2k/colab/install_torch_cp2k_colab.sh
    /opt/python311/bin/pip install wandb
    /opt/python311/bin/pip install mkl mkl-include
    /opt/python311/bin/pip install --force-reinstall nequip==0.6 torch==1.13
    /opt/python311/bin/pip install --force-reinstall numpy==1.26.4
    /opt/python311/bin/pip install jupyter jupyter_contrib_nbextensions nglview
    # cloning allegro
    cd / && git clone --depth 1 https://github.com/mir-group/allegro.git
    # Force reinstall allegro
    echo "Reinstalling allegro..."
    /opt/python311/bin/pip install --force-reinstall allegro
    # downloading libtorch
    echo "Downloading libtorch..."
    cd / && wget https://download.pytorch.org/libtorch/cu118/libtorch-cxx11-abi-shared-with-deps-2.0.0%2Bcu118.zip -O libtorch.zip
    echo "Unzipping libtorch..."
    unzip /libtorch.zip -d /
    cd /libtorch/lib && ln -s libnvrtc-builtins-7237cb5d.so.11.7 libnvrtc-builtins.so.11.8

    # Clean pip cache
    /opt/python311/bin/pip cache purge

%runscript
    exec "$@"

%help
    Container with:
    - Python 3.11.12
    - NequIP
    - PyTorch 1.13.1 + cu118
    - NumPy 1.26.4
    Usage:
        apptainer exec --nv nequip.sif nequip-train nequip-water.yaml
```

`nequip.def`是Apptainer的定义文件，这其中%post部分的脚本会在容器构建时执行，包括安装Python、NequIP、Allegro和PyTorch等。%runscript部分定义了容器的默认运行命令。如果需要的话，可以添加%files部分可以添加额外的文件或目录到容器中。

然后，使用`cd`命令进入到存放`nequip.def`文件的目录，输入以下命令以构建容器：

```bash
apptainer build --fakeroot nequip.sif nequip.def
```

这行命令会构建一个名为`nequip.sif`的容器文件。`--fakeroot`选项允许在没有root权限的情况下构建容器，`--nv`选项启用NVIDIA GPU支持。

如果一切顺利，构建完成后会看到类似以下的输出：

```INFO:    Creating SIF file...
INFO:    Build complete: nequip.sif
```

### 在DRAC上运行容器

将构建好的`nequip.sif`文件上传到DRAC的工作目录中。

运行容器时，可以将nequip所需的yaml配置文件放在同一目录下，然后使用以下命令：

```bash
apptainer exec --nv nequip.sif nequip-train your-yaml-file.yaml
```

---

附录：Nequip官方给出的一个简单的yaml配置文件：

```yaml
# IMPORTANT: READ THIS

# This is a full yaml file with all nequip options.
# It is primarily intented to serve as documentation/reference for all options
# For a simpler yaml file containing all necessary features to get you started, we strongly recommend to start with configs/example.yaml

# Two folders will be used during the training: 'root'/process and 'root'/'run_name'
# run_name contains logfiles and saved models
# process contains processed data sets
# if 'root'/'run_name' exists, 'root'/'run_name'_'year'-'month'-'day'-'hour'-'min'-'s' will be used instead.
root: results
run_name: water-example
seed: 123 # model seed
dataset_seed: 456 # data set seed
append: true # set true if a restarted run should append to the previous log file
default_dtype: float32 # type of float to use, e.g. float32 and float64
allow_tf32: false # whether to use TensorFloat32 if it is available
# device:  cuda                                                                   # which device to use. Default: automatically detected cuda or "cpu"

# network
r_max: 4.9 # cutoff radius in length units, here Angstrom, this is an important hyperparamter to scan
num_layers: 3 # number of interaction blocks, we find 3-5 to work best

l_max: 1 # the maximum irrep order (rotation order) for the network's features, l=1 is a good default, l=2 is more accurate but slower
parity: true # whether to include features with odd mirror parityy; often turning parity off gives equally good results but faster networks, so do consider this
num_features: 32 # the multiplicity of the features, 32 is a good default for accurate network, if you want to be more accurate, go larger, if you want to be faster, go lower

# alternatively, the irreps of the features in various parts of the network can be specified directly:
# the following options use e3nn irreps notation
# either these four options, or the above three options, should be provided--- they cannot be mixed.
# chemical_embedding_irreps_out: 32x0e                                              # irreps for the chemical embedding of species
# feature_irreps_hidden: 32x0o + 32x0e + 32x1o + 32x1e                              # irreps used for hidden features, here we go up to lmax=1, with even and odd parities; for more accurate but slower networks, use l=2 or higher, smaller number of features is faster
# irreps_edge_sh: 0e + 1o                                                           # irreps of the spherical harmonics used for edges. If a single integer, indicates the full SH up to L_max=that_integer
# conv_to_output_hidden_irreps_out: 16x0e                                           # irreps used in hidden layer of output block

nonlinearity_type: gate # may be 'gate' or 'norm', 'gate' is recommended
resnet:
  false # set true to make interaction block a resnet-style update
  # the resnet update will only be applied when the input and output irreps of the layer are the same

# scalar nonlinearities to use — available options are silu, ssp (shifted softplus), tanh, and abs.
# Different nonlinearities are specified for e (even) and o (odd) parity;
# note that only tanh and abs are correct for o (odd parity).
# silu typically works best for even
nonlinearity_scalars:
  e: silu
  o: tanh

nonlinearity_gates:
  e: silu
  o: tanh

# radial network basis
num_basis: 8 # number of basis functions used in the radial basis, 8 usually works best
BesselBasis_trainable: true # set true to train the bessel weights
PolynomialCutoff_p: 6 # p-exponent used in polynomial cutoff function, smaller p corresponds to stronger decay with distance

# radial network
invariant_layers: 2 # number of radial layers, usually 1-3 works best, smaller is faster
invariant_neurons: 64 # number of hidden neurons in radial function, smaller is faster
avg_num_neighbors: auto # number of neighbors to divide by, null => no normalization, auto computes it based on dataset
use_sc: true # use self-connection or not, usually gives big improvement

# to specify different parameters for each convolutional layer, try examples below
# layer1_use_sc: true                                                             # use "layer{i}_" prefix to specify parameters for only one of the layer,
# priority for different definitions:
#   invariant_neurons < InteractionBlock_invariant_neurons < layer{i}_invariant_neurons

# data set
# there are two options to specify a dataset, npz or ase
# npz works with npz files, ase can ready any format that ase.io.read can read
# in most cases working with the ase option and an extxyz file is by far the simplest way to do it and we strongly recommend using this
# simply provide a single extxyz file that contains the structures together with energies and forces (generated with ase.io.write(atoms, format='extxyz', append=True))

include_keys:
  - user_label
key_mapping:
  user_label: label0

# alternatively, you can read directly from a VASP OUTCAR file (this will only read that single OUTCAR)
# # for VASP OUTCAR, the yaml input should be
# dataset: ase
# dataset_file_name: OUTCAR
# ase_args:
#   format: vasp-out
# important VASP note: the ase vasp parser stores the potential energy to "free_energy" instead of "energy".
# Here, the key_mapping maps the external name (key) to the NequIP default name (value)
# key_mapping:
#   free_energy: total_energy

# npz example
# the keys used need to be stated at least once in key_mapping, npz_fixed_field_keys or include_keys
# key_mapping is used to map the key in the npz file to the NequIP default values (see data/_key.py)
# all arrays are expected to have the shape of (nframe, natom, ?) except the fixed fields
# note that if your data set uses pbc, you need to also pass an array that maps to the nequip "pbc" key
# dataset: npz                                                                       # type of data set, can be npz or ase
# dataset_url: http://quantum-machine.org/gdml/data/npz/toluene_ccsd_t.zip           # url to download the npz. optional
# dataset_file_name: ./benchmark_data/toluene_ccsd_t-train.npz                       # path to data set file
# key_mapping:
#   z: atomic_numbers                                                                # atomic species, integers
#   E: total_energy                                                                  # total potential eneriges to train to
#   F: forces                                                                        # atomic forces to train to
#   R: pos                                                                           # raw atomic positions
# npz_fixed_field_keys:                                                              # fields that are repeated across different examples
#   - atomic_numbers

# A list of chemical species found in the data. The NequIP atom types will be named after the chemical symbols and ordered by atomic number in ascending order.
# (In this case, NequIP's internal atom type 0 will be named H and type 1 will be named C.)
# Atoms in the input will be assigned NequIP atom types according to their atomic numbers.
chemical_symbols:
  - H
  - O

# Alternatively, you may explicitly specify which chemical species in the input will map to NequIP atom type 0, which to atom type 1, and so on.
# Other than providing an explicit order for the NequIP atom types, this option behaves the same as `chemical_symbols`
# chemical_symbol_to_type:
#   H: 0
#   C: 1

# Alternatively, if the dataset has type indices, you may give the names for the types in order:
# (this also sets the number of types)
# type_names:
#   - my_type
#   - atom
#   - thing

# As an alternative option to npz, you can also pass data ase ASE Atoms-objects
# This can often be easier to work with, simply make sure the ASE Atoms object
# has a calculator for which atoms.get_potential_energy() and atoms.get_forces() are defined
dataset: ase
dataset_file_name: AIMD_data/conc_wat_pos_frc.extxyz # need to be a format accepted by ase.io.read
ase_args: # any arguments needed by ase.io.read
  format: extxyz

# If you want to use a different dataset for validation, you can specify
# the same types of options using a `validation_` prefix:
# validation_dataset: ase
# validation_dataset_file_name: xxx.xyz                                            # need to be a format accepted by ase.io.read

# logging
#wandb: true # we recommend using wandb for logging
#wandb_project: water-example # project name used in wandb
#wandb_watch: false

# see https://docs.wandb.ai/ref/python/watch
# wandb_watch_kwargs:
#   log: all
#   log_freq: 1
#   log_graph: true

verbose: info # the same as python logging, e.g. warning, info, debug, error. case insensitive
log_batch_freq: 1 # batch frequency, how often to print training errors withinin the same epoch
log_epoch_freq: 1 # epoch frequency, how often to print
save_checkpoint_freq: -1 # frequency to save the intermediate checkpoint. no saving of intermediate checkpoints when the value is not positive.
save_ema_checkpoint_freq: -1 # frequency to save the intermediate ema checkpoint. no saving of intermediate checkpoints when the value is not positive.

# training
n_train: 100 # number of training data
n_val: 50 # number of validation data
learning_rate: 0.005 # learning rate, we found values between 0.01 and 0.005 to work best - this is often one of the most important hyperparameters to tune
batch_size: 5 # batch size, we found it important to keep this small for most applications including forces (1-5); for energy-only training, higher batch sizes work better
validation_batch_size: 10 # batch size for evaluating the model during validation. This does not affect the training results, but using the highest value possible (<=n_val) without running out of memory will speed up your training.
max_epochs: 100000 # stop training after _ number of epochs, we set a very large number here, it won't take this long in practice and we will use early stopping instead
train_val_split: random # can be random or sequential. if sequential, first n_train elements are training, next n_val are val, else random, usually random is the right choice
shuffle: true # If true, the data loader will shuffle the data, usually a good idea
metrics_key: validation_loss # metrics used for scheduling and saving best model. Options: `set`_`quantity`, set can be either "train" or "validation, "quantity" can be loss or anything that appears in the validation batch step header, such as f_mae, f_rmse, e_mae, e_rmse
use_ema: true # if true, use exponential moving average on weights for val/test, usually helps a lot with training, in particular for energy errors
ema_decay: 0.99 # ema weight, typically set to 0.99 or 0.999
ema_use_num_updates: true # whether to use number of updates when computing averages
report_init_validation: true # if True, report the validation error for just initialized model

# early stopping based on metrics values.
# LR, wall and any keys printed in the log file can be used.
# The key can start with Training or validation. If not defined, the validation value will be used.
early_stopping_patiences: # stop early if a metric value stopped decreasing for n epochs
  validation_loss: 50

early_stopping_delta: # If delta is defined, a decrease smaller than delta will not be considered as a decrease
  validation_loss: 0.005

early_stopping_cumulative_delta: false # If True, the minimum value recorded will not be updated when the decrease is smaller than delta

early_stopping_lower_bounds: # stop early if a metric value is lower than the bound
  LR: 1.0e-5

early_stopping_upper_bounds: # stop early if a metric value is higher than the bound
  cumulative_wall: 1.0e+100

# loss function
loss_coeffs: # different weights to use in a weighted loss functions
  forces: 1 # if using PerAtomMSELoss, a default weight of 1:1 on each should work well
  total_energy:
    - 1
    - PerAtomMSELoss

# # default loss function is MSELoss, the name has to be exactly the same as those in torch.nn.
# the only supprted targets are forces and total_energy

# here are some example of more ways to declare different types of loss functions, depending on your application:
# loss_coeffs:
#   total_energy: MSELoss
#
# loss_coeffs:
#   total_energy:
#   - 3.0
#   - MSELoss
#
# loss_coeffs:
#   total_energy:
#   - 1.0
#   - PerAtomMSELoss
#
# loss_coeffs:
#   forces:
#   - 1.0
#   - PerSpeciesL1Loss
#
# loss_coeffs: total_energy
#
# loss_coeffs:
#   total_energy:
#   - 3.0
#   - L1Loss
#   forces: 1.0

# output metrics
metrics_components:
  - - forces # key
    - mae # "rmse" or "mae"
  - - forces
    - rmse
  - - forces
    - mae
    - PerSpecies: True # if true, per species contribution is counted separately
      report_per_component: False # if true, statistics on each component (i.e. fx, fy, fz) will be counted separately
  - - forces
    - rmse
    - PerSpecies: True
      report_per_component: False
  - - total_energy
    - mae
  - - total_energy
    - mae
    - PerAtom: True # if true, energy is normalized by the number of atoms

# optimizer, may be any optimizer defined in torch.optim
# the name `optimizer_name`is case sensitive
optimizer_name: Adam # default optimizer is Adam
optimizer_amsgrad: false
optimizer_betas: !!python/tuple
  - 0.9
  - 0.999
optimizer_eps: 1.0e-08
optimizer_weight_decay: 0

# gradient clipping using torch.nn.utils.clip_grad_norm_
# see https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_
# setting to inf or null disables it
max_gradient_norm: null

# lr scheduler, currently only supports the two options listed below, if you need more please file an issue
# first: on-plateau, reduce lr by factory of lr_scheduler_factor if metrics_key hasn't improved for lr_scheduler_patience epoch
lr_scheduler_name: ReduceLROnPlateau
lr_scheduler_patience: 100
lr_scheduler_factor: 0.5

# second, cosine annealing with warm restart
# lr_scheduler_name: CosineAnnealingWarmRestarts
# lr_scheduler_T_0: 10000
# lr_scheduler_T_mult: 2
# lr_scheduler_eta_min: 0
# lr_scheduler_last_epoch: -1

# we provide a series of options to shift and scale the data
# these are for advanced use and usually the defaults work very well
# the default is to scale the energies and forces by scaling them by the force standard deviation and to shift the energy by its mean
# in certain cases, it can be useful to have a trainable shift/scale and to also have species-dependent shifts/scales for each atom

per_species_rescale_scales_trainable: false
# whether the scales are trainable. Defaults to False. Optional
per_species_rescale_shifts_trainable: false
# whether the shifts are trainable. Defaults to False. Optional
per_species_rescale_shifts: dataset_per_atom_total_energy_mean
# initial atomic energy shift for each species. default to the mean of per atom energy. Optional
# the value can be a constant float value, an array for each species, or a string
# string option include:
# *  "dataset_per_atom_total_energy_mean", which computes the per atom average
# *  "dataset_per_species_total_energy_mean", which automatically compute the per atom energy mean using a GP model
per_species_rescale_scales: dataset_forces_rms
# initial atomic energy scale for each species. Optional.
# the value can be a constant float value, an array for each species, or a string
# string option include:
# *  "dataset_per_atom_total_energy_std", which computes the per atom energy std
# *  "dataset_per_species_total_energy_std", which uses the GP model uncertainty
# *  "dataset_per_species_forces_rms", which compute the force rms for each species
# If not provided, defaults to dataset_per_species_force_rms or dataset_per_atom_total_energy_std, depending on whether forces are being trained.
# per_species_rescale_kwargs:
#   total_energy:
#     alpha: 0.1
#     max_iteration: 20
#     stride: 100
# keywords for GP decomposition of per specie energy. Optional. Defaults to 0.1
# per_species_rescale_arguments_in_dataset_units: True
# if explicit numbers are given for the shifts/scales, this parameter must specify whether the given numbers are unitless shifts/scales or are in the units of the dataset. If ``True``, any global rescalings will correctly be applied to the per-species values.

# global energy shift and scale
# When "dataset_total_energy_mean", the mean energy of the dataset. When None, disables the global shift. When a number, used directly.
# Warning: if this value is not None, the model is no longer size extensive
#global_rescale_shift: null

# global energy scale. When "dataset_force_rms", the RMS of force components in the dataset. When "dataset_total_energy_std", the stdev of energies in the dataset. When null, disables the global scale. When a number, used directly.
# If not provided, defaults to either dataset_force_rms or dataset_total_energy_std, depending on whether forces are being trained.
#global_rescale_scale: dataset_forces_rms

# whether the shift of the final global energy rescaling should be trainable
#global_rescale_shift_trainable: false

# whether the scale of the final global energy rescaling should be trainable
# global_rescale_scale_trainable: false
# # full block needed for per specie rescale
# global_rescale_shift: null
# global_rescale_shift_trainable: false
# global_rescale_scale: dataset_forces_rms
# global_rescale_scale_trainable: false
# per_species_rescale_trainable: true
# per_species_rescale_shifts: dataset_per_atom_total_energy_mean
# per_species_rescale_scales: dataset_per_atom_total_energy_std

# # full block needed for global rescale
# global_rescale_shift: dataset_total_energy_mean
# global_rescale_shift_trainable: false
# global_rescale_scale: dataset_forces_rms
# global_rescale_scale_trainable: false
# per_species_rescale_trainable: false
# per_species_rescale_shifts: null
# per_species_rescale_scales: null

# Options for e3nn's set_optimization_defaults. A dict:
# e3nn_optimization_defaults:
#   explicit_backward: True

global_rescale_shift: null
global_rescale_shift_trainable: false
global_rescale_scale: dataset_forces_rms
global_rescale_scale_trainable: false
per_species_rescale_shifts_trainable: false
per_species_rescale_scales_trainable: true
per_species_rescale_shifts: dataset_per_species_total_energy_mean
per_species_rescale_scales: dataset_per_species_forces_rms
```