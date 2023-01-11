from zope.interface import Interface, Attribute

class Physical(Interface):
    """Thing that takes up space in a `Tile`, has physical space.
    """

    def greet():
        print('im physical!')
