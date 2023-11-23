import seaborn as sns
from load_csv import load
import pandas as pd
import warnings

"""program that load the good file and displays the country information of 
your campus"""


def main():
    # Ignorer les avertissements
    #  les avertissements sont liés à des fonctionnalités obsolètes dans seaborn et pandas.
    # use_inf_as_na option is deprecated and will be removed in a future version
    warnings.filterwarnings("ignore")

    mydata = load("life_expectancy_years.csv")
    france_data = mydata.loc[mydata['country'] == 'France', :]
    print(france_data)

    mydata_transposed = france_data.set_index("country").T  # set index permt avant la transposition de set country comme index , car apres la transposition, index se met en ligne 1 , dc france est le 58 
    print(mydata_transposed)
    # utilisé mydata_transposed.index comme abscisse dans sns.lineplot
    # type de données de l'index est numérique (int ou float) pour que le tracé de la ligne fonctionne correctement. 
    mydata_transposed.index = mydata_transposed.index.astype(int)
    print(mydata_transposed.index)
    sns.lineplot(data=mydata_transposed, x=mydata_transposed.index, y="France")


if __name__ == "__main__":
    main()