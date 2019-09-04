#%%
# Librerias
import os
import numpy as np
import matplotlib.pyplot as plt
# Directorio madre
os.chdir('/home/kevin/Documentos/MATERIAS_UBA/CG/P/P_02/oceano/salidas_5m')
# Parametros de funcion Cargar
dir_salida1='/home/kevin/Documentos/MATERIAS_UBA/CG/P/P_02/oceano/salidas_5m/out_tmp1/'
dir_salida2='/home/kevin/Documentos/MATERIAS_UBA/CG/P/P_02/oceano/salidas_5m/out_tmp2/'
dir_salida3='/home/kevin/Documentos/MATERIAS_UBA/CG/P/P_02/oceano/salidas_5m/out_tmp3/'
dir_salida4='/home/kevin/Documentos/MATERIAS_UBA/CG/P/P_02/oceano/salidas_5m/out_tmp4/'
dir_salida5='/home/kevin/Documentos/MATERIAS_UBA/CG/P/P_02/oceano/salidas_5m/out_tmp5/'
Lx=1000000; Ly=500000; nx=100; ny=50
# Funcion Cargar 
from Cargar import cargar
psi_temp1,vort_temp1,psiF1,vortF1,QG_diag1,QG_curlw1,X1,Y1,dx1,dy1=cargar(dir_salida1,Lx,Ly,nx,ny)
psi_temp2,vort_temp2,psiF2,vortF2,QG_diag2,QG_curlw2,X2,Y2,dx2,dy2=cargar(dir_salida2,Lx,Ly,nx,ny)
psi_temp3,vort_temp3,psiF3,vortF3,QG_diag3,QG_curlw3,X3,Y3,dx3,dy3=cargar(dir_salida3,Lx,Ly,nx,ny)
psi_temp4,vort_temp4,psiF4,vortF4,QG_diag4,QG_curlw4,X4,Y4,dx4,dy4=cargar(dir_salida4,Lx,Ly,nx,ny)
psi_temp5,vort_temp5,psiF5,vortF5,QG_diag5,QG_curlw5,X5,Y5,dx5,dy5=cargar(dir_salida5,Lx,Ly,nx,ny)
#%%
#1
plt.plot(np.array(QG_diag1[:,3]),label="Ev1=0.025")
plt.plot(np.array(QG_diag2[:,3]),label="Ev2=0.015")
plt.plot(np.array(QG_diag3[:,3]),label="Ev3=0.010")
plt.plot(np.array(QG_diag4[:,3]),label="Ev4=0.005")
plt.plot(np.array(QG_diag5[:,3]),label="Ev5=0.001")
plt.grid(); plt.minorticks_on(); plt.grid(True,which='minor'); plt.title('Variacion temporal de la Energia Cinetica')
plt.xlabel('tiempo'); plt.ylabel('Energia cinetica');
plt.legend(loc='lower right', bbox_to_anchor=(1.3,0.6))
#%%
#2
energia=QG_diag1[:,3]
nend=len(energia)-1
iteracion=0
for i in reversed(energia):   #empezamos por el final del vector
    ecinet=((energia[nend]-i)/energia[nend])*100
    if abs(ecinet) >= 1:      #hasta encontrar que no cumpla esta condicion
        break                 #detenemos el bucle
    iteracion=iteracion+1     #contador de veces que si cumple q sea < 1
print('El numero de iteracion necesario es:',len(energia)-iteracion+1)
#%%
#3
#Funcion corriente
psiF=psiF1
beta=1.9*10**(-11); taus=0.3; ro=1025; D=2000
U=(2*np.pi*taus)/(ro*D*beta*Lx); U1=U*Lx; psi=psiF*U1 
plt.contour(psi); plt.grid(True); plt.colorbar()
plt.xlabel('longitud'); plt.ylabel('latitud'); plt.title('Funcion corriente')

#%%
#3
#Vorticidad 
vortF=vortF1
U2=U/Lx; vort=vortF*U2
plt.contourf(vort); plt.grid(True); plt.colorbar()
plt.xlabel('longitud'); plt.ylabel('latitud'); plt.title('Vorticidad')
