from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Sector, Server
from .forms import MyForm
from ping3 import ping, verbose_ping
import time
# from .mymodule import hostping

# Create your views here.


def index(request):

    if request.method=="POST":
        list_vozrata = hostping('127.0.0.1')
        ping_count1 = list_vozrata[0]
        lost_count1 = list_vozrata[1]
        form = MyForm(request.POST)
        data = {"ping_count1": ping_count1, "lost_count1": lost_count1}
        # return render(request, "index.html", context=data)
        # data = {"ping_count1": ping_count1, "lost_count1": lost_count1}
    else:
        ping_count1 = 0
        lost_count1 = 0
        form = MyForm()

    # data = {"ping_count1": ping_count1, "lost_count1": lost_count1}
    return render(request, "index.html", {"form": form, "ping_count1": ping_count1, "lost_count1": lost_count1})


def start(request, sector_id):
    servers = Server.objects.filter(sector=sector_id)
    server_list = []
    for server in servers:
        server_list.append({'id': server.id, 'name': server.name})
    return JsonResponse(server_list, safe=False)


def message(request, ping100):
    hostping('192.168.11.76')
    # count_ping = ping_count
    # mess = '111'
    ping100 = 999
    return render(request,"index.html", {'ping100': ping100})
        #HttpResponse('sdafsdfs')

def hostping(host_ip):
    average = 0.00000
    ip = f'{host_ip}'
    time_response = 0.000000
    # global ping_count
    ping_count = 10         #Количество отправляемых пакетов
    lost_count = 0          #Количество потерянных пакетов
    size_package = 128       #Размер отправляемых пакетов в байтах
    for count in range(1, ping_count + 1):
        time_response = ping(ip, size=size_package, unit='s')
        if time_response is not False:
            # print(f'{count}: Ответ от {ip}: время = {"%.6f" % (time_response)}')
            average = average + time_response
            # print('█' , end='')
            # time.sleep(0.05)
        else:
            # print(f'Хост {ip} не отвечает')
            lost_count += 1
    # print('**************************************')
    # print(' ► Хост:', host_ip)
    # print(f'Среднее время отклика для {ip} = {"%.6f" % (average/ping_count)}')
    # print(f'Отправлено пакетов: {ping_count}')
    # print(f'Потеряно пакетов: {lost_count}')
    # print(f'Процент потерь пакетов: {int(lost_count/ping_count*100)}%')
    sr = average/ping_count
    return [ping_count, sr]
