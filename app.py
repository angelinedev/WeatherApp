from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_secret_api_key"
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
            }
        else:
            error = "City not found. Please enter a valid city name."
    return render_template("index.html", weather=weather, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
