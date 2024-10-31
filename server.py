"""
This script is used to create a Flask server that will be used 
to detect the emotion of a given text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/emotionDetector')

def sent_detector():
    '''Detect the emotion of a given text.'''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (f"For the given statement, the system response is 'anger': {result['anger']},"
            f" 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. The dominant emotion "
            f"is {result['dominant_emotion']}.")

@app.route('/')
def render_index_page():
    '''Render the index page.'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
