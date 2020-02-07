import os
import sys
import numpy as np

from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import svm

def load_data():
    data = []
    tar  = []
    with open("train.txt") as f:
        counter = 0
        for line in f:
            counter += 1
            split_res = line.strip().split("\t")
            data_item = [float(item) for item in split_res[3:-1]]
            tar_item  = int(split_res[-1])
            data.append(data_item)
            tar.append(tar_item)
            if counter == 50000:
                break
    return data, tar

if __name__ == "__main__":
    data, tar = load_data()
    clf = DecisionTreeClassifier()
    #print cross_val_score(clf, data, tar, cv=10)
    X_train, X_test, y_train, y_test = train_test_split(data, tar, test_size=0.4, random_state=0)
    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(X_train, y_train)
    print clf.score(X_test, y_test)
