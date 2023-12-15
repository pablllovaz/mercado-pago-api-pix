import mercadopago
import datetime
import base64

credentials = {
    "public_key": "ENTRE COM SUA PUBLIC KAY AQUI!",
    "access_token": "ENTRE COM SEU ACESS TOKEN AQUI"
}

def get_qrcode(base64_string):
    date = str(datetime.datetime.now())
    b64 = base64.b64encode(date.encode()).decode()
    
    filepath = f"qrcode/{((b64.replace('=', '')) + '.png').lower()}"

    image_data = base64.b64decode(base64_string)
    with open(f"app/{filepath}", 'wb') as f:
         f.write(image_data)

    return filepath

def get_payment(price, description):
    payment_data = {
        "transaction_amount": price,
        "description": description,
        "payment_method_id": "pix",
        "payer": { "email": "pabllovaz@gmail.com" }
    }

    sdk = mercadopago.SDK(credentials['access_token'])
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    try:
        data = payment["point_of_interaction"]['transaction_data']

        filepath = get_qrcode(data['qr_code_base64'])

        return {
            'id': payment['id'],
            'clipboard': str(data['qr_code']), 
            'qrcode_png_filepath': filepath
        }
    except:
        return payment

def verify_payment(payment_id):
    sdk = mercadopago.SDK(credentials['access_token'])
    payment_response = sdk.payment().get(payment_id)
    payment = payment_response["response"]
    status = payment['status']
    detail = payment['status_detail']
    return {
        'id': payment_id, 
        'status': status, 
        'status_detail': detail
    }