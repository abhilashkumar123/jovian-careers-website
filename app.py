from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Software Engineer 1',
  'Location': 'Delhi',
  'Sal': 'Rs. 10,00000'
}, {
  'id': 2,
  'title': 'Software Engineer 2',
  'Location': 'Delhi',
  'Sal': 'Rs. 12,00000'
}, {
  'id': 3,
  'title': 'Software Engineer 3',
  'Location': 'Delhi',
  'Sal': 'Rs. 15,00000'
}, {
  'id': 4,
  'title': 'Software Engineer 4',
  'Location': 'Delhi'
}]
#Now we have to make this available in home.html.Will pass this through render_template function.Then inside home.html will use some code to make it visible in UI.


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, Company_Name='Jovian Careers')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
