
# this file contains the homepage class for our program

# importing libraries
import justpy as jp
from webapp.navbar import NavBar
from webapp import page


class HomePage(page.Page):
    """
    This class doesn't instantiate any object instead it,
    executes the serve() function call for HomePage.
    """

    # PATH
    path = '/'

    # serve()
    @classmethod
    def serve(cls, req):
        """
        This function will create the HomePage Webpage using
        Tailwind CSS and Quasar Technology.
        :return:
        """

        # creating main div
        web_page = jp.QuasarPage(tailwind=True)
        container = NavBar.serve(web_page)

        # main_div
        main_div = jp.Div(a=container, classes='bg-gray-200 h-screen p-4 grid grid-cols-1 gap-2 text-center')

        # title
        title = jp.H1(a=main_div, text='ZED Instant Dictionary WebApp', classes='text-xlg font-serif')
        # description
        description = jp.P(a=main_div, text='''
        This program lets the user to type in a word and search it definitions as the user is typing.
        ''', classes='text-lg font-serif')

        # Return
        return web_page


