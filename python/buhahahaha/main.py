from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    difference = None

    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        date1 = datetime.strptime(start_date, '%Y-%m-%d')
        date2 = datetime.strptime(end_date, '%Y-%m-%d')

        difference = abs((date2 - date1).days)

    return render_template('index.html', difference=difference)

if __name__ == '__main__':
    app.run(debug=True)
