# import ping3
from ping3 import ping, verbose_ping
list_host = [1, 47, 180]
# for i in range(23,26):
for id, i in enumerate(list_host):
    average = 0
    ip = f'192.168.32.{i}'
    time_response = ping(ip)
    ping_count = 100
    lost_count = 0
    for count in range(1, ping_count+1):
        # print(f'{count}: Ответ от {ip}: время={time_response}')
        if time_response != None:
            if time_response < 0.001:
                print(f'{count}: Ответ от {ip}: время отклика < 1 мс')
            else:
                print(f'{count}: Ответ от {ip}: время={float(time_response)}')
            average += ping(ip)
        else:
            print(f'Хост {ip} не отвечает')
            lost_count += 1
            average = 0

    print(f'Среднее время отклика для {ip} = {float(average/ping_count)}')
    print(f'Отправлено пакетов: {ping_count}')
    print(f'Потеряно пакетов: {lost_count}')
    print(f'Процент потерь пакетов: {int(lost_count/ping_count*100)}%')
    print('**************************************')
# print(verbose_ping('base1.sao.ru'))