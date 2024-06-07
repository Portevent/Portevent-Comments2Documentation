"""
Parser abstract class
"""
from abc import ABC
from pathlib import Path
from typing import List

from code_parser.structure.class_ import Class


class ParsingError(Exception):
    """
    Custom error, that can be linked to a certain line in a file
    """
    def __init__(self, message: str, line: str = "", line_number: int = None, file: str = ""):
        super().__init__(message)

        self.line = line
        self.line_number = line_number
        self.file = file


# pylint: disable=too-few-public-methods
class Parser(ABC):
    """
    Parse file an extract code
    """

    def __init__(self, parameters: dict = None):
        self.parameters = parameters or {}

    def parse(self, file: Path, encoding="utf-8") -> List[Class]:
        """
        Open a file and parse its content
        @param file: Path to the code
        @param encoding: Encoding, default is utf-8
        @return: List of classes
        """
        with open(file, 'r', encoding=encoding) as f:
            try:
                return self._parse(f.readlines())
            except ParsingError as e:
                e.file = file.name
                raise e

    def _parse(self, lines: List[str]) -> List[Class]:
        raise NotImplementedError
