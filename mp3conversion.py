from flask import Flask, request, jsonify, make_response
import base64

app = Flask(__name__)
from flask_restful import Api, Resource
api = Api(app)

class DecodeMP3(Resource):
    def post(self):
        try:
            # get the base64 encoded MP3 from the request
            data = request.json
            data = data['b64_mp3'].encode('ascii')
            print(len(data))
            # decode the base64 encoded MP3
            binary_mp3 = base64.b64decode(data)
            
            # return the binary format
            response = make_response(binary_mp3)
            response.headers.set('Content-Type', 'audio/mpeg')
            return response
        except Exception as e:
            return jsonify({"error": str(e)})

# add the resource to the API
api.add_resource(DecodeMP3, "/decode")

if __name__ == '__main__':
    app.run(debug=True)