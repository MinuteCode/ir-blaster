#!flask/bin/python
from flask import Flask
import requests
import time
import threading

app = Flask(__name__)

signals = {}
signals["Source"] = [9004, 4500, 560, 568, 560, 568, 558, 568, 560, 568, 560, 568, 558, 568, 558, 568, 560, 566, 560, 1694, 560, 1696, 558, 1696, 560, 1694, 560, 1694, 560, 1696, 560, 1694, 560, 568, 560, 568, 560, 1694, 560, 568, 560, 568, 558, 1694, 560, 568, 560, 568, 558, 568, 560, 1694, 560, 568, 560, 1694, 560, 1696, 558, 568, 560, 1694, 560, 1696, 560, 1694, 560]
signals["DTV"] = [9150, 4352, 682, 446, 706, 422, 678, 448, 680, 448, 678, 448, 696, 430, 682, 444, 680, 446, 706, 1548, 706, 1546, 682, 1574, 678, 1576, 678, 1576, 678, 1578, 680, 1574, 680, 446, 678, 1576, 678, 1576, 680, 446, 678, 1576, 706, 422, 706, 422, 680, 446, 678, 448, 704, 422, 678, 448, 678, 1576, 706, 420, 676, 1578, 678, 1578, 680, 1574, 680, 1574, 678]
signals["Down"] = [9134, 4350, 678, 448, 682, 446, 704, 422, 680, 446, 708, 420, 682, 446, 680, 446, 680, 448, 682, 1574, 682, 1574, 678, 1574, 682, 1574, 680, 1576, 682, 1572, 704, 1550, 680, 448, 680, 1574, 682, 444, 678, 1576, 680, 1574, 682, 444, 678, 448, 682, 446, 682, 446, 706, 422, 706, 1546, 680, 448, 708, 418, 680, 1574, 680, 1574, 706, 1548, 682, 1572, 708]
signals["Enter"] = [9152, 4350, 680, 446, 682, 446, 676, 450, 680, 448, 678, 448, 708, 420, 682, 446, 682, 444, 676, 1578, 680, 1574, 684, 1570, 682, 1574, 682, 1572, 708, 1546, 680, 1574, 678, 450, 682, 444, 680, 446, 678, 450, 678, 448, 708, 1546, 678, 448, 682, 446, 706, 418, 682, 1574, 678, 1576, 678, 1576, 680, 1574, 680, 448, 678, 1574, 682, 1572, 680, 1574, 682]
#signals["ampli toggle"] = [272, 782, 272, 1834, 270, 782, 272, 780, 270, 782, 272, 782, 270, 782, 270, 782, 270, 782, 270, 1834, 270, 1838, 272, 1834, 270, 1836, 272, 780, 272, 780, 272]

@app.route('/')
def index():
	return "Hello, World"

@app.route('/api/scene/chromecast')
def trigger_chromecast_scene():
	index = 0
	print(str(index))
	sent_signals = [signals["DTV"], signals["Source"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Enter"]]
	url = "http://192.168.1.56/play"
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	def run_job(index):
		while index < 10:
			timings = ""
			for element in sent_signals[index]:
				timings += str(element) + ", "

			timings = timings[:-2]
			payload = {'timings': timings}
			r = requests.post(url, data=payload, headers=headers)
			print(r.text)
			index += 1

	thread = threading.Thread(target=run_job, args=[index])
	thread.start()
	return "Chromecast scene successfully triggered"

@app.route('/api/scene/kodi')
def trigger_kodi_scene():
	index = 0
	sent_signals = [signals["DTV"], signals["Source"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Enter"]]
	url = "http://192.168.1.56/play"
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	def run_job(index):
		while index < 8:
			timings = ""
			for element in sent_signals[index]:
				timings += str(element) + ", "

			timings = timings[:-2]
			payload = {'timings': timings}
			r = requests.post(url, data=payload, headers=headers)
			index += 1

	thread = threading.Thread(target=run_job, args=[index])
	thread.start()
	return "Kodi scene successfully triggered"
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
