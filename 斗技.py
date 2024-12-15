from module.adb import ADB
from module.ocr import *
import time
import re

# 初始化
op = ADB()
pattern = re.compile(r"[0-9]{2,}/[0-9]{2,}")
start = None
end = (int(op.height*3/5), int(op.width*1/5), int(op.width*1/10))


def wait():     # 等待斗技页面
    global start
    while True:
        result = op.找图(op.获取截图对象(), 0.9, '斗技图片/斗技.png', '斗技图片/战1.png', '斗技图片/战2.png', '斗技图片/战3.png', '斗技图片/练.png')
        if '斗技.png' in result:
            if '战1.png' in result:
                start = result['战1.png']
                print('准备运行脚本')
                return True
            elif '战2.png' in result:
                start = result['战2.png']
                print('准备运行脚本')
                return True
            elif '战3.png' in result:
                start = result['战3.png']
                print('准备运行脚本')
                return True
            elif '练.png' in result:
                print('未在活动时间内')
                return False
                
def main():
    while True:
        result = 找字框(op.获取截图对象(int(op.height/2), int(op.width/2), op.height, op.width))
        state = 0
        for i in result:
            re_result = pattern.search(i)
            if re_result != None:
                ls = re_result.group().split('/')
                if ls[0] == ls[1]:
                    print(ls)
                    state = 1
                    break
        if state == 1:
            print('本周荣誉值已满，停止运行')
            break 
        if '观战' in result:
            op.点击(*start)
            while True:
                time.sleep(1)
                result = 找字框(op.获取截图对象(0, int(op.width/2), op.height, op.width))
                print(result)
                if '点击屏幕继续' in result or '战斗数据' in result:
                    op.点击(*end) 
                elif '自动' in result:
                    time.sleep(5)
                elif '手动' in result:
                    op.点击(result['手动'][0], result['手动'][1]+int(op.width/2), result['手动'][2])
                elif '准备' in result:
                    op.点击(op.点击(result['准备'][0], result['准备'][1]+int(op.width/2), result['准备'][2]))
                    time.sleep(2)
                elif '确定' in result:
                    op.点击(result['确定'][0], result['确定'][1]+int(op.width/2), result['确定'][2])
                    time.sleep(2)
                elif '观战' in result:
                    break
                
    
if __name__ == '__main__':
    if wait() == True:
        main()