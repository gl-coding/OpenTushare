#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.web         #导入tornado模块下的web文件

import json
import os

GLOBAL_CODE_FILE = "log/log.code"

#post get communication, write and read
def write_code(code):
    filename = GLOBAL_CODE_FILE
    if os.path.exists(filename):
        os.remove(filename)
    fin = open(filename, "a+")
    print >> fin, code
    fin.flush()
    fin.close()

def read_code():
    res = ""
    with open(GLOBAL_CODE_FILE) as f:
        for line in f:
            res = line.strip()
    return res

#load stock history data
def read_data(sid):
    path = "../data_id/log." + sid
    res_data = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            res_item = []
            split_res = line.split("\t")

            date_str = split_res[0].replace("-", "/")
            data_list = [split_res[0], split_res[2], split_res[1], split_res[3]]
            data_item = [float(item) for item in data_list]

            res_item.append(date_str)
            res_item.extend(data_item)
            res_data.append(res_item)

    res_data.reverse()
    return res_data

def load_category_info():
    path = "../data/log.basics"
    res_data = {}
    with open(path) as f:
        counter = 0
        for line in f:
            counter += 1
            if counter == 1:
                continue
            line      = line.strip()
            split_res = line.split("\t")
            code      = split_res[0]
            detail    = "\t".join(split_res[1:3])
            res_data[code] = detail
    return res_data

stock_category_dict = load_category_info()

#return echart init page, receive arg 
class initPage(tornado.web.RequestHandler):
    global GLOBAL_CODE;
    def get(self):
        code = self.get_argument('code', 0)
        code = str(code)
        print "get:" + str(code)
        write_code(code)
        #print sid
        #res = read_data(sid)
        #res = json.dumps(res)
        #print res
        self.render("templete.html")

#return post request
class updatePage(tornado.web.RequestHandler):
    global GLOBAL_CODE;
    def post(self):
        res = self.request.body
        #print res
        #print type(res)

        code = read_code()
        print "post:" + code
        res_list = read_data(code)
        category = stock_category_dict(code)
        res_json = json.dumps({"res":res_list, "cate":category})

        self.write(res_json)

settings = {                                            #html文件归类配置，设置一个字典
    "template_path": "views",                           #键为template_path固定的，值为要存放HTML的文件夹名称
    "static_path":   "statics",                         #键为static_path固定的，值为要存放js和css的文件夹名称
}

#路由映射
application = tornado.web.Application(
    [                                                   #创建一个变量等于tornado.web下的Application方法
    (r"/init",   initPage),
    (r"/update", updatePage),
    ],
    **settings)                                          #将html文件归类配置字典，写在路由映射的第二个参数里

if __name__ == "__main__":
    #内部socket运行起来
    application.listen(8008)                            #设置端口
    tornado.ioloop.IOLoop.instance().start()
