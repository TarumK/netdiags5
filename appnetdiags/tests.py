from django.test import TestCase
import mymodule
# Create your tests here.
host_list = input('Введите адреса хостов для проверки: ').split(' ')

# print('░' * 100)
# host2 = input('Введите ip хоста 2 для проверки: ')
# host3 = input('Введите ip хоста 3 для проверки: ')
for host in host_list:
    mymodule.hostping(host)
# mymodule.hostping(host2)
# mymodule.hostping(host3)
