import uiautomator2 as u2

import cv2
import numpy as np

import os
import time 
from concurrent.futures import ThreadPoolExecutor


class ADB:
    adb_path = os.path.dirname(__file__)   #取文件所在文件夹绝对路径
    width = 0
    height = 0
    
    def __init__(self, adb_tcp:str=None, mode:int=1):
        '''
        adb_tcp：无线调试端口或ip+端口
        mode: 1.开启日志  0. 关闭日志
        '''
        self.mode = mode     
        try:
            if adb_tcp == None:
                self.d = u2.connect()
            else:
                self.d = u2.connect('127.0.0.1:'+adb_tcp.split(':')[-1])
            self._size()
        except AttributeError:
            print('设备初始化失败, 请检查设备是否连接')
            exit()
            
    def _size(self):
        size = self.d.window_size()
        self.width = size[0] if size[0]<size[1] else size[1]
        self.height = size[1] if size[0]<size[1] else size[0]
        if self.mode == 1:
            print(f'设备初始化完成:宽:{self.width},高:{self.height}')
    
    def 启动应用(self, package_name:str):
        self.d.app_start(package_name)
        if self.mode == 1:
            print('启动应用:{0}'.format(package_name))
        
    def 关闭应用(self, package_name:str):
        if package_name == 'all':
            self.d.app_stop_all()
            if self.mode == 1:
                print('关闭全部用户应用')
        else:
            self.d.app_stop(package_name)
            if self.mode == 1:
                print('关闭应用:{0}'.format(package_name))
                
    def 息屏(self):
        self.d.screen_off()
        if self.mode == 1:
            print('已息屏')
    
    def 截图保存(self, save_path:str=adb_path, *point:tuple):
        if len(point) == 0:
            cv2.imwrite(save_path, self.d.screenshot(format='opencv'))
        else:
            cv2.imwrite(save_path, self.d.screenshot(format='opencv')[point[1]:point[3], point[0]:point[2]])
        if self.mode == 1:
            print('已保存截图到:{0}'.format(save_path))
            
    def 获取截图对象(self, x1:int=None, y1:int=None, x2:int=None, y2:int=None):
        img = self.d.screenshot(format='opencv')
        # cv2.imshow('img', img)    # 显示图片
        if x1!=None and y1!=None and x2!=None and y2!=None:
            x1 = int(self.height*x1) if isinstance(x1, float) else x1
            y1 = int(self.width*y1) if isinstance(y1, float) else y1
            x2 = int(self.height*x2) if isinstance(x2, float) else x2
            y2 = int(self.width*y2) if isinstance(y2, float) else y2
            return img[y1:y2, x1:x2]
        else:
            return img
        if self.mode == 1:
            print('已保存截图到:{0}'.format(save_path))
                     
    def 简单点击(self, x:int, y:int, r, *els):
        X, Y = x+r, y+r
        self.d.click(X, Y)
        if self.mode == 1:
            print('快速点击{0} {1}'.format(X, Y))
              
    def 点击(self, x:int, y:int, loc:int='均值(一般取正态分布的生成半径)', *els):
        # x,y应为左上角坐标
        mouse = np.random.normal(loc, int(loc**0.5), 2)
        X, Y = int(mouse[0]+x), int(mouse[1]+y)
        # self.d.click(X, Y)
        self.d.touch.down(X, Y)
        time.sleep(np.random.uniform(0, 0.4))
        self.d.touch.up(X, Y)
        if self.mode == 1:
            print('模拟点击{0} {1}'.format(X, Y))
    
    def 简单滑动(self, dir:float, scale:float=0.5, *box:tuple):
        '''
        dir可选:
                'up', 'down', 'left', 'right'
        '''
        if len(box) == 4:
            self.d.swipe_ext(dir, scale=scale, box=box)
        else:
            self.d.swipe_ext(dir, scale=scale)
        if self.mode == 1:
            print('模拟滑动{0}'.format(dir))
    
    def 滑动(self, x_start:int, y_start:int, offset:str):
        '''
        x_start, y_start为起始坐标,
        offset格式是:移动方向|偏移阈值 => x|500 或 -y|250
        '''
        track = [(x_start, y_start)]
        offs = offset.split('|')
        axis, dis = offs[0], int(offs[1])
        num = 0
        if axis == 'x':   #y随机增加
            y = y_start
            for n in range(10, dis, 10):
                num += np.random.randint(1, 5)
                if num > dis:
                    break
                track.append((x_start+n, y_start-num))
        elif axis == 'y':   # x随机增加
            for n in range(10, dis, 10):
                num += np.random.randint(1, 5)
                if num > dis:
                    break
                track.append((x_start+num, y_start-n))
        elif axis == '-x':   #y随机增加
            y = y_start
            for n in range(10, dis, 10):
                num += np.random.randint(1, 5)
                if num > dis:
                    break
                track.append((x_start-n, y_start+num))
        elif axis == '-y':   # x随机减少
            for n in range(10, dis, 10):
                num += np.random.randint(1, 5)
                if num > dis:
                    break
                track.append((x_start-num, y_start+n))
        self.d.swipe_points(track, 0.03)
        if self.mode == 1:
            print('模拟滑动{0}'.format(offset))
    
    def 找字点击(self, target_txt:str, wait_time:int=180):
        self.d.implicitly_wait(10)
        self.d(text=target_txt).click()
        if self.mode == 1:
            print('模拟点击{0}'.format(target_txt))
        
    def 输入(self, txt:str):
        self.d.clear_text() # 清除输入框所有内容
        self.d.send_keys(txt)
        self.d.send_action("send") # 根据输入框的需求，自动执行回车、搜索等指令,支持 go, search, send, next, done, previous
        if self.mode == 1:
            print('模拟输入{0}'.format(txt))
        
    def 命令行(self, shell:str):
        os.system(shell)
        if self.mode == 1:
            print('执行命令行:{0}'.format(shell))

    def 缩扩图(self, img_path:str, resolution:tuple=(1028,720), save_path=None):
        '''
        img_path:目标图片路径
        resolution:导入图片的分辨率 例:(1028, 720）
        save_path:是否保存结果图(保存路径)
        '''
        # 获取原始图片的名字、高度和宽度
        img_name = os.path.basename(img_path)
        image = cv2.imread(img_path)
        height, width = image.shape[:2]
        # 计算新的宽度和高度
        old_width, old_height = resolution
        ratio = self.height/old_width if abs(self.height-old_width)<abs(self.width-old_height) else self.width/old_height
        if ratio == 1.0:
            return (img_name, image)
        else:
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            # 扩大图片
            resized_image = cv2.resize(image, (new_width, new_height))
            # 返回结果
            if save_path != None:
                cv2.imwrite(save_path, resized_image)
            else:
                return(img_name, resized_image)
    
    def 比色(self, match_img:str, pos:tuple=None, color_threshold:int=30):
        sub_image = cv2.imread(match_img)
        sub_image_size = sub_image.shape[:2]
        if pos == None:
            # 寻找match_img位置
            _result = self._match_image(cv2.cvtColor(self.获取截图对象(), cv2.COLOR_BGR2GRAY), sub_image, 0.9, os.path.basename(match_img), sub_image_size)[1]
            x1, y1, w, h = _result[0], _result[1], _result[3], _result[4]
            x2, y2 = x1+w, y1+h
        elif isinstance(pos, tuple):
            x1, y1, w, h = pos
            x2, y2 = x1+w, y1+h
        else:
            raise ValueError('match_img并非路径或元组')
        # 提取矩形区域
        rect_area = w * h
        roi = self.获取截图对象(x1,y1,x2,y2)
        
        # 简单地取平均颜色作为主要颜色
        main_color_roi = np.mean(roi, axis=(0, 1)).astype(int)
        main_color_sub = np.mean(sub_image, axis=(0, 1)).astype(int)
        # 计算颜色差值
        diff = np.sum(np.abs(main_color_roi - main_color_sub))
        if self.mode == 1:
            print('{0}匹配结果:{1}'.format(os.path.basename(match_img), diff))
        return diff < color_threshold
    
    def 找图(self, main_img, sim=0.95, *image_list):
        if type(main_img) == str:
            main_img = cv2.imread(main_img)
        main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
        output = {}
        sub_images_info = []
    
        for image in image_list:
            try:
                img_name = os.path.basename(image)
                if os.path.exists(image):
                    sub_image = cv2.imread(image)
                    sub_image_size = sub_image.shape[:2]
                    sub_images_info.append((sub_image, sim, img_name, sub_image_size))
                else:
                    continue
            except TypeError:
                img_name = image[0]
                sub_image = image[1]
                sub_image_size = sub_image.shape[:2]
                sub_images_info.append((sub_image, sim, img_name, sub_image_size))
            
    
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda info: self._match_image(main_gray, *info), sub_images_info))
    
        for result in results:
            if result:
                img_name, value = result
                output[img_name] = value
    
        if self.mode == 1:
            print(output)
        return output
        
    def _match_image(self, main_gray, sub_image, sim:float, img_name:str, sub_image_size:tuple):    #多线程匹配小图
        sub_gray = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(main_gray, sub_gray, cv2.TM_CCOEFF_NORMED)
        try:
            loc = np.where(result >= sim)
            frist_element = (loc[1][0], loc[0][0])
            if isinstance(frist_element, (list, tuple)) and len(frist_element) >= 2:
                x, y = frist_element
                w, h = sub_image_size[1], sub_image_size[0]
                r = int(w / 2) if w < h else int(h / 2)
                return img_name, (int(x), int(y), r, w, h)
        except IndexError:
            return None
