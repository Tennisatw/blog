---
title: 使用R语言分析各国的新冠死亡率 - Analyzing COVID-19 Mortality Rates Among Countries Using R
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 编程
  - 随想
excerpt: ''
date: 2024-03-27 21:31:00
---

<!-- more -->
约翰霍普金斯大学有新冠期间的确诊人数和死亡人数的数据文件。利用这些文件，可以分析各国的新冠死亡率。

Johns Hopkins University provides data files on confirmed cases and deaths during the COVID-19 pandemic. Using these files, one can analyze the COVID-19 mortality rates of different countries.

[https://github.com/CSSEGISandData/COVID-19/tree/master/csse\_covid\_19\_data/csse\_covid\_19\_time\_series](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series)

  

首先，下载csv文件，并读取数据。一共有4个文件，美国的确诊和死亡人数，以及其他国家的确诊和死亡人数。

First, download the CSV files and load the data. There are four files: confirmed and death cases in the USA, and confirmed and death cases in other countries.

\`\`\`
us\_conf\_raw <- read.csv("covid\_19/time\_series\_covid19\_confirmed\_US.csv")
us\_death\_raw <- read.csv("covid\_19/time\_series\_covid19\_deaths\_US.csv")
global\_conf\_raw <- read.csv("covid\_19/time\_series\_covid19\_confirmed\_global.csv")
global\_death\_raw <- read.csv("covid\_19/time\_series\_covid19\_deaths\_global.csv")
\`\`\`

  

从数据中读取日期信息。

Extract the date information from the data.

\`\`\`
dates <- us\_conf\_raw %>%
    select(-c(UID, iso2, iso3, code3, FIPS, Admin2, Country\_Region, 
    Province\_State, Lat, Long\_, Combined\_Key)) %>%
    colnames() %>%
    as.Date(format = "X%m.%d.%y")
\`\`\`

  

读取美国的确诊人数，使用select方法选择需要的列，然后将各个郡的确诊人数相加。死亡人数的读取方法与之相同。

For the USA, read the number of confirmed cases, use the select method to choose the necessary columns, then sum the confirmed cases across counties. Follow the same method to read the number of deaths.

\`\`\`
us\_conf <- us\_conf\_raw %>%
    select(-c(UID, iso2, iso3, code3, FIPS, Admin2, Country\_Region, 
    Province\_State, Lat, Long\_, Combined\_Key)) %>%
    colSums() %>%
    as.vector()
\`\`\`

  

读取其他国家的确诊人数，使用filter选取感兴趣的行。死亡人数的读取方法与之相同。这里选择了3个国家：中国，日本，和加拿大。

For other countries, read the number of confirmed cases, using the filter to select the rows of interest. The method for reading the number of deaths is the same. Three countries were chosen for this analysis: China, Japan, and Canada.

\`\`\`
global\_conf <- global\_conf\_raw %>%
    select(-c(Province.State, Lat, Long)) %>%
    filter(Country.Region %in% c("China", "Japan", "Canada"))

china\_conf <- global\_conf %>%
    filter(Country.Region == "China") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()
\`\`\`

  

把所有的数据都储存在一个data.frame中。由于美国的数据的前10天的死亡率过高，所以从11天开始。

Store all the data in a data.frame. Since the mortality rate in the USA was abnormally high in the first 10 days, the analysis starts from day 11.

\`\`\`
data <- data.frame(
    dates = dates\[11:length(dates)\],
    us\_death = us\_death\[11:length(us\_death)\],
    us\_conf = us\_conf\[11:length(us\_conf)\],
    china\_death = china\_death\[11:length(china\_death)\],
    china\_conf = china\_conf\[11:length(china\_conf)\],
    japan\_death = japan\_death\[11:length(japan\_death)\],
    japan\_conf = japan\_conf\[11:length(japan\_conf)\],
    canada\_death = canada\_death\[11:length(canada\_death)\],
    canada\_conf = canada\_conf\[11:length(canada\_conf)\]
)
\`\`\`

  

画图

Plotting the Data

\`\`\`
graph\_death\_rate <- ggplot(data) +
    geom\_line(aes(x = dates, y = us\_death / us\_conf), color = "black") +
    geom\_line(aes(x = dates, y = china\_death / china\_conf), color = "red") +
    geom\_line(aes(x = dates, y = japan\_death / japan\_conf), color = "blue") +
    geom\_line(aes(x = dates, y = canada\_death / canada\_conf), color = "green") + 
    scale\_y\_continuous(labels = scales::percent) +
    labs(y = "Death rate", x = "Date", title = "Death rate of COVID-19") +

print(graph\_death\_rate)
\`\`\`

  

最后得到的图像如下。黑色代表美国，红色代表中国，蓝色为日本，绿色为加拿大。

The resulting graph is as follows. Black represents the USA, red for China, blue for Japan, and green for Canada.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjY0eXwnXLwKKGQCrFA1qh2CZzSCkMF2dmxD2eSVtNcB_cUUB80F51CxgAw-7qxx3mLMmTHo9LErNZ-_BZhUy2GrrgOvuu4UHQjGrvdvHayNgvgRwHg3V8jBP96V3HhgG5w0Yp27WUHTr1gFP0tOZe4jIrPsv3CKPGtfk-VMKETwj0iWU-cXx6lEN9XwNU=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjY0eXwnXLwKKGQCrFA1qh2CZzSCkMF2dmxD2eSVtNcB_cUUB80F51CxgAw-7qxx3mLMmTHo9LErNZ-_BZhUy2GrrgOvuu4UHQjGrvdvHayNgvgRwHg3V8jBP96V3HhgG5w0Yp27WUHTr1gFP0tOZe4jIrPsv3CKPGtfk-VMKETwj0iWU-cXx6lEN9XwNU)

  

完整版的代码如下：

The full code is as follows:

\`\`\`
library(dplyr)
library(ggplot2)
library(tidyr)

# 读取数据 - Read data
us\_conf\_raw <- read.csv("covid\_19/time\_series\_covid19\_confirmed\_US.csv")
us\_death\_raw <- read.csv("covid\_19/time\_series\_covid19\_deaths\_US.csv")
global\_conf\_raw <- read.csv("covid\_19/time\_series\_covid19\_confirmed\_global.csv")
global\_death\_raw <- read.csv("covid\_19/time\_series\_covid19\_deaths\_global.csv")

# 读取日期信息 - Read date information
dates <- us\_conf\_raw %>%
    select(-c(UID, iso2, iso3, code3, FIPS, Admin2, Country\_Region, 
    Province\_State, Lat, Long\_, Combined\_Key)) %>%
    colnames() %>%
    as.Date(format = "X%m.%d.%y")

# 美国确诊数据 - US confirmed data
us\_conf <- us\_conf\_raw %>%
    select(-c(UID, iso2, iso3, code3, FIPS, Admin2, Country\_Region, 
    Province\_State, Lat, Long\_, Combined\_Key)) %>%
    colSums() %>%
    as.vector()

# 美国死亡数据 - US death data
us\_death <- us\_death\_raw %>%
    select(-c(UID, iso2, iso3, code3, FIPS, Admin2, Country\_Region, 
    Province\_State, Lat, Long\_, Combined\_Key, Population)) %>%
    colSums() %>%
    as.vector()

# 全球确诊数据 - Global confirmed data
global\_conf <- global\_conf\_raw %>%
    select(-c(Province.State, Lat, Long)) %>%
    filter(Country.Region %in% c("China", "Japan", "Canada"))

# 全球死亡数据 - Global death data
global\_death <- global\_death\_raw %>%
    select(-c(Province.State, Lat, Long)) %>%
    filter(Country.Region %in% c("China", "Japan", "Canada"))

# 中国确诊数据 - China confirmed data
china\_conf <- global\_conf %>%
    filter(Country.Region == "China") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()

# 中国死亡数据 - China death data
china\_death <- global\_death %>%
    filter(Country.Region == "China") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()

# 日本确诊数据 - Japan confirmed data
japan\_conf <- global\_conf %>%
    filter(Country.Region == "Japan") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()

# 日本死亡数据 - Japan death data
japan\_death <- global\_death %>%
    filter(Country.Region == "Japan") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()

# 加拿大确诊数据 - Canada confirmed data
canada\_conf <- global\_conf %>%
    filter(Country.Region == "Canada") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()

# 加拿大死亡数据 - Canada death data
canada\_death <- global\_death %>%
    filter(Country.Region == "Canada") %>%
    select(-Country.Region) %>%
    colSums() %>%
    as.vector()

# 整理数据 - Organize data
data <- data.frame(
    dates = dates\[11:length(dates)\],
    us\_death = us\_death\[11:length(us\_death)\],
    us\_conf = us\_conf\[11:length(us\_conf)\],
    china\_death = china\_death\[11:length(china\_death)\],
    china\_conf = china\_conf\[11:length(china\_conf)\],
    japan\_death = japan\_death\[11:length(japan\_death)\],
    japan\_conf = japan\_conf\[11:length(japan\_conf)\],
    canada\_death = canada\_death\[11:length(canada\_death)\],
    canada\_conf = canada\_conf\[11:length(canada\_conf)\]
)

# 画图 - Plot
# 确诊人数 - Confirmed cases
graph\_conf <- ggplot(data) +
    geom\_line(aes(x = dates, y = us\_conf), color = "black") +
    geom\_line(aes(x = dates, y = china\_conf), color = "red") +
    geom\_line(aes(x = dates, y = japan\_conf), color = "blue") +
    geom\_line(aes(x = dates, y = canada\_conf), color = "green")

# 死亡人数 - Death cases
graph\_death <- ggplot(data) +
    geom\_line(aes(x = dates, y = us\_death), color = "black") +
    geom\_line(aes(x = dates, y = china\_death), color = "red") +
    geom\_line(aes(x = dates, y = japan\_death), color = "blue") +
    geom\_line(aes(x = dates, y = canada\_death), color = "green")

# 死亡率 - Death rate
# 添加图例 - Add legend
graph\_death\_rate <- ggplot(data) +
    geom\_line(aes(x = dates, y = us\_death / us\_conf), color = "black") +
    geom\_line(aes(x = dates, y = china\_death / china\_conf), color = "red") +
    geom\_line(aes(x = dates, y = japan\_death / japan\_conf), color = "blue") +
    geom\_line(aes(x = dates, y = canada\_death / canada\_conf), color = "green") + 
    scale\_y\_continuous(labels = scales::percent) +
    labs(y = "Death rate", x = "Date", title = "Death rate of COVID-19") +

print(graph\_death\_rate)
\`\`\`

  

我感觉R比起python来，至少有2大优点：

I feel that R has at least two major advantages over Python:

  

R的很多数据结构和功能都是原生的，比如data.frame，或是vector。相比之下，虽然Python也有类似的结构，但是需要导入其他的包才能获得。

Many of R's data structures and functions are native, such as data.frame and vector. In contrast, although Python has similar structures, they require importing additional packages to be accessed.

  

R不需要配置复杂的环境变量，只需要下载一个软件，相比之下，python的环境的配置方法能直接劝退初学者，我现在都数不清我电脑里有多少python.exe。此外，R在包管理和环境配置上非常的舒服。python想要安装一个包时（如果不通过ipynb的魔法命令的话），只能离开编程界面，去控制台输入pip install ... ，而R不需要去控制台输入rir install，直接在编程界面中使用 install.packages("...") 就可以了。这一点真是大大的舒服。

R does not require complex environment variable configuration. One just needs to download the software. In comparison, the method of configuring Python's environment can be daunting for beginners; I've lost count of how many python.exe files I have on my computer. Moreover, R is very user-friendly in terms of package management and environment configuration. In Python, to install a package (if not using the magic commands in ipynb), one has to leave the programming interface and enter "pip install ..." in the console, while in R, one can simply use install.packages("...") directly in the programming interface rather than using "rir install ...". This is a significant convenience.

  

但与此同时，R也有很多缺点，其中有一些我实在是难以忍受：

However, R also has several drawbacks, some of which I find quite intolerable:

  

R的函数命名有点混乱，比如将矩阵（matrix）转换成数据框（tibble）使用as\_tibble函数，但反过来就使用as.matrix函数。

R's function naming can be confusing; for example, converting a matrix to a data frame (tibble) uses the as\_tibble function, but the reverse uses the as.matrix function.

\`\`\`
m <- as.matrix(df)
print(m)

df <- as\_tibble(m)
print(df)
\`\`\`

R的一些函数的格式有时显得莫名奇妙，比如where函数仅在select函数内才有意义等等。

The syntax of some R functions can sometimes be peculiar, such as the "where" function only making sense within the "select" function, and so on.

\`\`\`
select(where(is.character))
\`\`\`

  

ggplot的数据导入的方法也让我难以理解，可能是因为我没有熟悉R的逻辑吧。

I also find the method of importing data into ggplot difficult to understand, perhaps because I am not familiar with R's logic.

  

我最不能忍受，最不能理解的一点是为什么要允许点号“.”出现在变量名称里，不仅如此，带有点号的R的默认函数名和默认变量简直是铺天盖地，对我来说，代码阅读速度直接腰斩。

What I find most intolerable and incomprehensible is the allowance of the dot “.” in variable names. Moreover, R's default function and variable names contain so many dots. For me, this significantly slows down the speed of reading code.