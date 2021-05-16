#EXERCISE_3

import pickle as p

def secondletter(a):
    return a[1]

def sorter(x):
    spx=[]
    for i in x.split():
        if i[-1]=="." or i[-1]=="?" or i[-1]=="!" or i[-1]==",":
            i=i.replace(i[-1],"")
        if len(i)>=2:
            spx.append(i)

    if x!="previous":
        #spx=y.split()
        spx.sort(key = secondletter)
        p.dump(x,open("exercise3_stored_data","wb"))
        return spx

    try:
        if x=="previous":
            spx2=p.load(open("exercise3_stored_data","rb"))
            return spx2

    except:
        #spx=y.split()
        spx.sort(key = secondletter)
        p.dump(x,open("exercise3_stored_data","wb"))


def counter(x):
    if x!="previous":
        spx=x.split()
        totalwords=len(spx)
        spx2=x.split(". ")
        spx3=x.split("? ")
        spx4=x.split("! ")
        totalsen=len(spx2)+len(spx3)+len(spx4)-2
        return totalwords,totalsen
    else:
        pass

def finder1(x):
    e=[]
    f=[]
    if x=="previous":
        pass

    elif x!="previous":
        for y in x.split():
            if y[-1]=="." or y[-1]=="?" or y[-1]=="!" or y[-1]==",":
                y=y.replace(y[-1],"")
                e.append(y)
            else:
                e.append(y)

        for d in e:
            if len(d)<5:
                f.append(d)

        return f

def finder2(x):
    aiueo=["a","i","u","e","o",".","?","!","A","I","U","E","O"]
    k=x
    l=[]
    m=[]
    n=[]
    c=[]
    if x=="previous":
        pass

    elif x!="previous":
        for y in x.split():
            if y[-1]=="." or y[-1]=="?" or y[-1]=="!" or y[-1]==",":
                y=y.replace(y[-1],"")
                l.append(y)
            else:
                l.append(y)    
        #for r in x.split():
            #if r=="a" or r=="i" or r=="u" or r=="e" or r=="o":
                #l.append(r)
        
        for g in l:
            p=g
            for letter in g:
                if letter in aiueo:
                    p=p.replace(letter,"")
            n.append(p)
                

        z=0
        for u in n:
            if len(u)<5:
                c.append(x.split()[z])
                z=z+1
            elif len(u)>=5:
                z=z+1
        for o in c:
            if o[-1]=="." or o[-1]=="?" or o[-1]=="!" or o[-1]==",":
                o=o.replace(o[-1],"")
                m.append(o)
            else:
                m.append(o)
        
        return m