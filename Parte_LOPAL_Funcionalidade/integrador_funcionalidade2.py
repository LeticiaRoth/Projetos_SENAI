import pandas as pd
#Biblioteca usada para enviar e-mail via protocolo SMTP
import smtplib
#Uso elas para enviar mensagens formatadas, no caso html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Lê o arquivo em CSV e transforma em um dataframe
#Data Frame organiza os dados em linhas e colunas
df = pd.read_csv("LOPAL_Integrador.csv")

#Pego o data frame e converto para Execel, com o comando (to_excel)
df.to_excel("funcionalidade_dois.xlsx", index=False)

#Dados para conseguir enviar o e-mail
remetente = 'leticiaroth1@gmail.com'
senha = 'qlgh uykw acrn xigv'
destinatario = 'leticiaroth1@gmail.com'
assunto = 'Projeto Integrador - Funcionalidade Email'


#Tentará ler o Excel, antes de gerar erro, qualquer coisa roda o Exception
try:
    df =pd.read_excel("funcionalidade_dois.xlsx")

    #Gera uma tabela em HTML simples
    tabela_html = df.to_html(classes='table table-striped')

    #MIMEMultiparti cria a estrtura do email, com os valores atribuido lá em cima
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem ['To'] = destinatario
    mensagem['Subject'] = assunto

    #Manda a mensagem
    corpo = f"<html><body><p>Abaixo veja os dados do Excel do Projeto Integrador.</p>{tabela_html}</body></html>"
    parte_html = MIMEText(corpo, 'html')
    mensagem.attach(parte_html)

    #Servidor SMTP, necessário inserir o gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remetente,senha)
        servidor.sendmail(remetente,destinatario,mensagem.as_string())
    print("Email enviado com sucesso!")

except Exception as e:
    print(f"Erro ao enviar email {e}")


