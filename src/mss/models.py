"""This is part of the MSS Python's module.
Source: https://github.com/BoboTiG/python-mss.
"""

from typing import Any, NamedTuple

Monitor = dict[str, int]
Monitors = list[Monitor]

Window = dict[str, Any]
Windows = list[Window]

Pixel = tuple[int, int, int]
Pixels = list[tuple[Pixel, ...]]

CFunctions = dict[str, tuple[str, list[Any], Any]]
CConstants = dict[str, Any]


class Pos(NamedTuple):
    left: int
    top: int


class Size(NamedTuple):
    width: int
    height: int
