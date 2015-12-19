from sklearn.datasets import load_iris
from sklearn import tree
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

def generate_tree_pdf():
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=iris.feature_names)
    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("demo.pdf")

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
# print(iris.data)
# print(iris.target)
#
# print(iris.feature_names)
# print(iris.target_names)
generate_tree_pdf()