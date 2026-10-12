class Double(object):
	def __init__(self, num_of_pics_in_card):
		self.num_of_pics_in_card = num_of_pics_in_card
		self._total_num_of_pics = None
		self._list_of_groups = None
		self._get_the_cards_yay = None


	@property
	def total_num_of_pics(self):
		if not self._total_num_of_pics:
			self._total_num_of_pics = (self.num_of_pics_in_card * \
				(self.num_of_pics_in_card - 1)) + 1
		return self._total_num_of_pics
	
	@property
	def list_of_groups(self):
		if not self._list_of_groups:
				range_list = [i for i in range(2, self.total_num_of_pics + 1)]
				list_of_groups = []
				while range_list:
					list_of_groups.append(range_list[:(self.num_of_pics_in_card - 1)])
					range_list = range_list[(self.num_of_pics_in_card - 1):]
				self._list_of_groups = list_of_groups
		return self._list_of_groups

	@staticmethod
	def push(list_to_push, times_to_push):
		return list_to_push[times_to_push:] + list_to_push[:times_to_push]

	@property
	def get_the_cards_yay(self):
		if not self._get_the_cards_yay:
			cards_list = [[1] + group for group in self.list_of_groups]
			list_to_push = self.list_of_groups.copy()
			group_to_add = list_to_push.pop()
			i = 1
			while i < self.num_of_pics_in_card:
				list_to_push = [self.push(list_to_push[i], i) for i in range(len(list_to_push))]
				ziped_list = zip(*list_to_push)
				cards_list += [list(j) + [group_to_add[i - 1]] for j in ziped_list]
				i +=1
			self._get_the_cards_yay = cards_list	
		return self._get_the_cards_yay

def main():
	d = Double(8)
	print (d.get_the_cards_yay)
	
if __name__ == "__main__":
	main()									
