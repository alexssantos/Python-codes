import psutil


def get_free():
    free = psutil.virtual_memory().free
    return free


def get_total():
    total = psutil.virtual_memory().total
    return total


def get_percent():
    percent = psutil.virtual_memory().percent
    return percent


def get_used():
    used = psutil.virtual_memory().used
    return used


def get_active():
    active = psutil.virtual_memory().active
    return active


def get_swap_total():
    swap_total = psutil.swap_memory().total
    return swap_total


def get_swap_used():
    swap_used = psutil.swap_memory().used
    return swap_used


print(psutil.swap_memory().free)
