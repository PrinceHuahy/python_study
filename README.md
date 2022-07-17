## 国内用户请点击[这里](#chinese)修改源提高下载速度。

---

Personal python study and share everything I meet.   
based on:[https://www.w3schools.com/python/default.asp](https://www.w3schools.com/python/default.asp)

# learning environment build

## ubuntu(22.04)

- 1\.install toolbox. [click here](https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.24.12080.tar.gz)
- 2\.open terminal
  ```ubuntu
    sudo apt update&&sudo apt upgrade
  ```
  ```ubuntu
    sudo apt install fuse
  ```
  ```ubuntu
    cd /your/toolbox_download/path
  ```
  ```ubuntu
    tar -zxvf jetbrains-toolbox-1.24.12080.tar.gz
  ```
  ```ubuntu
    cd jetbrains-toolbox-1.24.12080/
  ```
  ```ubuntu
    ./jetbrains-toolbox
  ```
- 3\.open toolbox at top-right corner and install Pycharm Community

### optional (Recommend)

use conda instead build-in python

- 1\. install conda. [click here](https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh)

- 2\. close all terminal and restart a terminal. enter the following code:
  ```ubuntu
    conda create -n py310 python==3.10.4
  ```
  ```ubuntu
    conda activate py310
  ```
  &emsp;&emsp;<b>py310</b> is what virtual python environment name  
  &emsp;&emsp;<b>3.10.4</b> is your python version
- 3\. open Pycharm and create a new project for more info about how to use conda in pycharm you
  should [chick here](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html).

enjoying your python learning.   
:D

---

## 修改程序源 (显著提高国内下载速度)

<span id="chinese"></span>
&emsp;&emsp;ubuntu(22.04)源修改：  
&emsp;&emsp;编辑 /etc/apt/sources.list 终端输入：

```ubuntu
    suda nano /etc/apt/sources.list
```

&emsp;&emsp;通过上下左右移动光标到第一行第一列，按住`ctrl + k`不放会删除所有行。  
复制下面的代码以后使用 `ctrl + shift + v`可以粘贴进命令行。粘贴完成以后使用  
`ctrl + x`下面会出现提示是否保存，`y`为保存，然后会询问你写入的文件名，保持不动直接回车即可。

```ubuntu
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
```

### conda相关：

&emsp;&emsp;打开终端输入:

```ubuntu
conda config --set show_channel_urls yes
```  

&emsp;&emsp;编辑.condarc文件:

```ubuntu
sudo nano ./condarc
```

&emsp;&emsp;将其全部删除，然后替换为

```ubuntu
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

&emsp;&emsp;保存以后可以输入下面的命令来清除conda缓存。

```ubuntu
    conda clean -i
``` 

&emsp;&emsp;当你激活对应环境以后在终端输入下面两行代码则可以更改当前虚拟环境的pip源。如果你更换了新的虚拟环境需要在激活对应的虚拟环境以后重新输入一次下面两行代码。所有的第三方库都需要在对应激活的虚拟环境下使用pip install 安装，不是很推荐conda安装。

```ubuntu
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
``` 

```ubuntu
    python -m pip install --upgrade pip
``` 
