from dataclasses import asdict, dataclass,field
from typing import List, Optional

@dataclass
class Series:
    """
    Data model for cricket series details.
    """
    series_id: str  # Unique identifier for the series.
    name: str  # Name of the series (e.g., "England tour of Ireland, 2025").
    start_date: str  # Start date of the series (e.g., "2025-09-17").
    end_date: str  # End date of the series (e.g., "2025-09-21").
    odi: int  # Number of ODI matches in the series.
    t20: int  # Number of T20 matches in the series.
    test: int  # Number of Test matches in the series.
    squads: int  # Indicates if squads are announced (1 = Yes, 0 = No).
    matches: int  # Total number of matches in the series.

    @classmethod
    def from_dict(cls, data: dict) -> "Series":
        """
        Create an instance from a dictionary.
        
        :param data: (dict) Dictionary containing series information.
        :return: (Series) An instance of the Series class.
        """
        return cls(
            series_id=data.get("id"),
            name=data.get("name"),
            start_date=data.get("startDate"),
            end_date=data.get("endDate"),
            odi=data.get("odi", 0),
            t20=data.get("t20", 0),
            test=data.get("test", 0),
            squads=data.get("squads", 0),
            matches=data.get("matches", 0)
        )

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.
        
        :return: (dict) Dictionary representation of the Series object.
        """
        return asdict(self)


@dataclass
class Score:
    """
    Represents the score of a specific inning in a cricket match.
    """
    r: int  # Runs scored
    w: int  # Wickets lost
    o: float  # Overs played
    inning: str  # Description of the inning (e.g., "Western Australia Inning 1")

    @classmethod
    def from_dict(cls, data: dict) -> "Score":
        """
        Create an instance of Score from a dictionary.

        :param data: (dict) Dictionary containing score information.
        :return: (Score) An instance of the Score class.
        """
        return cls(
            r=data.get("r"),
            w=data.get("w"),
            o=data.get("o"),
            inning=data.get("inning")
        )
    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: (dict) Dictionary representation of the Score object.
        """
        return asdict(self) 




@dataclass
class Match:
    """
    Data model for cricket match details.
    """
    match_id: str  # Unique identifier for the match.
    name: str  # Name of the match (e.g., "Western Australia vs New South Wales, Final").
    status: str  # Current status or result of the match.
    match_type: str  # Type of match (e.g., "odi", "t20", "test").
    venue: str  # Venue where the match was played.
    date: str  # Date of the match.
    datetime_gmt: str  # Match date and time in GMT (ISO format).
    teams: List[str]  # List of teams playing in the match.
    score: Optional[List[Score]] = field(default_factory=list)  # Scores for the innings.
    series_id: str  # ID of the series to which this match belongs.
    fantasy_enabled: bool = False  # Indicates if fantasy cricket is enabled for this match.

    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        """
        Create an instance of Match from a dictionary.

        :param data: (dict) Dictionary containing match information.
        :return: (Match) An instance of the Match class.
        """
        return cls(
            match_id=data.get("id"),
            name=data.get("name"),
            status=data.get("status"),
            match_type=data.get("matchType"),
            venue=data.get("venue"),
            date=data.get("date"),
            datetime_gmt=data.get("dateTimeGMT"),
            teams=data.get("teams", []),
            score=[Score.from_dict(score) for score in data.get("score", [])],
            series_id=data.get("series_id"),
            fantasy_enabled=data.get("fantasyEnabled", False)
        )
    
    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: (dict) Dictionary representation of the Match object.
        """
        return asdict(self)


@dataclass
class Players:
    player_id: str #Player ID
    name: str #Player Name
    country: str #Player Country

    @classmethod
    def from_dict(cls, data: dict) -> "Players":
        """
        Create an instance from a dictionary.

        :param data: (dict) Dictionary containing match information.
        :return: (Match) An instance of the Player class.
        """
        return cls(
            player_id=data.get("id"),
            name=data.get("name"),
            country=data.get("country")
        )

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: (dict) Dictionary representation of the Match object.
        """
        return asdict(self)
