import pymysql
import os
import dotenv

#carrega o arquivo .env
dotenv.load_dotenv('container_mysql/.env')
#função que conecta no servidor mysql
def conn_db():
    connection = pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
    )
    return connection