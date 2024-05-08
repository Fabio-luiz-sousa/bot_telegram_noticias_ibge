from conn_db import conn_db
import json
from datetime import datetime

# conecta com o servidor mysql
connection = conn_db()

# carrega o json com as noticias
with open('data/news.json','r') as file:
    news = json.load(file)

# lista para armazenar as noticias
news_list_dict = list()

with connection:
    with connection.cursor() as cursor:
        # função que insere as noticias no banco de dados
        def insert_data():
            for i in range(0,len(news['items'])):
                id_news = news['items'][i]['id']
                titulo= news['items'][i]['titulo']
                introducao = news['items'][i]['introducao']
                date = news['items'][i]['data_publicacao'].replace('/','-')
                data_publicacao= datetime.strptime(date,"%d-%m-%Y %H:%M:%S")
                editorias = news['items'][i]['editorias']
                link = news['items'][i]['link']
                news_list_dict.append(
                    {'id_news':f'{id_news}','titulo':f'{titulo}','introducao':f'{introducao}','data_publicacao':f'{data_publicacao}',
                    'editorias':f'{editorias}','link':f'{link}'}
                )

            sql = (
                    'INSERT INTO ibge_noticias'
                    '(id_news,titulo,introducao,data_publicacao,editorias,link) '
                    'VALUES '
                    '(%(id_news)s, %(titulo)s, %(introducao)s, %(data_publicacao)s, %(editorias)s, %(link)s) '
                )
            cursor.executemany(sql,news_list_dict)
        insert_data()
    connection.commit()
    
    

