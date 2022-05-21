import json
import random
from datetime import date
from flask import Flask
app = Flask(__name__)

today_date = date.today()
DAY = int(today_date.strftime('%d'))
print(f"Today is: {today_date}")


@app.route("/")
def main():
  return get_word_of_day()


def get_word_of_day():
	with open('data.json', 'r') as f:
		data = json.load(f)
		return dict(data["words"][DAY])



if __name__ == '__main__':
	main()