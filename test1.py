import MySQLdb
import datetime

'''连接数据库'''
conn = MySQLdb.connect(host = 'autocoach.cexuitmi8ofq.us-west-1.rds.amazonaws.com',

                             user = 'admin',

                             passwd = 'password',

                            database = 'ourdata',


                             charset = 'utf8')


cursor = conn.cursor()
filter_merge_data = [['Testid','test_name','1','1','1','o_x','o_y','o_z','str(datetime.time)']]
filter_merge_len = len(filter_merge_data)
for x in range(filter_merge_len):
    try:
        temp=filter_merge_data[x]
        sql = "INSERT INTO rawdata VALUES('"+temp[0]+"','"+temp[1]+"','"+temp[2]+"','"+temp[3]+"','"+temp[4]+"','"+temp[5]+"','"+temp[6]+"','"+temp[7]+"','"+temp[8]+"' );"
        print(sql)
        cursor.execute(sql
            )
        # insert data
        conn.commit()
    except Exception as e:
        print('Insert Failed')


# close
conn.commit()
cursor.close()
conn.close()