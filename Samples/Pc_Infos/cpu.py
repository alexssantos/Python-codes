import cpuinfo
import psutil


print('----- CPUINFO ------')
info = cpuinfo.get_cpu_info()

model_cpu = info['brand']
print('model_cpu:', model_cpu)

arquitetura = info['arch']
print('arquitetura: ', arquitetura)

bits = info['bits']
print('bits:', bits)

techs = info['flags']
print('techs:', techs)  #list

family_cpu = info['family']
print('family_cpu: ', family_cpu)

freq_now = info['hz_actual']
print('freq_now: ', freq_now)

freq_max = info['hz_advertised']
print('freq_max: ', freq_max)

cache_l2 = info['l2_cache_size']
print('cache_l2: ', cache_l2)

cache_l3 = info['l3_cache_size']
print('cache_l3: ', cache_l3)

marca = info['vendor_id']
print('marca: ', marca)




print('----- PSUTIL ------')
p = psutil
print(p)