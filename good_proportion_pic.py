import cv2
import numpy
from PIL import Image
import os

class Pic(object):
    GOOD_PROPORTION = 0.75

    def __init__(self, pic_path):
        self.pic_path = pic_path
        self._pil_pic = None
        self._pic_proportion = None
        self._is_widthwise = None

    @property
    def pil_pic(self):
        if not self._pil_pic:
            self._pil_pic = Image.open(self.pic_path)
        return self._pil_pic


    @property
    def is_widthwise(self):
        if not self._is_widthwise:
            if self.pil_pic.width > self.pil_pic.height:
                self._is_widthwise = True
            else:
                self._is_widthwise = False
        return self._is_widthwise

    @property
    def pic_proportion(self):
        if not self._pic_proportion:
            if self.is_widthwise:
                self._pic_proportion =  round((self.pil_pic.height / self.pil_pic.width), 2)
            else:
                self._pic_proportion =  round((self.pil_pic.width / self.pil_pic.height), 2)
        return self._pic_proportion


    @staticmethod
    def add_rows(pic_path, num_rows_to_add):
        cv2_pic = cv2.imread(pic_path)
        new_pic = numpy.ndarray((cv2_pic.shape[0] + num_rows_to_add, cv2_pic.shape[1], 3))
        new_pic = 255 - new_pic

        for row in range(cv2_pic.shape[0]):
            new_pic[int(num_rows_to_add / 2) + row] = cv2_pic[row]

        cv2.imwrite("temp_good_proportion.png", new_pic)
        return Image.open("temp_good_proportion.png")

    @staticmethod
    def add_columns(pic_path, num_columns_to_add):
        cv2_pic = cv2.imread(pic_path)
        new_pic = numpy.ndarray((cv2_pic.shape[0], cv2_pic.shape[1] + num_columns_to_add, 3))
        new_pic = 255 - new_pic
        side = int(num_columns_to_add / 2)
        
        for row in range(cv2_pic.shape[0]):
            new_pic[row, side: side + cv2_pic.shape[1]] = cv2_pic[row]

        cv2.imwrite("temp_good_proportion.png", new_pic)
        pil_pic = Image.open("temp_good_proportion.png")
        return pil_pic

    def good_proportion_pic(self):
        if self.pic_proportion == self.GOOD_PROPORTION:
            return self.pil_pic
        if self.pic_proportion < self.GOOD_PROPORTION:
            if self.is_widthwise:
                num_rows_to_add = int(self.pil_pic.width * self.GOOD_PROPORTION - self.pil_pic.height)
                return self.add_rows(self.pic_path, num_rows_to_add)
            else:
                num_columns_to_add = int(self.pil_pic.height * self.GOOD_PROPORTION - self.pil_pic.width)
                return self.add_columns(self.pic_path, num_columns_to_add)
        else:
            if self.is_widthwise:
                num_columns_to_add = int(self.pil_pic.height / self.GOOD_PROPORTION - self.pil_pic.width)
                return self.add_columns(self.pic_path, num_columns_to_add)
            else:
                num_rows_to_add = int(self.pil_pic.width / self.GOOD_PROPORTION - self.pil_pic.height)
                return self.add_rows(self.pic_path, num_rows_to_add)

    def return_final_pic(self):
        pic = self.good_proportion_pic()
        if pic.width > pic.height:
            return pic
        else:
            return pic.rotate(90, expand=True)