from flask import Flask, request, jsonify
import whisper
import subprocess
import os

app = Flask(__name__)

# Load Whisper model
model = whisper.load_model("large-v3")


@app.route('/translate', methods=['POST'])
def translate_audio():
    # Check if the audio file is part of the request
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    audio_path = os.path.join("/tmp", audio_file.filename)
    audio_file.save(audio_path)

    # Run translation task using Whisper model
    result = model.transcribe(audio_path, task="translate")

    # Clean up the saved audio file
    os.remove(audio_path)

    return jsonify({"translation": result['text']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
