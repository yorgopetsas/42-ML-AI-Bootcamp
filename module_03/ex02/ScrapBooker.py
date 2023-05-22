
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


		# if axis == 0:
		# 	axis = 1
		# elif axis == 1:
		# 	axis = 0 


		if y < n:
			print(f'Please provide a value under {y}')
			quit()


		if axis < 0 or axis > 1:
			print(f'Please provide a value between 0 and 1')
			quit()


		if axis == 0:
			to_delete = []	
			for i in range(1,y+1):
				r = (n*i) - 1
				if r > y-1 :
					break
				if r < 0:
					continue
				to_delete.append(r)
				# Check what will be deleted
				print(to_delete)
			# Delete specified columns
			array = np.delete(array, to_delete, axis=1)
			return(array)

		elif axis == 1:
			to_delete = []
			print(to_delete)

			for i in range(1,x+1):
				r = (n*i) - 1
				if r > x-1 :
					break
				if r < 0:
					continue
				to_delete.append(r)
				# Check what will be deleted
				print(to_delete)
			# Delete specified columns
			array = np.delete(array, to_delete, axis=0)
			return(array)


def main():
	
	spb = ScrapBooker()
	# arr1 = np.arange(0,25).reshape(5,5)
	# print(arr1)
	# spb.crop(arr1, (3,1),(1,0))

	arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
	# Deletes every n-th line pixels along the specified axis 
	# Last argument -> (0: Horizontal, 1: Vertical)
	new = spb.thin(arr2,3,1)
	new = spb.thin(arr2,3,0)

	print(new)


if __name__ == "__main__":
    main()



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



