#encoding=utf8
import tushare as ts

###交易数据

#一次性获取全部日k线数据
#print ts.get_hist_data('300001')
print ts.get_hist_data('600848')

#实时行情, 一次性获取当前交易所有股票的行情数据
#print ts.get_today_all()

#df = ts.get_tick_data('600848', start='2020-01-07')
#print df.head(10)

#获取实时分笔数据，可以实时取得股票当前报价和成交信息
#df = ts.get_realtime_quotes('000581') #Single stock symbol
#print df[['code','name','price','bid','ask','volume','amount','time']]

#symbols from a list
#df = ts.get_realtime_quotes(['600848','000980','000981'])
#print df
#from a Series
#print ts.get_realtime_quotes(df['code'].tail(10))  #一次获取10个股票的实时分笔数据

#大单数据
#print ts.get_sina_dd('600848', date='2019-12-24') #默认400手

#大盘数据
#print ts.get_index() 

#上证指数
#print ts.get_realtime_quotes('sh')
#上证指数 深圳成指 沪深300指数 上证50 中小板 创业板
#print ts.get_realtime_quotes(['sh','sz','hs300','sz50','zxb','cyb'])
#或者混搭
#print ts.get_realtime_quotes(['sh','600848'])




###参考数据

#分配预案
#df = ts.profit_data(top=60)
#print df

#获取2014年中报的业绩预告数据
#print ts.forecast_data(2014,2)

#获取每个季度基金持有上市公司股票的数据。
#print ts.fund_holdings(2014, 4)

#获取IPO发行和上市的时间列表，包括发行数量、网上发行数量、发行价格已经中签率信息等。
#print ts.new_stocks()

#沪市的融资融券数据从上海证券交易所网站直接获取
#print ts.sh_margins(start='2015-01-01', end='2015-04-19')

###分类数据

#行业分类
#print ts.get_industry_classified()

#概念分类
#print ts.get_concept_classified()

#地域分类
#print ts.get_area_classified()

#中小板分类
#print ts.get_sme_classified()

#创业板分类
#print ts.get_gem_classified()

#风险警示板分类
#print ts.get_st_classified()

#沪深300成份及权重
#print ts.get_hs300s()

#上证50成份股
#print ts.get_sz50s()

#中证500成份股
#print ts.get_zz500s()

#终止上市股票列表, error
#print ts.get_terminated()

#暂停上市股票列表, error
#print ts.get_suspended()

#获取沪深上市公司基本情况
#print ts.get_stock_basics()





###基本面

#股票列表
#df = ts.get_report_data(2019, 3)
#for i in df['code'].values: print i


#业绩报告
#print ts.get_profit_data(2019,3)

#盈利能力
#print ts.get_profit_data(2019, 4)

#营运能力
#print ts.get_operation_data(2019,3)

#成长能力
#获取2014年第3季度的成长能力数据
#print ts.get_growth_data(2019, 3)

#获取2014年第3季度的现金流量数据
#print ts.get_cashflow_data(2014,3)




###龙虎榜
#按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据。
#print ts.top_list('2020-01-07')

#个股上榜统计
#print ts.cap_tops()

#营业部上榜统计
#print ts.broker_tops()

#获取机构近5、10、30、60日累积买卖次数和金额等情况。
#print ts.inst_tops()

#获取最近一个交易日机构席位成交明细统计数据
#print ts.inst_detail()
