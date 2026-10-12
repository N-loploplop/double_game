from PIL import Image
import os
from good_proportion_pic import Pic

PATH_OF_CIRCLE = r""

class Card(object):
    DICT_OF_PARAMS_FOR_PIC = {
                              0:{'size':(494, 498), 'rotation':313, 'quards':(462, 41)},
                              1:{'size':(368, 356), 'rotation':322, 'quards':(82, 665)},
                              2:{'size':(244, 218), 'rotation':337, 'quards':(206, 124)},
                              3:{'size':(267, 200), 'rotation':0, 'quards':(829, 494)},
                              4:{'size':(214, 242), 'rotation':248, 'quards':(418, 501)},
                              5:{'size':(323, 286), 'rotation':22, 'quards':(49, 349)},
                              6:{'size':(230, 250), 'rotation':300, 'quards':(410, 908)},
                              7:{'size':(379, 314), 'rotation':348, 'quards':(610, 718)}
                            }
    def __init__(self, list_of_pictures, path_of_circle):
        self.list_of_pictures = list_of_pictures
        self.path_of_circle = path_of_circle
        self._card_object = None


    @property
    def card_object(self):
        if not self._card_object:
            counter = 0
            card_object = Image.open(self.path_of_circle)
            card_object = card_object.resize((1200, 1200))
            for pic_path in self.list_of_pictures:
                pic = Pic(pic_path).return_final_pic()
                #we should first of all rotate the picture and only then resize it
                #otherwise it might be blurred

                pic = pic.rotate(self.DICT_OF_PARAMS_FOR_PIC[counter]['rotation'], \
                    expand=True, fillcolor='white')
                pic = pic.resize(self.DICT_OF_PARAMS_FOR_PIC[counter]['size'])

                
                card_object.paste(pic, self.DICT_OF_PARAMS_FOR_PIC[counter]['quards'])
                counter += 1
            self._card_object = card_object
        return self._card_object

    def save_card(self, path_to_save):
        self.card_object.save(path_to_save)

#this code is for checking
path = r""
pic_list = os.listdir(path)
pic_list = list(map(lambda pic: os.path.join(path, pic), pic_list))
h = Card(pic_list, PATH_OF_CIRCLE)
h.save_card(r"")