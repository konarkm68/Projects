import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,1,1)
x=range(11)
y=np.log(x)
plt.plot(x,y,marker='o',label='log')
for a,b in zip(x,y):
	plt.text(a,b,str(round(b,3)))
		
y=np.log10(x)
plt.plot(x,y,marker='o',label='log10')
for a,b in zip(x,y):
	plt.text(a,b,str(round(b,3)))

plt.xlim(0,11)
plt.legend()
plt.grid()


plt.subplot(2,1,2)
x=range(0,11)
y=np.exp(x)
plt.plot(x,y,marker='o',label='antilog')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()	

