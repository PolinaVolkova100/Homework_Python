from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    for iterable in iterables:
        for el in iterable:
            yield el

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self.iterables = iterables
        self.count = len(iterables)
        self.iter_ind = 0
        self.el_ind = 0
        self.object = tuple(iterables[self.iter_ind])
    def __iter__(self):
        return self
    def __next__(self):
        if self.el_ind < len(self.object):
            result = self.object[self.el_ind]
            self.el_ind += 1
            return result
        else:
            self.iter_ind += 1
            self.el_ind = 1
            self.object = tuple(self.iterables[self.iter_ind])
            if self.count == self.iter_ind:
                raise
            return self.object[0]
