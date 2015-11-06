from flask import Flask, session, request, redirect, render_template
import random
app = Flask(__name__)
app.secret_key ='wordsAndStuffAndThings'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	try:
		session['gold']
	except:
		session['gold'] = 0

	try: 
		session['activities']
	except:
		session['activities'] = 0

	if request.form['whatever'] == 'farm':
		gold = random.randrange(10,21)
		# session['activity] = 'test'
	elif request.form['whatever'] == 'cave':
		gold = random.randrange(5,11)
	elif request.form['whatever'] == 'house':
		gold = random.randrange(2,6)
	elif request.form['whatever'] == 'casino':
		gold = random.randrange(-50,51)

	session['gold'] += gold
	session['activity'] 

	return redirect('/')

app.run(debug=True)