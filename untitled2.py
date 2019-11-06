# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 01:44:23 2019

@author: zhy94
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:13:05 2019

@author: zhy94
"""
import numpy as np
def getexpvp():
    f = open("E:\\research\\mechine learning\\vtime.txt","r")
    fr=f.read()
    fr=fr.strip(' ')
    fr=fr.split(" ")
    for i in range(len(fr)):
        fr[i]=float(fr[i])
    lt=fr
    f.close()
    f = open("E:\\research\\mechine learning\\vb.txt","r")
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
        
    expvpl=[]
    expvph=[]
    for i in range(len(lz)):
        tem=np.array([lz[i],lx[i]])
        tem=tem.transpose(1,0)
        tem=tem[np.lexsort([tem[:,1],tem[:,0]])]
        pos=-1
        expvpl.append([])
        expvph.append([])
        for j in range(len(tem)):
            if tem[j,0]!=pos:
                pos=tem[j,0]
                expvpl[i].append(tem[j,1])
                expvph[i].append(tem[j,1])
            else:
                if tem[j,1]>expvph[i][-1]:
                    expvph[i][-1]=tem[j,1]
                if tem[j,1]<expvpl[i][-1]:
                    expvpl[i][-1]=tem[j,1]
            
    f.close()
    return [lt,lz,expvph,expvpl]

if __name__ == "__main__":
    [lt,lz,expvph,expvpl]=getexpvp()
    ip=270
    vpplt=plt.plot(np.unique(lz[ip]),expvph[ip],np.unique(lz[ip]),expvpl[ip])
    vpplt=plt.ylim([-0.02,0.02])
    vpplt=plt.xlim([0,0.2])
    vpplt=plt.show()
    
    #plt.plot(lz[ip],lx[ip])
   # plt.ylim([-0.02,0.02])
   # plt.xlim([0,0.2])


