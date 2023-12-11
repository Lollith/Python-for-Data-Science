import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt
# pip install --force-reinstall
# https://github.com/mwaskom/seaborn/archive/refs/heads/master.tar.gz
# seaborn==0.14.0.dev0
# Transpose is used here, but Melt is a better choice.


"""program that load the good file and displays the country information of
your campus"""


def clean_value(x):
    '''Cleanse the values of the dataframe (M, K and B)) and return them as
    integers'''
    if not x:
        return 0

    if isinstance(x, str):
        if 'M' in x:
            return int(float(x.replace('M', '')) * 1e6)
        elif 'k' in x:
            return int(float(x.replace('k', '')) * 1e3)
        elif 'B' in x:
            return int(float(x.replace('B', '')) * 1e9)
    return int(x)


def main():
    try:
        mydata = load("population_total.csv")
    except FileNotFoundError as e:
        print(FileNotFoundError.__name__, e, sep=": ")
    else:
        try:
            # set_index :enlever les index sinon passe comme colonnes
            mydata_transposed = mydata.set_index("country").T
        except AttributeError as er:
            print(AttributeError.__name__, er, sep=": ")
        else:
            mydata_transposed = mydata_transposed.map(clean_value)
            mylineplot = sns.lineplot(data=mydata_transposed,
                                      x=mydata_transposed.index, y="Belgium")
            print(mydata_transposed["France"])
            mylineplot = sns.lineplot(data=mydata_transposed,
                                      x=mydata_transposed.index, y="France")
            mylineplot.set_xlabel("Year")
            mylineplot.set_ylabel("Population")
            mylineplot.set_title('Population Projections')
            mylineplot.set_xticks(range(0, 240 + 1, 40))
            mylineplot.set_xlim(0, 250)
            mylineplot.set_yticks(range(0, int(8e7), int(2e7)))
            mylineplot.set_yticklabels([None, "20M", "40M", "60M"])
            plt.legend(labels=["Belgium", "France"])
            plt.show()


if __name__ == "__main__":
    main()
