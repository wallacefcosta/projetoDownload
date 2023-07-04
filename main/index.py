# selenium_teste.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests
import traceback
import time

ZOOMIN = 4 # número de vezes para zoom

class Client:
    """
    O cliente www.
    A classe só abre uma instância do firefox (headless) e fica pronta para
    aceitar links.
    Client.get() recebe a url e executa toda a mágica.
    Não esquecer de chamar Client.quit() para fechar o firefox ao final.
    """
    def _init_(self):
        opts = Options()
        opts.add_argument('-headless')
        self.driver = webdriver.Firefox(options=opts)
        self.wait = WebDriverWait(self.driver, 20)

    def quit(self):
        self.driver.quit()

    def get(self, url, fname):
        """Pega a url, baixa a imagem para fname"""
        print(f'Client fetching source {url}')
        self.driver.get(url)

        # Esperar a primeira imagem estar visível
        # O intuito é dar uma segurada no processamento até que toda a página
        # esteja mais ou menos carregada.
        imgElement = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//img[contains(@src, "JPG")]')))
        jpgLink = [imgElement.get_attribute('src')]
        jpgLink.append(jpgLink[0])

        # Esperar pelo frame onde está o botão 'ok'. Trocar para o frame,
        # apertar o botão e voltar para o conteúdo principal.
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@name="PesqOpniaoRadWindow"]')))
        fechar = self.wait.until(EC.element_to_be_clickable((By.NAME, 'FecharBtn')))
        fechar.click()
        self.driver.switch_to.default_content()

        # aperta zoomIN um número de vezes
        for i in range(ZOOMIN):
            zoomIN = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="ZoomInBtn"]')))
            zoomIN.click()

            # Essa é difícil:
            # nós temos que esperar para que a imagem carregue toda vez antes
            # de apertar zoom novamente.
            # Isso é feito verificando a visibilidade da imagem (imgElement).
            # O problema é que após o zoom.click(), a última imagem ainda vai
            # estar visível antes da nova imagem carregar.
            # Por isso, precisamos manter o registro de qual foi a última imagem
            # carregada e comparar a url dela com a que está atualmente visível.
            # zoom só é apertado novamente quando a imagem visível é diferente
            # da última.
            # Um delay de 1s foi necessário aqui para evitar iterações
            # excessivas desse loop.
            while jpgLink[1] == jpgLink[0]:
                time.sleep(1)
                imgElement = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//img[contains(@src, "JPG")]')))
                jpgLink[1] = imgElement.get_attribute('src')
            jpgLink[0] = jpgLink[1]

        # Depois de chegar na imagem que queremos, não podemos usar o método
        # do screenshot, porque ele reduz a resolução da imagem. Por isso,
        # passamos a url encontrada para outra biblioteca - requests - que fará
        # o download. Para isso dar certo, requests.get() precisa ter uma cópia
        # dos cookies que a página passou para o firefox.
        cookieList = self.driver.get_cookies()
        cookieDict = {c['name']: c['value'] for c in cookieList}
        jar = requests.cookies.cookiejar_from_dict(cookieDict)
        download = requests.get(jpgLink[1], cookies=jar)
        download.raise_for_status()

        # Salva a imagem em fname
        print(f'Downloaded {download.url}')
        with open(fname, 'wb') as fp:
            fp.write(download.content)

        return self

def main():
    initialUrl = 'http://memoria.bn.br/docreader/DocReader.aspx?bib=030015_12&pagfis=233456'
    browser = Client()
    try:
        browser.get(initialUrl, 'pg_test.jpg')
    except:
        print(traceback.format_exc())

    browser.quit()

    return 0

if '_name_' == '_main_':
    import sys
    sys.exit(main())