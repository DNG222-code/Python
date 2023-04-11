import random

def llista_20_elements():
    # Generate a list of 20 random integers between 1 and 100
    l = []
    for i in range(20):
        l.append(random.randint(1,100))
    return l

def hi_ha_duplicats(a):
    # Check if there are any duplicate elements in the input list
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]
    if len(dupes) > 0:
        # Print the input list and the duplicate elements
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        # Print the input list and an empty list for duplicate elements
        print("La llista {} no té elements duplicats".format(a))

def elimina_duplicats(a):
    # Remove duplicate elements from the input list and return a new list
    b = list(set(a))
    return b

# Main program
x = llista_20_elements()
hi_ha_duplicats(x)
y = elimina_duplicats(x)
y.sort()
print("Llavors, la llista sense elements duplicats és {}".format(y))