#encoding=utf8
import os
import time
import tushare as ts

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def ropen(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return open(filename, "a+")

def gen_stock_dic(df, names, filename, idx=False):
    fin = ropen(filename)
    print >> fin, "\t".join(names)
    for index, row in df.iterrows():
        in_list = []
        if idx != False:
            in_list.append(index)
        for name in names:
            in_list.append(str(row[name]).decode("utf8"))
        print >> fin, "\t".join(in_list)

def gen_stock_line(df, names):
    res = []
    for index, row in df.iterrows():
        #print index
        in_list = []
        for name in names:
            in_list.append(str(row[name]).decode("utf8"))
        res = in_list
    return res

def class_stock():
    df = ts.get_industry_classified()
    args = ["code", "name", "c_name"]
    gen_stock_dic(df, args, "data/log.class")

def concept_stock():
    df = ts.get_concept_classified()
    args = ["code", "name", "c_name"]
    gen_stock_dic(df, args, "data/log.concept")

def area_stock():
    df = ts.get_area_classified()
    args = ["code", "name", "area"]
    gen_stock_dic(df, args, "data/log.area")

def sme_stock():
    df = ts.get_sme_classified()
    args = ["code", "name"]
    gen_stock_dic(df, args, "data/log.middle")

def gem_stock():
    df = ts.get_gem_classified()
    args = ["code", "name"]
    gen_stock_dic(df, args, "data/log.chuangye")

def hs300_stock():
    df = ts.get_hs300s()
    args = ["code", "name"]
    gen_stock_dic(df, args, "data/log.hs300")

def sz50_stock():
    df = ts.get_sz50s()
    args = ["code", "name"]
    gen_stock_dic(df, args, "data/log.sz50")

def zz500_stock():
    df = ts.get_sz50s()
    args = ["code", "name"]
    gen_stock_dic(df, args, "data/log.zz500")

def get_daily_info(sid):
    df = ts.get_hist_data(sid)
    #args = ["open", "close", "high", "low", "volume", "price_change", "ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"]
    #print args
    args = df.columns.values.tolist()
    #print args
    gen_stock_dic(df, args, "data_id/log."+sid, idx=True)

def get_stock_basics():
    date_str = time.strftime("%Y_%m_%d", time.localtime())
    df = ts.get_stock_basics()
    args = df.columns.values.tolist()
    gen_stock_dic(df, args, "data/log.basics." + date_str, True)

def get_stock_info(code, date_str):
    #date_str = time.strftime("%Y-%m-%d", time.localtime())
    df = ts.get_hist_data(code, start=date_str, end=date_str)
    args = df.columns.values.tolist()
    #print args
    res = [date_str]
    res.extend(gen_stock_line(df, args))
    return "\t".join(res) 

def get_realtime_info():
    df = ts.get_today_all()
    #args = df.columns.values.tolist()
    #gen_stock_dic(df, args, "data/log.realtime")

if __name__ == "__main__":
    #get_realtime_info()
    #get_stock_basics()
    #get_stock_info('600848', '2020-02-05')
    get_daily_info("600848")
