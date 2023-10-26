# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agouet <agouet@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 13:56:58 by agouet            #+#    #+#              #
#    Updated: 2023/10/26 12:20:07 by agouet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# # • There is no global variable.

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
 # list : modifiable
ft_list[1] = "World!"

#tuple : non modifiable
new_tuple = ("Hello",)
ft_tuple = new_tuple +(("France!"),)

#pas d ordre et pas dindex => list pour etre dans le bon ordre
ft_set.discard("tutu!")
ft_set.add('Paris!')
# ft_set = list(ft_set)
# ft_set.sort()

 #modifiable
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
