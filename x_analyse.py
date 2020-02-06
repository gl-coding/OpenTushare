#encoding=utf8
import os
import time
import x_utils as ut

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def write_stock():
    ut.class_stock()
    ut.concept_stock()
    ut.area_stock()
    ut.sme_stock()
    ut.gem_stock()
    ut.hs300_stock()
    ut.sz50_stock()
    ut.zz500_stock()

def write_all_data():
    filename = "id.all"
    with open(filename) as f:
        counter = 0
        for line in f:
            counter += 1
            sid = line.strip().split("\t")[0]
            #print sid
            try:
                ut.get_daily_info(sid)
                print "counter:" + str(counter)
            except:
                print "error:" + str(counter)

def gen_type_dic(filename, idx=2):
    res = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            split_res = line.split("\t")
            code = split_res[0]
            val = split_res[idx]
            if code in res:
                res[code].add(val)
            else:
                res[code] = set([val])
    return res

def merge_sid_info():
    fout = ut.ropen("id.merge")
    ids = []
    dict_name  = gen_type_dic("id.all", 1)
    dict_area  = gen_type_dic("data/log.area")
    dict_class = gen_type_dic("data/log.class")
    dict_concept = gen_type_dic("data/log.concept")

    ids.extend(dict_name.keys())
    ids.extend(dict_area.keys())
    ids.extend(dict_class.keys())
    ids.extend(dict_concept.keys())

    ids = list(set(ids))
    ids.sort()

    #print dict_area
    #print dict_class
    #print dict_concept

    for i in ids:
        name = dict_name.get(i, ["noname"])
        name = "_".join(name)
        area = dict_area.get(i, ["noarea"])
        area = "_".join(area)
        clas = dict_class.get(i, ["noclass"])
        clas = "_".join(clas)
        conc = dict_concept.get(i, ["noconcept"])
        conc = "_".join(conc)
        print >> fout, "\t".join([i, name, area, clas, conc])

def update_daily(fin_name, date_str=""):
    if date_str == "":
        date_str = time.strftime("%Y-%m-%d", time.localtime())

    name = "data_daily/stock_detail." + date_str
    fout = ut.ropen(name)

    name = "data_daily/stock_detail." + date_str + ".err"
    ferr = ut.ropen(name)

    with open(fin_name) as f:
        counter = 0
        for line in f:
            counter += 1
            if counter == 1:
                continue
            line = line.strip()
            split_res = line.split("\t")
            code = split_res[0]
            print code
            try:
                res = ut.get_stock_info(code, date_str)
                res = code + "\t" + res
                print >> fout, res
            except:
                print >> ferr, code

if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "category":
        #write all kinds of ids
        write_stock()
    elif arg == "detail":
        #write all data of id
        write_all_data()
    elif arg == "merge":
        merge_sid_info()
    elif arg == "basic":
        ut.get_stock_basics()
    elif arg == "update":
        date_str = "2020-02-03"
        date_str = "2020-02-04"
        date_str = "2020-02-05"
        date_str = "2020-02-06"
        date_str = "2020-02-03"
        #update_daily("data/log.basics", date_str)
        code = "603290"
        res = ut.get_stock_info(code, date_str)
        print res
    else:
        print "arg error"
