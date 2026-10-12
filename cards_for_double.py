from PIL import Image
import os
from pictures_for_double import Card
from double import Double

class CreateDoubleCards(object):
	def __init__(self, num_of_pics_in_card, dir_path_of_pictures, dir_path_for_cards, path_of_circle):
		self.num_of_pics_in_card = num_of_pics_in_card
		self.dir_path_of_pictures = dir_path_of_pictures
		self.dir_path_for_cards = dir_path_for_cards
		self.path_of_circle = path_of_circle
		self._list_of_paths_list_for_card = None

	def check_amount_of_pics(self):
		pictures_path_list = list(map(lambda pic: os.path.join(self.dir_path_of_pictures, pic),\
		os.listdir(self.dir_path_of_pictures)))

		raw_double = Double(self.num_of_pics_in_card)
		if len(pictures_path_list) < raw_double.total_num_of_pics:
			raise Exception (f"Not enough pictures in this dir_path, please put \
			in the dir {raw_double.total_num_of_pics} pictures, and run again")
		if len(pictures_path_list) > raw_double.total_num_of_pics:
			print(f"Too many pictures, just the first {raw_double.total_num_of_pics} will be taken")
		return pictures_path_list, raw_double

	@property
	def list_of_paths_list_for_card(self):
		if not self._list_of_paths_list_for_card:
			pictures_path_list, raw_double = self.check_amount_of_pics()
			
			raw_numbers_cards_list = raw_double.get_the_cards_yay
			numbers_paths_dict = {}
			for i in range(raw_double.total_num_of_pics):
				numbers_paths_dict[i + 1] = pictures_path_list[i]
			list_of_paths_list_for_card = [[numbers_paths_dict[i] for i in card] for card in raw_numbers_cards_list]
			
			self._list_of_paths_list_for_card = list_of_paths_list_for_card
		return self._list_of_paths_list_for_card

	def create_the_cards(self):
		counter = 1
		for list_of_paths in self.list_of_paths_list_for_card:
			card = Card(list_of_paths, self.path_of_circle)
			path_to_save = os.path.join(self.dir_path_for_cards, f"{str(counter)}.png")
			card.save_card(path_to_save)
			counter += 1
		print("All done :)")



