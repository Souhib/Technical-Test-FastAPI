class BaseError(Exception):
    """
    Base class for custom exceptions.

    Attributes:
        name (str): The name of the error.
        message (str): The error message.
        status_code (int): The HTTP status code associated with the error.
    """

    def __init__(self, name: str, message: str, status_code: int):
        self.name = name
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class NoFramesFound(BaseError):
    """
    Exception raised when no frames are found within a specified depth range.

    Attributes:
        depth_min (float): The minimum depth of the range.
        depth_max (float): The maximum depth of the range.
        status_code (int): The HTTP status code associated with the error. Defaults to 404.
        name (str): The name of the error. Defaults to "NoFramesFound".
    """

    def __init__(
        self,
        depth_min: float,
        depth_max: float,
        status_code: int = 404,
        name: str = "NoFramesFound",
    ):
        self.name = name
        self.message = f"No Frames found between {depth_min} and {depth_max}"
        self.status_code = status_code
        super().__init__(
            name=self.name, message=self.message, status_code=self.status_code
        )
