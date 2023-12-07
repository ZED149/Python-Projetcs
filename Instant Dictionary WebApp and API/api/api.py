


# this file contains the api class which serves as the api handler for our program

# importing libraries
import justpy as jp

import definition
from webapp import page
from webapp import dictionarypage
import json


class ApiHandler(page.Page):
    """
    This class handles the api requests for our website
    """

    # path
    path = '/api'

    # serve()
    @classmethod
    def serve(cls, req):
        """
        This function handles get request for our api page.
        :param req:
        :return:
        """
        # webpage
        webpage = jp.WebPage()

        word = req.query_params.get('w')
        # finding definition
        _definition = definition.Definition(word).get()
        response = {
            'word': word,
            'definition': _definition
        }
        webpage.html = json.dumps(response)
        return webpage


