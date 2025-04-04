# 陰陽師か:

## ヒント:
uiautomator2のグルチャからのヒント、termuxのproot容器に通じてpythonを運行して(だからproot容器はLinuxに近づく)、uiautomator2(pythonのクラスライブラリの一つ)を利用して、Androidのスマホで自動操作ができる。

## 声明:
本プロジェクトは学習に向けだけだ。


## 準備:
### 1.環境配置:
サイト(<https://www.123684.com/s/rPHrVv-iXZ9A>)からzerotermuxのアプリと復帰のアーカイブがダウンロードできる。


* (1).termuxやzerotermuxでprootの容器をインストール(ここでDebianを選んでデモする)

pkg update

pkg install tsu

pkg install proot-distro

proot-distro install debian    #vpnを使うかも

proot-distro login debian    #Debianに入る

* (2).pythonとuiautomator2をダウンロードする

#aptを更新してpython(pipぐるみ)とadbをインストールする
apt update

apt install python3

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py --break-system-packages

apt install adb

#uiautomator2とopencv_pythonとrapidocrのクラスライブラリをインストールする
pip install -U uiautomator2 --break-system-packages

pip install opencv_python --break-system-packages

pip install rapidocr_onnxruntime --break-system-packages

#もしopencv_pythonクラスライブラリはlibGL.so.1やlibgthread-2.0.so.0などミスがあれば：
apt install libgl1-mesa-glx

apt install libglib2.0-0

* (3).termuxのスタート配置
経路'/data/data/com.termux/files/usr/etc/bash.bashrc'のファイルで以下の内容を付け加えて:

#寛容モードをトライする

sudo setenforce 0

#debianに入った後の配置

proot-distro login debian -- sh -c "cd /storage/emulated/0/termux_project && python3 start.py"
proot-distro login debian -- sh -c "cd /storage/emulated/0/termux_project && exec bash"

### 2.資源ダウンロード:
termux_projectのアーカイブが「/sdcard/termux_project/」に解凍する

