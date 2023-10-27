""" Module that contains a function that takes any object as argument and define its type."""


def all_thing_is_obj2(input_object: any) -> int:
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


def all_thing_is_obj(input_object: any) -> int:
    """Same function without "if".

    parameters
    ----------
    param1 : any
        Any object that we want to know the type
    returns
    -------
    int
        1 if the object is a container, 0 otherwise """
    my_objects = {
        list: "list",
        tuple: "tuples",
        set: "set",
        dict: "dict",
        str: "str"
        }
    object_type = type(input_object)
    # get cherche la clé "object_type" , et si elle n'existe pas, renvoie "Type
    # not found"(valeur par default)
    my_object = my_objects.get(object_type, "Type not found")
    if object_type == str:
        print(input_object, "is in the kitchen", object_type)
    elif my_object == "Type not found":
        print(f"{my_object}")
    else:
        print(f"{my_object}: {object_type}")
    return 42
