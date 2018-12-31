import psutil


def GetFreq():
    return psutil.cpu_freq()


def cores():
    return psutil.cpu_count()


print('cores: ', cores())
print('freq: ', GetFreq())