import pymysql
import os
import dotenv

dotenv.load_dotenv('container_mysql/.env')
print(os.environ['MYSQL_HOST'])
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        print(cursor)