from flask import FLask, session, request, redirect, render_template
import random
app = Flask(__name__)
app.secret_key ='wordsAndStuffAndThings'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money' methods=['POST'])
	return redirect('/')

app.run(debug=True)