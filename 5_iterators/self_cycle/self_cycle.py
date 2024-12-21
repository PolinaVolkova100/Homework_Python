from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    while obj:
        for el in obj:
            yield el

class Cycle:
    def __init__(self, obj: Iterable[T]):
        self.obj = tuple(obj)
        self.len = len(obj)
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.len:
            self.index += 1
            return self.obj[self.index - 1]
        elif self.index == self.len:
            self.index = 1
            return self.obj[0]

