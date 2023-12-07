
# importing libraries
import requests

# this file contains the news_feed class


class NewsFeed:
    """
    This class contains the data on which news need to be constructed.
    """

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "bc522e4ccbcf440090f7fea7725e156d"

    # constructor
    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    # get()
    def get(self):
        """
        This function creates an email_body string and returns it.
        :return:
        """
        # creating url string
        url = (f"{self.base_url}"
               f"qInTitle={self.interest}&"
               f"from={self.from_date}&"
               f"to={self.to_date}&"
               f"language={self.language}&"
               f"apiKey={self.api_key}")
        # making a request to the server
        response = requests.get(url)
        # storing data in JSON format
        json_form = response.json()
        # extracting the list of dictionaries that contains all news
        list_of_news = json_form['articles']
        # creating email_body string
        email_body = ""
        for i in list_of_news:
            email_body = email_body + i['title'] + '\n' + i['url'] + '\n\n'

        # returning email_body
        return email_body

