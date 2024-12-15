from module.adb import ADB
from module.ocr import *
import time


# 初始化
op = ADB()
结束点击 = int(op.height*4/5), int(op.width*2/5), int(op.height*1/10)
加成顺序 = ['无畏附魂', '天下布武绝命', '天下布武刃降', '天下布武血怒', '血之契刃反', '血之契追袭', '暴击加成', '暴击伤害加成', '伤害加成', '速度提升']
'''
奖励加成按顺序选择:六个加成，四个属性
加成:
    天下布武绝命, 天下布武刃降, 天下布武血怒；  
    血之契追袭, 血之契刃反, 血之契锐利；
    八华斩血啸, 八华斩追斩, 八华斩增进；
    鬼神之策剑势, 鬼神之策刃破, 鬼神之策暴烈；
    天剑退敌, 天剑连破, 天剑协战；
    无畏附魂, 无畏透甲；
    鬼胄诱敌, 鬼胄追击；
    剑之垒万刃, 剑之垒乘胜；
    
属性:
    暴击加成，暴击伤害加成，伤害加成，速度提升
'''

def wait():     # 等待运行条件
    while True:
        time.sleep(1)
        result = op.找图(op.获取截图对象(), 0.95, '兵藏图片/兵藏秘境.png', '兵藏图片/未锁定.png', '兵藏图片/已锁定.png')
        if '未锁定.png' in result:
            op.点击(result['未锁定.png'][0], result['未锁定.png'][1], result['未锁定.png'][2])
        elif '已锁定.png' in result:
            if '兵藏秘境.png' in result:
                print('找到主界面，准备运行脚本')
                break
        else:
            time.sleep(5)
    
def main():    # 运行脚本
    wait()
    while True:
        time.sleep(1)
        result = op.找图(op.获取截图对象(), 0.95, '兵藏图片/挑战.png', '兵藏图片/选加成.png', '兵藏图片/战斗中.png', '兵藏图片/胜利.png', '兵藏图片/失败.png', '兵藏图片/结束.png')
        print(result)
        if '结束.png' in result:
            print('兵藏秘境.py', '挑战次数已用完')
            #op.发邮件('兵藏秘境.py', '挑战次数已用完')
            break
        if '挑战.png' in result:
            op.点击(result['挑战.png'][0], result['挑战.png'][1], result['挑战.png'][2])
        elif '战斗中.png' in result:
            time.sleep(5)
        elif '胜利.png' in result:
            op.点击(结束点击[0], 结束点击[1], 结束点击[2])
        elif '失败.png' in result:
            op.点击(结束点击[0], 结束点击[1], 结束点击[2])
            time.sleep(2)
            print('准备重置关卡')
            while True:
                time.sleep(1)
                result = 找字框(op.获取截图对象())
                if '确认重置' in result:
                    op.点击(result['确认重置'][0], result['确认重置'][1], result['确认重置'][2])
                    break
                elif '关卡' in result:  
                    op.点击(result['关卡'][0], result['关卡'][1]-result['关卡'][2], result['关卡'][2])      
        elif '选加成.png' in result:
            result = 找字框(op.获取截图对象())
            sign = True
            for i in 加成顺序:
                for l in list(result.keys()):
                    if l.replace('.', '').replace('·', '') == i:
                        print('选择加成:', i)
                        op.点击(result[l][0], result[l][1], result[l][2])
                        time.sleep(1)
                        sign = False
                        break
                if sign == False:
                    break
            while True:
                time.sleep(1)
                result = 找字框(op.获取截图对象())
                if '确定' in result:
                    op.点击(result['确定'][0], result['确定'][1], result['确定'][2])
                    break
                    
        
if __name__ == '__main__':
    main()