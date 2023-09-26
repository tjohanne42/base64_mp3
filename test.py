import requests

url = "https://base64-mp3.vercel.app"
fname = "base64.txt"
output_fname = "music.mp3"

with open(fname, 'rb') as data:
	r = requests.post(url, files={'file': data})
print(r)

with open(output_fname, "wb") as fout:
	fout.write(r.content)