# Automation-on-Android
运行于termux的python自动化项目

## 思路:
思路来源于uiautomator2项目群里的大佬，通过termux的proot容器运行python(因为proot容器更加接近Linux环境，大多库都能自行编译)，运用uiautomator2(python封装的adb方法的项目)操作手机进行自动化操作
## 声明:
此项目下的自动化实例仅供学习

## 启动模式:
### 1.root模式:
需要打开宽容模式，即终端执行'setenforce 0'，此模式下无需手动打开无线调试和输入端口号，甚至可以不连接WiFi

### 2.普通模式:
此模式需要手动开启无线调试和输入端口号，必须连接WiFi(即使WiFi无网络)

## 准备工作:
### 1.下载环境:
从123云盘下载zerotermux和我配置好的恢复包

< zerotermux: https://www.123865.com/s/rPHrVv-WBb9A >

< 恢复包: https://www.123865.com/s/rPHrVv-dgb9A >
### 2.下载脚本:
从主分支中下载termux_project压缩包，解压至内部空间(即/sdcard目录)
### 3.创建环境:
zerotermux恢复安装网盘下载的恢复包
### 4.安装插件:
打开zerotermux左侧划出菜单栏，找到悬浮窗口(ZeroTermux:Float)下载安装插件
