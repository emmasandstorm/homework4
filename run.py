from flask import Flask, render_template

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
	name = {'name':'Carlos'}
	city_names = [{'city':'Paris'}, {'city':'New york'}, {'city': 'Tokyo'}, {'city':'Livermore'}]
	return render_template('not_google.html', username = name, city_names = city_names)

if __name__ = '__main__':
	myapp_obj.run()
