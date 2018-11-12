'''Create Gender Data Picture'''

def genderData(file):
	import numpy as np

	genotypes=np.load(file)

	# Create a new PCA object.
	pca = PCA(n_components=3)

	# Find three principal components, and project the dataset onto them.
	# This outputs an array of three-dimensional vectors, one per sample.
	genotypes_fit = pca.fit_transform(genotypes)

	## Plot the dataset projected onto oe of the principal directions
	# Prepare axis for scatter, and for histogram to show distribution along axis.
	scatter_axes = plt.subplot2grid((3, 2), (1, 0), rowspan=2, colspan=2)
	x_hist_axes = plt.subplot2grid((3, 2), (0, 0), colspan=2,
								   sharex=scatter_axes)

	# Plot scatter of genotypes on PC 2
	scatter_axes.scatter(genotypes_fit[:,2], np.zeros_like(genotypes_fit[:,2]), color='blue', marker='.', s=3)

	# Plot histogram of distribution on PC2
	x_hist_axes.hist(genotypes_fit[:,2],histtype='step',bins=40)

	plt.savefig("scatter.png")




'''Analyze Populations'''

def analyzePopulations(flabel, file2):
	# Import required Python libraries and genotypes dataset
	from sklearn.decomposition import PCA
	import matplotlib.pyplot as plt
	import numpy as np
	labels=np.load(flabel)
	genotypes=np.load(file2)

	# Create a new PCA object.
	pca = PCA(n_components=3)

	# Find three principal components, and project the dataset onto them
	genotypes_fit = pca.fit_transform(genotypes)

	# Plot the dataset projected onto the two principal directions with labels
	for i in range(len(labels)):
		if labels[i] == 'LWK':
			color='green'
			lwk=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'YRI':
			color='purple'
			yri=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'MSL':
			color='orange'
			msl=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'ESN':
			color='blue'
			esn=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'GWD':
			color='black'
			gwd=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)

	# Create a legend
	plt.legend((lwk,yri,msl,esn,gwd),['Luhya in Webuye, Kenya',
												 'Yoruba in Ibadan, Nigeria','Mende in Sierra Leone',
												 'Esan in Nigeria','Gambian in Western Divisions'], scatterpoints=1, 
												   loc='upper right',ncol=1,fontsize=8)
	plt.xlabel("PC 1")
	plt.ylabel("PC 2")
	plt.savefig('pca.png')



'''Genotype Average'''

def genotypeAvg():
	import numpy as np

	# Y-chromosome genotypes and their frequencies in the three populations (Icelandic, Nordic, and Irish)
	y = np.array([[1, 1, 1, 0, 0, 0, 0],
				  [0, 0, 1, 0, 0, 0, 0],
				  [1, 1, 0, 0, 0, 0, 0],
				  [0, 1, 1, 1, 1, 1, 1]])
	freq_y = np.array([[0.41, 0.26, 0.82],
					   [0.34, 0.51, 0.15],
					   [0.23,0.18,0],
					   [0.01,0.03,0.42]])

	# Mitochondrial genotypes and theif frequencies in the three populations (Icelandic, Nordic, and Irish)
	m = np.array([[1,1,1,0,1,0,0,0],
				  [0,0,1,1,0,1,0,0],
				  [0,0,1,1,1,1,1,0],
				  [0,0,0,0,1,0,0,1],
				  [1,0,0,0,0,1,0,0]])
	freq_m = np.array([[0.6, 0.29, 0.7],
					   [0.14, 0.52, 0.21],
					   [0.40,0.04,0.35],
					   [0.04,0.65,0.03],
					   [0.08,0.16,0.07]])

	# Calculate average y-chromosome and mitochondrial genotypes for each population
	avg_y =[]
	avg_m =[]
	for i in range(3):
		avg_y.append(freq_y[0,i]*y[0,:]+freq_y[1,i]*y[1,:]+freq_y[2,i]*y[2,:]+freq_y[3,i]*y[3,:])
		avg_m.append(freq_m[0,i]*m[0,:]+freq_m[1,i]*m[1,:]+freq_m[2,i]*m[2,:]+freq_m[3,i]*m[3,:]+freq_m[4,i]*m[4,:])
	avg_y = np.array(avg_y)
	avg_m = np.array(avg_m)

	# Generate the two distance matrices
	map_y = np.zeros((3,3))
	map_m = np.zeros((3,3))
	for i in range(3):
		for j in range(3):
			map_y[i,j]= np.sqrt(np.sum((avg_y[i,:]-avg_y[j,:])**2))
			map_m[i,j]= np.sqrt(np.sum((avg_m[i,:]-avg_m[j,:])**2))

	print(avg_y)
	print(avg_m)

	import matplotlib.pyplot as plt
	plt.imshow(map_y)
	plt.colorbar()
	plt.savefig("map_y.png")
	plt.imshow(map_m)
	plt.savefig("map_m.png")




''' Know Ancestry '''

def knowAncestry(flabel1, file3):
	# Import required Python libraries and genotypes dataset
	from sklearn.decomposition import PCA
	import matplotlib.pyplot as plt
	import numpy as np
	labels=np.load(flabel1)
	genotypes=np.load(file3)

	# Create a new PCA object.
	pca = PCA(n_components=3)

	# Find three principal components, and project the dataset onto them
	genotypes_fit = pca.fit_transform(genotypes)

	# Plot the dataset projected onto the two principal directions with labels
	for i in range(len(labels)):
		if labels[i] == 'LWK':
			color='green'
			lwk=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'YRI':
			color='purple'
			yri=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'MSL':
			color='orange'
			msl=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'ESN':
			color='blue'
			esn=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)
		elif labels[i] == 'GWD':
			color='black'
			gwd=plt.scatter(genotypes_fit[i,1],genotypes_fit[i,0], c=color)

	# Create a legend
	plt.legend((lwk,yri,msl,esn,gwd),['Luhya in Webuye, Kenya',
												 'Yoruba in Ibadan, Nigeria','Mende in Sierra Leone',
												 'Esan in Nigeria','Gambian in Western Divisions'], scatterpoints=1, 
												   loc='upper right',ncol=1,fontsize=8)
	plt.xlabel("PC 1")
	plt.ylabel("PC 2")
	plt.savefig('pca.png')

	sample = np.load("data/sample.npy")
	[[1, 1, 0, ..., 0, 0, 0]]
	sample_proj = pca.transform(sample)
	plt.scatter(sample_proj[0][1], sample_proj[0][0], c='red', marker='X', s = 500)
	plt.savefig('indi.png')
