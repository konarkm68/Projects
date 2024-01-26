import numpy
import matplotlib.pyplot


class LogAntilogGraphs:
    def __init__(self):
        self.plot_val_x = range(0, 11)
        ## Ignore the divide by zero error
        numpy.seterr(divide="ignore")

    def Log(self):
        matplotlib.pyplot.subplot(2, 1, 1)
        matplotlib.pyplot.title("Logarithm Graph")

        ## Natural Logarithm
        ## Calculate & Plot the values
        plot_val_y = numpy.log(self.plot_val_x)
        matplotlib.pyplot.plot(self.plot_val_x, plot_val_y, marker="o", label="log()")
        ## Print x, y values
        for a, b in zip(self.plot_val_x, plot_val_y):
            matplotlib.pyplot.text(a, b, str(round(b, 3)))

        ## Common Logarithm
        ## Calculate & Plot the values
        plot_val_y = numpy.log10(self.plot_val_x)
        matplotlib.pyplot.plot(self.plot_val_x, plot_val_y, marker="o", label="log(10)")
        ## Print x, y values
        for a, b in zip(self.plot_val_x, plot_val_y):
            matplotlib.pyplot.text(a, b, str(round(b, 3)))

        ## Show legend and grid
        matplotlib.pyplot.legend()
        matplotlib.pyplot.grid()

    def Antilog(self):
        matplotlib.pyplot.subplot(2, 1, 2)
        matplotlib.pyplot.title("Antilogarithm Graph")

        ## Calculate & Plot the values
        plot_val_y = numpy.exp(self.plot_val_x)
        matplotlib.pyplot.plot(
            self.plot_val_x, plot_val_y, marker="o", label="antilog()"
        )
        ## Print x, y values
        for a, b in zip(self.plot_val_x, plot_val_y):
            matplotlib.pyplot.text(a, b, str(round(b, 3)))

        ## Show legend and grid
        matplotlib.pyplot.legend()
        matplotlib.pyplot.grid()

    def main(self):
        try:
            self.Log()
            self.Antilog()
            ## tight_layout() adjusts the padding between and around subplots
            matplotlib.pyplot.tight_layout()
            matplotlib.pyplot.show()
            ## matplotlib.pyplot.savefig('Log and Antilog Graphs.png')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    LogAntilogGraphs().main()
