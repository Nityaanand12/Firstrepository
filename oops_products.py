
class product:
    def __init__(x,name,quantity,price):
        x.name = name
        x.quantity = quantity
        x.price = price
    def get(x):
        return x.name,x.quantity, x.price
    def get_salesprice(x):
        pass
    def get_costprice(x):
        pass
    
class warehouse:
    def __init__(y,sqftprice,address,area,pin):
        y.sqftprice=sqftprice
        y.address=address
        y.area = area
        y.pin = pin
    def connect(y):
        import psycopg2
        con = psycopg2.connect(dbname='app',user='postgres',password='root',host='localhost',port=5432)
        return con,con.cursor()
    def create_table(y):
        con,cur = y.connect()
        print(con,cur)
        cur.execute("create table details(id serial primary key,sqftprice int,address varchar(250),area int,pin int)")
        con.commit()
        con.close()
    def create(y):
        con,cur = y.connect()
        cur.execute("insert into details(sqftprice,address,area,pin) values(%s,'%s',%s,%s)"%(y.sqftprice,y.address,y.area,y.pin))
        con.commit()
        con.close()
    def delete(y):
        con,cur = y.connect()
        cur.execute("delete from details where sqftprice=%s and address='%s'and area=%s and pin=%s"%(y.sqftprice,y.address,y.area,y.pin))
        con.commit()
        con.close()
    def update(y,place):
        con,cur = y.connect()
        cur.execute("update details set area=%s where sqftprice=%s and address='%s'and area=%s and pin=%s"%(place,y.sqftprice,y.address,y.area,y.pin))
        con.commit()
        con.close()
    def browse(y):
        con,cur = y.connect()
        cur.execute("select * from details where sqftprice=%s and address='%s' and area=%s and pin=%s"%(y.sqftprice,y.address,y.area,y.pin))
        data = cur.fecthone()
        print(data)
        con.close()
