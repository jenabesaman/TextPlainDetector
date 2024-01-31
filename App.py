import os
from flask import Flask, request, jsonify
import TextPlainDetector

app = Flask(__name__)
app.debug = True


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'message': 'Invalid Input Url'})


@app.errorhandler(400)
def invalid_route(e):
    return jsonify({'errorCode': 400, 'message': 'Bad Request,input json text is not correct'})


@app.errorhandler(500)
def invalid_route(e):
    return jsonify({'errorCode': 500, 'message': 'Internal Server Error'})


@app.route("/ping")
def ping():
    return "This is a api test only"

@app.route("/textplain", methods=["post"])
def predicting():
    try:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        data = request.get_json(force=True)
        if "string" in data and data["string"]:
            string = data["string"]
            obj = TextPlainDetector.TextPlainDetector(string)
            result = obj.predicting()
            return jsonify({'result': result})
        else:
            return "No string provided in the request data"
    except Exception as e:
        print(e)  # This will print the exception message, which can help with debugging
        return "cant predict"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8544, use_reloader=False)
