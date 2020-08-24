import requests
import datetime

todate = datetime.date.today()
fromdate = datetime.date(todate.year, todate.month, todate.day - 2)
url = 'https://api.stackexchange.com/2.2/questions'
payload = {'site': 'stackoverflow', 'tagged': 'python', 'fromdate': f'{fromdate}', 'todate': f'{todate}'}

response = requests.get(url, params=payload)
questions_json = response.json()

for question in questions_json['items']:
    print(f"Title: {question['title']}\nId: {question['question_id']}\nLink: {question['link']}\n")