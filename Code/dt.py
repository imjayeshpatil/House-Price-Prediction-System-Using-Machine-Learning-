# CART on the Bank Note dataset
from random import seed
from random import randrange


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column])


# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split


# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores


# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)
    return gini


# Select the best split point for a dataset
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 2):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}


# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    #return max(set(outcomes), key=outcomes.count)
    classify=[0,0,0]
    for out in outcomes:
	    classify[(int(out))]+=1
    if(classify[0]>classify[1]):
	    return 0
    elif (classify[1]>classify[2]):
        return 1
    else:
	    return 2


# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del (node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)


# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root


# Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


# Classification and Regression Tree Algorithm
def decision_tree(train, test, max_depth, min_size):    
    tree = build_tree(train, max_depth, min_size)
    predictions = list()
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return (predictions)



seed(1)
# load and prepare data
# dataset = [[8450,7,5,2003,856,208500,2],
  # [9600,6,8,1976,1262,181500,2],
  # [9600,6,8,1976,1262,181500,2],
  # [9600,6,8,1976,1262,181500,2],
  # [11250,7,5,2001,920,223500,2],
  # [9550,7,5,1915,756,140000,1],
  # [9550,7,5,1915,756,140000,1],
  # [9550,7,5,1915,756,140000,1],
  # [9550,7,5,1915,756,140000,1],
  # [9550,7,5,1915,756,140000,1],
  # [9550,7,5,1915,756,140000,1],
  # [9550,7,5,1915,756,140000,0],
  # [9550,7,5,1915,756,140000,0],
  # [14260,8,5,2000,1145,250000,2],
  # [14115,5,5,1993,796,143000,1],
  # [10084,8,5,2004,1686,307000,2],
  # [10382,7,6,1973,1107,200000,2],
  # [6120,7,5,1931,952,129900,1],
  # [7420,5,6,1939,991,118000,1],
  # [11200,5,5,1965,1040,129500,1],
  # [11924,9,5,2005,1175,345000,2],
  # [12968,5,6,1962,912,144000,1],
  # [10652,7,5,2006,1494,279500,2],
  # [10920,6,5,1960,1253,157000,2],
  # [6120,7,8,1929,832,132000,1],
  # [11241,6,7,1970,1004,149000,1],
  # [10791,4,5,1967,0,90000,0],
  # [13695,5,5,2004,1114,159000,2],
  # [7560,5,6,1958,1029,139000,1],
  # [14215,8,5,2005,1158,325300,2],
  # [7449,7,7,1930,637,139400,1],
  # [9742,8,5,2002,1777,230000,2],
  # [4224,5,7,1976,1040,129900,1],
  # [8246,5,8,1968,1060,154000,2],
  # [14230,8,5,2007,1566,256300,2],
  # [7200,5,7,1951,900,134800,1],
  # [11478,8,5,2007,1704,306000,2],
  # [16321,5,6,1957,1484,207500,2],
  # [6324,4,6,1927,520,68500,0],
  # [8500,4,4,1920,649,40000,0],
  # [8544,5,6,1966,1228,149350,1],
  # [11049,8,5,2007,1234,179900,2],
  # [10552,5,5,1959,1398,165500,2],
  # [7313,9,5,2005,1561,277500,2],
  # [13418,8,5,2004,1117,309000,2],
  # [10859,5,5,1994,1097,145000,1],
  # [8532,5,6,1954,1297,153000,2],
  # [7922,5,7,1953,1057,109000,1],
  # [6040,4,5,1955,0,82000,0],
  # [8658,6,5,1965,1088,160000,2],
  # [16905,5,6,1959,1350,170000,2],
  # [9180,5,7,1983,840,144000,1],
  # [9200,5,6,1975,938,130250,1],
  # [7945,5,6,1959,1150,141000,1],
  # [7658,9,5,2005,1752,319900,2],
  # [12822,7,5,2003,1434,239686,2],
  # [11096,8,5,2006,1656,249700,2],
  # [4456,4,5,1920,736,113000,1],
  # [7742,5,7,1966,955,127000,1],
  # [13869,6,6,1997,794,177000,2],
  # [6240,6,6,1934,816,114500,1],
  # [8472,5,5,1963,816,110000,1],
  # [50271,9,5,1981,1842,385000,2],
  # [7134,5,5,1955,384,130000,1],
  # [10175,6,5,1964,1425,180500,2],
  # [2645,8,5,1999,970,172500,2],
  # [11645,7,5,2004,860,196500,2],
  # [13682,10,5,2006,1410,438780,2],
  # [7200,5,7,1972,780,124900,1],
  # [13072,6,5,2004,1158,158000,2],
  # [7200,5,7,1920,530,101000,1],
  # [6442,8,5,2006,1370,202500,2],
  # [10300,7,6,1921,576,140000,1],
  # [9375,7,5,1997,1057,219500,2],
  # [9591,8,5,2004,1143,317000,2],
  # [19900,7,5,1970,1947,180000,2],
  # [10665,7,5,2003,1453,226000,2],
  # [4608,4,6,1945,747,80000,0],
  # [15593,7,4,1953,1304,225000,2]]

# 2- high 
# 1- medium
# 0 - low

# convert string attributes to integers
# for i in range(len(dataset[0])):
    # str_column_to_float(dataset, i)
# evaluate algorithm
n_folds = 5
max_depth = 5
min_size = 10
#scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)

# print ('============ 1. Testing input =================')
# print ('============== Hight 2 (9600,6,8,1976,1262)==========')
# predictions = decision_tree(dataset, [[9550,7,5,1915,756,-1]], max_depth, min_size)
# print (str(predictions))

# print ('============== Medium 1 (8472,5,5,1963,816,110000,1)==========')
# predictions = decision_tree(dataset, [[8472,5,5,1963,816,110000]], max_depth, min_size)
# print (str(predictions))

# print ('============== Low 0 (4608,4,6,1945,747,80000,0)==========')
# predictions = decision_tree(dataset, [[4608,4,6,1945,747,80000]], max_depth, min_size)
# print (str(predictions))

# print ('============ 2. Testing input =================')

# print ('============== Hight 2 ([11478,8,5,2007,1704,306000,2])==========')
# predictions = decision_tree(dataset, [[11478,8,5,2007,1704,306000]], max_depth, min_size)
# print (str(predictions))

# print ('============== Medium 1 (6120,7,8,1929,832,132000,1)==========')
# predictions = decision_tree(dataset, [[6120,7,8,1929,832,132000]], max_depth, min_size)
# print (str(predictions))

# print ('============== low 0 (10791,4,5,1967,0,90000,0)==========')
# predictions = decision_tree(dataset, [[10791,4,5,1967,0,90000]], max_depth, min_size)
# print (str(predictions))
