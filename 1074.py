N, x, y = map(int, input().split())

# lets try in recursion version 

print("lets get it")

#version.2


num = 0 
while N != 0:
    N -= 1
    if x < 2 **N and y < 2**N:
        num+=0
        
    elif x < 2 **N and y >= 2**N:
        num+= (2**N) * (2**N) *1
        y -=2**N
        
    elif x >= 2 **N and y < 2**N:
        num+= (2**N) * (2**N) *2
        x -=2**N
        
    elif x >= 2 **N and y >= 2**N:
        num+= (2**N) * (2**N) *3
        x -=2**N
        y -=2**N
        
print(num)
