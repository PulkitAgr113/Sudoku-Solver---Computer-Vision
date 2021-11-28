class SlowMatrix:

	## The constructor
	# @param matrix A 2d Python list containing data
	def __init__(self, matrix):
		self.matrix = matrix

	## Matrix multiplication
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __matmul__(self, mat2):
		result = SlowMatrix([ [0]*len(mat2.matrix[0]) for i in range(len(self.matrix)) ])
		for i in range(len(self.matrix)):
			for j in range(len(mat2.matrix[0])):
				for k in range(len(mat2.matrix)):
					result[(i,j)] += self[(i,k)] * mat2[(k,j)]

		return result

	## Element wise multiplication
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __mul__(self, mat2):
		result = self
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				result[(i,j)] = self[(i,j)] * mat2[(i,j)]

		return result

	## Element wise addition
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __add__(self, mat2):
		result = self
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				result[(i,j)] = self[(i,j)] + mat2[(i,j)]

		return result

	## Element wise subtraction
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __sub__(self, mat2):
		result = self
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				result[(i,j)] = self[(i,j)] - mat2[(i,j)]

		return result

	## Equality operator
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __eq__(self, mat2):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				if(self[(i,j)] != mat2[(i,j)]):
					return False

		return True

	## Calculate transpose
	def transpose(self):
		for i in range(len(self.matrix)):
			for j in range(i,len(self.matrix[0])):
				temp = self[(i,j)]
				self[(i,j)] = self[(j,i)]
				self[(j,i)] = temp


	## Creates a SlowMatrix of 1s
	# @param shape A python pair (row, col)
	def ones(shape):
		return SlowMatrix([ [1]*shape[0] for i in range(shape[1]) ])

	## Creates a SlowMatrix of 0s
	# @param shape A python pair (row, col)
	def zeros(shape):
		return SlowMatrix([ [0]*shape[0] for i in range(shape[1]) ])

	## Returns i,jth element
	# @param key A python pair (i,j)
	def __getitem__(self, key):
		return self.matrix[key[0]][key[1]]

	## Sets i,jth element
	# @param key A python pair (i,j)
	# #param value Value to set
	def __setitem__(self, key, value):
		self.matrix[key[0]][key[1]] = value

	## Converts SlowMatrix to a Python string
	def __str__(self):
		string = ""
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				string += str(self[(i,j)]) + " "

		return string