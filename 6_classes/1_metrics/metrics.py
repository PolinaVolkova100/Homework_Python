import csv
from typing import Protocol
from datetime import datetime, timezone


class Txt:
    def __init__(self, path: str):
        self._path_file = path
        self._file_creating()

    def _file_creating(self) -> None:
        with open(self._path_file, "w", newline="") as _:
            pass

    def file_writing(self, data: list[list[str | int]]) -> None:
        with open(self._path_file, "a", newline="") as txt_file:
            for info in data:
                date, metric, value = info
                txt_file.write(f"{date} {metric} {value}\n")


class Csv:
    def __init__(self, path: str):
        self._path = path
        self._file_creating()

    def _file_creating(self) -> None:
        with open(self._path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])

    def file_writing(self, data: list[list[str | int]]) -> None:
        with open(self._path, "a", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";", lineterminator="\n")
            writer.writerows(data)


class TypeFile(Protocol):
    def writer(self, data: list[list[str | int]]) -> None:
        pass


class Statsd:
    def __init__(self, buffer_max: int, storage_type: TypeFile):
        self._buffer = []
        self._storage = storage_type
        self._buffer_max = buffer_max

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._data_transfer()

    def _writing_to_buf(self, metric: str, value: int) -> None:
        self._buffer.append(
            [
                datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z"),
                metric,
                value,
            ]
        )
        if self._buffer_max <= len(self._buffer):
            self._data_transfer()

    def _data_transfer(self) -> None:
        self._storage.file_writing(self._buffer)
        self._buffer.clear()

    def incr(self, metr: str) -> None:
        self._writing_to_buf(metr, 1)

    def decr(self, metr: str) -> None:
        self._writing_to_buf(metr, -1)


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    if path.endswith(".txt") == False:
        raise ValueError
    return Statsd(buffer_limit, Txt(path))


def get_csv_statsd(path: str, buffer_max: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    if path.endswith(".csv") == False:
        raise ValueError
    return Statsd(buffer_max, Csv(path))
