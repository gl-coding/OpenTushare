import os
import sys
import numpy as np

def load_data(dateflag=False):
    base_dir = "../data_merge/"
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
                    split_res = []
                    if dateflag:
                        split_res.append(line.split("\t")[0])
                    split_res.extend([float(item) for item in line.split("\t")[1:]])
                    code_lines.append(split_res)
                kv_res[code] = code_lines
    return kv_res

def load_name():
    res_dict = {}
    with open("../data/log.basics") as f:
        for line in f:
            split_res = line.strip().split("\t")
            code = split_res[0]
            detail = split_res[1:4]
            res_dict[code] = detail
    return res_dict

def react():
    kv  = load_data(True)
    dic = load_name()
    data_list = []
    for k, v in kv.items():
        code = k
        name_list = dic.get(k, [])
        if len(name_list) == 0:
            continue
        name = "\t".join(name_list)
        if len(v) == 0 or len(v[-1]) < 8:
            continue
        #print v[-1]
        score = v[-1][7]
        data_list.append((code, name, float(score)))
    result = sorted(data_list, key=lambda x:x[2])
    for line in result:
        print line[0], line[1], line[2]

def gen_train_data():
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
    
    
if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "gen":
        gen_train_data ()
    else:
        react()
