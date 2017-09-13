# Write a function, remove_duplicates that takes a list as its argument and returns a new list containing the unique elements of the original list. The elements in the new list without duplicates can be in any order.

def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target
