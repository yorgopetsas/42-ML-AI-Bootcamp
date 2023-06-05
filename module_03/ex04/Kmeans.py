import numpy as np
import random
# from sklearn.preprocessing import MinMaxScaler
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
	

	def __init__(self, max_iter=20, ncentroid=4):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids
	
	def get_dist(self, a, b):
		
		# print(a)
		# print(b)

		x1 = round(float(a[1]), 5)
		x2 = round(float(b[1]), 5)
        
		y1 = round(float(a[2]), 5)
		y2 = round(float(b[2]), 5)

		z1 = round(float(a[3]), 5)
		z2 = round(float(b[3]), 5)

		dis = ( ((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2) ) ** 0.5
		
		return(dis)
        
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
		starting_centroids = random.sample(range(0, (len(X)+1) + 1), 4)
		
		print(starting_centroids)

		
		# Have to Normalize data:
		values = data[1:, 1:].astype(float)

		data_2 = []
        
		
		# Create data frame with the centroids
		for zz in data:
			try:
				if int(zz[0]) in starting_centroids:
					data_2.append(zz.tolist())
			except:
				pass

		# Create dictionary for each centroid
		for it in data_2:
			dict_name = "di_" + str(it[0])
			# Create dictionary with key as item value
			globals()[dict_name] = {it[0]: None}


		# Calculate shortest distance0
		for i,zz in enumerate(data):
			res = 10000000000000000000
			tmp_id = 0
			for sp in data_2:
				if i != 0:
					distance = self.get_dist(zz,sp)
					# print(zz[0], distance, sp[0])
					if distance < res:
						res = distance
						tmp_id = sp[0]
			# print(f"Smallest Distance {zz[0]} is {res} and is for {tmp_id}")
			dict_name = "di_" + str(tmp_id)
			globals()[dict_name] = {tmp_id: [None]}
			# dict_name 
			print(dict_name)


			# print(f"Smallest Distance between {zz[0]} and {sp[0]} is {res}")
					# print(zz[0], distance, sp[0])


		# # Access and modify the dictionaries
		# di_30[30] = "Value of di_30"
		# di_95[95] = "Value of di_95"
		# di_94[94] = "Value of di_94"
		# di_26[26] = "Value of di_26"


        	# for every point in the array I have to calculate the difference to each centroid and return the smallest

		#
		# scaler = MinMaxScaler()
		# normalized_values = scaler.fit_transform(values)
		# data[1:, 1:] = normalized_values






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


	filepath='code.csv' 
	ncentroid=4
	max_iter=30


	with CsvReader("code.csv", header=True) as file:
		data = np.array(file.getdata())
            
                
	# k.get_dist(self, entries, point_1, point_2):
	k.fit(data)
	# k.get_dist(a,b)