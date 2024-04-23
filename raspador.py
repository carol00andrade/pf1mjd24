#G1 via busca do Google - 1 de março a 31 de março de 2024
#tag: "mulher morta" site:G1

import requests
import bs4

requisicao = requests.get ('https://www.google.com.br/search?q=mulher+morta+uol+site%3Ahttps%3A%2F%2Fwww.uol.com.br%2F&lr=&sca_esv=539b7d30e843b5e1&hl=pt-BR&as_qdr=all&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2024%2Ccd_max%3A3%2F31%2F2024&tbm=#ip=1')

soup=bs4.BeautifulSoup(requisicao.text)

soup

# Encontrar todas as tags 'a' com o atributo 'href'
links = soup.find_all('a')

# Lista para armazenar os links
links_list = []

# Iterar sobre as tags 'a' para extrair os links
for link in links:
    href = link.get('href')  # Extrair o valor do atributo 'href'
    links_list.append(href)

# Exibir os links
print("Links:")
for link in links_list:
    print(link)

import re

links = [
    "/url?q=https://g1.globo.com/sp/sao-carlos-regiao/noticia/2024/03/15/mulher-de-32-anos-e-encontrada-morta-com-sinais-de-violencia-no-interior-de-sp.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAUQAg&usg=AOvVaw2MTKhWOGk9NFY7z6F8YThO",
    "/url?q=https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2024/03/16/mulher-e-morta-espancada-em-lorena-ex-namorado-e-investigado-pela-policia-civil.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAkQAg&usg=AOvVaw3kS41rb5lb51T3SmXoygFx",
    "/url?q=https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2024/03/04/mulher-e-encontrada-morta-dentro-de-casa-em-estado-avancado-de-decomposicao-em-cacapava-sp.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAAQAg&usg=AOvVaw0WmNgWP2ooWAzOZ_JgOIj5",
    "/url?q=https://g1.globo.com/sp/sao-jose-do-rio-preto-aracatuba/noticia/2024/03/31/mulher-encontrada-morta-planejava-se-separar-do-companheiro-e-preparava-mudanca-coisas-estavam-encaixotadas-diz-amiga.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAcQAg&usg=AOvVaw3hniSqr9H9lj5x38kFNp1g",
    "/url?q=https://g1.globo.com/sp/santos-regiao/noticia/2024/03/23/mulher-e-encontrada-morta-em-praia-do-litoral-de-sp.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAEQAg&usg=AOvVaw3fDQGWRnQva4MjlnAfezO5",
    "/url?q=https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2024/03/12/mulher-de-29-anos-e-assassinada-a-tiros-em-potim-sp.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAYQAg&usg=AOvVaw3Evl-x5OAuvJHvJZ5Kjxlw",
    "/url?q=https://g1.globo.com/sp/sao-carlos-regiao/noticia/2024/02/15/mulher-e-encontrada-morta-com-sinais-de-violencia-em-rio-claro.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAMQAg&usg=AOvVaw2Wi665e_6D-Ruv-4T2yKzD",
    "/url?q=https://g1.globo.com/sp/sao-jose-do-rio-preto-aracatuba/noticia/2024/03/14/corpo-de-mulher-gravida-morta-a-facadas-e-encontrado-coberto-por-lencol-em-cama-no-interior-de-sp.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAQQAg&usg=AOvVaw2BqOvOXQqBHl490DXX-YGk",
    "/url?q=https://g1.globo.com/sp/santos-regiao/noticia/2024/03/06/mulher-e-encontrada-morta-em-calcada-no-litoral-de-sp.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAIQAg&usg=AOvVaw0C4DY3W79jZMuwCQFmIEd6",
    "/url?q=https://g1.globo.com/sp/bauru-marilia/noticia/2024/02/27/mulher-que-teve-orgaos-arrancados-pelo-marido-denunciou-estupro-e-rastreamento-do-celular-no-dia-do-assassinato.ghtml&sa=U&ved=2ahUKEwjxlqmO2ryFAxUjRDABHf1XADwQFnoECAgQAg&usg=AOvVaw3wcXn5fMDG5DHt96CuUBns",
]

