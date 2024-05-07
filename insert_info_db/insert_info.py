import json

with open('data/news.json','r') as file:
    news = json.load(file)

for i in range(0,len(news['items'])):
    id_news = news['items'][i]['id']
    titulo = news['items'][i]['titulo']
    introducao = news['items'][i]['introducao']
    data_publicacao = news['items'][i]['data_publicacao']
    editorias = news['items'][i]['editorias']
    link = news['items'][i]['link']
    

