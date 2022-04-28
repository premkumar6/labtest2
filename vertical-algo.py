from itertools import combinations

def get_data():
    return [
        ['T100',['I1','I2','I5']],
        ['T200',['I2','I4']],
        ['T300',['I2','I3']],
        ['T400',['I1','I2','I4']],
        ['T500',['I1','I3']],
        ['T600',['I2','I3']],
        ['T700',['I1','I3']],
        ['T800',['I1','I2','I3','I5']],
        ['T900',['I4','I2','I3']]
        ]

data=get_data()

items = []
for i in data:
    for q in i[1]:
        if(q not in items):
            items.append(q)

items.sort()

min_supp_perc = 0.3
min_supp = int(min_supp_perc*len(data))

print(min_supp)
c1,l1={},{}
for itm in items:
    c1[itm]=set()

for trans in data:
    for itm in trans[1]:
        c1[itm].add(trans[0])

for itm in c1:
    if(len(c1[itm])>=min_supp):
        l1[itm]=c1[itm]

print('C1')
for itm,val in c1.items():
    print(itm,":",val)

print('L1')
for itm,val in l1.items():
    print(itm,":",val)
print()

def stagek(items,minimum_support_count,k,c1):
    combi=list(combinations(items,k))

    ck,lk={},{}
    for iter1 in combi:
        curr=c1[iter1[0]]
        for itm in iter1:
            curr=curr.intersection(c1[itm])
        ck[iter1]=curr
   
    for itm in ck:
        if(len(ck[itm])>=min_supp):
            lk[itm]=ck[itm]
   
    return ck,lk

max_freq_size=len(c1)
l_last=None

min_conf_perc = 0.5
for i in range(2,max_freq_size+1):
    ci,li=stagek(items,min_supp,i,c1)
   
    print('C%d' %(i))
    for itm,val in ci.items():
        print(itm,":",val)
       
    if(not li):
        break
   
    print('L%d' %(i))
    for itm,val in li.items():
        print(itm,":",val)
       
    print()
    l_last=li

print()
print()

for l in l_last:
    for lsize in range(1,(len(l)//2)+1):
        c = list(combinations(l,lsize))
        for a in c:
            b = set(l)-set(a)
            ab = l
            sab = 0
            sa = 0
            sb = 0
            for q in data:
                temp = set(q[1])
                if(set(a).issubset(temp)):
                    sa+=1
                if(set(b).issubset(temp)):
                    sb+=1
                if(set(ab).issubset(temp)):
                    sab+=1
           
            if(sab/sa>=min_conf_perc):
                print(a," -> ",b," = ",str(sab/sa*100)+"%")
            if(sab/sb>=min_conf_perc):
                print(b," -> ",a," = "+str(sab/sb*100)+"%")
        curr = 1
    print()