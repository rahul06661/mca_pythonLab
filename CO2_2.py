"Generate Fibonacci series of N terms"

n_terms=int(input("Enter no.of terms"))
a=0
b=1
c=0
print(0)
print(1)

for i in range(1, n_terms-1):
    c = a + b
    a = b
    b = c
    print(b)