import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt

"""program that load the good file and displays the country information of
your campus"""


def main():
    try:
        mydata = load("life_expectancy_years.csv")
    except FileNotFoundError as e:
        print(FileNotFoundError.__name__, e, sep=": ")
    else:
        # set index permet d enlever les index sinon passe comme colonnes
        try:
            mydata_transposed = mydata.set_index("country").T
        except AttributeError as er:
            print(AttributeError.__name__, er, seo=": ")
        else:
            mylineplot = sns.lineplot(data=mydata_transposed,
                                      x=mydata_transposed.index, y="France")
            mylineplot.set_xlabel("Year")
            mylineplot.set_ylabel("Life expectancy")
            mylineplot.set_title('France Life expectancy Projections')
            mylineplot.set_xticks(range(0, 300, 40))
            plt.show()


if __name__ == "__main__":
    main()
