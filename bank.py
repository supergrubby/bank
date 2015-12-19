from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

data = []
target = []
feature_names = ["age", "job", "marital", "education", "default", "balance", "housing", "loan"]
target_names = ["yes", "no"]
count = {"00": 0, "01": 0, "10": 0, "11": 0}


def calculate_types(result):
    for item in result:
        if item[0] == '0' and item[1] == '0':
            count["00"] += 1
        elif item[0] == '0' and item[1] == '1':
            count["01"] += 1
        elif item[0] == '1' and item[1] == '0':
            count["10"] += 1
        elif item[0] == '1' and item[1] == '1':
            count["11"] += 1


def calculate_accuracy_precision_recall():
    accuracy = float((count["11"] + count["00"])) / float(count["11"] + count["01"] + count["10"] + count["00"])
    precision = float(count["11"]) / float(count["11"] + count["01"])
    recall = float(count["11"]) / float(count["11"] + count["10"])
    f = 2 * precision * recall / (precision + recall)
    return accuracy, precision, recall, f


def load_data():
    with open("processed-bank-additional-full.csv") as data_source:
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
    graph.write_pdf("bank-20.pdf")


load_data()
print(len(data))
print(len(target))

clf = tree.DecisionTreeClassifier(max_leaf_nodes=20)
clf = clf.fit(data, target)

generate_tree_pdf()

result = clf.predict(data)
print(result)

with open("result.txt", "w") as outfile:
    outfile.write("\n".join(result))

evaluation = clf.score(data, target)
print(evaluation)

to_be_counted = []

print(len(target))
print(len(result))

for i in range(0, len(result)):
    unit = []
    unit.append(target[i])
    unit.append(result[i])
    to_be_counted.append(unit)

# print(to_be_counted)

print(count)

calculate_types(to_be_counted)

print(count)

print("accu, precision, recall, f:")
print(calculate_accuracy_precision_recall())