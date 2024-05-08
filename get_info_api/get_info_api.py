import requests
import json

# url da api contendo as noticias do ibge
url = 'https://servicodados.ibge.gov.br/api/v3/noticias/?de=12-31-2023'

# função que pega as noticias e salva me um json
def get_info(url:str)-> None: 
    news = requests.get(url).json()

    with open('data/news.json','w') as file:
        json.dump(news,file,indent=4,ensure_ascii=False)
get_info(url)