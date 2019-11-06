# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:59:58 2019

@author: zhy94
"""

import matplotlib.pyplot as plt
import numpy as np


def get2Ddata(filename):
    f = open(filename,"r")
    A=[]
    fr=f.read()
    fr=fr.strip('\n')
    fr=fr.split("\n")
    for i in range(len(fr)):
        fr[i]=fr[i].split(",")
        for j in range(len(fr[i])):
            t=float(fr[i][j])
            if abs(t)<1e-17:
                t=0
            fr[i][j]=t
    a1=np.array(fr)
    t=np.unique(np.sort(a1[:,0]))
    x=np.unique(np.sort(a1[:,1]))
    z=np.unique(np.sort(a1[:,3]))
    nz=len(z)
    l=int(len(a1)/len(t))
    so=a1[np.lexsort([a1[:,3],a1[:,1],a1[:,0]])]
    data=[]
    for i in range(len(t)):
        data.append([])
        for j in range(len(x)):
            data[i].append(so[j*nz+l*i:(j+1)*nz+l*i,5:7])
    return data=np.array(data)

def getevenlop(time, filename):
    
    f = open(filename,"r")
    A=[]
    fr=f.read()
    fr=fr.strip('\n')
    fr=fr.split("\n")
    #print(len(fr))
    for i in range(len(fr)):
        fr[i]=fr[i].split(",")
        for j in range(len(fr[i])):
            t=float(fr[i][j])
            if abs(t)<1e-17:
                t=0
            fr[i][j]=t
    a1=np.array(fr)
        #fr[i]=tuple(fr[i])
    """    
    dtype= [("time",float),("x",float),("y",float),("z",float),("vf",float),("lf",float),("lm",float)]
    a=np.array(fr,dtype=dtype)
    a0=np.sort(a,order=["time","x","z"])
    t=-1.0
    time=[]
    t=a0[0][0]
    l=0
    newa=[]
    
    for i in range(len(a0)):
        if a0[i][0]!=t:
            l=i
            break
    if len(a0)%l!=0:
        print("error!")
    
    numtime=int(len(a0)/l)
    for i in range(numtime):
        newa.append([a0[i*l][0],a0[i*l:(i+1)*l-1]])
    """  
    t=np.unique(np.sort(a1[:,0]))
    x=np.unique(np.sort(a1[:,1]))
    z=np.unique(np.sort(a1[:,3]))
    """
    for i in range(len(x)):
        if abs(x[i])<1e-8:
            x[i]=0
    for i in range(len(t)):
        if abs(t[i])<1e-8:
            t[i]=0
    for i in range(len(z)):
        if abs(z[i])<1e-8:
            z[i]=0
    t=np.unique(np.sort(t))
    x=np.unique(np.sort(x))
    z=np.unique(np.sort(z))
    """
    l=int(len(a1)/len(t))
    so=a1[np.lexsort([a1[:,3],a1[:,1],a1[:,0]])]
    data=[]
    for i in range(len(t)):
        data.append([])
        for j in range(len(x)):
            data[i].append(so[j*221+l*i:(j+1)*221+l*i,4:7])
    data=np.array(data)
    vpth=0.01
    lpth=1e-8
    
    vph=[]
    vpl=[]
    
    for i in range(len(time)):
        plc=np.searchsorted(t, time[i])
        al=(t[plc+1]-time[i])/(t[plc+1]-t[plc])
        data1=al*data[plc]+(1-al)*data[plc+1]
        vph.append([])
        vpl.append([])
        for j in range(len(z)):
            inivph=len(x)-1
            inivpl=0
            flag=0
            while inivph>inivpl:
                if data1[inivph-1,j,0]>=vpth:
                    #print(j,inivph-1,data[i,j,inivph-1,0])
                    vph[i].append(((x[inivph]-x[inivph-1])*vpth+x[inivph-1]*data1[inivph,j,0]-x[inivph]*data1[inivph-1,j,0])/(data1[inivph,j,0]-data1[inivph-1,j,0]))
                    while inivph>inivpl:
                        if data1[inivpl+1,j,0]>=vpth:
                            vpl[i].append(((x[inivpl]-x[inivpl+1])*vpth+x[inivpl+1]*data1[inivpl,j,0]-x[inivpl]*data1[inivpl+1,j,0])/(data1[inivpl,j,0]-data1[inivpl+1,j,0]))
                            flag=1
                            break
                        inivpl+=1
                elif data1[inivpl+1,j,0]>=vpth:
                    #print(j,inivph-1,data[i,j,inivpl+1,0],data[i,j,inivpl]-data[i,j,inivpl+1])
                    vpl[i].append(((x[inivpl]-x[inivpl+1])*vpth+x[inivpl+1]*data1[inivpl,j,0]-x[inivpl]*data1[inivpl+1,j,0])/(data1[inivpl,j,0]-data1[inivpl+1,j,0]))
                    while inivph>inivpl:
                        if data1[inivph-1,j,0]>=vpth:
                            vph[i].append(((x[inivph]-x[inivph-1])*vpth+x[inivph-1]*data1[inivph,j,0]-x[inivph]*data1[inivph-1,j,0])/(data1[inivph,j,0]-data1[inivph-1,j,0]))
                            flag=1
                            break
                        inivph-=1
                else:
                    inivpl+=1
                    inivph-=1
                if flag==1:
                    break
            if flag==0:
                vph[i].append(x[inivph])
                vpl[i].append(x[inivpl])
    lph=[]
    lpl=[]
    for i in range(len(time)):
        plc=np.searchsorted(t, time[i])
        al=(t[plc+1]-time[i])/(t[plc+1]-t[plc])
        data1=al*data[plc]+(1-al)*data[plc+1]
        lph.append([])
        lpl.append([])
        for j in range(len(z)):
            inilph=len(x)-1
            inilpl=0
            flag=0
            while inilph>inilpl:
                if data1[inilph-1,j,2]>=lpth:
                    #print(j,inilph-1,data[i,j,inilph-1,2])
                    lph[i].append(((x[inilph]-x[inilph-1])*lpth+x[inilph-1]*data1[inilph,j,2]-x[inilph]*data1[inilph-1,j,2])/(data1[inilph,j,2]-data1[inilph-1,j,2]))
                    while inilph>inilpl:
                        if data1[inilpl+1,j,2]>=lpth:
                            lpl[i].append(((x[inilpl]-x[inilpl+1])*lpth+x[inilpl+1]*data1[inilpl,j,2]-x[inilpl]*data1[inilpl+1,j,2])/(data1[inilpl,j,2]-data1[inilpl+1,j,2]))
                            flag=1
                            break
                        inilpl+=1
                elif data1[inilpl+1,j,2]>=lpth:
                    #print(j,inivph-1,data[i,j,inivpl+1,0],data[i,j,inivpl]-data[i,j,inivpl+1])
                    lpl[i].append(((x[inilpl]-x[inilpl+1])*lpth+x[inilpl+1]*data1[inilpl,j,2]-x[inilpl]*data1[inilpl+1,j,2])/(data1[inilpl,j,2]-data1[inilpl+1,j,2]))
                    while inilph>inilpl:
                        if data1[inilph-1,j,2]>=lpth:
                            lph[i].append(((x[inilph]-x[inilph-1])*lpth+x[inilph-1]*data1[inilph,j,2]-x[inilph]*data1[inilph-1,j,2])/(data1[inilph,j,2]-data1[inilph-1,j,2]))
                            flag=1
                            break
                        inilph-=1
                else:
                    inilpl+=1
                    inilph-=1
                if flag==1:
                    break
            if flag==0:
                lph[i].append(x[inilph])
                lpl[i].append(x[inilpl])
    return [t,x,z,vph,vpl,lph,lpl]

if __name__ == "__main__":
    get2Ddata("G:\\test\\2D_12_5.0_.02.txt")
    """
    [t,x,z,vph,vpl,lph,lpl]=getevenlop([0.0005,0.0005],"G:\\test\\2D_12_5.0_.02.txt")
    vpplt=plt.plot(z,vpl[0],z,vph[0])
    vpplt=plt.ylim([-0.02,0.02])
    vpplt=plt.show()
    


    plt.plot(z,lpl[1],z,lph[1])
    plt.ylim([-0.002,0.002])
    plt.xlim([0,0.02])
    """
            
    
