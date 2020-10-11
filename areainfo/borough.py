from dataclasses import dataclass


@dataclass
class Borough:
    name: str
    is_inner: bool
    rightmove_code: str