def limpar_link(link):
    # Regex para extrair o URL após "?q=" e antes do próximo "&"
    match = re.search(r'\?q=(.*?)&', link)
    if match:
        return match.group(1)
    return None

links_limpos = [limpar_link(link) for link in links]

# Remover links que não foram extraídos corretamente
links_limpos = [link for link in links_limpos if link]

# Imprimir os links limpos
for link in links_limpos:
    print(link)

# Encontrar todas as tags 'a' com o atributo 'href'
links = soup.find_all('a')

# Lista para armazenar os títulos
titles_list = []

# Iterar sobre as tags 'a' para extrair os títulos
for link in links:
    # Encontrar a primeira tag 'h3' dentro do link (se existir) e extrair o texto
    title_tag = link.find('h3')
    title = title_tag.text if title_tag else "Título não encontrado"
    titles_list.append(title)

# Exibir os títulos
print("Títulos:")
for title in titles_list:
    print(title)

import pandas as pd

# Links corrigidos
links_limpos = [
    "https://g1.globo.com/sp/sao-carlos-regiao/noticia/2024/03/15/mulher-de-32-anos-e-encontrada-morta-com-sinais-de-violencia-no-interior-de-sp.ghtml",
    "https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2024/03/16/mulher-e-morta-espancada-em-lorena-ex-namorado-e-investigado-pela-policia-civil.ghtml",
    "https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2024/03/04/mulher-e-encontrada-morta-dentro-de-casa-em-estado-avancado-de-decomposicao-em-cacapava-sp.ghtml",
    "https://g1.globo.com/sp/sao-jose-do-rio-preto-aracatuba/noticia/2024/03/31/mulher-encontrada-morta-planejava-se-separar-do-companheiro-e-preparava-mudanca-coisas-estavam-encaixotadas-diz-amiga.ghtml",
    "https://g1.globo.com/sp/santos-regiao/noticia/2024/03/23/mulher-e-encontrada-morta-em-praia-do-litoral-de-sp.ghtml",
    "https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2024/03/12/mulher-de-29-anos-e-assassinada-a-tiros-em-potim-sp.ghtml",
    "https://g1.globo.com/sp/sao-carlos-regiao/noticia/2024/02/15/mulher-e-encontrada-morta-com-sinais-de-violencia-em-rio-claro.ghtml",
    "https://g1.globo.com/sp/sao-jose-do-rio-preto-aracatuba/noticia/2024/03/14/corpo-de-mulher-gravida-morta-a-facadas-e-encontrado-coberto-por-lencol-em-cama-no-interior-de-sp.ghtml",
    "https://g1.globo.com/sp/santos-regiao/noticia/2024/03/06/mulher-e-encontrada-morta-em-calcada-no-litoral-de-sp.ghtml",
    "https://g1.globo.com/sp/bauru-marilia/noticia/2024/02/27/mulher-que-teve-orgaos-arrancados-pelo-marido-denunciou-estupro-e-rastreamento-do-celular-no-dia-do-assassinato.ghtml",
]

# Lista de títulos
titles_list = [
    "Mulher de 32 anos é encontrada morta com sinais de violência no interior de SP",
    "Mulher é morta espancada em Lorena; ex-namorado é investigado pela Polícia Civil",
    "Mulher é encontrada morta dentro de casa em estado avançado de decomposição em Caçapava, SP",
    "Mulher encontrada morta planejava se separar do companheiro e preparava mudança: 'coisas estavam encaixotadas', diz amiga",
    "Mulher é encontrada morta em praia do litoral de SP",
    "Mulher de 29 anos é assassinada a tiros em Potim, SP",
    "Mulher é encontrada morta com sinais de violência em Rio Claro",
    "Corpo de mulher grávida morta a facadas é encontrado coberto por lençol em cama no interior de SP",
    "Mulher é encontrada morta em calçada no litoral de SP",
    "Mulher que teve órgãos arrancados pelo marido denunciou estupro e rastreamento do celular no dia do assassinato",
]

# Criar DataFrame
df = pd.DataFrame({'Link': links_limpos, 'Título': titles_list})

# Exibir o DataFrame
print("DataFrame:")
print(df)

df.to_csv('df.csv', index=False)
