

from flask.views import MethodView
from flask import Flask, render_template, request
import pandas
import yagmail
import datetime
import requests

app = Flask(__name__)

TOTAL_ROWS = int
LIST_OF_CANDIDATE_EMAILS = []

class UploadFile(MethodView):

    _file_name = ''
    _base_url = "https://newsapi.org/v2/everything?"
    _api_key = "bc522e4ccbcf440090f7fea7725e156d"
    _total_rows = 0

    def get(self):
        return render_template("index.html")

    def post(self):
        f = request.files['file']
        f.save(f.filename)
        # storing filename
        self._file_name = f.filename
        self.do_stuff()
        return render_template('sending_emails.html', total_rows=str(TOTAL_ROWS),
                               candidate_email_address=LIST_OF_CANDIDATE_EMAILS,
                               total_rows_int=int(TOTAL_ROWS))

    def do_stuff(self):
        """
        This function will read Excel file, scrap news using api, and send emails to users specified.
        :return:
        """
        # first, we need to read from Excel file
        # reading from Excel file
        data_frame_object = self.read_from_excel_file()
        # now, we have our data frame object
        # we need to iterate on it
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
        for i, row in data_frame_object.iterrows():
            # putting candidate emails in list
            LIST_OF_CANDIDATE_EMAILS.append(row['email'])
            # construct an url based on person interest
            url = self.construct_url(row['interest'], yesterday, today)
            # make a request on the specified url
            json_format = self.make_request(url)
            # now we have our particular interest type of news in JSON form
            # we just need to parse it to get our data
            list_of_news = json_format['articles']
            email_body = self.construct_email_body(list_of_news)
            # now we have our email_body, we can start sending an email
            subject = f"{row['name'].capitalize()} your {row['interest'].capitalize()} for today!"
            self.send_email(email_address=row['email'],
                            subject=subject,
                            content=email_body)

    def make_request(self, url):
        """
        This function makes a request on the specified url.
        :param url:
        :return:
        """
        # making a request
        response = requests.get(url)
        # storing in JSON format
        json_format = response.json()
        return json_format

    def read_from_excel_file(self):
        """
        This function constructs a data frame object
        and returns it
        :return:
        """
        # reading from Excel file
        df = pandas.read_excel(self._file_name)
        # storing total rows in global variable
        global TOTAL_ROWS
        TOTAL_ROWS = len(df.index)
        return df

    def construct_url(self, interest, from_date, to_date, language='en'):
        """
        This function creates an url on which request is to be made.
        :param interest:
        :param from_date:
        :param to_date:
        :param language:
        :return:
        """
        # first we need base url
        url = self._base_url
        url = url + (f"qInTitle={interest}&"
                     f"from={from_date}&"
                     f"to={to_date}&"
                     f"language={language}&"
                     f"apiKey={self._api_key}")
        # now we have the proper url, we need to return it
        return url

    def construct_email_body(self, list_of_news):
        """
        This function constructs an email body depending on person interests
         to be sent to users emails
        :return:
        """
        email_body = ""
        for i in list_of_news:
            email_body = email_body + f"{i['title']}\n{i['url']}\n\n"
        # returning email_body
        return email_body

    def send_email(self, email_address, subject, content):
        """
        This function sends an email to the specified email address
        :param email_address:
        :param subject:
        :param content:
        :return:
        """
        email = yagmail.SMTP("salmanahmad111499@gmail.com", "hozh uhdy dllv fpct")
        email.send(email_address, subject, content)


class SendingEmails(MethodView):
    """
    This class creates a webpage that shows to whom emails are being sent.
    """

    def get(self):
        return render_template("sending_emails.html", total_rows=str(TOTAL_ROWS))


app.add_url_rule("/", view_func=UploadFile.as_view("upload_file"))
app.add_url_rule("/sending_emails", view_func=SendingEmails.as_view("sending_emails"))

app.run()
