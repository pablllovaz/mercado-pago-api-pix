# mercado-pago-api-pix

# Configurar Credenciais

Para configurar, Precisamos das credenciais do Mercado Pago, public_key e access_token, iremos adicionar elas no arquivo Controller.py.

# Bibliotecas

Para instalar as bibliotecas necessarias basta utilizar o requirements.txt que se encontra na raiz do projeto! Use: pip install -r requirements. txt

# Criando Um Pagamento
/get_payment Gera uma solicitação de pagamento com o paramentro price e description passado no Body da requisição.

# Verificando Status do Pagamento
/verify_payment Status da Transação criada! Passando o parametro ID no Body da requisição.
