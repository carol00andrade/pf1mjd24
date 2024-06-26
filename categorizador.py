# -*- coding: utf-8 -*-

!pip install openai --upgrade
import openai

from google.colab import files

# Faça o upload do arquivo 'G1-G1'
uploaded = files.upload()

import pandas as pd

# Carregar o arquivo CSV em um DataFrame pandas
df = pd.read_csv('g1 - g1.csv')

# Exibir as primeiras linhas do DataFrame para verificar se os dados foram carregados corretamente
print(df.head())

# Exemplo de como acessar as primeiras 10 linhas da coluna 'links'
print(df['Link'].head(10))

# Exemplo de como acessar as primeiras 10 linhas da coluna 'títulos'
print(df['Título'].head(10))

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Carregar o arquivo CSV em um DataFrame pandas
df = pd.read_csv('g1 - g1.csv')

# Função para extrair o título e a linha fina da página
def extract_content(link):
    try:
        response = requests.get(link)
        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extrair título
            title = soup.title.string if soup.title else "Título não encontrado"
            # Extrair linha fina (se houver)
            tagline = soup.find("meta", {"name": "description"})['content'] if soup.find("meta", {"name": "description"}) else "Linha fina não encontrada"
            return title, tagline
        else:
            return f"Erro: {response.status_code}"
    except Exception as e:
        return f"Erro ao extrair conteúdo: {str(e)}"

# Aplicar a função à coluna 'Link' do DataFrame e armazenar os resultados em novas colunas
df[['titulo', 'linha_fina']] = df['Link'].apply(lambda link: pd.Series(extract_content(link)))

# Mostrar o DataFrame resultante
print(df)

# Salvar o DataFrame resultante em um arquivo CSV
df.to_csv('df_categorizado.csv', index=False)

!pip install newspaper3k
!python -m spacy download pt_core_news_sm

!pip install dateparser

import pandas as pd
from newspaper import Article
import spacy
import re

# Carregar modelo do spaCy em português
nlp = spacy.load('pt_core_news_sm')

# Carregar o arquivo CSV em um DataFrame pandas
df = pd.read_csv('g1 - g1.csv')

# Função para extrair a data do texto
def extract_date(text):
    # Expressão regular para encontrar o dia da semana
    regex = r"(?i)(?:segunda|terça|quarta|quinta|sexta|sábado|domingo)"
    match = re.search(regex, text)
    return match.group(0) if match else "Data não encontrada"

# Lista de nomes femininos
nomes_femininos = ["Maria", "Ana", "Beatriz", "Jéssica", "Elda", "Bárbara", "Joana", "Patrícia", "Carla", "Sandra"]

# Função para extrair informações sobre a vítima
def extract_victim_info(article):
    # Inicializar variáveis para a vítima
    identificacao_mulher = "Não"
    nao_identificada = "Não"

    # Extrair o título, linha fina e o texto completo
    titulo = article.title
    linha_fina = article.meta_description
    texto_completo = article.text

    # Verificar se algum nome feminino está presente no título, linha fina ou no texto completo
    for nome in nomes_femininos:
        if nome.lower() in titulo.lower() or nome.lower() in linha_fina.lower() or nome.lower() in texto_completo.lower():
            identificacao_mulher = "Sim"
            break

    # Verificar se a palavra "não identificada" está presente no título, linha fina ou no texto completo
    if "não identificada" in titulo.lower() or "não identificada" in linha_fina.lower() or "não identificada" in texto_completo.lower():
        nao_identificada = "Sim"

    return identificacao_mulher, nao_identificada

# Função para extrair informações sobre o agente da violência
def extract_violence_agent(doc):
    agent = "Não encontrado"
    # Procurar por padrões que sugerem o agente da violência no texto
    for token in doc:
        if token.text.lower() in ["marido", "esposo", "namorado", "ex-namorado", "ex-marido", "companheiro", "ex-companheiro", "filho", "pai", "suspeito"]:
            for ancestor in token.ancestors:
                if ancestor.dep_ == "nsubj":
                    agent = token.text
                    return agent
        elif token.text.lower() in ["obrigada a", "descoberto que", "forçada a", "matou", "assassinou", "facada", "agrediu"]:
            for ancestor in token.ancestors:
                if ancestor.dep_ == "nsubj":
                    agent = token.text
                    return agent
    return agent

def categorize_news(link):
    try:
        article = Article(link)
        article.download()
        article.parse()
        content = article.text

        dia_semana = extract_date(content)

        nlp = spacy.load('pt_core_news_sm')
        doc = nlp(content)

        nome_feminino = "Não encontrado"
        agent_violencia = "Não encontrado"
        morta_como = "Não encontrado"
        info_local = "Não encontrado"
        feminicidio = "Não"

        for entidade in doc.ents:
            if entidade.label_ == "PER":
                nome_feminino = entidade.text
                break

        keywords = {
            "morte": ["tiro", "faca", "espancada", "facada", "arma", "estupro", "violência", "esfaqueada", "queimada", "afogada", "homicídio", "sangramento", "paulada"],
            "local": ["casa", "rua", "calçada", "garagem", "sala", "cama", "cozinha", "trabalho", "motel"],
            "feminicídio": ["feminicídio", "assassinada", "assassinato"]
        }

        for token in doc:
            for category, words in keywords.items():
                if any(word in token.text.lower() for word in words):
                    if category == "morte":
                        morta_como = token.text
                    elif category == "local":
                        info_local = token.text
                    elif category == "feminicídio":
                        feminicidio = "Sim"

        agent_violencia = extract_violence_agent(doc)

        return nome_feminino, agent_violencia, morta_como, info_local, dia_semana, feminicidio, ""
    except Exception as e:
        return "Erro ao processar notícia", "", "", "", "", "", str(e)

# Carregar o arquivo CSV em um DataFrame pandas
df = pd.read_csv('g1 - g1.csv')

# Aplicar a função à coluna 'Link' do DataFrame e armazenar os resultados em novas colunas
df[['nome_feminino', 'agente_violencia', 'morta_como', 'info_local', 'dia_semana', 'feminicidio', 'erro']] = df['Link'].apply(lambda link: pd.Series(categorize_news(link)))

# Mostrar o DataFrame resultante
print(df)
