a = int(input("lado A: "))
b = int(input("lado B: "))
c = int(input("lado C: "))

if a == b or a == c or c == b:
    if b == c and b == a:
        print("TRINGULO EQUILATERO")
    else:
        print("TRINAGULO ISOSCELES")
else:
    print("TODOS LADOS DIFERENTES")