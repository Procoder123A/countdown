import time 
def countdown(n):
    if n==0:
        print('Blast off')
    else:
        print(n)
        print('*'*n)
        time.sleep(1)
        countdown(n-1)
n=int(input('enter your limit='))
countdown(n)


