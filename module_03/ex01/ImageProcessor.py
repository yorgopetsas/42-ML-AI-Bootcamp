from numpy import asarray
from matplotlib import image
from matplotlib import pyplot
from matplotlib import pyplot as plt
# from matplotlib import image as mpimg


class ImageProcessor():
	def __init__(self):
		pass


	def load(self, path):
		img = image.imread(path)
		print(f"\nImage dimentions: {img.shape[:-1]}\n")
		plt.imshow(img)
		plt.show()
		return(asarray(img))


	def display(self, array):
		# convert image to numpy array
		print(array)


def main():


	path = "42AI.png"
	my_obj = ImageProcessor()
	array = my_obj.load(path)
	my_obj.display(array)


if __name__ == "__main__":
    main()

