from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('window-size=1280,720')
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.tripadvisor.com.br')

# clica no botão 'Mais'
primeiro_input = navegador.find_elements_by_tag_name('button')[-27]
primeiro_input.click()
sleep(1)

# clica no botao 'Adicione um local'
campo_pesquisa = navegador.find_element_by_id('menu-item-0')
campo_pesquisa.click()
sleep(2)

# clica no botão 'Aceitar'
button_aceitar = navegador.find_element_by_id('onetrust-accept-btn-handler')
button_aceitar.click()
sleep(2)

# pesquisa no search
pesquisar = navegador.find_element_by_xpath('//*[@id="lithium-root"]/header/div/nav/div/div[1]/div/div/form/input[1]')
pesquisar.click()
pesquisar.send_keys('Belo Horizonte')
pesquisar.submit()
sleep(3)

# realiza web scraping
cidade = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]').text
estado = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]').text
descricao = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div').text
ponto_turistico = navegador.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]').text

navegador.close()

# guarda na TripAdvisor.txt
with open('tripadvisor.txt', 'w+') as arquivo:
    arquivo.write(f'cidade: {cidade}\n')
    arquivo.write(f'cidade: {estado}\n')
    arquivo.write(f'cidade: {descricao}\n')
    arquivo.write(f'cidade: {ponto_turistico}\n')
    arquivo.close()


            
    
        
