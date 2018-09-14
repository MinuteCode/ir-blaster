#!flask/bin/python
from flask import Flask
import requests

app = Flask(__name__)

signals = {}
signals["Source"] = [9004, 4500, 560, 568, 560, 568, 558, 568, 560, 568, 560, 568, 558, 568, 558, 568, 560, 566, 560, 1694, 560, 1696, 558, 1696, 560, 1694, 560, 1694, 560, 1696, 560, 1694, 560, 568, 560, 568, 560, 1694, 560, 568, 560, 568, 558, 1694, 560, 568, 560, 568, 558, 568, 560, 1694, 560, 568, 560, 1694, 560, 1696, 558, 568, 560, 1694, 560, 1696, 560, 1694, 560]
signals["ampli toggle"] = [272, 782, 272, 1834, 270, 782, 272, 780, 270, 782, 272, 782, 270, 782, 270, 782, 270, 782, 270, 1834, 270, 1838, 272, 1834, 270, 1836, 272, 780, 272, 780, 272]

@app.route('/')
def index():
	return "Hello, World"

@app.route('/api/scene/cinema')
def trigger_cinema_scene():
	url = "http://192.168.1.56/play"
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	timings = ""
	for element in signals['ampli toggle']:
		timings += str(element) + ", "
	timings = timings[:-2]
	payload = {'timings': timings}
	r = requests.post(url, data=payload, headers=headers)
	return r.text
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
