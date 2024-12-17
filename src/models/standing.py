from dataclasses import dataclass


@dataclass
class Standing:
    """Standing dataclass"""
    position: int
    driver: str
    nationality: str
    constructor: str
    points: int
