# Youtube Summarizer - Gerador de Resumos

<div align="center"> 
  
![Python](https://img.shields.io/badge/-Python-1e272e?style=for-the-badge&logo=python)&nbsp;
</div>


## Descrição:
Ferramenta geradora de resumos do conteúdo de videos do YouTube.


## Sobre o projeto:
O projeto faz integração com a API do OpenAI para ChatGPT. 
A ferramenta é capaz de gerar um resumo do assunto do vídeo através da sua descrição.
Primeiro é extraída a descrição de um video para em seguida fazer o resumo dessa descrição.


## Créditos:

- Documentação da API da OpenAI ( https://platform.openai.com )

- Video utilizado: ["Quem foi Aristóteles e como desenvolveu uma fórmula filosófica para viver bem? - Canal Casa do Saber"](https://youtu.be/YW6rp2Gu99c?si=O8AT3Hi7QcB2hFlL)
</p>


## Como utilizar:


1. Clonando o projeto para a sua máquina

```sh
# Por HTTPS
git clone https://github.com/clevernvs/youtube-summanizer.git

# ou

# Por SSH
git clone git@github.com:clevernvs/youtube-summanizer.git
```

2. Criando um ambiente virtual

```sh
# Para Linux ou MacOS
cd youtube-summanizer
python3 -m venv .venv


# Para Windows
cd youtube-summanizer
py -3 -m venv .venv
```

3. Ativar o ambiente de desenvolvimento

```sh
# Para Linux ou MacOS
. .venv/bin/activate


# Para Windows
.venv\Scripts\activate
```


4. Instalando as dependências

```sh
pip install -r requirements.txt
```


</p>
