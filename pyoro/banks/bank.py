import typing

T = typing.TypeVar("T")


class Bank(typing.Generic[T]):
    def __init__(self):
        self.data: dict[str, T] = {}
        self.fallback: T | None = None

    def load(self) -> None:
        pass

    def get(self, key: str) -> T:
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found in bank '{self.__class__.__name__}'")
        return self.data[key]

    def __getitem__(self, key: str):
        return self.get(key)

    def get_fallback(self) -> T:
        if not self.fallback:
            raise NotImplementedError()
        return self.fallback
