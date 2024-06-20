import typing

T = typing.TypeVar("T")


class SingletonWrapper(typing.Generic[T]):
    """
    A singleton wrapper class. Its instances would be created
    for each decorated class.
    """

    def __init__(self, cls: typing.Type[T]) -> None:
        self.__wrapped__ = cls
        self._instance: T | None = None

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> T:
        """Returns a single instance of decorated class"""
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance


def singleton(cls: typing.Type[T]) -> SingletonWrapper[T]:
    """
    A singleton decorator. Returns a wrapper objects. A call on that object
    returns a single instance object of decorated class. Use the __wrapped__
    attribute to access decorated class directly in unit tests
    """
    return SingletonWrapper[T](cls)
