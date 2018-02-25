import pymysql
import pymysql.cursors
class MySQL(object):
    '''
    connection=pymysql.connect(host ='localhost',
                                       user='root',
                                       password='xL889530',
                                       db='students',
                                       charset='utf8mb4')
    creat_sql = 'create table company(id int primary key not null,emp_name char(8) not null);'
    #drop_table = 'drop table company;'
    #with connection.cursor() as cursor:
        #cursor.execute(drop_table)  删除表
        #cursor.execute(creat_sql)
    
    with connection.cursor() as cursor:
        insert_sql = 'INSERT INTO company (id,emp_name) VALUES(%s,%s)'
        sql = 'select id, emp_name from company'
        #cursor.execute(insert_sql,(100,"XL"))
        #cursor.execute(insert_sql,(200,"yasuo"))
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    connection.commit()

    connection.close()
    '''
    def search_book_id(self,keyword):
        connection=pymysql.connect(host ='localhost',
                                       user='root',
                                       password='xL889530',
                                       db='students',
                                       charset='utf8mb4')
        #sql = 'select * from company where emp_name like "%s"'
        with connection.cursor() as cursor:
            cursor.execute('select id from company where emp_name like "%' + keyword + '%"')
            result_id = cursor.fetchall()
            
            #print(result_id[0][0])
            #print(type(result_id[0][0]))
            cursor.execute('select emp_name from company where emp_name like %s',keyword)
            result_emp_name = cursor.fetchall()
            #print(result_emp_name)
            return result_id[0][0]
            
a = MySQL()
id = a.search_book_id(keyword="XL")
print(type(id))

