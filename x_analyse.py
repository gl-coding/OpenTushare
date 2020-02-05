#encoding=utf8
import os
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

def gen_type_dic(filename):
    res = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            split_res = line.split("\t")
            code = split_res[0]
            val = split_res[2]
            if code in res:
                res[code].add(val)
            else:
                res[code] = set([val])
    return res

def merge_sid_info():
    ids = []
    dict_area  = gen_type_dic("data/log.area")
    dict_class = gen_type_dic("data/log.class")
    dict_concept = gen_type_dic("data/log.concept")

    ids.extend(dict_area.keys())
    ids.extend(dict_class.keys())
    ids.extend(dict_concept.keys())

    ids = list(set(ids))
    ids.sort()

    print dict_area
    print dict_class
    print dict_concept

    for i in ids:
        area = dict_area.get(i, ["noarea"])
        area = "_".join(area)
        clas = dict_class.get(i, ["noclass"])
        clas = "_".join(clas)
        conc = dict_concept.get(i, ["noconcept"])
        conc = "_".join(conc)
        print "\t".join([i, area, clas, conc])

if __name__ == "__main__":
    #write all kinds of ids
    #write_stock()

    #write all data of id
    #write_all_data()

    merge_sid_info()
