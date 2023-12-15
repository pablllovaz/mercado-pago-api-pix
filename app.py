from flask import Flask, jsonify, make_response, request, send_from_directory, Response, abort
import controller
import json

app = Flask(__name__)

@app.route('/list_payments',  methods=["GET"])
def list_payments():
    return "{\"msg\":\"hello\"}" 
    # tem que buscar no model.py os ids, valores e descrições dos pagamentos

@app.route('/get_payment', methods=["POST"])
def get_payment():

    try:
        res = controller.get_payment(
            request.json["price"], 
            request.json["description"]
        )
        if "id" in res.keys():
            return jsonify(res)
        else:
            return Response(
                json.dumps(res),
                mimetype="application/json",
                status=res["status"],
            )
    except:
        res = {
            'message': 'The \'price\' and \'description\' parameters are required!',
            'error': 'bad_request',
            'status': 400
        }
        return Response(
            json.dumps(res),
            mimetype="application/json",
            status=400,
        )

@app.route('/verify_payment',  methods=["GET"])
def verify_payment():
    
    try:
        res = controller.verify_payment(request.json["id"])
        return jsonify(res) 
    except:
        return make_response('Bad Request', 400)

@app.route('/qrcode/<path:path>')
def serve_static(path):
    return send_from_directory('qrcode', path)

if __name__ == '__main__':
    app.run(debug=True)