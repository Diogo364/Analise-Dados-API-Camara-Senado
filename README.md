# Analise de Dados Abertos da API da Câmara e do Senado
<h2 align=center> - Em Desenvolvimento - </h2> 

---

## Autor:
Diogo Telheiro do Nascimento.
- [Linkedin](https://www.linkedin.com/in/diogo-telheiro-do-nascimento-95384a104/)

## Descrição:
Análise Exploratória de Dados - EDA - utilizando os dados provenientes da API da Câmara 
dos Deputados e do Senado Federal.

## Objetivo:
O objetivo desse projeto é servir como um exemplo de como criar relatórios rápidos 
e interativos utilizando o Streamlit.

## Tecnologias:
_Python3, Docker, ShellScript, Streamlit._  

## Quickstart:
O projeto foi construído de forma que o Streamlit e todos os códigos python são executados 
dentro de um container Docker, portanto para fazer esse projeto funcionar você deverá ter o 
_Docker_ instalado em sua máquina.
> NOTA: Para mais detalhes a respeito da instalação do _Docker_ [clique aqui](https://www.docker.com/).

### Passos para execução:
Todos os passos para a execução desse programa foram facilitados com a utilização de _ShellScript_
1. Acesse o diretório raiz do projeto utilizando o terminal,
2. Execute o ShellScript: `docker-build.sh` para a construção do container utilizando o Dockerfile
como base
3. Execute o ShellScript: `docker-run.sh` para a execução do container e da aplicação.
4. Acesse o link a seguir pelo seu browser: [localhost:8501](localhost:8501)

## Links:
- [API da Câmara dos Deputados](https://dadosabertos.camara.leg.br)