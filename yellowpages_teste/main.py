from webbrowser import Chrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


# entra no site
options = Options()
options.add_argument('window-size=1280,720')
driver = webdriver.Chrome(options=options)
driver.get('https://www.yellowpages.com/')

servicos = ['destists']

# faz a pesquisa
def pesquisa_servico(servico):
    pesquisa = driver.find_element_by_id('query')
    pesquisa.send_keys(servico)
    pesquisa.submit()
    sleep(2)

# captura os dados
def faz_raspagem():
    telefone = driver.find_elements_by_xpath('//div[@class="phones phone primary"]')
    endereco = driver.find_elements_by_xpath('//div[@class="street-address"]')
    cidade = driver.find_elements_by_xpath('//div[@class="locality"]')
    comentario = driver.find_elements_by_xpath('//p[@class="body with-avatar"]')

    # primeiro serviço
    telefone1 = telefone[0].text
    endereco1 = endereco[0].text
    cidade1 = cidade[0].text
    comentario1 = comentario[0].text

    # segundo serviço
    telefone2 = telefone[1].text
    endereco2 = endereco[1].text
    cidade2 = cidade[1].text
    comentario2 = comentario[1].text

    # terceiro serviço
    telefone3 = telefone[2].text
    endereco3 = endereco[2].text
    cidade3 = cidade[2].text
    comentario3 = comentario[2].text

    primeiro_dado = (telefone1 + ';' + endereco1 + ';' + cidade1 + ';' + comentario1)
    segundo_dado = (telefone2 + ';' + endereco2 + ';' + cidade2 + ';' + comentario2)
    terceiro_dado = (telefone3 + ';' + endereco3 + ';' + cidade3 + ';' + comentario3)

    # salva em arquivo .txt
    with open('yellowpages.txt', 'w+') as arquivo:
        arquivo.write(primeiro_dado + '\n')
        arquivo.write(segundo_dado + '\n')
        arquivo.write(terceiro_dado + '\n')
        arquivo.close()

for servico in servicos:
    pesquisa_servico(servico)
    faz_raspagem()
