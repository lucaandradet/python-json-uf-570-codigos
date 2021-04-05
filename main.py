import json
import urllib.request

#Carrega um JSON
url = 'https://sisu-api-pcr.apps.mec.gov.br/api/v1/oferta/instituicao/570'
with urllib.request.urlopen(url) as response:
  resp = response.read()

#Faz a análise desse JSON.
resp = json.loads(resp.decode('utf-8'))

with open('codigos.csv', 'w', encoding='utf-8') as arquivo:
  #Itera por todos os itens do dicionário principal....
  for k, v in resp.items():
    #...se a have 'co_oferta' está contida no dicionário aninhado...
    if 'co_oferta' in v:
      print(v['co_oferta'], end=";", file=arquivo)         #...se sim, imprime seu valor.
    #...se a have 'co_curso' está contida no dicionário aninhado...
    if 'co_curso' in v:
      print(v['co_curso'], end=";", file=arquivo)#...se sim, imprime seu valor.
    #...se a have 'no_curso' está contida no dicionário aninhado...
    if 'no_curso' in v:
      print(v['no_curso'], end=";", file=arquivo)#...se sim, imprime seu valor. 
    #...se a have 'no_turno' está contida no dicionário aninhado...
    if 'no_turno' in v:
      print(v['no_turno'], end=";", file=arquivo)#...se sim, imprime seu valor. 
    #...se a have 'no_campus' está contida no dicionário aninhado...
    if 'no_campus' in v:
      print(v['no_campus'], end=";", file=arquivo)#...se sim, imprime seu valor. 
    #...se a have 'sg_ies' está contida no dicionário aninhado...
    if 'sg_ies' in v:
      print(v['sg_ies'], end=";", file=arquivo)#...se sim, imprime seu valor. 
    #...se a have 'nu_nmin_cn' está contida no dicionário aninhado...
    if 'nu_nmin_cn' in v:
      print(v['nu_nmin_cn'], end=";", file=arquivo)#...se sim, imprime seu valor. 
    #...se a have 'nu_nmin_ch' está contida no dicionário aninhado...
    if 'nu_nmin_ch' in v:
      print(v['nu_nmin_ch'], end=";", file=arquivo)#...se sim, imprime seu valor.
    #...se a have 'nu_nmin_l' está contida no dicionário aninhado...
    if 'nu_nmin_l' in v:
      print(v['nu_nmin_l'], end=";", file=arquivo)#...se sim, imprime seu valor. 
    #...se a have 'nu_nmin_m' está contida no dicionário aninhado...
    if 'nu_nmin_m' in v:
      print(v['nu_nmin_m'], end=";", file=arquivo)#...se sim, imprime seu valor.
    #...se a have 'nu_nmin_r' está contida no dicionário aninhado...
    if 'nu_nmin_r' in v:
      print(v['nu_nmin_r'], end=";", file=arquivo)#...se sim, imprime seu valor.
    #...se a have 'nu_media_minima' está contida no dicionário aninhado...
    if 'nu_media_minima' in v:
      print(v['nu_media_minima'], file=arquivo) #...se sim, imprime seu valor.