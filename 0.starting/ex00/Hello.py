# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agouet <agouet@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 13:56:58 by agouet            #+#    #+#              #
#    Updated: 2023/10/25 18:34:20 by agouet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Your lib imports must be explicit, for example you must "import numpy as np".
# Importing "from pandas import *" is not allowed, and you will get 0 on the exercise.
# # • There is no global variable.

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

new_tuple = ("Hello",)

ft_set.discard("tutu!")
ft_set.add('Paris!')
ft_setlist = list(ft_set)
ft_setlist.sort()

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)