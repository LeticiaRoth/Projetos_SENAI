import pandas as pd
#Usado para pegar a hora e data especificias
#Timdelta consigo manipular a data e hora
from datetime import datetime, timedelta
import pywhatkit as kit

# Caminho do seu arquivo CSV
arquivo_csv = r'LOPAL_Integrador.csv'

# Lê o arquiv CSV com o pandas
df = pd.read_csv(arquivo_csv)

#Pega a coluna nomeada com data dentro do arquivo e formata
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')

#Data de exemplo, converte para o formato data
data_escolhida = datetime.strptime('16/11/2024', '%d/%m/%Y').date()

# Filtra pela linha escolhida usando o data frame
df_data = df[df['Date'].dt.date == data_escolhida]

if df_data.empty:
    print("Nenhum dado encontrado para a data 16/11/2024.")
else:
    #Pega o último resgistro do dia, iloc idexador de posição do pandas
    linha = df_data.iloc[-1]
    mapa_niveis = {
        1: '🔴',
        2: '🟡',
        3: '🟢'
    }

    # Gera a mensagem
    msg = f"Estoque em 16/11: "
    msg += f"Esteira 1: {mapa_niveis.get(linha['esteira1'])} | "
    msg += f"Esteira 2: {mapa_niveis.get(linha['esteira2'])} | "
    msg += f"Esteira 3: {mapa_niveis.get(linha['esteira3'])}"

    numero = '+5519995594323'

    # Define o horário de envio 1 minuto após
    agora = datetime.now() + timedelta(minutes=1)
    hora = agora.hour
    minuto = agora.minute

    print("Mensagem agendada para envio:")
    print(msg)


    # Envia pelo navegador, no whatsapp web
    kit.sendwhatmsg(numero, msg, hora, minuto)
