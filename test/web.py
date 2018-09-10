from Util.ChoiceUtil import Choice
from Util.ConnUtil import Oracle
from Util.LogUtil import get_log

#连接日志
logger = get_log('数据实验')
logger.info('开始实验')
#choice登陆
c = Choice()
c.login()

# 连接数据库
db = Oracle()
conn = db.get_conn()
cursor = conn.cursor()

#日志
# logger.error('有错误发生!', exc_info=1)
# logger.info('你好啊')

#choice
StartDate_2018=0
codes=0
EndDate=0
#取数据
data=c.csd("000001.OF,000003.OF,000004.OF,000005.OF,000008.OF,000009.OF,000010.OF,000011.OF,000013.OF,000014.OF","FUNDSCALE,UNITNAV,ADJUSTEDNAV,YIELDOF7DAYS,10KUNITYIELD,UNITTOTAL","2018-09-01","2018-09-10","period=1,adjustflag=1,curtype=1,pricetype=1,order=1,market=CNSESH")
#数据库
sql_query="insert into TEST1(CODE,FUNDSCALE,UNITNAV,ADJUSTEDNAV,YIELDOF7DAYS,KUNITYIELD,UNITTOTAL) values(:1,:2,:3,:4,:5,:6,:7)"

print(data.Data['000001.OF'])
update_data=[]
# for k,v in data.Data.items():
#     for lit in v:
#        lit.insert(0,k)
#        update_data.append(lit)
    # print(k,v)
# try:
#     # 存数据
#     cursor.executemany(sql_query, update_data)
#     conn.commit()
# except Exception as e:
#     logger.error('插入错误', exc_info=1)


# 关闭数据库连接和游标以及choice
db.close_all(cursor, conn)
c.close()
logger.info('插入成功')

