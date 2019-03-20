import psutil, time

print ( psutil.pids())  # todos os processos ativos

cmdList = p.cwd()   # 
pid = 543
cmdLIst = psutil.pid_exists(pid)  # indica se existe

print( psutil.process_iter())   # PID's - permite iterar com 'for' e etc.