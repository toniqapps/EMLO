
import PIL.Image
from flask import Flask, render_template, request, jsonify
from models import MobileNet
import os
import time
import sys
from shutil import copyfile
from math import floor

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

model = MobileNet()

def main():
    files = sys.argv[1:]
    if(files and len(files) > 0):
        filename = files[0]
        saveLocation = os.path.join('static/img', filename)
        f = PIL.Image.open(saveLocation)
        inference, confidence = model.infer(saveLocation)
        confidence = floor(confidence * 10000) / 100
        newFileName = str(inference)+'_'+str(confidence) + \
                '_'+filename
        filepath = os.path.join('static/results', newFileName)
        f.save(filepath)

@app.route('/')
def index():
    results = os.listdir('static/results')
    results = sorted(results, key=lambda t: os.stat(
            os.path.join('static/results', t)).st_mtime, reverse=True)
    return render_template('main.html', results=results)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/infer', methods=['POST'])
def success():
    if request.method == 'POST':
        files = request.files.getlist('file')

        preFiles = os.listdir('static/results')
        preFiles = sorted(preFiles, key=lambda t: os.stat(
            os.path.join('static/results', t)).st_mtime)
        totalFiles = len(preFiles) + len(files)
        if totalFiles > 5:
            removeCount = totalFiles - 5
            print(removeCount)
            for i in range(removeCount):
                print(i, preFiles[i])
                os.remove(os.path.join('static/results', preFiles[i]))
        results = []
        for f in files:
            saveLocation = os.path.join('static/results', f.filename)
            f.save(saveLocation)
            inference, confidence = model.infer(saveLocation)
            # # make a percentage with 2 decimal points
            confidence = floor(confidence * 10000) / 100

            # # rename file with result
            newFileName = str(inference)+'_'+str(confidence) + \
                '_'+str(time.time())+'_'+f.filename
            old_file = os.path.join("static/results", f.filename)
            new_file = os.path.join("static/results", newFileName)
            os.rename(old_file, new_file)
            result = {'name': inference, 'confidence': confidence,
                      'imagepath': newFileName}
            results.append(result)
        # respond with the inference
        return render_template('inference.html', results=results)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 80))
    main()
    app.run(host='0.0.0.0', port=port, debug=True)
