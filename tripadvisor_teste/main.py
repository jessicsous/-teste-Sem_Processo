from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

# entra no site
options = Options()
options.add_argument('window-size=1280,720')
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.tripadvisor.com.br')

# escreve o local à ser pesquisado
pesquisas = ['Belo Horizonte']
sleep(4)

# clica no botão 'Aceitar'
def primeiro_botao():
    button_aceitar = navegador.find_element_by_id('onetrust-accept-btn-handler')
    button_aceitar.click()
    sleep(2)

# faz a pesquisa
def input(pesquisa):
    primeiro_input = navegador.find_element_by_xpath('//input[contains(@placeholder, "Aonde você quer ir?")]')
    primeiro_input.click()
    primeiro_input.send_keys(pesquisa)
    primeiro_input.submit()
    sleep(3)


# realiza web scraping
def raspagem():
    cidade = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]').text
    estado = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]').text
    descricao = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div').text
    ponto_turistico = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]').text

    # guarda na pasta TripAdvisor.txt
    with open('tripadvisor.txt', 'w+') as arquivo:
        arquivo.write(f'cidade: {cidade}\n')
        arquivo.write(f'estado: {estado}\n')
        arquivo.write(f'descrição: {descricao}\n')
        arquivo.write(f'ponto turístico: {ponto_turistico}\n')
        arquivo.close()

# mata o navegador
def sair():
    navegador.quit()

# iteração com a ordem de execução
for pesquisa in pesquisas:
    primeiro_botao()
    input(pesquisa)
    raspagem()
    sair()




            
    
        
