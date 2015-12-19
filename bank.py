from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

data = []
target = []
feature_names = ["age", "job", "marital", "education", "default", "balance", "housing", "loan"]
target_names = ["yes", "no"]


def load_data():
    with open("processed_bank.csv") as data_source:
        next(data_source)
        for line in data_source:
            item = line.strip().split(",")
            data.append(item[:-1])
            target.append(item[len(item) - 1])


def generate_tree_pdf():
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=feature_names)
    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("bank.pdf")

load_data()
print(len(data))
print(len(target))

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, target)

generate_tree_pdf()

result = clf.predict(data[:100])
print(result)

with open("result.txt","w") as outfile:
    outfile.write("\n".join(result))
