from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
#objeto site recebendo o conteudo da rquisição http do site climatempo

soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html

print(soup.prettify())
#transforma htm em string e o print vai exibir o html



