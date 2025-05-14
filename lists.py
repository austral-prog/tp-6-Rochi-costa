# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista1 = list_to_remove_elements [:]
    remove = [5,4,0]
    for i in (remove) :
        if i <len(lista1):
            del lista1 [i]
    return lista1

def add_elements(list_to_add_elements):
    lista1 = list_to_add_elements
    lista1.append ("Yellow")
    lista1.insert(0,"Pink")

    return lista1


def is_empty(list_to_check):
    lista1 = list_to_check
    if len(lista1) == 0:
        return True
    else: 
        return False


def check_lists(list_to_compare1, list_to_compare2):
    lista1 = list_to_compare1
    lista2 = list_to_compare2
    if len(lista1) >= 3 and len(lista2) >= 3:
        if lista1[2] == lista2 [2]:
            return True
        else:
            return False
    else:
        return False

    


def list_of_lists(list_of_lists_to_modify):
    list1 = list_of_lists_to_modify
    list1 [0] = list1 [0] [:2]
    list1 [1] = list1 [1] [1:4]
    list1 [2] = list1 [2] [-2:]
    return list1