#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn import cross_validation

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, random_state=42, test_size=0.3)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test, labels_test)

print "Accuracy Score: ", accuracy_score(pred, labels_test)

print "POI's predicted in test set: ", sum(pred)
print "Number of people in test set: ", len(pred)
print "If Identifier predicted 0, what is its accuracy: ", pred.tolist().count(0) / 29.0
print "\n"

n_true_positives = 0
for i in range(len(pred)):
    if (labels_test[i] == pred[i]) and labels_test[i] == 1:
        n_true_positives += 1
print "True Positives: ", n_true_positives

print "Precision Score: ", precision_score(pred, labels_test)
print "Recall Score: ", recall_score(pred, labels_test)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
n_true_positives = 0

for i in range(len(predictions)):
    if (predictions[i] == 1) and (true_labels[i] == 1):
        n_true_positives += 1
print "True Positives in Hypothetical Test: ", n_true_positives

n_true_negatives = 0

for i in range(len(predictions)):
    if (predictions[i] == 0) and (true_labels[i] == 0):
        n_true_negatives += 1
print "True Negatives in Hypothetical Test: ", n_true_negatives

n_false_positives = 0
for i in range(len(predictions)):
    if (predictions[i] == 1) and (true_labels[i] == 0):
        n_false_positives += 1
print "False Positives: ", n_false_positives

n_false_negatives = 0
for i in range(len(predictions)):
    if (predictions[i] == 0) and (true_labels[i] == 1):
        n_false_negatives += 1
print "False Negatives: ", n_false_negatives

print "Precision Score (Hypothetical): ", precision_score(true_labels, predictions)
print "Recall Score (Hypothetical): ", recall_score(true_labels, predictions)
