from flask import Blueprint, render_template, url_for, request, redirect
import speech_recognition as sr


transcription = Blueprint('transcription', __name__, template_folder='templates')


@transcription.route('/transcribe', methods=['GET', 'POST'])
def transcribe():
	transcript = ""
	if request.method == 'POST':
		
		if 'file' not in request.files:
			return redirect(request.url)

		file = request.files['file']
		if file.filename == "":
			return redirect(request.url)

		if file:
			recognizer = sr.Recognizer()
			audioFile = sr.AudioFile(file)
			with audioFile as source:
				data = recognizer.record(source)
			transcript = recognizer.recognize_google(data, key=None)
		
	return render_template('transcribe.html', transcript=transcript)
