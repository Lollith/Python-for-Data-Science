"""copy the function tqdm with the yield operator
def ft_tqdm(lst: range) -> None: """


import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst) 
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        bar_lengh = 145
        bar = "=" * int(bar_lengh * progress) + ">"
        espaces = ' ' * (bar_lengh - len(bar))
        sys.stdout.write(f"\r{int(progress * 100)}%|[{bar}{espaces}]|\
                         {i + 1}/{total}) ")  # \r permet de revenir a la ligne  pour recommencer a 0 => donne l impression d evoluer
        sys.stdout.flush()  # force l ecriture immediate ds la sortie standard, sans les maj pourraient etre stockee ds le tampon et ne s afficher quapres un delai
        yield item
    sys.stdout.write("\n")