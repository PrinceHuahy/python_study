## if you are interesting markdown grammar just click [here](#markdown)
## 国内用户请点击[这里](#chinese)修改源提高下载速度。

---

Personal python study. share everything I meet. based on:[https://mofanpy.com/tutorials/python-basic/interactive-python/](https://mofanpy.com/tutorials/python-basic/interactive-python/)  
# learning environment build
## ubuntu(22.04)
- 1\.install toolbox. [click here](https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.24.12080.tar.gz)
- 2\.open terminal
  ```ubuntu
  $ sudo apt update&&sudo apt upgrade
  $ sudo apt install fuse
  $ cd /your/toolbox_download/path
  $ tar -zxvf jetbrains-toolbox-1.24.12080.tar.gz
  $ cd jetbrains-toolbox-1.24.12080/
  $ ./jetbrains-toolbox
  ```
- 3\.open toolbox and install Pycharm Community

### optional (Recommend)
use conda instead build-in python  
- 1\. install conda. [click here](https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh)  
- 2\. open terminal
  ```ubuntu
  $ cd /your/miniconda_download/path
  $ bash Miniconda3-py39_4.12.0-Linux-x86_64.sh
  ...
  
  # All requested packages already installed.

  installation finished.  
  Do you wish the installer to initialize Miniconda3  
  by running conda init? [yes|no]
  $ yes (recommend)
  ```
- 2.5\. close all terminal and restart a terminal. it should looks like this:  
`(base) user@computer:~$`,enter the following code:
  ```ubuntu
  $ conda create -n py310 python==3.10.4
  $ conda activate py310
  ```
    py310 is what virtual python environment name  
    3.10.4 is your python version  
- 3\. open Pycharm and create a new project  
for more info about how to use conda in pycharm you should [chick here](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html)  

enjoying your python learning.   
:D

---
## Change source (optional)
<span id="chinese"></span>
ubuntu(22.04)源修改：  
编辑 /etc/apt/sources.list 终端输入：  
`suda nano /etc/apt/sources.list`  
通过上下左右移动光标到第一行第一列，按住`ctrl + k`不放会删除所有行。  
复制下面的代码以后使用 `ctrl + shift + v`可以粘贴进命令行。  
粘贴完成以后使用`ctrl + x`下面会出现提示是否保存，`y`为保存，然后问你写入的文件名，保持不动直接回车即可。  
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
打开终端输入:  
`conda config --set show_channel_urls yes`  
然后编辑.condarc文件:  
`sudo nano ./condarc`  
将其全部删除，然后替换为
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
保存以后可以输入 `conda clean -i` 清除缓存。在激活对应环境以后在终端输入下面两行代码则可以更改当前虚拟环境的pip源。    
如果你更换了新的虚拟环境需要在激活对应的虚拟环境以后重新输入一次下面两行代码。  
所有的第三方库都需要在对应激活的虚拟环境下使用pip install 安装，不是很推荐conda安装。  
`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`  
`python -m pip install --upgrade pip`








---
<span id="markdown"></span>
# markdown basic grammar study  
you can find all base-syntax in:
[Basic-Syntax | Markdown](https://www.markdownguide.org/basic-syntax/)   
`anything write in this block is original input`

---

## title:
write # at start like:  
`# level 1 with`  
`## level 2 with`   
`### level 3 with`  
`#### level 4 with`  
`##### level 5 with`  
`###### level 6 with` 
# level 1 with  
## level 2 with  
### level 3 with  
#### level 4 with  
##### level 5 with  
###### level 6 with  

---

## Emphasis
use * or _ at word both sides to *italic* word.eg:`*italic*`  
use ** or __ at word both sides to **Blod** word.  `**Blod** `  
use *** or ___ to ***italic and blod***.`***italic and blod***` 
use asterisks to bold and italicize the middle of a word for emphasis.  
eg:
emph***as***is `emph***as***is`

---

## Blockquotes
To create a blockquotes,add a > in front of paragraph.  
with multiple paragraph need add a > on the blank lines between the paragraphs.
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.  

`> Dorothy followed her through many of the beautiful rooms in her castle.`  
`>`  
`> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.`  

---

## Lists
use numbers followed by periods  

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item  
`1. First item`  
`2. Second item`  
### Unordered list  
- First item
- Third item
- Second item  
`- Second item`  
### number start unordered list
- 121\. test  
`- 121\. test`

---

## Code
\`at code bothside to write code.it can show # > ~ _ * normally.like this\`  
`at code bothside to write code.it can show # > ~ _ * normally.like this`  
multiple line code use \``` at start and end   
```python
def add(a,b):
    return a + b
print(3,5)
```

## Web link
`[show name](web link)`  
you can find all base-syntax in:
[Basic-Syntax | Markdown](https://www.markdownguide.org/basic-syntax/)  
`you can find all base-syntax in:
[Basic-Syntax | Markdown](https://www.markdownguide.org/basic-syntax/) `

### Picture link
use a `!`to show picture if you want.  
`![pic name](pic link)`  
This is my github Logo:  
![my logo](https://avatars.githubusercontent.com/u/96762801?v=4)  
`![my logo](https://avatars.githubusercontent.com/u/96762801?v=4)`
### Linking picture
if you click under logo it will go to pic link.  
[![my logo](https://avatars.githubusercontent.com/u/96762801?v=4)](https://avatars.githubusercontent.com/u/96762801?v=4)
```
[![my logo](https://avatars.githubusercontent.com/u/96762801?v=4)](https://avatars.githubusercontent.com/u/96762801?v=4)
```
## markdown page jump
use `<span id="markdown"></span>` at where you want to jump, then replace web link `[here](#markdown)`.  
now you can click here to jump to where `<span id="markdown"></span>` is.