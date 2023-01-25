# from ping3 import ping, verbose_ping
#
# for i in range(24,26):
#     average = 0
#     ip = f'192.168.2.{i}'
#     for count in range(3):
#         print(f'Ответ от {ip}: время={ping(ip)}')
#         if ping(ip) != None:
#             average += int(ping(ip))
#         else:
#             average = 0
#
#     print(f'Среднее время отклика для {ip} = {average/3}')
# print(verbose_ping('base1.sao.ru'))

host_list = input('Введите ip-адреса хостов для проверки: ').split(' ')
print(host_list)