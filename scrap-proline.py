from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import time


resultados = []
options = Options()
options.headless = True
options.add_argument("window-size=1920,1080")
navegador = webdriver.Chrome(chrome_options=options,executable_path='C:/webdrivers/chromedriver.exe')
f = open("results.json", "a")

def get_sku_and_href(codigo):
    navegador.get( 'https://www.proline4life.com/catalogsearch/result/?q=' + codigo)
    btnCart = navegador.find_elements(By.CSS_SELECTOR,'.item .product-image-wrapper')
    if(btnCart.__len__() > 1):
        print('mais de 1 - ' + codigo)
    if(btnCart.__len__() == 0):
        print('nenhum - ' + codigo)
    if(btnCart.__len__() == 1):
        btnCart = btnCart[0]
        btnCart.click()
        #### imgs
        produtoImgs = []
        imgElement = navegador.find_element(By.CLASS_NAME,'product-image-gallery')
        owlItems = navegador.find_elements(By.CSS_SELECTOR,'.product-img-column .owl-wrapper > .owl-item')
        # for ate 4 iteracoes
        for owlItem in owlItems:
            if(produtoImgs.__len__() == 4):
                break

            owlItem.click()
            imgElement = navegador.find_element(By.CLASS_NAME,'product-image-gallery')
            href = imgElement.get_attribute('href')
            produtoImgs.append(href)


        ### sku
        skuSite = navegador.find_element(By.CSS_SELECTOR,'.sku > .value').text
        #salvar nome
        nomeSite = navegador.find_element(By.CSS_SELECTOR,'.product-name > h1[itemprop="name"]').text
        #salvar legenda
        legenda = navegador.find_element(By.CSS_SELECTOR,'.short-description > .std').text
        #salvar detalhes em html
        detalhes = navegador.find_element(By.CSS_SELECTOR,'.collateral-block--product_description_wrapper .std').get_attribute('innerHTML')



        #categorias
        categorias = navegador.find_element(By.CSS_SELECTOR,'.inner-container > .breadcrumbs > .items')
        items = categorias.find_elements(By.TAG_NAME,'li')
        categoriasName = []
        for categoria in items:
            if(categoria.text != 'Início'):
                categoriasName.append(categoria.text)



        resultado = {
            'sku': skuSite,
            'nome': nomeSite,
            'legenda': legenda,
            'detalhes': detalhes,
            'imgs': produtoImgs,
            'categorias': categoriasName
        }



        f.write(json.dumps(resultado) + ',\n')








codigos = []
# read codigos from codigos.txt
with open('./codigos.txt') as file:
    codigos = [line.rstrip() for line in file]

for codigo in codigos:
    if codigo != '':
        get_sku_and_href(codigo)



f.close()
