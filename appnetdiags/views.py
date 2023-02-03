from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Sector, Server, Log
from .forms import MyForm
from ping3 import ping, verbose_ping
# Create your views here.


def index(request):

    if request.method == "POST":
        host_list = ['127.0.0.1', 'localhost']
        form_ping_count = 100
        for host in host_list:
            list_vozrata = hostping(host)
            ping_count1 = list_vozrata[0]
            average1 = list_vozrata[1]
            current_host = host

            log = Log()
            log.log_host = host
            log.log_ping_count = ping_count1
            log.log_average = average1
            log.save()

        form = MyForm(request.POST)

    else:
        ping_count1 = 0
        average1 = 0
        current_host = []
        form = MyForm()

    # data = {"ping_count1": ping_count1, "lost_count1": lost_count1}
    allrec = Log.objects.all()
    return render(request, "index.html", {"allrec": allrec, "form": form, "ping_count1": ping_count1, "average1": average1, "host": current_host})


def start(request, sector_id):
    servers = Server.objects.filter(sector=sector_id)
    server_list = []
    for server in servers:
        server_list.append({'id': server.id, 'name': server.name})
    return JsonResponse(server_list, safe=False)


def hostping(host_ip):
    average = 0.00000
    ip = f'{host_ip}'
    time_response = 0.000000
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
