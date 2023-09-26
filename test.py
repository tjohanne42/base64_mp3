import requests

url = "http://127.0.0.1:5000/"
fname = "base64.txt"
output_fname = "music.mp3"

with open(fname, 'rb') as data:
	r = requests.post(url, files={'file': data})

with open(output_fname, "wb") as fout:
	fout.write(r.content)