import re   # Regex Lib

from subprocess import Popen, PIPE, check_output

def get_processes_running():
    
    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
        if m is not None:
            p.append({  "image":m.group(1).decode(),
                        "pid":int(m.group(2).decode()),
                        "session_name":m.group(3).decode(),
                        "session_num":int(m.group(4).decode()),
                        "mem_usage":int(m.group(5).decode('ascii', 'ignore'))
                        })
    return( p)

def test():
    print(*[line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()])


if __name__ == '__main__':
    test()
