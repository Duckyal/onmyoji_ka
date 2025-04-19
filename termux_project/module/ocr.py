from rapidocr_onnxruntime import RapidOCR

class OCR:
    def __init__(self):
        self.engine = RapidOCR()
        
    def 找字(self, img_path):
        result_list, elapse = self.engine(img_path, use_det=True, use_cls=False, use_rec=True)
        try:
            result_text = ''
            for i in result_list:
                result_text += i[1]
            return result_text
        except TypeError:
            return 'NotFind'
        
    def 找字框(self, img_path):
        result_list, elapse = self.engine(img_path, use_det=True, use_cls=True, use_rec=True)
        try:
            result_dict = {}
            for i in result_list:
                word, x1, y1, x2, y2 = i[1], int(i[0][0][0]), int(i[0][0][1]), int(i[0][2][0]), int(i[0][2][1])
                w, h = (x2-x1)//2, (y2-y1)//2
                r = w if w <= h else h
                result_dict[word] = (x1, y1, r)
            return result_dict
        except TypeError:
            return 'NotFind'