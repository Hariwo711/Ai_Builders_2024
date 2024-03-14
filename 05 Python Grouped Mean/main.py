import numpy as np

# implement your solution here
def get_grouped_mean():
  sepeal_width = iris_data[:, 1].astype('f')
  sepeal_name = iris_data[:, -1].astype(str)
  grouped_data ={}
  for label, width in zip(sepeal_name,sepeal_width):
    if label not in grouped_data:
      grouped_data[label]=[]
    grouped_data[label].append(width)
  for names,all_width in grouped_data.items():
    mean_width = np.mean(all_width)
    print("[b'{}', {}]".format(names,mean_width))
  
# get data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_data = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# calculate grouped mean and print
grouped_mean = get_grouped_mean()
