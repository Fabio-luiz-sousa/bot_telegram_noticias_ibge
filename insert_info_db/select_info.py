from conn_db import conn_db
from datetime import datetime

def select_info_news(option):
    connection = conn_db()
    with connection:
        with connection.cursor() as cursor:
            if option == '1':
                def select_news_today():
                    sql = (
                        'SELECT * FROM ibge_noticias '
                        f'WHERE DAY(data_publicacao) = {datetime.now().day} '
                        f'AND MONTH(data_publicacao) = {datetime.now().month}'
                    )
                    cursor.execute(sql)
                    news_today = cursor.fetchall()
                    print(news_today)
            elif option == '2':
                def select_news_week():
                    sql = (
                        'SELECT * FROM ibge_noticias '
                        f'WHERE WEEK(data_publicacao) = 18'
                    )
                    cursor.execute(sql)
                    news_week = cursor.fetchall()
                    for id_news,titulo,introducao,data_publicacao,editorias,link in news_week:
                        return (
                            f'data publicação:{data_publicacao}' \
                            f'**{titulo}**\n' \
                            f'{introducao}\n' \
                            f'{editorias}\n'
                            f'link: {link}'
                        ) 
                
                return select_news_week()

