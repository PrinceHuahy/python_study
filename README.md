# python_study
## if you are interesting markdown grammar just click [here](#markdown)
based on https://mofanpy.com/tutorials/python-basic/interactive-python/
下载python:
windows：
https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe
ubuntu系统自带，要升级只需要终端输入: sudo apt-get update && sudo apt-get upgrade

下载Pycharm：
推荐下载Toolbox然后从Toolbox安装pycharm，其中 pycharm community为免费版，pycharm professional为专业版。
Toolbox：
    windows：
	https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.24.12080.exe
    ubuntu：需要先在终端安装 FUSE : sudo apt install fuse
	https://download-cdn.jetbrains.com/toolbox/jetbrains-toolbox-1.24.12080.tar.gz


单行代码的每一行均为 -----隔开。 多行的内容只需要复制####里面的内容即可。
pip相关：
-----------------------------------------------------------------------------------------------------------------------
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
-----------------------------------------------------------------------------------------------------------------------
python -m pip install --upgrade pip
-----------------------------------------------------------------------------------------------------------------------

ubuntu(22.04)相关：
编辑 /etc/apt/sources.list

##################################复制井号里面的内容###################################
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
####################################################################################

conda相关：
首先激活对应环境，激活之后想用pip则在对应环境下重复执行pip相关的两行代码。
-----------------------------------------------------------------------------------------------------------------------
conda config --set show_channel_urls yes
-----------------------------------------------------------------------------------------------------------------------
然后编辑.condarc文件
windows在 用户名/.condarc
ubuntu在 ~/.condarc

将其全部删除，然后替换为
##################################复制井号里面的内容###################################
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
####################################################################################








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