import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt

"""program that load the good file and displays the country information of
your campus"""


def main():
    try:
        mydata = load("population_total.csv")
    except FileNotFoundError as e:
        print(FileNotFoundError.__name__, e, sep=": ")
    else:
        # set index permet d enlever les index sinon passe comme colonnes
        try:
            mydata_transposed = mydata.set_index("country").T
            print(mydata_transposed)
            print(mydata_transposed.index)
        except AttributeError as er:
            print(AttributeError.__name__, er, sep=": ")
        else:
            mylineplot = sns.lineplot(data=mydata_transposed,
                                      x=mydata_transposed.index, y="France")
            # mylineplot = sns.lineplot(data=mydata_transposed,
            #                           x=mydata_transposed.index, y="Belgium")
            mylineplot.set_xlabel("Year")
            mylineplot.set_ylabel("Population")
            mylineplot.set_title('Population Projections')
            mylineplot.set_xticks(range(0, 300, 40))
            mylineplot.set_xlim(-10, 260)
            mylineplot.set_yticks(range(0, 3, 20000000))
            
            plt.show()


if __name__ == "__main__":
    main()
