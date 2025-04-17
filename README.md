# 是阴阳师吗:  
> 手机独立执行python脚本方法有:

|方法|优势|劣势|
|---|---|---|
|termux|扩展性较好|使用较复杂|
|ascript|扩展性差|使用简单|
> 
> 声明:
> + 此项目下的自动化实例仅供学习  
## termux方法
### 思路:
思路来源于uiautomator2项目群里的大佬，通过termux的proot容器运行python(因为proot容器更加接近Linux环境，大多库都能自行编译)，运用uiautomator2(python封装的adb方法的项目)操作手机进行自动化操作  
### 准备:
> 一、环境配置:
图省事可以从123云盘(https://www.123684.com/s/rPHrVv-iXZ9A<)中下载zerotermux和我配置好的恢复包，怎么恢复直接百度  
1. termux或zerotermux中安装proot容器(我这里安装的是Debian)
~~~
pkg update

pkg install tsu

pkg install proot-distro

proot-distro install debian    # 此操作可能需要换源或者魔法

proot-distro login debian    # 进入Debian
~~~
2. 安装python和uiautomator2
~~~
#更新apt并安装python(以及pip)和adb
apt update

apt install python3

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py --break-system-packages

apt install adb

#安装uiautomator2库，opencv_python库和rapidocr库
pip install -U uiautomator2 --break-system-packages

pip install opencv_python --break-system-packages

pip install rapidocr_onnxruntime --break-system-packages
~~~
> cv库报错找不到 libGL.so.1，libgthread-2.0.so.0 共享对象文件时：  
~~~
apt install libgl1-mesa-glx
apt install libglib2.0-0
~~~
3. 初始化配置
编辑'/data/data/com.termux/files/usr/etc/bash.bashrc'文件(推荐mt管理器)，添加如下内容:
~~~
#尝试宽容模式
sudo setenforce 0
#进入debian并cd到termux_project目录
proot-distro login debian -- sh -c "cd /storage/emulated/0/termux_project && python3 start.py"
proot-distro login debian -- sh -c "cd /storage/emulated/0/termux_project && exec bash"
~~~

> 二、资源下载:

从主分支termux_project文件夹中下载脚本到内部空间的termux_project目录(即/sdcard/termux_project/)  

---
## ascript方法  
### 思路:  
> 通过使用[airscript](http://ascript.cn/)及其函数方法创建阴阳师脚本，通过无障碍服务模拟点击，这种方法使用第三方库需要自己重新编译  
### 配置  
> 1.参考[官方文档](http://ascript.cn/docs/android/guide/first)打开编辑器并创建项目
> 
> 2.复制粘贴主分支下的ascript文件夹下的py文件内容并保存  
### 使用  
> 1.打开应用按照提示打开无障碍服务并共享屏幕
> 
> 2.打开游戏后，点开右侧悬浮窗
> 
> 3.点击放大镜按钮，选择脚本，此时脚本开始执行

