from flask import Flask, jsonify, request
from flask_cors import CORS

import time

from deepface import DeepFace

app = Flask(__name__)
CORS(app)
CORS(app, origins=['*'])


@app.route('/verify', methods=['GET', 'POST'])
def verify():

	tic = time.time()
	req = request.get_json()

	try:

		verif_result = DeepFace.verify(req["img1"], req["img2"], model_name = req["model_name"])

		#response
		resp_obj = jsonify({'success': True, 'result': verif_result})
		resp_obj.status_code = 200

	except Exception as e:

		resp_obj = jsonify({'success': False, 'error': str(e)})
		resp_obj.status_code = 400

	toc = time.time()
	print("Response time: ", toc-tic, " seconds")

	return resp_obj

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000, debug=True)

	