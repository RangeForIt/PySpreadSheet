from time import sleep


a = open('common/logs.log', 'a')

while True:
    sleep(0.000015)
    a.write('aaa')
    print('test')