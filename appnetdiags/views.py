from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Sector, Server, Log
from .forms import MyForm
from ping3 import ping, verbose_ping
# Create your views here.


def index(request):
    # host_list = []
    if request.method == "POST":
# Если нажата кнопка "Отправить", то из POST-потока формы получаем количество отправляемых пакетов
# и размер пакета
        package_count = int(request.POST.get('packet_count'))
        # server_name = request.POST.get('server_name')
        # # host_list = t_s
# Поочередно, в цикле выбираем хосты из глобального списка серверов t_s,
# закрепленных за подразделением и стравливаем (передаем) ее на вход
# в качестве аргумента функции hostping()
        for host in t_s:
            # print(host)
            # assert host != 'Null', 'errrrrrrrrror'
            list_vozrata = hostping(host, package_count)
# Возвращаем из функции hostping количество вернувшихся пакетов, среднее время отклика и т.д.
            package_send = list_vozrata[0]
            average1 = list_vozrata[1]
            package_lost = list_vozrata[2]
            package_percent = package_lost*100/package_count
            current_host = host

# Создаем экземпляр класса модели Log, где накапливаются данные по доступности хостов
# записываем в таблицу логов данные
            log = Log()
            log.log_host = host
            log.log_ping_count = package_send
            log.log_ping_receive = package_send - package_lost
            log.log_ping_lost = package_lost
            log.log_percent_lost = package_percent
            log.log_average = average1
            log.save()
# Создаем экземпляр формы, связанной с моделю Log для передачи его в шаблон index.html
# в качестве параметра функции прорисовки render()
        form = MyForm(request.POST)

    else:
# Это часть отрабатывает, если мы просто запустили хомячок-домашнюю страницу и ничего не передали
# Проше говоря, не нажали на кнопку submit "Запустить тест"
        package_send = 0
        package_lost = 0
        package_percent = 0
        average1 = 0
        current_host = []
        form = MyForm()
# Выбираем все записи логов, пользуяст ORM-кой, а не чистым SQL. Типа, это SELECT * FROM Log
    allrec = Log.objects.all()
# Отрисовываем шаблон с данными, полученными с функциональных представлений вьюхи
    return render(request, "index.html", {"allrec": allrec, "form": form,
                                          "average1": average1, "ping_count1": package_send,
                                          "package_lost": package_lost, "host": current_host,
                                          "package_percent": package_percent})


def start(request, sector_id):
    global t_s
    servers = Server.objects.filter(sector=sector_id)
    # clean_list = []
    # for s in servers:
    #     clean_list.append(s)
    #     s = "".join(str(clean_list).split('<Server: '))
    #     true_list = "".join(str(s).split('>'))
    # print(type(true_list))
    server_list = []
    t_s = []
    for server in servers:
        server_list.append({'id': server.id, 'name': server.name})
        t_s.append(server.name)
    # print('spisok serverov', t_s)
    # (type(t_s))
    return JsonResponse(server_list, safe=False)

def hostping(host, packet_count):
    average = 0
    time_response = 0
    ping_count = packet_count         #Количество отправляемых пакетов
    lost_count = 0          #Количество потерянных пакетов
    size_package = 128       #Размер отправляемых пакетов в байтах
    for count in range(1, ping_count + 1):
        time_response = ping(host, size=size_package, unit='s')
        if time_response is not False:
            average = average + time_response
        else:
            lost_count += 1
    sr = average/ping_count
    return [ping_count, sr, lost_count]
