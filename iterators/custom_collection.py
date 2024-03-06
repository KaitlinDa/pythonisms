class CustomCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        """ Makes the collection iterable """
        for item in self.data:
            yield item

    def __getitem__(self, index):
        """ Allows the collection to be used in a list comprehension and direct indexing """
        return self.data[index]

