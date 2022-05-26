import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,(4*np.pi),256,endpoint=True)

plt.subplot(2,3,1)
plt.title('sine')
plt.plot(x,np.sin(x))
plt.grid()

plt.subplot(2,3,4)
plt.title('cosecant')
y=1/np.sin(x)
y[:-1][np.diff(y)>np.pi]=np.nan
plt.plot(x,y)
plt.ylim(-5,5)
plt.grid()


plt.subplot(2,3,2)
plt.title('cosine')
plt.plot(x,np.cos(x))
plt.grid()

plt.subplot(2,3,5)
plt.title('secant')
y=1/np.cos(x)
y[:-1][np.diff(y)>np.pi]=np.nan
plt.plot(x,y)
plt.ylim(-5,5)
plt.grid()


plt.subplot(2,3,3)
plt.title('tangent')
y=np.tan(x)
y[:-1][np.diff(y)<0]=np.nan
plt.plot(x,y)
plt.ylim(-5,5)
plt.grid()

plt.subplot(2,3,6)
plt.title('cotangent')
y=1/np.tan(x)
y[:-1][np.diff(y)>0]=np.nan
plt.plot(x,y)
plt.ylim(-5,5)
plt.grid()

plt.tight_layout()
plt.show()
