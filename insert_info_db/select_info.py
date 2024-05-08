from conn_db import conn_db
from datetime import datetime

# função que contem as funções para selecionar as noticas do dia, da semana, do mes e do ano
def select_info_news(option):
    connection = conn_db()
    with connection:
        with connection.cursor() as cursor:
            if option == '1':
                # função que seleciona as noticas do dia
                def select_news_today():
                    sql = (
                        'SELECT * FROM ibge_noticias '
                        f'WHERE DAY(data_publicacao) = {datetime.now().day} AND MONTH(data_publicacao) = {datetime.now().month}'
                    )
                    cursor.execute(sql)
                    news_today = cursor.fetchall()
                    news_list = list()
                    if len(news_today)!=0:
                        for id_news,titulo,introducao,data_publicacao,editorias,link in news_today:
                            news_list.append(f'*********\ndata publicação: {data_publicacao}\n\n{titulo}\n\n{introducao}\n{link}\n*********\n')
                        news_list = '\n'.join(news_list)
                        print(news_list)
                    else:
                        news_list  = 'Não há notícias para hoje ainda!'
                    return news_list
                return select_news_today()
            elif option == '2':
                # função que seleciona as noticas da semana
                def select_news_week():
                    sql = (
                        'SELECT * FROM ibge_noticias '
                        f'WHERE WEEK(data_publicacao) = {datetime.now().strftime('%U')}'
                    )
                    cursor.execute(sql)
                    news_week = cursor.fetchall()
                    news_list = list()
                    if len(news_week)!=0:
                        for id_news,titulo,introducao,data_publicacao,editorias,link in news_week:
                            news_list.append(f'*********\ndata publicação: {data_publicacao}\n\n{titulo}\n\n{introducao}\n{link}\n*********\n')
                        news_list = '\n'.join(news_list)
                        print(news_list)
                    else:
                        news_list = 'Não há noticias para essa semana ainda!'
                    return news_list
                return select_news_week()       

                

                