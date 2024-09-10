class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Implementing the __iter__ method to make the class iterable
    def __iter__(self):
        # Returning a custom iterator object
        return RectangleIterator(self)

class RectangleIterator:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        # Iterator starts at 0, 0 means 'length', 1 means 'width'
        self.index = 0

    def __next__(self):
        if self.index == 0:
            self.index += 1
            return {'length': self.rectangle.length}
        elif self.index == 1:
            self.index += 1
            return {'width': self.rectangle.width}
        else:
            raise StopIteration  # End of iteration


# Example usage
rect = Rectangle(10, 20)
for dimension in rect:
    print(dimension)
