from matplotlib import image
from matplotlib import pyplot
from numpy import asarray


class ImageProcessor():
	def __init__(self):
		pass

	def load(self, path):
		img = image.imread(path)
		print(f"\nImage dimentions: {img.shape[:-1]}\n")
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