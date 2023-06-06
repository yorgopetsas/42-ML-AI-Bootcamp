import numpy as np
import random
# from sklearn.preprocessing import MinMaxScaler
import csv



########################################################################
# HAVE TO FINISH THE METHOD FOR DEFINITION OF MEAN OF CLUSTERED POINTS
########################################################################


# class Points:
# 	def __init__(self, id, x, y, z):
# 		self.id = id
# 		self.x = x
# 		self.y = y
# 		self.z = z


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


	def get_mean(self, values, data):

		x=y=z=0
		cnt = 0
		md = 0
		
		for l in data:
			if cnt > 0:
				for v in values:
					if int(l[0]) == v:
						x+=float(l[1])
						y+=float(l[2])
						z+=float(l[3])
						md +=1
			cnt+=1

		id = 1000 + md
		res = [f'{id}', f'{x/md}', f'{y/md}', f'{z/md}']
		return(res)


	def get_dist(self, a, b):


		x1 = round(float(a[1]),5)
		x2 = round(float(b[1]),5)
		y1 = round(float(a[2]),5)
		y2 = round(float(b[2]),5)
		z1 = round(float(a[3]),5)
		z2 = round(float(b[3]),5)


		dis = ( ((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2) ) ** 0.5


		return(dis)


	def fit(self, X, centro=None):
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


		# Temp fixed centroides
		starting_centroids = [32, 12, 36, 58]
		
		# Randonmy chose a number in the range of the available IDs
		# starting_centroids = random.sample(range(0, (len(X)+1) + 1), 4)


		print(starting_centroids)

		
		# !!! 
		# Here I have to normalize the data:
		values = X[1:, 1:].astype(float)
		
		# print(values)
		data_2 = []


		# # Create data frame with the centroids
		if centro == None:
			for zz in X:
				try:
					if int(zz[0]) in starting_centroids:
						data_2.append(zz.tolist())
				except:
					pass
		else:
			data_2 = centro
		# print(data_2)
		# print()


		dicts = {}
		lst = []


		for elem in starting_centroids:
			dicts[elem] = []


		# # Calculate shortest distance
		for i,zz in enumerate(X):
			if i == 0:
				continue
			res = 10000000000000000000000000000
			tmp_id = 0
			for sp in data_2:
				distance = self.get_dist(zz,sp)
				if distance < res:
					res = distance
					tmp_id = sp[0]
			dicts[int(tmp_id)].append(int(zz[0]))


		meanz = []


		print(dicts)


		for k,v in dicts.items():
			meanz.append(self.get_mean(v, X))
		print(meanz)


		# self.fit(data, meanz)


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



#########
# END
#########

		# for every point in the array I have to calculate the difference to each centroid and return the smallest
		#
		# scaler = MinMaxScaler()
		# normalized_values = scaler.fit_transform(values)
		# data[1:, 1:] = normalized_values
