""" Function that prints the object type of all types of "Null.
 that prints the object type of all types of "Null"."""


def NULL_not_found(input_object: any) -> int:
    # dictionary of objects
    my_objects_zero = {
        None: "Nothing",
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake",
    }
    type_object = type(input_object)
    if (input_object and type_object != float):
        print("Type not found")
        return 1
    else:
        object_zero = my_objects_zero.get(type_object)
        if object_zero is None:
            print(f"Nothing: {input_object} {type_object}")
        else:
            print(f"{object_zero}: {input_object} {type_object}")
        return 0
