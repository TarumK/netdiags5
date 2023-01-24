from django.test import TestCase
import mymodule
# Create your tests here.
host = input('Введите ip хоста для проверки: ')
mymodule.hostping(host)
