from matplotlib import image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import asarray


class ColorFilter():
	def __init__(self, path):
		pass

	
	def load(self, path):
		img = image.imread(path)
		print(f"\nImage dimentions: {img.shape[:-1]}\n")
		plt.imshow(img)
		plt.show()
		return(asarray(img))


	def to_blue(self, array):


		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		--> Authorized functions: .copy, .zeros,.shape,.dstack.
		--> Authorized operators: =.
		"""


		array = (array - np.min(array)) / (np.max(array) - np.min(array)) * 255
		array = array.astype(np.uint8)

		img_blue = np.copy(array)
		img_blue[:, :, 0] = 0
		img_blue[:, :, 1] = 0 
		plt.imsave('blue.png', img_blue)



	def to_red(self, array):


		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		--> Authorized functions: .copy, .to_green,.to_blue.
		--> Authorized operators: -,+, =.
		"""
		

		array = (array - np.min(array)) / (np.max(array) - np.min(array)) * 255
		array = array.astype(np.uint8)


		img_blue = np.copy(array)
		img_blue[:, :, 1] = 0
		img_blue[:, :, 2] = 0


		plt.imsave('red.png', img_blue)

	def to_green(self, array):


		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		--> Authorized functions: .copy
		--> Authorized operators: *, =.
		"""


		array = (array - np.min(array)) / (np.max(array) - np.min(array)) * 255
		array = array.astype(np.uint8)

		img_blue = np.copy(array)
		img_blue[:, :, 0] = 0
		img_blue[:, :, 2] = 0
		plt.imsave('green.png', img_blue)


	def invert(self, path):


		"""
		Inverts the color of the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		--> Authorized functions: .copy.
		--> Authorized operators: +,-,=.
		"""


		img = plt.imread(path)
		gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
		max_value = np.max(gray)
		gray_inv = max_value - gray
		gray_inv = (gray_inv - np.min(gray_inv)) / (np.max(gray_inv) - np.min(gray_inv))
		threshold = 0.2
		binary = np.greater(gray_inv, threshold)
		dots = np.zeros_like(gray_inv)
		dots[binary] = 1
		celluloid = dots * gray_inv
		celluloid = (celluloid - np.min(celluloid)) / (np.max(celluloid) - np.min(celluloid)) * 255
		celluloid = celluloid.astype(np.uint8)
		plt.imsave('celluloid_inv.png', celluloid, cmap='gray')


	def to_celluloid(self, path):


		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		--> Authorized functions: .copy, .arange,.linspace, .min, .max
		--> Authorized operators: =, <=, >, & (or and).
		"""


		img = plt.imread(path)

		gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

		gray = (gray - np.min(gray)) / (np.max(gray) - np.min(gray))

		threshold = 0.25 * (np.min(gray) + np.max(gray))
		binary = np.greater(gray, threshold)

		dots = np.zeros_like(gray)
		dots[binary] = 1

		celluloid = dots * gray

		celluloid = (celluloid - np.min(celluloid)) / (np.max(celluloid) - np.min(celluloid)) * 255
		celluloid = celluloid.astype(np.uint8)

		plt.imsave('celluloid.png', celluloid, cmap='gray') 


	def to_grayscale(self, array, filter, **kwargs):


		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = 'mean'/'m': performs the mean of RBG channels.
		For filter = 'weight'/'w': performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in ['m','mean','w','weight']
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		--> Authorized functions: .sum,.shape,.reshape,.broadcast_to,.as_type.
		--> Authorized operators: *,/, =
		"""		

def main():


	path = "elon_canaGAN.png"


	my_obj = ColorFilter(path)
	array = my_obj.load(path)


	# TEST BLUE
	my_obj.to_blue(array)
	# TEST RED
	my_obj.to_red(array)
	# TEST GREEN
	my_obj.to_green(array)
	# TEST CELLULOID
	my_obj.to_celluloid(path)
	# TEST INVERT
	my_obj.invert(path)


if __name__ == "__main__":
    main()

