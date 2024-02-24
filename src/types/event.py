import dataclasses


@dataclasses.dataclass
class Event:
    event_id: int
    args: tuple
