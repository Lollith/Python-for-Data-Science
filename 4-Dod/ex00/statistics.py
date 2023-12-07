def calculate_mean(my_tuple: tuple):
    '''Calculate the mean of the numbers in the tuple.'''
    return (sum(my_tuple)/len(my_tuple))


def calculate_quartile(my_tuple: tuple, quartile):
    '''Calculate the quartiles of the numbers in the tuple.
    Arguments:
    (median : quartile = 2, Q1: quartile = 4, Q3 = quartile = -4).'''
    # -4 pour index negatif
    data = sorted(my_tuple)
    index = (len(data) // quartile)
    if (len(data) % quartile == 0):
        return (data[index - 1] + data[index]) / 2
    else:
        return data[index]


def calculate_variance(my_tuple: tuple):
    '''Calculate the variance of the tuple'''
    mean = calculate_mean(my_tuple)
    sum_of_squares = sum((x - mean)**2 for x in my_tuple)
    return sum_of_squares / len(my_tuple)


def calculate_standard_deviation(my_tuple: tuple):
    '''Calculate the standard deviation of the numbers in the tuple'''
    variance = calculate_variance(my_tuple)
    return (pow(variance, 0.5))


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''get args and do the operation gived by the kwargs'''
    try:
        if (len(args) < 1):
            raise AssertionError("ERROR")
    except AssertionError as e:
        print(e)

    else:
        mydict = {
            "mean": calculate_mean(args),
            "median": calculate_quartile(args, 2),
            "quartile": [float(calculate_quartile(args, 4)),
                         float(calculate_quartile(args, -4))],
            "std": calculate_standard_deviation(args),
            "var": calculate_variance(args),
        }

        for name in kwargs:
            if kwargs[name] in mydict:
                print(kwargs[name], mydict[kwargs[name]], sep=": ")
            else:
                print("ERROR")


if __name__ == "__main__":
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
