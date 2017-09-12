weather = {}  # Creat a dict to save info about weather
history = {}  # Creat a dict to save query history

with open('weather_info.txt') as f:
    for line in f:
        # Define element before 's' as key and element after 's' as value
        key, value = line.split(',') 
        # weather = {key: value}
        weather[key] = value  

def get_help():
    print('''
    输入城市名，查询该城市的天气数据；
    输入help或者h，获得帮助信息；
    输入history，显示查询历史；
    输入exit, 退出程序。
    ''')

def get_history():
    for key, value in history.items():
        print('{}: {}'.format(key, value))

def get_weather_info():
    try:
        print('{}的天气为: {}'.format(city, weather[city]))
        # Save query history into dict_history
        history[city] = weather[city]  
    except:
        print('找不到指令或城市名，请重新输入。')
        get_help()

while True:
    city = input('请输入指令或您要查询的城市名：')
    if city in ['help', 'h']:
        get_help()
    elif city == 'history':
        get_history()
    elif city == 'exit':
        get_history()
        exit(0)
    else:
        get_weather_info()
