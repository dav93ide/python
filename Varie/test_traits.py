from traits.api import Enum, HasTraits, List


class A(HasTraits):
    values = List([1, 2, 3])
    enum = Enum(values='values')


a = A()
a.configure_traits()