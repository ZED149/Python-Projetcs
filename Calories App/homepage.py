

# this is the homepage that goes onto web

# importing libraries
from flask.views import MethodView
from wtforms import SubmitField, StringField, Form
from flask import Flask, render_template, request
from calories import Calories
from user import User
from weather import Weather

# creating our app instance
app = Flask(__name__)

# homepage class
class HomePage(MethodView):
    def get(self):
        home_page_form = HomePageForm()
        return render_template("index.html",
                               homepageform=home_page_form)

    def post(self):
        home_page_form = HomePageForm(request.form)
        user = User(float(home_page_form.weight.data), float(home_page_form.height.data), int(home_page_form.age.data))
        weather = Weather(home_page_form.country.data, home_page_form.city.data)
        calories = Calories()
        answer = calories.calculates(user, weather)
        temperature = weather.calculate_temperature(weather)

        return render_template("index.html",
                               homepageform=home_page_form, result=True,
                               calories=str(answer), temperature=str(temperature))


class HomePageForm(Form):
    weight = StringField("Weight(kg): ", default=99)
    height = StringField("Height(cm): ", default=169)
    age = StringField("Age(yrs): ", default=25)

    country = StringField("Country: ", default="Pakistan")
    city = StringField("City: ", default="Lahore")

    button = SubmitField("Continue")


# adding url rules
app.add_url_rule("/", view_func=HomePage.as_view("home_page"))

# running our app
app.run(debug=True)