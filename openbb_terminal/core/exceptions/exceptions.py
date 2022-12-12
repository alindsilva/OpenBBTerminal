import os
from openbb_terminal.rich_config import console

ERROR_COLOR = "red"


def handle_exception(exception: Exception) -> None:
    """Handle exceptions

    Parameters
    ----------
    exception : Exception
        Exception to handle

    Returns
    -------
    None
    """

    exception_name = exception.__class__.__name__

    if exception_name == "OpenBBUserError":
        console.print("Error:", exception, style=ERROR_COLOR)
    elif os.environ.get("DEBUG_MODE") == "true":
        raise exception
    elif exception_name == "RequestException":
        console.print(
            "Error: There was an error connecting to the API. Please try again later.",
            style=ERROR_COLOR,
        )
    elif exception_name == "SSLError":
        console.print(
            "Error: There was an error connecting to the API. "
            + "Please check whether your wifi is blocking this site.",
            style=ERROR_COLOR,
        )
    else:
        console.print("Error: An unexpected error occurred.", style=ERROR_COLOR)


def shout(message: str) -> None:
    """Raises an OpenBBUserError

    Parameters
    ----------
    message : str
        Error message

    Returns
    -------
    None
    """
    raise OpenBBUserError(message)


class OpenBBUserError(Exception):
    """OpenBB exception"""

    def __init__(self, message: str):
        self.message = message
