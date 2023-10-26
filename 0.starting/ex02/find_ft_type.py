# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agouet <agouet@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/26 13:21:36 by agouet            #+#    #+#              #
#    Updated: 2023/10/26 18:06:40 by agouet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(input_object: any) -> int:
	"""Function that takes any object as argument and define its type.

	parameters
	----------
	param1 : any
		Any object that we want to know the type
	
	returns
	-------
	int
		1 if the object is a container, 0 otherwise """

	if isinstance(input_object, list):
		print("List: ", type(input_object))
		return 1
	if isinstance(input_object, tuple):
		print("Tuple: ", type(input_object))
		return 1
	if isinstance(input_object, set):
		print("Set: ", type(input_object))
		return 1
	if isinstance(input_object, dict):
		print("Dict: ", type(input_object))
		return 1
	if isinstance(input_object, str):
		print(input_object, "is in the kitchen", type(input_object))
		return 1
	else:
		print("Type not found")
		return 42