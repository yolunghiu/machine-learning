from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

print(iris)

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([[7.7,  3. ,  6.1,  2.3]])
print (predictedLabel)