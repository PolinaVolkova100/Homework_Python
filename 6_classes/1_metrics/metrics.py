import csv
from typing import Protocol
from datetime import datetime, timezone

class Txt:
    def __init__(self, path: str):
        self._path_file = path
        self._file_creating()

    def file_writing(self, data: list[list[str | int]]) -> None:
        with open(self._path_file, "a", newline="") as file:
            for date_metric_value in data:
                date, metric, value = date_metric_value
                file.write(f"{date} {metric} {value}\n")

    def _file_creating(self) -> None:
        with open(self._path_file, "w", newline="") as _:
            pass

class Csv:
    def __init__(self, path: str):
        self._path = path
        self._create_file()

    def file_writing(self, data: list[list[str | int]]) -> None:
        with open(self._path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
            writer.writerows(data)

    def _create_file(self) -> None:
        with open(self._path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])

class TypeFile(Protocol):
    def writer(self, data: list[list[str | int]]) -> None:
        pass

class Statsd:
    def __init__(self, buffer_limit: int, storage_type: TypeFile):
        self._buffer_max = buffer_limit
        self._storage = storage_type
        self._buffer = []

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
        if len(self._buffer) >= self._buffer_max:
            self._data_transfer()

    def _data_transfer(self) -> None:
        self._storage.file_writing(self._buffer)
        self._buffer = []

    def incr(self, metric_name: str) -> None:
        self._writing_to_buf(metric_name, 1)

    def decr(self, metric_name: str) -> None:
        self._writing_to_buf(metric_name, -1)


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
