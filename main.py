# import ping3
import ping3
import time
from ping3 import ping, verbose_ping

list_host = [47, 48]        #Список хостов(ip-адресов) для проверки
# for i in range(23,26):
for id, i in enumerate(list_host):
    average = 0.00000
    ip = f'192.168.32.1' \
         # f'{i}'
    time_response = 0.00000
    # time_response = ping(ip, size=128, unit='ms')
    # time_response = ping(ip, unit='s')
    ping_count = 100         #Количество отправляемых пакетов
    lost_count = 0          #Количество потерянных пакетов
    for count in range(1, ping_count+1):
        time_response = ping(ip, size=128, unit='s')
        if time_response is not False:
            print(f'{count}: Ответ от {ip}: время = {"%.5f" % (time_response)}')
            average = average + time_response
            # print('1', average)
            # time_response = 0.0
            time.sleep(0.5)
        else:
            # print(time_response)
            print(f'Хост {ip} не отвечает')
            lost_count += 1
            # average = 0
    # print(f'Суммарное время для {ip} = {"%.5f" % (average)}')
    print(f'Среднее время отклика для {ip} = {"%.5f" % (average/ping_count)}')
    print(f'Отправлено пакетов: {ping_count}')
    print(f'Потеряно пакетов: {lost_count}')
    print(f'Процент потерь пакетов: {int(lost_count/ping_count*100)}%')
    print('**************************************')
# print(verbose_ping('base1.sao.ru'))