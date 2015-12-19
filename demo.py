from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(iris.data, iris.target)
print(iris.data)
print(iris.target)

print(iris.feature_names)
print(iris.target_names)