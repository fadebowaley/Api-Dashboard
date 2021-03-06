from flask import Flask
from flask import request, render_template, jsonify
import json
import schedule
import time
import requests

app = Flask(__name__)

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
page = requests.get(url)
data = page.json()


def fetch_bitcoin():
    print("Getting Prices ........")
    result  = data['bpi']['USD']
    print(result)


@app.route('/Dashboard')
def fetch_bitcoin_by_currency(x):
    print("Getting Prices  in ........", x)
    result  = data['bpi'][x]
    print(result)

#schedule.every(10).seconds.do(fetch_bitcoin)
schedule.every(10).seconds.do(fetch_bitcoin_by_currency, 'USD')
schedule.every(10).seconds.do(fetch_bitcoin_by_currency, 'GBP')
schedule.every(10).seconds.do(fetch_bitcoin_by_currency, 'EUR')


while True:
    schedule.run_pending()
    time.sleep(1)



@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # You'd normally use the variables above to limit the data returned
    # you don't want to return ALL events like in this code
    # but since no db or any real storage is implemented I'm just
    # returning data from a text file that contains json elements

    with open("flaskcalendar/events.json", "r") as input_data:
        # you should use something else here than just plaintext
        # check out jsonfiy method or the built in json module
        # http://flask.pocoo.org/docs/0.10/api/#module-flask.json
        return input_data.read()







if __name__ == '__main__':
    app.debug = True
    app.run()
