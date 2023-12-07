


# this file contains the dictionary page class

# importing libraries
import justpy as jp
from definition import Definition
from webapp.navbar import NavBar
from webapp import page


class Dictionary(page.Page):
    """
    This class doesn't instantiate any object instead it serves the function call for serve()
    and stores dictionary_page url.
    """

    # path
    path = '/dictionary'

    # serve
    @classmethod
    def serve(cls, req):
        """
        This function creates a webpage using Tailwind Css and Quasar.
        :return:
        """

        # webpage
        webpage = jp.QuasarPage(tailwind=True)
        # adding navigation menu
        container = NavBar.serve(webpage)

        # main_div
        main_div = jp.Div(a=container, classes='h-screen p-4 bg-gray-300')

        # title
        jp.H1(a=main_div, text='Dictionary Page', classes='text-4xl font-sans m-2')
        # description
        jp.Div(a=main_div, text='''
        This is the dictionary page. User can type in a word and its definition will be shown below.
        ''', classes='bg-blue-200 text-lg font-serif m-2')


        # definition
        definition = jp.Div(a=main_div, classes='m-2 p-2 text-lg h-40 border-2 text-black')
        # input
        word = jp.Input(a=main_div, placeholder='Enter Word',
                        classes='input-form focus:bg-darkgray-400 focus:text-black '
                                'focus:outline-none rounded m-2 border-2 border-gray-200'
                                ' w-64 focus:border-purple-500 py-4 px-2',
                        defi=definition)
        # firing event
        word.on('input', cls.get_definition)

        # return
        return webpage

    # click
    @staticmethod
    def get_definition(widget, msg):
        d = Definition(widget.value)
        widget.defi.text = "".join(d.get())
