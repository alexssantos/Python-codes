import psutil

# total de uso no HD


def get_user():
    disk_user = psutil.disk_usage('/').used
    return disk_user
# total de memoria no HD


def get_total():
    disk_total = psutil.disk_usage('/').total
    return disk_total
# total livre no HD


def get_free():
    disk_free = psutil.disk_usage('/').free
    return disk_free
# valor do HD em porcentagem


def get_porcent():
    disk_porcent = psutil.disk_usage('/').percent
    return disk_porcent
# Partição do HD


def get_part():
    disk_part = psutil.disk_partitions(all=False)
    return disk_part
# estatus do HD


def get_estat():
    disk_estat = psutil.disk_io_counters(perdisk=False, nowrap=True)
    return disk_estat
# leitura do HD em bytes


def get_read():
    disk_read = psutil.disk_io_counters().read_bytes
    return disk_read
# escrita do HD em bytes


def get_write():
    disk_write = psutil.disk_io_counters().write_bytes
    return disk_write
