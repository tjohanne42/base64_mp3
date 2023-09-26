from flask import Flask, request, jsonify, make_response
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_file():
	if request.method == 'POST':
		try:
			file = request.files['filedata'].read()
			binary_mp3 = base64.b64decode(file)
			response = make_response(binary_mp3)
			response.headers.set('Content-Type', 'audio/mpeg')
			return response
		except Exception as e:
			return f"ERROR:\n{str(e)}"
	else:
		return "base64 -> mp3 API"

if __name__ == '__main__':
	app.run(debug=True)