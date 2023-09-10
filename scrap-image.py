import os
import requests
from bs4 import BeautifulSoup
import cv2
from skimage import io


def recursiveUrl(url, link, depth):
    if depth == 5:
        return url
    else:
        print(link['href'])
        page = requests.get(url + link['href'])
        soup = BeautifulSoup(page.text, 'html.parser')
        newlink = soup.find('a')
        if len(newlink) == 0:
            return link
        else:
            return link, recursiveUrl(url, newlink, depth + 1)

def getLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    print(links)
    for link in links:
        links.append(recursiveUrl(url, link, 0))
    return links

links = getLinks("https://suplementosnow.com.br/")
print(links)

exit()


















def create_dir(path):
    """ Create folders """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error")

def create_file(path):
    """ Create a file """
    try:
        if not os.path.exists(path):
            f = open(path, "w")
            f.write("Name,Alt\n")
            f.close()
    except OSError:
        print("Error")

def save_image(search_term, page_num=1):
    ## URL and headers
    url = "https://www.nowsuplementos.com.br/"
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    ## making a GET request to the website and getting the information in response.
    result = requests.get(url, headers=header)

    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")
    else:
        print("Error")
        exit()

    ## Paths and file for saving the images and data.
    dir_path = f"Downloads/{search_term}/"
    file_path = f"Downloads/{search_term}/{search_term}.csv"

    create_dir(dir_path)
    create_file(file_path)

    f = open(file_path, "a")

    for tag in soup.find_all("div", class_="imagem-produto"):
        if tag.img:
            try:
                src = tag.img["src"]
                alt = tag.img["alt"]
            except Exception as e:
                alt = None

            try:
                if alt:
                    image = io.imread(src)
                    name = alt.split("/")[-1].split("?")[0]
                    data = f"{name},{alt}\n"
                    f.write(data)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    cv2.imwrite(dir_path + name + '.jpg', image)
                    print(name, ": ", alt)
            except Exception as e:
                pass


if __name__ == "__main__":
    terms = ['Vitamina']
    for term in terms:
        save_image(term, page_num=1)
        save_image(term, page_num=2)
