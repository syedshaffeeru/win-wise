from dataclasses import asdict, dataclass

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
class Match:
    """
    Data model for cricket match details.
    """
    match_id: str  # Unique identifier for the match.
    name: str  # Name of the match (e.g., "Pakistan A vs West Indies, 3-day Warm-up Match").
    match_type: str  # Type of match (e.g., "test", "odi", "t20").
    status: str  # Current status of the match (e.g., "Match not started").
    venue: str  # Venue where the match is being played.
    date: str  # Date of the match.
    datetime_gmt: str  # Match date and time in GMT.
    teams: list  # List of teams playing in the match.
    series_id: str  # ID of the series to which this match belongs.
    fantasy_enabled: bool  # Indicates if fantasy cricket is enabled for this match.
    bbb_enabled: bool  # Indicates if ball-by-ball updates are enabled.
    has_squad: bool  # Indicates if squads have been announced for the match.
    match_started: bool  # Indicates if the match has started.
    match_ended: bool  # Indicates if the match has ended.

    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        """
        Create an instance from a dictionary.

        :param data: (dict) Dictionary containing match information.
        :return: (Match) An instance of the Match class.
        """
        return cls(
            match_id=data.get("id"),
            name=data.get("name"),
            match_type=data.get("matchType"),
            status=data.get("status"),
            venue=data.get("venue"),
            date=data.get("date"),
            datetime_gmt=data.get("dateTimeGMT"),
            teams=data.get("teams", []),
            series_id=data.get("series_id"),
            fantasy_enabled=data.get("fantasyEnabled", False),
            bbb_enabled=data.get("bbbEnabled", False),
            has_squad=data.get("hasSquad", False),
            match_started=data.get("matchStarted", False),
            match_ended=data.get("matchEnded", False)
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
