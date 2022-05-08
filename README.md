# MeuPortifolio
meu site para portfólio 
Feito com django, HTML, CSS e SQL

# Antes de rodar
* Instale o virtualenv na raíz do projeto```python3 -m venv .venv```
* Ative o virtualenv ```.\venv\Scripts\Activate```
* Instale as libs necessárias no arquivo requirements.txt na raíz do projeto ```pip install -r requirements.txt```
* agora rode ```python manage.py runserver```

## detalhe
crie um arquivo ```.env``` na raiz do projeto e coloque as variaveis do arquivo ```.env.exemplo``` nele

### Conteudo dinamico e estatico 'Sobre' e 'Projetos'
tens a opção de mostrar o conteudo 'Sobre' e 'Projetos' estaticamente ou dinamicamente, de acordo com a caixa 'mostrar' na pagina adm-Django (tabela: sobremim)
