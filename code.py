import requests, folium, time
from tqdm import tqdm


def info_ip(ip='100.0.0.1'):

    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {

            '[IP]': response.get('query'),
            '[Интернет провайдер - Internet Provaider]': response.get('isp'),
            '[Страна - Country]': response.get('country'),
            '[Город - City]': response.get('city'),
            '[Имя региона - Region Name]': response.get('regionName'),
            '[Организация - Org]': response.get('org'),
            '[Почтовый индекс - ZIP]': response.get('zip'),
            '[Широта - Lat]': response.get('lat'),
            '[Долгота - Lon]': response.get('lon'),

        }

        for i in tqdm(range(int(100)), ncols=95):
            print(i, end='')
            time.sleep(0.04)

        for k, v in data.items():
            print(f'{k} : {v}')
            time.sleep(1)

        location = folium.Map(location=[response.get('lat'), response.get('lon')])
        location.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError and ValueError:
        print()
        print('[!!!] You have entered an incorrect IP address. Check your connection (Вы ввели некорректный IP-адрес. Проверьте ваше соединение)')


def main():

    ip = input('Enter the IP-address (Введите IP-адресс): ')

    info_ip(ip)


if __name__ == '__main__':
    main()
