#!flask/bin/python
from flask import Flask
from flask_assistant import Assistant, ask, tell
import requests
import time
import threading
import json

app = Flask(__name__)
assist = Assistant(app, route='/')

signals = {}
signals["Power TV"] = [9010, 4474, 584, 544, 584, 544, 584, 544, 584, 542, 584, 544, 584, 544, 556, 570, 584, 544, 582, 1672, 584, 1670, 584, 1672, 584, 1670, 584, 1670, 584, 1672, 582, 1672, 582, 544, 584, 1672, 584, 542, 558, 1698, 584, 544, 582, 1672, 584, 542, 584, 544, 584, 544, 582, 544, 584, 1670, 558, 570, 584, 1670, 582, 544, 582, 1672, 584, 1670, 584, 1670, 582]
signals["Source"] = [9004, 4500, 560, 568, 560, 568, 558, 568, 560, 568, 560, 568, 558, 568, 558, 568, 560, 566, 560, 1694, 560, 1696, 558, 1696, 560, 1694, 560, 1694, 560, 1696, 560, 1694, 560, 568, 560, 568, 560, 1694, 560, 568, 560, 568, 558, 1694, 560, 568, 560, 568, 558, 568, 560, 1694, 560, 568, 560, 1694, 560, 1696, 558, 568, 560, 1694, 560, 1696, 560, 1694, 560]
signals["DTV"] = [9150, 4352, 682, 446, 706, 422, 678, 448, 680, 448, 678, 448, 696, 430, 682, 444, 680, 446, 706, 1548, 706, 1546, 682, 1574, 678, 1576, 678, 1576, 678, 1578, 680, 1574, 680, 446, 678, 1576, 678, 1576, 680, 446, 678, 1576, 706, 422, 706, 422, 680, 446, 678, 448, 704, 422, 678, 448, 678, 1576, 706, 420, 676, 1578, 678, 1578, 680, 1574, 680, 1574, 678]
signals["Down"] = [9134, 4350, 678, 448, 682, 446, 704, 422, 680, 446, 708, 420, 682, 446, 680, 446, 680, 448, 682, 1574, 682, 1574, 678, 1574, 682, 1574, 680, 1576, 682, 1572, 704, 1550, 680, 448, 680, 1574, 682, 444, 678, 1576, 680, 1574, 682, 444, 678, 448, 682, 446, 682, 446, 706, 422, 706, 1546, 680, 448, 708, 418, 680, 1574, 680, 1574, 706, 1548, 682, 1572, 708]
signals["Enter"] = [9152, 4350, 680, 446, 682, 446, 676, 450, 680, 448, 678, 448, 708, 420, 682, 446, 682, 444, 676, 1578, 680, 1574, 684, 1570, 682, 1574, 682, 1572, 708, 1546, 680, 1574, 678, 450, 682, 444, 680, 446, 678, 450, 678, 448, 708, 1546, 678, 448, 682, 446, 706, 418, 682, 1574, 678, 1576, 678, 1576, 680, 1574, 680, 448, 678, 1574, 682, 1572, 680, 1574, 682]

@app.route('/')
def hello():
	speech = "Hey ! Are you a male or a female ?"
	return tell(speech)


# @assist.action('give-gender')
# def ask_for_gender(gender):
# 	if gender == 'male':
# 		gender_msg = 'Sup bro !'
# 	else:
# 		gender_msg = 'Haay gurl!'

# 	speech = gender_msg + ' What is you favorite color ?'
# 	return ask(speech)

# @assist.action('give-color', mapping={'color': 'sys.color'})
# def ask_for_color(color):
# 	speech = 'Ok {} is an ok color I guess'.format(color)
# 	return ask(speech)

if __name__ == '__main__':
	app.run(debug=True)

# #DENON AVR COMMANDS
# signals["ampli toggle"] = [250, 806,  248, 1858,  246, 806,  246, 806,  248, 804,  248, 1858,  248, 804,  248, 804,  248, 804,  248, 806,  248, 804,  248, 1858,  248, 1858,  248, 806,  246, 806,  248]

