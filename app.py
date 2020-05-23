
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@stocktrial.route('/')
def index():
  return render_template('index.html')

@stocktrial.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
