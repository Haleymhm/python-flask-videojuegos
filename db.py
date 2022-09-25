import pymysql

def conexion_db():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='python_games')