from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Sector, Server
from .forms import MyForm

# Create your views here.


def index(request):
    form = MyForm()
    # data = Sector.objects.all()
    return render(request, 'index.html', {'form': form} )


def start(request, sector_id):
    servers = Server.objects.filter(sector=sector_id)
    server_list = []
    for server in servers:
        server_list.append({'id': server.id, 'name': server.name})
    return JsonResponse(server_list, safe=False)


def message(request):
    return HttpResponse('sdafsdfs')