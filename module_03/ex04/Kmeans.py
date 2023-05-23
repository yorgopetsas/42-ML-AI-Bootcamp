import numpy as np

import csv

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header_state = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_obj = None
        self.fulldata = []
        self.header = []


    def __enter__(self):
        self.file_obj = open(self.filename, mode="r", encoding="utf-8")

        for i, line in enumerate(self.file_obj):
            self.fulldata.append(list(map(str.strip, line.split(self.sep))))

        if all(len(elem) == len(self.fulldata[0]) for elem in self.fulldata):
            return self
        else:
            return None


    def __exit__(self, type, value, traceback):
        # print('Exit')
        self.file_obj.close()
    

    def getdata(self):
        start = self.skip_top
        end = len(self.fulldata) - self.skip_bottom
        if self.header_state == True:
            self.header = self.fulldata[0]
        if self.header_state == True:
            tmp = self.fulldata[ start + 1 : end ]
            tmp.insert(0, self.header)
            self.fulldata = tmp
            return self.fulldata
        else:
            return self.fulldata[ start : end ]


    def getheader(self):
        if self.header_state == True:
            return(self.fulldata[0])
        else:
            return None







class KmeansClustering:
	

	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids
	

	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		None.
		Raises:
		-------
		This function should not raise any Exception.
		"""

		print('ohhh yeah')


def get_dist(self, entries, point_1, point_2):
		pass


	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
		This function should not raise any Exception.
		"""


if __name__ == "__main__":


	k = KmeansClustering()


	filepath='solar_system_census.csv' 
	ncentroid=4
	max_iter=30


	with CsvReader("solar_system_census.csv", header=True) as file:
		data = np.array(file.getdata())
            
                
	# k.get_dist(self, entries, point_1, point_2):
	# k.fit(data.astype(np.float))