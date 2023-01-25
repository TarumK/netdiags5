from django.test import TestCase
import mymodule2
# Create your tests here.
host_list = input('Введите ip-адреса хостов для проверки: ').split(' ')

# print('░' * 100)
# host2 = input('Введите ip хоста 2 для проверки: ')
# host3 = input('Введите ip хоста 3 для проверки: ')
for host in host_list:
    mymodule2.hostping(host)
# mymodule.hostping(host2)
# mymodule.hostping(host3)