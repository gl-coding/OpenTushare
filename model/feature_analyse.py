import os
import sys

def load_data():
    base_dir = "../data_id/"
    kv_res = {}
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            filename = os.path.join(root, f)
            print filename
            with open(filename) as f:
                code = filename.split(".")[-1]
                code_lines = []
                counter = 0
                for line in f:
                    counter += 1
                    if counter == 1:
                        continue
                    line = line.strip()
                    split_res = line.split("\t")
                    code_lines.append(split_res)
                kv_res[code] = code_lines
    return kv_res
                

if __name__ == "__main__":
    load_data()
