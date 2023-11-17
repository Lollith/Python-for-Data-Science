"""copy the function tqdm with the yield operator
def ft_tqdm(lst: range) -> None: """

# creation d'un generateur, conserve son etat actuel
# lors dune nouvelle excecution, on repart de cette etat pour generer une
# nouvelle value
# si term_w trop grande : genere une multitude de barre de chargement

import sys
import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    term_w = os.get_terminal_size(1).columns - 43
    for i, item in enumerate(lst):
        progress = ((i + 1) / total)
        bar = "=" * int(term_w * progress) + ">"
        espaces = ' ' * (term_w - len(bar))
        sys.stdout.write(f"\r{int(progress * 100)}%|[{bar}{espaces}]|"
                         f"{i + 1}/{total}")  # \r permet de revenir a la ligne
        sys.stdout.flush()  # force l ecriture ds la sortie standard
        yield item
    sys.stdout.write("\n")
