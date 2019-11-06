# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 02:08:32 2019

@author: zhy94
"""

import numpy as np
import matplotlib.pyplot as plt
import untitled0
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
    lpth=1e-9
    
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
                 #   if data1[inivph,j,0]>=vpth:
                  #      vph[i].append(x[inivph])
                   # else:
                    vph[i].append(((x[inivph]-x[inivph-1])*vpth+x[inivph-1]*data1[inivph,j,0]-x[inivph]*data1[inivph-1,j,0])/(data1[inivph,j,0]-data1[inivph-1,j,0]))
                    #if data1[inivph,j,0]-data1[inivph-1,j,0]==0:
                      #  print(i,j,inivph-1,data1[inivph,j,0]-data1[inivph-1,j,0],data1[inivph,j,0],data1[inivph-1,j,0])
                    while inivph>inivpl:
                        
                        if data1[inivpl+1,j,0]>=vpth:
                    #        if data1[inivpl,j,0]>=vpth:
                     #           vpl[i].append(x[inivpl])
                      #      else:
                            vpl[i].append(((x[inivpl]-x[inivpl+1])*vpth+x[inivpl+1]*data1[inivpl,j,0]-x[inivpl]*data1[inivpl+1,j,0])/(data1[inivpl,j,0]-data1[inivpl+1,j,0]))
                            flag=1
                            break
                        inivpl+=1
                elif data1[inivpl+1,j,0]>=vpth:
                    #if data1[inivpl,j,0]>=vpth:
                     #   vpl[i].append(x[inivpl])
                    #else:
                    #print(j,inivph-1,data[i,j,inivpl+1,0],data[i,j,inivpl]-data[i,j,inivpl+1])
                    vpl[i].append(((x[inivpl]-x[inivpl+1])*vpth+x[inivpl+1]*data1[inivpl,j,0]-x[inivpl]*data1[inivpl+1,j,0])/(data1[inivpl,j,0]-data1[inivpl+1,j,0]))
                    while inivph>inivpl:
                        if data1[inivph-1,j,0]>=vpth:
                     #       if data1[inivph,j,0]>=vpth:
                      #           vph[i].append(x[inivph])
                       #     else:
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
def interpolation(z,matz,vph,vpl):
    i=0
    newvpl=[]
    newvph=[]
    while i<len(matz):
        while i<len(matz) and matz[i]<=z[0]:
            i+=1
            newvpl.append(0)
            newvph.append(0)
        if i>=len(matz):
            break
        plc=np.searchsorted(z, matz[i])
        alp=(z[plc]-matz[i])/(z[plc]-z[plc-1])
        newvpl.append(alp*vpl[plc-1]+(1-alp)*vpl[plc])
        newvph.append(alp*vph[plc-1]+(1-alp)*vph[plc])
        i+=1
    return [newvph,newvpl]

def lossfun(newvph,newvpl,expvph,expvpl):
    s=0
    for i in range(len(newvph)):
        s+=abs(abs(newvph[i]-newvpl[i])-abs(expvph[i]-expvpl[i]))
    return s/len(newvph)




[lt,lz,explph,explpl]=getexplp()
[vt,vz,expvph,expvpl]=getexpvp()

for i in range(len(vz)):
    vz[i]=np.unique(vz[i])
vz=np.array(vz)
for i in range(len(lz)):
    lz[i]=np.unique(lz[i])
lz=np.array(lz)
prinlist=''
namelist=['.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
for ii in range(12,14,3):
    for jj in range(9,10):
        [t0,x,z,vph0,vpl0,lph,lpl]=untitled0.getevenlop(lt[0:121],"G:\\test\\2D_%d_%s_.02.txt"%(ii,namelist[jj]))
        [t1,x,z,vph,vpl,lph0,lpl0]=untitled0.getevenlop(vt[0:84],"G:\\test\\2D_%d_%s_.02.txt"%(ii,namelist[jj]))

        lossv=0
        for ip in range(84):
            [newvph,newvpl]=interpolation(z,vz[ip],vpl[ip],vph[ip])
            lossv+=lossfun(newvph,newvpl,expvpl[ip],expvph[ip])
        lossv/=84
#vpplt=plt.plot(vz[ip],newvpl,vz[ip],newvph ,vz[ip],expvpl[ip],vz[ip],expvph[ip])
#plt.show()
        lossl=0
        for ip in range(121):
            [newlph,newlpl]=interpolation(z,lz[ip],lpl[ip],lph[ip])
            lossl+=lossfun(newlph,newlpl,explpl[ip],explph[ip])
        lossl/=121
        prinlist+=" %f %f\n"%(lossv,lossl)
        print("G:\\test\\2D_%d_%s_.02.txt is done!"%(ii,namelist[jj]))

#vpplt=plt.plot(lz[ip],newlpl,lz[ip],newlph ,lz[ip],explpl[ip],lz[ip],explph[ip])
fout=open('G:\\test\\test.txt','w')
fout.write(prinlist)
fout.close()

"""
vpplt=plt.plot(z,vpl[50],z,vph[50])
vpplt=plt.ylim([-0.02,0.02])
vpplt=plt.show()
ip=50
vpplt=plt.plot(z,vpl[ip],z,vph[ip],vz[ip],expvpl[ip],vz[ip],expvph[ip])
vpplt=plt.ylim([-0.02,0.02])
vpplt=plt.show()
vpplt=plt.plot(z,lpl[ip],z,lph[ip],lz[ip],explpl[ip],lz[ip],explph[ip])
plt.ylim([-0.002,0.002])
plt.xlim([0,0.02])
vpplt=plt.show()
    """