from datetime import date

d_start=date(1900,1,1)

N,w = map(int,raw_input().split())

if(N>400 or N<1 or w>6 or w<0):
    count=-1
else:
    count=0
    for i in range(N):
        for j in range(12):
            d_now=date(d_start.year+i,j+1,13)
            if(d_now.isoweekday()%7==w):
                count=count+1

print count
