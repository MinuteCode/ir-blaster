#!flask/bin/python
from flask import Flask
import requests

app = Flask(__name__)

signals = {}
signals["Source"] = [9004, 4500, 560, 568, 560, 568, 558, 568, 560, 568, 560, 568, 558, 568, 558, 568, 560, 566, 560, 1694, 560, 1696, 558, 1696, 560, 1694, 560, 1694, 560, 1696, 560, 1694, 560, 568, 560, 568, 560, 1694, 560, 568, 560, 568, 558, 1694, 560, 568, 560, 568, 558, 568, 560, 1694, 560, 568, 560, 1694, 560, 1696, 558, 568, 560, 1694, 560, 1696, 560, 1694, 560]
signals["ampli toggle"] = [394, 660, 392, 1714, 366, 688, 362, 690, 366, 686, 390, 662, 364, 688, 364, 688, 362, 690, 362, 1744, 362, 1744, 336, 1770, 362, 1744, 390, 662, 360, 692, 360]

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
