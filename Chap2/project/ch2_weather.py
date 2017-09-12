import requests

history = []

def get_weather_info():
    try:
        payload = {'city':user_input, 'key':'fd2f5105e6eb4ec5bae6cefed8ee6cdd'}
        r = requests.get('https://free-api.heweather.com/v5/now', params=payload)
        result = r.json()
        weather = (
            user_input +
            '天气' + result['HeWeather5'][0]['now']['cond']['txt'] + '，' +
	        '温度' + result['HeWeather5'][0]['now']['tmp'] + '摄氏度，' +
	        result['HeWeather5'][0]['now']['wind']['dir'] +
	        result['HeWeather5'][0]['now']['wind']['sc'] + '级，' +
	        '更新时间当地时间' + result['HeWeather5'][0]['basic']['update']['loc'] + '。'
            )
        print(weather)
        history.append(weather) 
    except KeyError:
        print('找不到指令或城市名，请重新输入。')
        get_help()
    except requests.exceptions.RequestException:
	print('请求异常，请重新输入。')


def get_help():
    print('''
    输入城市名，查询该城市的天气数据；
    输入help或者h，获得帮助信息；
    输入history，显示查询历史；
    输入exit, 退出程序。
    ''')

def get_history():
    for i in history:
        print(i)


while True:
    user_input = input('请输入指令或您要查询的城市名：')
    if user_input in ['help', 'h']:
        get_help()
    elif user_input == 'history':
        get_history()
    elif user_input == 'exit':
        get_history()
        exit(0)
    else:
        get_weather_info()
