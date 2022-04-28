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
        ['T900',['I1','I2','I3']]
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

def stage_k(items,records, minimum_support_count,k):
    combi=list(combinations(items,k))
    ck = {}
    lk={}
   
    for iter1 in combi:
        count = 0
        for iter2 in records:
            if set(iter1).issubset(set(iter2[1])):
                count+=1
        ck[iter1] = count
       
    for key, value in ck.items():
        if value >= minimum_support_count:
            lk[key] = value
   
    return ck, lk

max_freq_size=max([len(i[1]) for i in data])
l_last=None

min_conf_perc = 50
for i in range(1,max_freq_size+1):
    ci,li=stage_k(items,data,min_supp,i)
   
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
           
            if(sab/sa*100>=min_conf_perc):
                print(a," -> ",b," = ",str(sab/sa*100)+"%")
            if(sab/sb*100>=min_conf_perc):
                print(b," -> ",a," = "+str(sab/sb*100)+"%")
        curr = 1
    print()
    