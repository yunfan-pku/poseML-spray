 # -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:13:05 2019

@author: zhy94
"""
import numpy as np
def getexplp():
    f = open("E:\\research\\mechine learning\\ltime.txt","r")
    fr=f.read()
    fr=fr.strip(' ')
    fr=fr.split(" ")
    for i in range(len(fr)):
        fr[i]=float(fr[i])
    lt=fr
    f.close()
    f = open("E:\\research\\mechine learning\\lb.txt","r")
    fr=f.read()
    fr=fr.strip('\n')
    fr=fr.split("\n")
    for i in range(len(fr)):
        fr[i]=fr[i].strip(' ')
        fr[i]=fr[i].split(" ")
        for j in range(len(fr[i])):
            fr[i][j]=float(fr[i][j])
    lx=[]
    lz=[]
    for i in range(len(fr)):
        if i%2==0:
            lx.append(fr[i])
        else:
            lz.append(fr[i])
    explpl=[]
    explph=[]
    for i in range(len(lt)):
        tem=np.array([lz[i],lx[i]])
        tem=tem.transpose(1,0)
        tem=tem[np.lexsort([tem[:,1],tem[:,0]])]
        pos=-1
        explpl.append([])
        explph.append([])
        for j in range(len(tem)):
            if tem[j,0]!=pos:
                pos=tem[j,0]
                explpl[i].append(tem[j,1])
                explph[i].append(tem[j,1])
            else:
                if tem[j,1]>explph[i][-1]:
                    explph[i][-1]=tem[j,1]
                if tem[j,1]<explpl[i][-1]:
                    explpl[i][-1]=tem[j,1]
    f.close()
    return [lt,lz,explph,explpl]
if __name__ == "__main__":
    [lt,lz,explph,explpl]=getexplp()
    ip=50
    vpplt=plt.plot(np.unique(lz[ip]),explph[ip],np.unique(lz[ip]),explpl[ip])
    vpplt=plt.ylim([-0.002,0.002])
    vpplt=plt.xlim([0,0.02])
    vpplt=plt.show()
    
    #plt.plot(lz[30],lx[30])
    #plt.ylim([-0.002,0.002])
    #plt.xlim([0,0.02])


