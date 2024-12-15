from module.adb import ADB
from module.ocr import *
import time


# 加载免注册dll
op = ADB()
start = None
end = int(op.height*3/5), int(op.width*3/5), int(op.width*1/10)
        
def Homeowner(targe):
    num = 0
    while True:
        time.sleep(1)
        result = op.找图(op.获取截图对象(int(op.height/2), int(op.width/2), op.height, op.width), 0.8, '御魂图片/开始.png')
        print(result)
        if '开始.png' in result:
            op.点击(start[0], start[1], start[2])
            num += 1
            time.sleep(2)
            while True:
                time.sleep(1)
                result = 找字框(op.获取截图对象(int(op.height/2), int(op.width/2), op.height, op.width))
                print(result)
                if '妖术' in result:
                    time.sleep(2)
                elif '点击屏幕继续' in result:
                    op.点击(end[0], end[1], end[2])
                    time.sleep(3)
                    op.点击(end[0], end[1], end[2])
                    time.sleep(1)
                elif '协战队伍' in result:
                    break
        else:
            time.sleep(2)
            continue
        if num == targe and targe != 0:
                print(f"脚本结束:本次脚本共刷{targe}把")
                break

def Players(targe):
    num = 0
    while True:
        result = 找字框(op.获取截图对象())
        if '妖术' in result:
            time.sleep(1)
        elif '点击屏幕继续' in result:
            op.点击(end[0], end[1], end[2])
            time.sleep(3)
            op.点击(end[0], end[1], end[2])
            time.sleep(1)
        elif '协战队伍' in result:
            num += 1
            print(f'第{num}把')
            while True:
                time.sleep(1)
                result = 找字框(op.获取截图对象(int(op.height/2), int(op.width/2), op.height, op.width))
                if '妖术' in result:
                        break
        if num == targe and targe != '0':
            print(f"脚本结束:本次脚本共刷{targe}把")
            break
        
if __name__ == "__main__":
    target = input('指定次数(0为无限制):')
    while True:
        time.sleep(1)
        result = 找字框(op.获取截图对象(0, 0, int(op.height/2), int(op.width/2)))
        if '协战队伍' in result:
            while True:   
                result = op.找图(op.获取截图对象(int(op.height/2), int(op.width/2), op.height, op.width), 0.8, '御魂图片/开始.png', '御魂图片/不可开始.png')        
                if '开始.png' in result:
                    start = result['开始.png']
                    print('司机')
                    Homeowner(target)         
                    break
                elif '不可开始.png' in result:
                    start = result['不可开始.png']
                    print('司机')
                    Homeowner(target)         
                    break
                else:
                    print('打手')
                    Players(target)  
                    break
        else:
            time.sleep(1)        
                