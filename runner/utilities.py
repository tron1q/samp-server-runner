"""This module contains all the utilities methods or constants used in the runner script"""

from typing import Dict, Any, Union
from json import dump

class Utilities:
    """The Utilities class, which we will allocate all important details"""

    # Constant variables
    COLORS = {
        "red": "\033[1;31m",
        "green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[1;34m",
        "purple": "\033[1;35m",
        "cyan": "\033[1;36m",
        "white": "\033[1;37m",
        "reset": "\033[0m"
    }

    # Important details
    PAWNO_PATH = ["pawno", "pawncc.exe"]
    PAWN_EXT = ".pwn"
    PAWNC_EXT = ".amx"

    # User-defined paths
    SERVER_CFG_PATH = ["server", "server.cfg"]
    DATABASE_PATH = ["src", "database", "credentials.inc"]
    HTTP_PATH = ["src", "http", "credentials.inc"]

    # Useful methods that runner use to display information
    @staticmethod
    def throw_log(subject: str, content: Dict[Union[str, Any], str]) -> Dict[str, str]:
        """
        This method will be used to display an special message with content as response

        Args:
            subject (str): The subject of the message
            content (Dict[Union[str, Any], str]): The content of the message
        
        Returns:
            Dict[str, str]: The message as response
        """
        contains = { "message": subject, "contains": content }
        output_file = open("logs.json", "w")
        dump(contains, output_file, indent=4)
        return print(contains)

    @staticmethod
    def message(color: str, message: str, icon: str = "✅") -> None:
        """
        This method will be used to display a message with a specific color

        Args:
            color (str): The color of the message
            message (str): The message to display
            icon (str, optional): The icon of the message. Defaults to "✅".
        """
        print(f"{Utilities.COLORS[color]}{icon} | {message} {Utilities.COLORS['reset']}")