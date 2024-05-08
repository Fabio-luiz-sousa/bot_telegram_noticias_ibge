from conn_db import conn_db
# coneção com o servido mysql
connection = conn_db()

with connection:
    with connection.cursor() as cursor:
        # função que cria a tabela ibge_noticias
        def create_db():
                cursor.execute(
                'CREATE TABLE IF NOT EXISTS ibge_noticias ('
                'id_news INT NOT NULL, '
                'titulo TEXT NOT NULL, '
                'introducao TEXT NOT NULL, '
                'data_publicacao DATETIME NOT NULL, '
                'editorias VARCHAR(50) NOT NULL, '
                'link TEXT NOT NULL, '
                'PRIMARY KEY (id_news)'
                ') '
            )
        create_db()



