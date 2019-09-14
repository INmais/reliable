# Notes

## Units and types

GIS

ETRS89 Portugal TM06
Timezone (Lisbon)

* shapefile INE:  {'init' :'epsg:3763'}
* googlemaps and folium: ({'init': 'epsg:4326'})
* sentinet 2 (ESA): ({'init': 'epsg:32629'})

### Shapefiles

Entity: INE

url: http://mapas.ine.pt/download/index2011.phtml

Extreme weather

Heat waves are formally defined by the World Health Organization as a period of 6 consecutive days in which there is a daily maximum temperature above 5 ° C to the average daily value for the reference period.

Benckmarks

+ 32º or 30.5º for 6 days consecutive days
if there is a day that is less (discount, -1), not start again counting (problem of consecutive waves)

### EE Certificates

Entity: ADENE

data: https://www.sce.pt/pesquisa-certificados/
(try to get with selenium)

### Population per BGRI

Entity: INE

Census 2011: http://mapas.ine.pt/download/index2011.phtml

### ZIP Codes

Entity: CTT

https://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx

### Vegetation Index calculation from Satellite Imagery

Entity: ESA

data: https://scihub.copernicus.eu/dhus/#/home

### CORINE Land Cover

data: https://land.copernicus.eu/pan-european/corine-land-cover

## EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification

url: https://github.com/phelber/eurosat
paper: https://arxiv.org/abs/1709.00029

### Informação dos Certificados de Óbito (SICO)

Entity: Direção-Geral da Saúde

data: https://evm.min-saude.pt/


### Causas de morte - 2017

Entity:INE

url: https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_publicacoes&PUBLICACOESpub_boui=358633033&PUBLICACOESmodo=2

### Healthcare

% de episódios (ambulatório e internamento), registados nos GDH com pelo menos um diagnóstico dos códigos 410-414 (CID 9)

https://transparencia.sns.gov.pt/explore/


Evolução Diária do Índice-Alerta-ÍCARO (ÍCARO é um instrumento de observação no âmbito do qual se estuda o efeito de fatores climáticos na saúde humana.)

url: http://www2.insa.pt/sites/INSA/Portugues/AreasCientificas/Epidemiologia/Unidades/UnInstrObser/Paginas/ICARO.aspx (tem metodologia e estão usar dados IPMA)

Atividade de Prestação do SNS 24 para Problemas relacionados com Calor e Exposição Solar

#### Other

Evolução Mensal das Ocorrências Pré-Hospitalares por Tipologia

Chamadas de Emergência Transferidas para a Saúde 24

Trabalho Noturno, Normal e Suplementar

Atividade do Síndrome Gripal nos Cuidados de Saúde Primários

Atendimentos por Tipo de Urgência Hospitalar

Atividade nos Cuidados Saúde Primários - Monitorização Sazonal

Atendimentos em Urgência Hospitalar por Triagem de Manchester

Taxa de Ocupação Hospitalar

Atividade de Prestação do SNS 24 para a Síndrome Gripal

Frequência de Casos Confirmados de Gripe

Incidência Semanal de Síndrome Gripal



### Estatísticas da Saúde - 2017 Ano de Edição: 2019
Entity: INE
URL: https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_publicacoes&PUBLICACOESpub_boui=384207665&PUBLICACOESmodo=2

### Morbilidade Hospitalar – Serviço Nacional de Saúde – 2016. Portugal Continental

Entity: Direção-Geral da Saúde

url: https://comum.rcaap.pt/bitstream/10400.26/22528/1/Morbilidade%20Hospitalar%20-%20Servi%c3%a7o%20Nacional%20de%20Sa%c3%bade%20-%202016.%20Portugal%20Continental.pdf

### Grupos de Diagnósticos Homogéneos (GDH) 

http://www2.acss.min-saude.pt/Default.aspx?TabId=460&language=pt-PT Base de Dados Nacional de Grupo de Diagnóstico Homogéneo (GDH) Base de Dados Nacional de Grupo de Diagnóstico Homogéneo Administração Central do Sistema de Saúde (ACSS) geral@acss.min-saude.pt

http://dis.dgs.pt/2010/08/23/base-de-dados-nacional-de-grupo-de-diagnostico-homogeneo-gdh/

### Morbilidade e Mortalidade Hospitalar
Codificar segundo CID9 MC os episódios de internamento e ambulatório das instituições Informação recolhida nas instituições hospitalares através de ficheiro que é carregado na base de dados nacional. Mensal Organismos do Ministério da saúde, Universidades e outras instituições que solicitam 
url: https://dados.gov.pt/en/datasets/morbilidade-e-mortalidade-hospitalar/

### INE/Income Tax

Estatísticas do rendimento ao nível local - indicadores de rendimento declarado no IRS - 2017 Ano de Edição: 2019
https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_publicacoes&PUBLICACOESpub_boui=384208622&PUBLICACOESmodo=2&xlang=pt


### Weather forecast 

Entity: MARETEC
script: https://github.com/INmais/reliable/tree/master/docs/reliable_getMeteo

### IPMA (historical data)
valores médios horários de temperatura e humidade relativa (paid, few gaps)

### Portugal Weather Stations data
Portugal Weather Stations data (from 01 Jan 2016 to 01 Jan 2019)
https://inmais.github.io/portugal-weather-stations/


### Language

R and Python

## Check

Planning for sustainable cities by estimating building occupancy with mobile phones
https://www.nature.com/articles/s41467-019-11685-w

The TimeGeo modeling framework for urban mobility without travel surveys
https://www.pnas.org/content/113/37/E5370

Social Physics: Uncovering Human Behaviour from Communication
https://arxiv.org/abs/1804.04907v1

