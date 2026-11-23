"""Build a day-10 prediction cohort from six invented timelines.

Study days are integers. Prediction is at the end of day 10.
All deaths and last contacts in this example are ascertained retrospectively.
"""

from dataclasses import dataclass
from typing import Optional, Tuple

LANDMARK = 10
HORIZON = 20


@dataclass(frozen=True)
class Lab:
    draw_day: int
    release_day: Optional[int]
    value: float


@dataclass(frozen=True)
class Timeline:
    case: str
    last_contact: int
    death: Optional[int] = None
    labs: Tuple[Lab, ...] = ()


CASES = (
    Timeline("A", 22, labs=(Lab(6, 8, 4.0), Lab(9, 12, 7.0))),
    Timeline("B", 16, death=16, labs=(Lab(8, 11, 8.0),)),
    Timeline("C", 15, labs=(Lab(7, None, 5.0),)),
    Timeline("D", 10, death=10),
    Timeline("E", 8),
    Timeline("F", 20, labs=(Lab(10, 10, 6.0),)),
)


def landmark_row(person):
    """Return the latest eligible lab and the later outcome for one timeline."""
    if person.death is not None and person.death <= LANDMARK:
        return None
    # A later recorded death also establishes survival through the landmark.
    if person.death is None and person.last_contact < LANDMARK:
        return None

    available = [lab for lab in person.labs
                 if lab.release_day is not None
                 and lab.draw_day <= lab.release_day <= LANDMARK]
    # Draw day determines recency. The fixture has one result per draw.
    latest = max(available, key=lambda lab: lab.draw_day, default=None)
    if person.death is not None:
        outcome = "died" if person.death <= HORIZON else "alive"
    elif person.last_contact >= HORIZON:
        outcome = "alive"
    else:
        outcome = "unknown"
    return person.case, latest.value if latest else None, outcome


def main():
    print("Case | Lab available on day 10 | Status at day 20")
    for person in CASES:
        row = landmark_row(person)
        if row is not None:
            case, value, outcome = row
            print(f"{case} | {value if value is not None else 'missing'} | {outcome}")


if __name__ == "__main__":
    main()
