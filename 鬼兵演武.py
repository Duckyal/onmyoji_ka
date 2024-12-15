from module.adb import ADB
from module.ocr import *
import time


# 初始化
op = ADB()
start = None
end = (int(op.height*3/5), int(op.width*1/5), int(op.width*1/10))


# 主要逻辑区
def wait():     
    global start
    while True:
        result = op.找图(op.获取截图对象(), 0.8, '演武图片/鬼兵演武.png', '演武图片/未锁定.png', '演武图片/已锁定.png', '演武图片/挑战.png')
        print(result)
        if '鬼兵演武.png' in result:
            if '未锁定.png' in result:
                op.点击(*result['未锁定.png'])
                time.sleep(0.5)
            elif '已锁定.png' in result:
                if '挑战.png' in result:
                    start = result['挑战.png']
                    print('准备运行脚本')
                    return True
        
def main():
    while True:
        time.sleep(1)
        result = 找字框(op.获取截图对象(0, int(op.width/2), op.height, op.width))
        if 'Lv.40满' in result:
            print('鬼兵部已满级')
            break
        elif '挑战' in result:
            op.点击(*start)
        elif '点击屏幕继续' in result:
            op.点击(*end)                
        elif '自动' in result:
            time.sleep(5)
    

if __name__ == '__main__':
    if wait() == True:
        main()