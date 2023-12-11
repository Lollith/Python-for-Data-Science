import pandas as pd

# conda install -c conda-forge libstdcxx-ng


def load(path: str) -> pd.DataFrame:
    '''takes a path as argument, writes the dimensions of the data set
and returns it.'''
    try:
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file fromat is not .csv")
    except AssertionError as e:
        print(AssertionError.__name__, e, sep=": ")
    try:
        data = pd.read_csv(path)
    except FileNotFoundError as error:
        print(FileNotFoundError.__name__, error, sep=": ")
    except pd.errors.EmptyDataError:
        print("Le fichier est vide.")
    except pd.errors.ParserError:
        print("Erreur de parsing. Vérifiez le format du fichier.")
    except pd.errors.DtypeWarning as e:
        print(f"Warning de type : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
    else:
        print(f"Loading dataset of dimensions {data.shape}")
        return data


if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))
    # print(load("empty.csv"))
    # print(load("file_not_exist.csv"))
    # print(load("life_expectancy_years.zip"))
