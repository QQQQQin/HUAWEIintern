from numpy import *
import operator

class myfloat:
    def __init__(self, f):
        self.f = f

    def __repr__(self):
        return '{:.5f}'.format(self.f)


N = input()

ans = {}
ans[0] = 1
for n in range(N):
    new={}
    for i in range(1, 7):
        for key, value in ans.items():
            if(key+i > 7*N/2):
                break
            else:
                new[key+i] = new.get(key+i, 0) + value

    ans=new

##print ans
##aa={7*N-key:value for key, value in ans.items()}
##print aa

ans.update({7*N-key:value for key, value in ans.items()})
ans = sorted(ans.iteritems(), key=operator.itemgetter(0))

sum = float(6**N)

anslist = [[key, myfloat(value/sum)] for key, value in ans]

print anslist
