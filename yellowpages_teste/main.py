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

    tel = []
    end = []
    cid = []
    com = []
    
    # iteração entre os indices dos dados
    for i in range(3):
        tel.append(telefone[i].text)
        end.append(endereco[i].text)
        cid.append(cidade[i].text)
        com.append(comentario[i].text)

    # junta os dados em variáveis
    primeiro_dado = (tel[0] + ';' + end[0] + ';' + cid[0] + ';' + com[0])
    segundo_dado = (tel[1] + ';' + end[1] + ';' + cid[1] + ';' + com[1])
    terceiro_dado = (tel[2] + ';' + end[2] + ';' + cid[2] + ';' + com[2])

    # salva em arquivo .txt
    with open('yellowpages.txt', 'w+') as arquivo:
        arquivo.write(primeiro_dado + '\n')
        arquivo.write(segundo_dado + '\n')
        arquivo.write(terceiro_dado + '\n')
        arquivo.close()

# mata o navegador
def sair():
    driver.quit()

# iteração com a ordem de execução
for servico in servicos:
    pesquisa_servico(servico)
    faz_raspagem()
    sair()
