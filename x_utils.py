#encoding=utf8
import os
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
    for index, row in df.iterrows():
        in_list = []
        if idx != False:
            in_list.append(index)
        for name in names:
            in_list.append(str(row[name]).decode("utf8"))
        print >> fin, "\t".join(in_list)

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
    args = ["open", "close", "high", "low", "volume", "price_change", "ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"]
    gen_stock_dic(df, args, "data_id/log."+sid, idx=True)

def get_realtime_info():
    df = ts.get_today_all()
    #args = df.columns.values.tolist()
    #gen_stock_dic(df, args, "data/log.realtime")

if __name__ == "__main__":
    get_realtime_info()
