#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1

#SBATCH --mem-per-cpu=3500mb
#SBATCH --time=24:00:00

#SBATCH --account=xxx
#SBATCH --mail-user=<xxx>
#SBATCH --mail-type=ALL

echo $(date +"%Y-%m-%d %H:%M:%S"); echo; cat "$0"; echo

module load StdEnv/2023  gcc/12.3
module load crest/3.0.1

crest L-Phenylalanine.xyz --gfn2 --gbsa h2o -T 4

echo $(date +"%Y-%m-%d %H:%M:%S")