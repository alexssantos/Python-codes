import os, os.path, subprocess, psutil, time
from datetime import datetime



#get Sistem Partiction path
#print disk_usage
sysDrivePath = psutil.Process().environ()['SYSTEMDRIVE']
driveUseGb = ("{:2.2f}").format(psutil.disk_usage(sysDrivePath).used / 1024**3)
print(f'Disco do Sistema - Usado: {driveUseGb} Gb')











memUsedGb = psutil.virtual_memory().used / 1024**3
swapUsedGb = psutil.swap_memory().used / 1024**3
print(f'Memória em uso: {"{:2.2f}".format(memUsedGb)} Gb')
print(f'Memória Swap em uso: {"{:2.2f}".format(swapUsedGb)} Gb')



count = 1
while True:
    p = psutil.cpu_percent(interval=1)
    now = datetime.now()
    _time = f'{now.hour}:{now.minute}:{now.second}'
    print(f'CPU: {p}% -- lap {count} -- time: {_time}')
    count += 1
    if count > 20:
        break

    # count = 1
    # if count > 15:
    #     break
    # #print(p.cpu_percent().user, " lap:", count)
    #ime.sleep(1)
    #count += 1

    
count = 1
while True:
    p = psutil.Process()    
    if count > 15:
        break
    print(p.cpu_times().user, " lap:", count)
    count += 1
    time.sleep(1)


while True:        
    pid = int(input('Digite o n° PID:'))
    try:
        p = psutil.Process(pid)
        print(p.username())
        print(time.ctime(p.create_time()))
        print(p.memory_info().rss / 1024, ' Kb')
        print((p.memory_info().rss / (1024*1024)), ' Mb')
        break
    except Exception:
        print('PID não existe!')

print(p.name())
print(p.exe())
print(p.cwd())
print(p.status())
print(p.username())
print(p.create_time())
print(time.ctime(p.create_time()))
print(p.cpu_times())
print(p.cpu_percent(interval=1.0))
print(p.cpu_affinity())
print(p.memory_percent())
print(p.memory_info())
print(p.num_threads())
threadList = p.threads()


for thread in threadList:
    print(thread)


# p.suspend() # Suspender processo
# p.resume() # Voltar de uma suspensão
# p.terminate() # terminar processo
# p.wait(timeout=3) # esperar 3s