

import yagmail
import pandas
from news_feed import NewsFeed
import datetime

df = pandas.read_excel("Sample Data.xlsx")
for i, row in df.iterrows():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    nf = NewsFeed(interest=row['interest'],
                  from_date=yesterday,
                  to_date=today,
                  language='en')
    content = nf.get()
    email = yagmail.SMTP("salmanahmad111499@gmail.com", "hozh uhdy dllv fpct")
    email.send(row['email'], subject=f"{row['name'].capitalize()} your {row['interest']} news for today!", contents=content)