# mercado-pago-api-pix

# Configurar Credenciais

Para configurar, Precisamos das credenciais do Mercado Pago, public_key e access_token, iremos adicionar elas no arquivo Controller.py.

# Bibliotecas

Para instalar as bibliotecas necessarias basta utilizar o requirements.txt que se encontra na raiz do projeto! Use: pip install -r requirements. txt

# Criando Um Pagamento
/get_payment Gera uma solicitação de pagamento com o paramentro price e description passado no Body da requisição.

# Verificando Status do Pagamento
/verify_payment Status da Transação criada! Passando o parametro ID no Body da requisição.

# QrCODE PNG
O qrcode em PNG pode ser obtido na criação do pagamento! Na chave de retorno qrcode_png_filepath É são armazenados na pasta /qrcode
Exemplo de retorno:

{
  "clipboard": "COPIA E COLA",
  "id": 68803678140,
  "qrcode_png_filepath": "qrcode/mjaymy0xmi0xncaymzo0odo1ns43ntgznty.png"
}


# Apagar QrCODEs
O arquivo schedule.py apaga todos os PNG de QrCODE gerados na pasta /qrcode de 8 em 8 horas! pode ser executado de forma opcional usando nohup.
