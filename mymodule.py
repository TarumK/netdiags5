import time
from ping3 import ping, verbose_ping

ping_count = 100
def hostping(host_ip):
    average = 0.00000
    ip = f'{host_ip}'
    time_response = 0.000000
    # global ping_count
    ping_count = 100         #Количество отправляемых пакетов
    lost_count = 0          #Количество потерянных пакетов
    size_package = 128       #Размер отправляемых пакетов в байтах
    for count in range(1, ping_count + 1):
        time_response = ping(ip, size=size_package, unit='s')
        if time_response is not False:
            # print(f'{count}: Ответ от {ip}: время = {"%.6f" % (time_response)}')
            average = average + time_response
            print('█' , end='')
            time.sleep(0.05)
        else:
            print(f'Хост {ip} не отвечает')
            lost_count += 1
    # print('**************************************')
    print(' ► Хост:', host_ip)
    print(f'Среднее время отклика для {ip} = {"%.6f" % (average/ping_count)}')
    print(f'Отправлено пакетов: {ping_count}')
    print(f'Потеряно пакетов: {lost_count}')
    print(f'Процент потерь пакетов: {int(lost_count/ping_count*100)}%')

    return ping_count