

# this is the main() of our program

from webapp.homepage import HomePage
from webapp.aboutpage import AboutPage
from webapp.dictionarypage import Dictionary
from api.api import ApiHandler
import justpy as jp
import inspect
from webapp import page

imports = list(globals().values())

for key in imports:
    if inspect.isclass(key):
        if issubclass(key, page.Page) and key is not page.Page:
            jp.Route(key.path, key.serve)


# jp.Route(HomePage.path, HomePage.serve)
# jp.Route(AboutPage.path, AboutPage.serve)
# jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy()