# @app.route('/')
# def index():
# 	return "Hello, World"

# @app.route('/api/scene/ampli_power')
# def ampli_power():
# 	url = "http://192.168.1.56/play"
# 	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# 	timings = ""
# 	for element in signals["ampli toggle"]:
# 		timings += str(element) + ", "
	
# 	timings = timings[:-2]
# 	payload = {'timings': timings}
# 	r = requests.post(url, data=payload, headers=headers)
# 	return r.text

# @app.route('/api/scene/power_tv')
# def power_tv():
# 	index = 0
# 	print(str(index))
# 	sent_signals = [signals["Power TV"]]
# 	url = "http://192.168.1.56/play"
# 	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# 	def run_job(index):
# 		while index < 1:
# 			timings = ""
# 			for element in sent_signals[index]:
# 				timings += str(element) + ", "

# 			timings = timings[:-2]
# 			payload = {'timings': timings}
# 			r = requests.post(url, data=payload, headers=headers)
# 			sleep_timer = 0.2
# 			if index <= 0:
# 				sleep_timer = 3
# 			time.sleep(sleep_timer)
# 			index += 1

# 	thread = threading.Thread(target=run_job, args=[index])
# 	thread.start()
# 	return "TV powered"

# @app.route('/api/scene/chromecast')
# def trigger_chromecast_scene():
# 	index = 0
# 	print(str(index))
# 	sent_signals = [signals["DTV"], signals["Source"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Enter"]]
# 	url = "http://192.168.1.56/play"
# 	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# 	def run_job(index):
# 		while index < 10:
# 			timings = ""
# 			for element in sent_signals[index]:
# 				timings += str(element) + ", "

# 			timings = timings[:-2]
# 			payload = {'timings': timings}
# 			r = requests.post(url, data=payload, headers=headers)
# 			sleep_timer = 0.2
# 			if index <= 0:
# 				sleep_timer = 3
# 			time.sleep(sleep_timer)
# 			index += 1

# 	thread = threading.Thread(target=run_job, args=[index])
# 	thread.start()
# 	return "Chromecast scene successfully triggered"

# @app.route('/api/scene/kodi')
# def trigger_kodi_scene():
# 	index = 0
# 	sent_signals = [signals["DTV"], signals["Source"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Enter"]]
# 	url = "http://192.168.1.56/play"
# 	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# 	def run_job(index):
# 		while index < 8:
# 			timings = ""
# 			for element in sent_signals[index]:
# 				timings += str(element) + ", "

# 			timings = timings[:-2]
# 			payload = {'timings': timings}
# 			r = requests.post(url, data=payload, headers=headers)
# 			sleep_timer = 0.2
# 			if index <= 0:
# 				sleep_timer = 3
# 			time.sleep(sleep_timer)
# 			index += 1

# 	thread = threading.Thread(target=run_job, args=[index])
# 	thread.start()
# 	return json.dumps({'fullfillmentText': 'Changement de la source pour kodi', 'outputContexts': []})

# @app.route('/api/scene/power_up_to_chromecast')
# def trigger_powerup_to_chromecast():
# 	index = 0
# 	print(str(index))
# 	sent_signals = [signals["Power TV"], signals["DTV"], signals["Source"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Down"], signals["Enter"]]
# 	url = "http://192.168.1.56/play"
# 	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# 	def run_job(index):
# 		while index < 11:
# 			timings = ""
# 			for element in sent_signals[index]:
# 				timings += str(element) + ", "

# 			timings = timings[:-2]
# 			payload = {'timings': timings}
# 			r = requests.post(url, data=payload, headers=headers)
# 			sleep_timer = 0.2
# 			if index == 0:
# 				sleep_timer = 15
# 			elif index == 1:
# 				sleep_timer = 5
# 			time.sleep(sleep_timer)
# 			index += 1

# 	thread = threading.Thread(target=run_job, args=[index])
# 	thread.start()
# 	return "Chromecast scene successfully triggered"
