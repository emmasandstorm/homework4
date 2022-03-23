from flask import Flask, render_template

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
        name = {'name':'Carlos'}
        city_names = [{'city':'Paris'}, {'city':'New york'}, {'city': 'Tokyo'}, {'city':'Livermore'}]
        return'''
<html>
    <head>
        <h1> Welcome''' + name['name'] +'''!</h1>
    </head>
    <body> <a href = "https://www.google.com/">not google</a>
      <div>
      <ul>
        {% for cities in city_names %}
          <li> '''+city_names['city']+''' </li>
        {% endfor %}
      </ul>
      </div>
    </body>
    </html> '''

if __name__ == '__main__':
        myapp_obj.run()
