
import numpy as np







class ScrapBooker():
	def __init__(self):
		pass

	def crop(self, array, dim, position=(0,0)):

		x = len(array)
		y = len(array[0])


		for v in range(x):
			for h in range(y):
				if v == position[0] and h == position[1]:
					# Start Point
					for z in range(dim[0]):
						for y in range(dim[1]):
							print(array[v+z][h+y])


	def thin(self, array, n, axis):
		
		x = len(array)
		y = len(array[0])

		arr2 = []


		for v in range(x):
			for h in range(y):
				if h != n - 1:
					arr2.append(array[v][h])
					# print(array[v][h], end="")
					# print(array[v][h])
			print()

		print(arr2)







def main():
	print('start')
	spb = ScrapBooker()
	# arr1 = np.arange(0,25).reshape(5,5)
	
	# spb.crop(arr1, (3,2),(1,0))
	arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
	spb.thin(arr2,3,0)
	# print(arr2)


if __name__ == "__main__":
    main()



# [0 1 2 3 4]
# [5 6 7 8 9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]



# [['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']]



# # within the class
# def crop(self, array, dim, position=(0,0)):
# """
# Crops the image as a rectangle via dim arguments (being the new height
# and width of the image) from the coordinates given by position arguments.
# Args:
# -----
# array: numpy.ndarray
# dim: tuple of 2 integers.
# position: tuple of 2 integers.
# Return:
# -------
# new_arr: the cropped numpy.ndarray.
# None (if combinaison of parameters not compatible).
# Raise:
# ------
# This function should not raise any Exception.
# """
# ... your code ...
# def thin(self, array, n, axis):
# """
# Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
# Args:
# -----
# array: numpy.ndarray.
# n: non null positive integer lower than the number of row/column of the array
# (depending of axis value).
# axis: positive non null integer.
# Return:
# -------
# new_arr: thined numpy.ndarray.
# None (if combinaison of parameters not compatible).
# Raise:
# ------
# This function should not raise any Exception.
# """
# ... your code ...
# def juxtapose(self, array, n, axis):
# """
# Juxtaposes n copies of the image along the specified axis.
# Args:
# -----
# array: numpy.ndarray.
# n: positive non null integer.
# axis: integer of value 0 or 1.
# Return:
# -------
# new_arr: juxtaposed numpy.ndarray.
# None (combinaison of parameters not compatible).
# Raises:
# -------
# This function should not raise any Exception.
# """
# ... your code ...
# def mosaic(self, array, dim):
# """
# Makes a grid with multiple copies of the array. The dim argument specifies
# the number of repetition along each dimensions.
# Args:
# -----
# array: numpy.ndarray.
# dim: tuple of 2 integers.
# Return:
# -------
# new_arr: mosaic numpy.ndarray.
# None (combinaison of parameters not compatible).
# Raises:
# -------
# This function should not raise any Exception.
# """