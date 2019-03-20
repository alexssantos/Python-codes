import multiprocessing

def funcProcess(i):
    print("Olá mundo! Da thread:", i)

if __name__ == "__main__":

    p0 = multiprocessing.Process(target=funcProcess, args=(0,))
    p0.start()  # inicia processo 0

    p1 = multiprocessing.Process(target=funcProcess, args=(1,))
    p1.start()  # inicia processo 1

    p0.join()  # espera processo 0
    p1.join()  # espera processo 1

    input('Digite qualquer tecla para sair...')
