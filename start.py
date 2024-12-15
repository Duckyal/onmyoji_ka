import os
from module.adb import ADB


# 初始化
op = ADB()


def choose():
    while True:
        app = input('输入游戏渠道:\n1.官服\t2.应用宝\n选择:')
        if app =='1':
            op.启动应用("com.netease.onmyoji")
            break
        elif app == '2':
            op.启动应用("com.tencent.tmgp.yys.zqb")
            break
        else:
            print('错误:重新选择')

while True:
    try:
        result = input('输入脚本序号:\n1.御魂\t2.斗技\t3.兵藏秘境\t4.鬼兵演武\t5.个人突破\n0.退出\t选择:')
        if  result == '1':
            print ('运行御魂脚本')
            choose()      
            os.system('python3 御魂.py')
        elif result == '2':
            print ('运行斗技脚本')
            choose()
            os.system('python3 斗技.py')
        elif result == '3':
            print ('运行兵藏秘境脚本')
            choose()
            os.system('python3 兵藏秘境.py')
        elif result == '4':
            print ('运行鬼兵演武脚本')
            choose()
            os.system('python3 鬼兵演武.py')
        elif result == '5':
            print ('运行个人突破脚本')
            choose()
            os.system('python3 个人突破.py')
        elif result == '0':
            print('退出')
            break
        else:
            print('序号错误')
    except:
        print('发生错误:回到启动页')

