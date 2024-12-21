from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    for i in range(0, len(obj) + 1, n):
        if i + n < len(obj):
            yield tuple(obj[i : i + n])
        else:
            yield tuple(obj[i:])

class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self.obj = iter(obj)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        batch = tuple(next(self.obj, None) for _ in range(self.n))
        if not batch or batch == (None,) * self.n:
            raise StopIteration
        return batch[: len(batch) - batch.count(None)]

