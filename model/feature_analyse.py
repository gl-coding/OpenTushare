import os
import sys
import numpy as np

from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import cross_val_score
clf = DecisionTreeClassifier()

def load_data():
    base_dir = "../data_id/"
    kv_res = {}
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            filename = os.path.join(root, f)
            #print filename
            with open(filename) as f:
                code = filename.split(".")[-1]
                code_lines = []
                counter = 0
                for line in f:
                    counter += 1
                    if counter == 1:
                        continue
                    line = line.strip()
                    split_res = [float(item) for item in line.split("\t")[1:]]
                    code_lines.append(split_res)
                kv_res[code] = code_lines
    return kv_res

if __name__ == "__main__":
    train = open("train.txt", "a+")
    kv = load_data()
    for k, v in kv.items():
        print k
        data = np.array(v)
        dt = data.T

        #print dt_date
        dt_part = dt[0:4]
        if len(dt_part) == 0:
            continue
        total = len(dt_part[0])
        for i in range(total-4):
            #get feature
            data = dt_part[:,i:i+3]
            #print data
            
            #get label
            pre  = dt_part[:,i+4]
            #print pre
            open_val = pre[0]
            close_val = pre[2]
            label = 1 if open_val - close_val < 0 else 0
            #print label
            
            #normalize
            amin, amax = data.min(), data.max()
            a = (data - amin) / (amax - amin)
            data_list = a.reshape(1,12).tolist()[0]
            #print data_list
            line = "\t".join([str(item) for item in data_list])
            line = line + "\t" + str(label)
            print >> train, line
            #break
        #break
    
