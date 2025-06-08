from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "df935c4f2a261477f519504d4dbea080"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data['name'],
                "temp": data['main']['temp'],
                "description": data['weather'][0]['description'].title(),
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "condition": get_weather_condition(data['weather'][0]['main'])
            }
        else:
            error = "City not found. Please enter a valid city name."
    return render_template("index.html", weather=weather, error=error)

def get_weather_condition(condition):
    if condition in ['Rain', 'Drizzle']:
        return 'rain'
    elif condition == 'Clear':
        return 'sunny'
    elif condition in ['Clouds', 'Overcast']:
        return 'cloudy'
    # Add more conditions as needed
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
