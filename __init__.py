
def keyset(d):
    return set(d.keys())

def union(d1, d2):
    return keyset(d1).union(keyset(d2))

def zip(d1, d2, std = None):
    """ Return a dictionary of tuples by putting together values with the same keys. Ex.:

    > zip({'name': "John", 'age': 20, 'favoriteMovie': "Godfather"}, {'name': "Mary", 'age': 26}, std = None)
    {'name': ("John", "Mary"), 'age': (20, 26), 'favoriteMovie': ("Godfather", None)}
    """
    return {key: (d1.get(key, std), d2.get(key, std)) for key in union(d1, d2)}

def zipWith(function, d1, d2, std = None):
    """ Return a dictionary resulting from appling a binary function over values with the same keys. Ex.:
    > purchase1 = {"mushrooms": 20, "beer": 293, "clothes": 1}
    > purchase2 = {"cognac": 1, "beer": 20, "cars": 2}
    > zipWith(lambda x,y : x + y, purchase1, purchase2, std = 0.0)
    {"mushrooms": 20, "beer": 313, "clothes": 1, "cognac": 1, "cars":2}
    """
    zipped = zip(d1, d2, std = std)
    return {key: function(value1, value2) for (key, (value1, value2)) in zipped.iteritems()}


if __name__ == "__main__":
    test1 = zip({'name': "John", 'age': 20, 'favoriteMovie': "Godfather"}, {'name': "Mary", 'age': 26}, std = None)
    assert test1 == {'name': ("John", "Mary"), 'age': (20, 26), 'favoriteMovie': ("Godfather", None)}
    purchase1 = {"mushrooms": 20, "beer": 293, "clothes": 1}
    purchase2 = {"cognac": 1, "beer": 20, "cars": 2}
    test2 = zipWith(lambda x,y : x + y, purchase1, purchase2, std = 0.0)
    assert test2 == {"mushrooms": 20, "beer": 313, "clothes": 1, "cognac": 1, "cars":2}

