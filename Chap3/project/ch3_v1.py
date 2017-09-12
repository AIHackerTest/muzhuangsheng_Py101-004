from flask import Flask, request, render_template
import requests

def get_weather_info(city):
    payload = {'city':city, 'key':'fd2f5105e6eb4ec5bae6cefed8ee6cdd'}
    r = requests.get('https://free-api.heweather.com/v5/now', params=payload)
    result = r.json()
    weather = (
        city +
        '天气' + result['HeWeather5'][0]['now']['cond']['txt'] + '，' +
	    '温度' + result['HeWeather5'][0]['now']['tmp'] + '摄氏度，' +
	    result['HeWeather5'][0]['now']['wind']['dir'] +
	    result['HeWeather5'][0]['now']['wind']['sc'] + '级，' +
	    '更新时间当地时间' + result['HeWeather5'][0]['basic']['update']['loc'] + '。'
        )
    return weather

app = Flask(__name__)
history = []

@app.route('/', methods=['GET', 'POST'])
def base_page():
    return render_template('base.html')

@app.route('/search', methods=['GET', 'POST'])
def search_page():
    while True:
        if request.args.get('help') == '帮助':
            return render_template('help.html')
        elif request.args.get('history') == '历史':
            return render_template('history.html', history=history)
        elif request.args.get('search') == '查询':
            city = request.args.get('city')
            try:
                weather = get_weather_info(city)
                history.append(weather)
                return render_template('search.html', weather=weather)
            except KeyError:
                return render_template('help.html', message='请重新输入城市名')


if __name__ == '__main__':
    app.debug = True
    app.run()
