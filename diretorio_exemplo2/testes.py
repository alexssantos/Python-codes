import os, os.path, subprocess, psutil, time
from datetime import datetime

while True:        
    pid = int(input('Digite o n° PID:'))
    try:
        p = psutil.Process(pid)
        print(p)
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
print(p.threads())
p.suspend() # Suspender processo
p.resume() # Voltar de uma suspensão
p.terminate() # terminar processo
p.wait(timeout=3) # esperar 3s