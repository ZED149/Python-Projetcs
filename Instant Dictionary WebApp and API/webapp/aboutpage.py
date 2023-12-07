

# this file contains the aboutpage class

# importing libraries
import justpy as jp
from webapp.navbar import NavBar
from webapp import page


class AboutPage(page.Page):
    """
    This class doesn't instantiate an object instead it calls serve() method.
    """

    # path
    path = '/about'

    # serve
    @classmethod
    def serve(cls, req):
        """
        This function creates an About Web Page using Tailwind and Quasar.
        :return:
        """

        # webpage
        webpage = jp.QuasarPage(tailwind=True)
        # adding navigation menu
        container = NavBar.serve(webpage)

        # main_div
        main_div = jp.Div(a=container, classes='bg-gray-400 h-screen p-2')

        # title
        jp.H1(a=main_div, text='This is the About Page', classes='font-serif text-xlg mb-4')
        # description
        jp.Div(a=main_div, text='''
        You can contact me at, 
        Name: Salman Ahmad
        Email: salmanahmad111499@gmail.com
        Github: https://www.github.com/zed149
        ''', classes='font-serif text-lg bg-gray-300')
        jp.Hr(a=main_div)
        # now printing some information about api
        jp.Div(a=main_div, text='Request = https://www.localhost.com/api?w=word', classes='text-lg px-4 py-2 m-2')
        jp.Hr(a=main_div)
        jp.Div(a=main_div, text='Reponse would be,', classes='text-lg px-4 py-2 m-2')
        jp.Div(a=main_div, text="""
        {
            'word':word,
            'definition':_definition
        }
        """, classes='text-lg px-4 py-2 m-2')
        jp.Hr(a=main_div)
        jp.H2(a=main_div, text='For Example:', classes='text-lg bg-gray-200 p-4')
        jp.Hr(a=main_div, classes='color-darkgray-600')
        jp.Div(a=main_div, text='https://www.localhost.com/api?w=moon', classes='text-lg bg-gray-200 p-4')
        jp.Div(a=main_div, text='''
        {"word": "moon", "definition": ["A natural satellite of a planet.", 
        "A month, particularly a lunar month (approximately 28 days).", 
        "To fuss over adoringly or with great affection.", 
        "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", 
        "To be lost in phantasies or be carried away by some internal vision, 
        having temorarily lost (part of) contact to reality."]}
        ''', classes='text-lg bg-gray-200 p-4')

        # return
        return webpage


