# Download Project 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

O objetivo deste projeto, selenium_teste.py, é automatizar o processo de download de uma imagem a partir de uma URL específica. O script utiliza a biblioteca Selenium para abrir um navegador Firefox sem interface gráfica e realizar várias ações para obter a imagem desejada. A classe Client representa o cliente web e possui métodos para buscar a imagem a partir de uma URL fornecida e salvá-la em um arquivo. O método get executa uma série de ações usando o Selenium, como aguardar o carregamento da página, interagir com elementos e clicar em botões. Também utiliza a biblioteca requests para baixar a imagem a partir da URL final. No final, o navegador é fechado e o script é encerrado com um código de retorno 0. Em resumo, este projeto tem como objetivo automatizar o processo de download de uma imagem de uma URL específica usando um navegador Firefox sem interface gráfica e a biblioteca Selenium.


The purpose of this project, selenium_teste.py, is to automate the process of downloading an image from a specific URL. The script uses the Selenium library to open a headless Firefox browser and perform various actions to retrieve the desired image. The Client class represents the web client and provides methods to fetch the image from a given URL and save it to a file. The get method executes a series of actions using Selenium, such as waiting for the page to load, interacting with elements, and clicking on buttons. It also utilizes the requests library to download the image from the final URL. Finally, the browser is closed, and the script exits with a return code of 0. In summary, this project aims to automate the image download process from a specific URL using a headless Firefox browser and the Selenium library.

## Getting Started <a name = "getting_started"></a>
Estas instruções irão guiá-lo através da configuração e execução do projeto em sua máquina local para fins de desenvolvimento e teste. Por favor, siga os passos abaixo:

These instructions will guide you through setting up and running the project on your local machine for development and testing purposes. Please follow the steps below:

### Prerequisites
Certifique-se de ter o Python instalado em sua máquina. Caso contrário, você pode baixar e instalar o Python no site oficial: Python.org.

Ensure you have Python installed on your machine. If not, you can download and install Python from the official website: Python.org.


### Installing
Clone ou baixe o repositório do projeto para sua máquina local.
Abra um terminal ou prompt de comando e navegue até o diretório do projeto.
     Crie um ambiente virtual para o projeto (opcional, mas recomendado):
         Execute o comando python3 -m venv myenv para criar um novo ambiente virtual chamado "myenv".
         Ative o ambiente virtual:
             Para Windows: Execute o comando myenv\Scripts\activate.
             Para macOS/Linux: Execute o comando source myenv/bin/activate.

     Instale as dependências do projeto executando o comando pip install -r requirements.txt.

Clone or download the project repository to your local machine.
Open a terminal or command prompt and navigate to the project directory.
    Create a virtual environment for the project (optional but recommended):
        Run the command python3 -m venv myenv to create a new virtual environment named "myenv".
        Activate the virtual environment:
            For Windows: Run the command myenv\Scripts\activate.
            For macOS/Linux: Run the command source myenv/bin/activate.

    Install the project dependencies by running the command pip install -r requirements.txt.

## Usage <a name = "usage"></a>
Depois de concluir as etapas de configuração, você pode executar o script executando o seguinte comando no terminal:

python selenium_teste.py

O script automatizará o processo de download de uma imagem de um URL específico. A imagem será salva em um arquivo chamado "pg_test.jpg".

Certifique-se de personalizar a URL inicial na função main() do script, se necessário.

After completing the setup steps, you can run the script by executing the following command in the terminal:

python selenium_teste.py

The script will automate the process of downloading an image from a specific URL. The image will be saved to a file named "pg_test.jpg".

Make sure to customize the initial URL in the main() function of the script if needed.
