#!flask/bin/python
from flask import Flask
import requests

app = Flask(__name__)

signals = {}
signals["Source"] = [9004, 4500, 560, 568, 560, 568, 558, 568, 560, 568, 560, 568, 558, 568, 558, 568, 560, 566, 560, 1694, 560, 1696, 558, 1696, 560, 1694, 560, 1694, 560, 1696, 560, 1694, 560, 568, 560, 568, 560, 1694, 560, 568, 560, 568, 558, 1694, 560, 568, 560, 568, 558, 568, 560, 1694, 560, 568, 560, 1694, 560, 1696, 558, 568, 560, 1694, 560, 1696, 560, 1694, 560]
signals["ampli toggle"] = [416, 658, 368, 1738, 368, 684, 366, 686, 366, 686, 394, 1710, 392, 662, 366, 686, 366, 686, 394, 658, 368, 684, 368, 1738, 338, 1768, 366, 686, 394, 658, 368]

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
