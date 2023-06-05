import numpy as np
import random
# from sklearn.preprocessing import MinMaxScaler
import csv



########################################################################
# HAVE TO FINISH THE METHOD FOR DEFINITION OF MEAN OF CLUSTERED POINTS
########################################################################


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


	def get_mean(self, source, data):


		x=y=z=0
		cnt = 0
		for d in data:
			if d[0] in source:
				print(d)
				# print(d[1],d[2],d[3])
				# x+=d[1]
				# y+=d[2]
				# z+=d[3]
				# cnt+=1


		# res = [x/cnt, y/cnt, z/cnt]
		res = "blah"


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


		dicts = {}
		lst = []


		for elem in starting_centroids:
			dicts[elem] = []


		# Calculate shortest distance
		for i,zz in enumerate(data):
			if i == 0:
				continue
			res = 10000000000000000000000000000
			tmp_id = 0
			for sp in data_2:
				distance = self.get_dist(zz,sp)
				if distance < res:
					res = distance
					tmp_id = sp[0]
			# print(f"Smallest Distance {zz[0]} is {res} and is for {tmp_id}")
			dicts[int(tmp_id)].append(int(zz[0]))


		for k,v in dicts.items():
			print(k,v)
			meanz = self.get_mean(v, data)
			print(meanz)



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


#########
# END
########
	# Create dictionary for each centroid
	# for it in data_2:
	# 	dict_name = "di_" + str(it[0])
	# 	# Create dictionary with key as item value
	# 	globals()[dict_name] = {it[0]: None}
	# 	print(dict_name)

	# for it in data_2:
	# 	print(type('di_' + str(it[0])))
	# print(dicts)