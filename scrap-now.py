import os
import requests
from bs4 import BeautifulSoup
import cv2
from skimage import io
import json
import mechanize
from fake_useragent import UserAgent


# # enter in https://www.nowfoods.com/products/supplements/all-products
# ## click in views-row class on div

# ### get field--name-title value
# ### get img src which have cloudzoom--1 class or cloudzoom--2 or cloudzoom--3 or cloudzoom--4


# def getCookies(cookie_jar, domain):
#     cookie_dict = cookie_jar.get_dict(domain=domain)
#     found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
#     return ';'.join(found)

# # enter in https://www.nowfoods.com/products/supplements/all-products

# links = []

# for i in range(1, 28):
#     if(i == 1):
#         pagination =  ''
#     else :
#         pagination = '?page=' + (i - 1).__str__()

#     principal_url = "https://www.nowfoods.com/products/supplements/all-products" + pagination
#     if(i != 1):
#         print(principal_url)

#     ua = UserAgent()

#     header = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
#         "cache-control": "max-age=0",

#         "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Opera\";v=\"101\", \"Chromium\";v=\"115\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "document",
#         "sec-fetch-mode": "navigate",
#         "sec-fetch-site": "none",
#         "sec-fetch-user": "?1",
#         "upgrade-insecure-requests": "1",
#         "cookie": "nlbi_2512457=VvS/PVD1LnFp5Y75zUwA9QAAAABicOlaButZYA5oBDNlyP36; incap_ses_9129_2512457=bREUWNm6QBCbzHn6obmwflmq4WQAAAAAA1HHbmV7C2AIW/n5Ko4wjg==; _gcl_au=1.1.1599652643.1692510790; _gid=GA1.2.1689985791.1692510790; _pin_unauth=dWlkPU5qazFPVFl5TkRrdFpqWmhOQzAwWldFeExUaG1Oekl0T1dFeE1qSXhZbVUxWXpWbQ; SLG_G_WPT_TO=pt; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; now-site-alert=[{\"id\":\"block-sdcookieconsentblock--1637612448\",\"expires\":\"2024-08-19T05:53:58.274Z\"}]; MCPopupClosed=yes; BVBRANDID=0cf3547e-327c-4992-a352-2d75fff4cd75; BVImplus=12100_4_0; _ga_MN2QWYWG3K=GS1.1.1692511444.1.1.1692511776.60.0.0; incap_ses_7241_2512457=b04LFNs20m2Lo+gZnjN9ZKBM4mQAAAAA9KpqqDvuG8zZhcGergHWAA==; visid_incap_2512457=gmXdDO2KRnqO++qjd5JVQlmq4WQAAAAAQkIPAAAAAACANXCuAQAQF1FBxxppVcGfmChCIZXY/y6q; _dc_gtm_UA-6115913-2=1; _gat_UA-6115913-2=1; _ga=GA1.2.848383657.1692510790; _ga_NK56YN3F9X=GS1.1.1692552339.2.1.1692555537.7.0.0; _derived_epik=dj0yJnU9LW55aDc1QmJYNFd6QTlzdW5ycFM2VWJLOGlXVFhWWVAmbj1UaDhjeG5QNS1vSDU4MzFPNl82VUlRJm09MSZ0PUFBQUFBR1RpV1NnJnJtPTEmcnQ9QUFBQUFHVGlXU2cmc3A9Mg",
#         "user-agent": ua.random
#     }


#     page = requests.get(principal_url, headers=header)

#     soup = BeautifulSoup(page.text, 'html.parser')
#     links += soup.find_all('a', class_='field--name-title')
#     print(links.__len__().__str__())

# print(links)
# results = []
# exit()

# print('links: ' + links.__len__().__str__())
# for link in links:
#     urlComplement = link.get('href')
#     url = "https://www.nowfoods.com" + urlComplement
#     print(url)
#     page = requests.get(url, headers=header)
#     soup = BeautifulSoup(page.text, 'html.parser')

#     title = soup.find('span', class_='field--name-title')
#     if title is None:
#         continue
#     else :
#         title = title.text

#     imgs = []
#     aux = 1
#     while(True):
#         img = soup.find('img', id='cloudzoom--' + aux.__str__())
#         if img is None:
#             break
#         imgs.append({
#             "id": aux,
#             "src": img.get('data-src')
#         })
#         aux += 1

#     results.append({
#         "title": title,
#         "imgs": imgs
#     })
# # write results in aa single file
# f = open("results.json", "a")
# f.write(json.dumps(results))
# f.close()



url = 'https://www.nowfoods.com/products/products-sku'
page = requests.get(url)

codigos = [
    '41005'
]

# pegar codigos
# fazer pesquisa
# se mais 1 resultado: erro
#se n
    # pegar sku
    # pegar fotos



for codigo in codigos:

    page = requests.get('https://www.proline4life.com/catalogsearch/result/?q=' + codigo)
    soup = BeautifulSoup(page.text, 'html.parser')
    # get all href on a tag with class button btn-cart
    a = soup.find_all('a', class_='button btn-cart')
    #  count how many matchs
    if(a.__len__() > 1):
        print('mais de 1 - ' + codigo)

    if(a.__len__() == 0):
        print('nenhum - ' + codigo)

    if(a.__len__() == 1):
        href = a[0].get('href')
        newPage = requests.get(href)
        newSoup = BeautifulSoup(newPage.text, 'html.parser')
        sku = newSoup.find('span', class_='value').text
        print(sku)


    # print(soup)
    # exit()
    # print(soup.text)
    # for spans in spans:
    #     text = spans.text
    #     # before - and get out blank spaces
    #     sku = text.split('-')[0].strip().replace(' ', '')
    #     # get child of span
    #     a = spans.find('a')
    #     # get href
    #     href = a.get('href')

    #     if sku == '' or href == '':
    #         continue
    #     else:
    #         print('sku: ' + sku)
    #         print('href: ' + href)

    #     print('----------------------')



