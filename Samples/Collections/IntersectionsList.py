# https://stackoverflow.com/a/2541823/8941680

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = set([2, 4, 6])
a = s1 & s2 & s3        # a type = set
print(a)


sets = [s1, s2, s3]     # list of SETs
b = set.intersection(*sets)
print(b)
