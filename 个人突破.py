from module.adb import ADB
from module.ocr import *
import time


# 初始化
op = ADB()
midx, midy = int(op.height/2), int(op.width/2)-130
start = [(midx-495, midy-200), (midx, midy-200), (midx+495, midy-200), (midx+495, midy), (midx, midy), (midx-495, midy), (midx-495, midy+200), (midx, midy+200), (midx+495, midy+200)]
end = (int(op.height*3/5), int(op.width*1/5), int(op.width*1/10))


# 主要逻辑区
def wait():
    while True:
        time.sleep(1)
        result = op.找图(op.获取截图对象(), 0.9, '突破图片/结界突破.png', '突破图片/锁定.png', '突破图片/未锁定.png')
        if '结界突破.png' in result:
            if '未锁定.png' in result:
                op.点击(*result['未锁定.png'])
            elif '锁定.png' in result:
                print('阵容已锁定，开始运行脚本')
                break
                
def refresh():
    while True:
        time.sleep(0.5)
        op.找图(op.获取截图对象(), 0.9, '突破图片/刷新.png', '突破图片/确定.png')
        if '确定.png' in result:
            op.点击(*result['确定.png'])
            return False
        elif '刷新.png' in result:
            op.点击(*result['刷新.png'])
        else:
            print('无刷新次数，继续往后刷')
            return True

def main():
    wait()
    while True:
        for i in start:
            state = True
            while True:
                time.sleep(0.5)
                result = op.找图(op.获取截图对象(i[0], i[1], i[0]+495, i[1]+200), 0.9, '突破图片/已突破1.png', '突破图片/已突破2.png')
                print(result)
                if '已突破1.png' in result or '已突破2.png' in result:
                    break
                else:
                    op.点击(i[0], i[1], 100)
                    while True:
                        time.sleep(0.5)
                        result = op.找图(op.获取截图对象(), 0.9, '突破图片/结束.png', '突破图片/进攻.png', '突破图片/结界突破.png')
                        if '结束.png' in result:
                            print('突破票已清空')
                            return 'OverError'
                        elif '进攻.png' in result:
                            op.点击(result['进攻.png'][0], result['进攻.png'][1], result['进攻.png'][2])      
                            time.sleep(1)
                        elif '结界突破.png' not in result:
                            print('进入战斗')
                            time.sleep(10)
                            failure = False
                            while True:
                                time.sleep(0.5)
                                result = op.找图(op.获取截图对象(), 0.9, '突破图片/胜利.png', '突破图片/失败.png', '突破图片/结界突破.png')
                                if '胜利.png' in result:
                                    op.点击(*end)
                                    time.sleep(1)
                                elif '失败.png' in result:
                                    op.点击(*end)
                                    time.sleep(1)                               
                                elif '结界突破.png' in result:
                                    if failure == True:
                                        state = refresh()
                                    break
                                else:
                                    time.sleep(2)
                            break
                        else:
                            break
            if state == False:  # 刷新循环
                break
                    
        
if __name__ == '__main__':
    main()