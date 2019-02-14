import os
import os.path
from datetime import datetime
import subprocess
import psutil

pid = input('Digite o n° PID:')
try:
    p = psutil.Process(pid)
except Exception:
    print('PID não existe!')
