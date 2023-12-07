


# this file contains the navigation menu class for the all webpages of website

import justpy as jp


class NavBar:
    """
    This class creates a Quasar Drawer.
    """

    # serve()
    @classmethod
    def serve(cls, web_page):
        """
        This function creates a navbar on the webpage.
        :return:
        """
        # adding drawer
        layout = jp.QLayout(a=web_page, view='hHh lpR fFf')
        header = jp.QHeader(a=layout, elevated=True)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model='left', bordered=True)
        # adding menu items
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-600'
        jp.A(a=qlist, text='Home', href='/', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Title')
        container = jp.QPageContainer(a=layout)
        return container

    # move_drawer
    @staticmethod
    def move_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value
