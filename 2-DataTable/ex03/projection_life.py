from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""program that loads the 2 given files and displays the projection of life
expectancy in relation to the gross national product of the year 1900 for each
country."""
# gpd = pib
# pb : aucune donnee du meme type => passer les colonnes interessantes en float
# 1.rendre facilement manipulable


def clean_value(x):
    if not x:
        return 0

    if isinstance(x, str):
        if 'M' in x:
            return (float(x.replace('M', '')) * 1e6)
        elif 'k' in x:
            return (float(x.replace('k', '')) * 1e3)
        elif 'B' in x:
            return (float(x.replace('B', '')) * 1e9)
    return float(x)


def data_melt(data_to_melt: pd.DataFrame, value: str):
    """Function that melts my dataframe: rearranges data for handling."""
    data_melted = data_to_melt.melt(id_vars=["country"],
                                    var_name="year", value_name=value)
    # print(data_melted)
    return data_melted


def display_scatterplot(df_1900: pd.DataFrame):
    mylineplot = sns.scatterplot(data=df_1900, x='gpd', y='life')
    mylineplot.set_xlabel("Gross domestic product")
    mylineplot.set_ylabel("Life Expectancy")
    mylineplot.set_title('1900')
    mylineplot.set_xscale('log')
    mylineplot.set_xticks([300, 1000, 10000])
    mylineplot.set_xticklabels(["300", "1k", "10k"])
    plt.show()


def main():
    try:
        gpd_data = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_data = load("life_expectancy_years.csv")
    except FileNotFoundError as e:
        print(FileNotFoundError.__name__, e, sep=": ")
    else:
        gpd_melted = data_melt(gpd_data, "gpd")
        life_melted = data_melt(life_data, "life")

        # str for clean_value => float
        gpd_melted["gpd"] = gpd_melted["gpd"].astype(str)
        gpd_melted["gpd"] = gpd_melted["gpd"].apply(clean_value)
        life_melted["life"] = life_melted["life"].astype(float)

        gpd_merged = gpd_melted.merge(life_melted)
        # print(gpd_merged)
        df_1900 = gpd_merged.loc[gpd_merged["year"] == "1900"]
        # print(df_1900.drop(columns='year'))

        display_scatterplot(df_1900)


if __name__ == "__main__":
    main()
