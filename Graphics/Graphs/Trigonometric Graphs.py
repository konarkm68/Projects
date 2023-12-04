import numpy
import matplotlib.pyplot 

class TrigonometricGraphs():
    def __init__(self):
        self.plot_val_x=numpy.linspace(0,(4*numpy.pi),255) # 255 points between 0 and 4pi
        ## Ignore the divide by zero error
        numpy.seterr(divide='ignore') 

    def sine(self):
        matplotlib.pyplot.subplot(2,3,1)
        matplotlib.pyplot.title('sine()')
        ## Calculate & Plot the values
        matplotlib.pyplot.plot(self.plot_val_x,numpy.sin(self.plot_val_x))
        ## Show grid
        matplotlib.pyplot.grid()

    def cosecant(self):
        matplotlib.pyplot.subplot(2,3,4)
        matplotlib.pyplot.title('cosecant()')
        ## calculate the cosecant values
        plot_val_y=1/numpy.sin(self.plot_val_x)
        plot_val_y[:-1][numpy.diff(plot_val_y)>numpy.pi]=numpy.NaN # remove the discontinuity
        matplotlib.pyplot.ylim(-5,5)
        ## Plot the values
        matplotlib.pyplot.plot(self.plot_val_x,plot_val_y)
        ## Show grid
        matplotlib.pyplot.grid()

    def cosine(self):
        matplotlib.pyplot.subplot(2,3,2)
        matplotlib.pyplot.title('cosine()')
        ## Calculate & Plot the values
        matplotlib.pyplot.plot(self.plot_val_x,numpy.cos(self.plot_val_x))
        ## Show grid
        matplotlib.pyplot.grid()

    def secant(self):
        matplotlib.pyplot.subplot(2,3,5)
        matplotlib.pyplot.title('secant()')
        ## calculate the secant values
        plot_val_y=1/numpy.cos(self.plot_val_x)
        plot_val_y[:-1][numpy.diff(plot_val_y)>numpy.pi]=numpy.NaN
        matplotlib.pyplot.ylim(-5,5)
        ## Plot the values
        matplotlib.pyplot.plot(self.plot_val_x,plot_val_y)
        ## Show grid
        matplotlib.pyplot.grid()

    def tangent(self):
        matplotlib.pyplot.subplot(2,3,3)
        matplotlib.pyplot.title('tangent()')
        ## calculate the tangent values
        plot_val_y=numpy.tan(self.plot_val_x)
        plot_val_y[:-1][numpy.diff(plot_val_y)<0]=numpy.NaN
        matplotlib.pyplot.ylim(-5,5)
        ## Plot the values
        matplotlib.pyplot.plot(self.plot_val_x,plot_val_y)
        ## Show grid        
        matplotlib.pyplot.grid()

    def cotangent(self):
        matplotlib.pyplot.subplot(2,3,6)
        matplotlib.pyplot.title('cotangent()')
        ## calculate the cotangent values
        plot_val_y=1/numpy.tan(self.plot_val_x)
        plot_val_y[:-1][numpy.diff(plot_val_y)>0]=numpy.NaN
        matplotlib.pyplot.ylim(-5,5)
        ## Plot the values
        matplotlib.pyplot.plot(self.plot_val_x,plot_val_y)
        ## Show grid
        matplotlib.pyplot.grid()

    def main(self):
        try:
            self.sine()
            self.cosecant()
            self.cosine()
            self.secant()
            self.tangent()
            self.cotangent()
            ## tight_layout() adjusts the padding between and around subplots
            matplotlib.pyplot.tight_layout()
            matplotlib.pyplot.show()
            ## matplotlib.pyplot.savefig('Trigonometric Graphs.png')
        except Exception as e:
            print(e)

if __name__=='__main__':
    TrigonometricGraphs().main()