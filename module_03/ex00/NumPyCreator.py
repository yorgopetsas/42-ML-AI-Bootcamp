import numpy as np

class NumPyCreator():


	def __init__(self):
		pass
	def from_list(self, a):
		print(np.asarray(a))
	def from_tuple(self, tpl):
		print(np.asarray(tpl))
	def from_iterable(self, itr):
		pass
	def from_shape(self, shapex, shapey, value="0"):
		print(np.full((shapex, shapey), 0))
	def random(self, shapex, shapey):
		print(np.random.rand(shapex,shapey))
	def identity(self, n):
		print(np.identity(n))


def main():
	a = [[1,2,3],[6,3,4]]
	b = ("a", "b", "c")
	shape = (3, 5)
	identity = 4


	my_obj = NumPyCreator()
	my_obj.from_list(a)
	my_obj.from_tuple(b)
	# my_obj.from_iterable(range(5))
	my_obj.from_shape(shape[0], shape[1])
	my_obj.random(shape[0], shape[1])
	my_obj.identity(identity)
	


if __name__ == "__main__":
    main()


