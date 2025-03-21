import requests
import urllib.parse
from bs4 import BeautifulSoup
import csv

def ajusta_url_de_pesquisa(vaga,localidade):
    local_pesquisa = urllib.parse.quote_plus(localidade)
    vaga_pesquisa = urllib.parse.quote_plus(vaga)
    return f'https://www.linkedin.com/jobs/search?keywords={vaga_pesquisa}&location={local_pesquisa}'

def scraping(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    vagas = soup.find_all('a', class_='base-card__full-link')
    vaga_link = []

    for vaga in  vagas:
        titulo = vaga.find('span', class_='sr-only').get_text(strip=True)
        link = vaga['href']
        
        vaga_link.append({
            'titulo': titulo,
            'link': link
        })
    return vaga_link

def criar_csv(vagas, arquivo='vagas.csv'):
    header =  ['titulo','link']
    with open(arquivo,   mode='w', newline='', encoding='utf-8') as  arquivo_csv:
        csv_vagas = csv.DictWriter(arquivo_csv, fieldnames=header)
        csv_vagas.writeheader()
        csv_vagas.writerows(vagas)

def run(vaga, pais, estado, cidade):
    localidade = f'{pais}, {estado}, {cidade}'
    url = ajusta_url_de_pesquisa(vaga,localidade)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        vagas = scraping(response)
        criar_csv(vagas)

    else:
        print('Error ao acessar url')


if __name__ == '__main__':
    run()