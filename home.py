from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
        name = {'name':'Carlos'}
        city_names = ['Paris', 'New york', 'Tokyo', 'Livermore']
        return'''
	<html>
		<head>
		<h1> Welcome '''+name['name']+'''!</h1> </head>
		<body> <a href = "https://www.google.com/">not google</a>
		<div>
			<ul>
			<li> '''+city_names[0]+''' </li> <li> '''+city_names[1]+''' </li>
			<li> '''+city_names[2]+''' </li> <li> '''+city_names[3]+''' </li>
			</ul>
		</div>
		</body>
	</html> '''

if __name__ == '__main__':
        myapp_obj.run()
