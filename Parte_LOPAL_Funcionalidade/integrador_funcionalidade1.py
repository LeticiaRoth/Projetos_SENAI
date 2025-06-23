#Importar a biblioteca para ler o CSV
import pandas as pd

#Pego para ler o arquivo csv, e atribuo a df
df = pd.read_csv('LOPAL_Integrador.csv')

#Mudo de CSV para HTML
integrador_esteiras = df.to_html(index=False)



#Escrevo o arquivo em formato de HTML dentro do (with opn)
with open ('integrador_LOPAL.html', 'w') as arquivo_html:
    arquivo_html.write("<!DOCTYPE html>\n")
    arquivo_html.write("<html>\n")
    arquivo_html.write("<head>\n")
    arquivo_html.write("<title>Status das Esterias - Monitoramento de Estoque</title>\n")
    arquivo_html.write("</head>\n")
    arquivo_html.write("<body>\n")
    arquivo_html.write(integrador_esteiras)
    arquivo_html.write("</body>\n")
    arquivo_html.write("</html>\n")

 
