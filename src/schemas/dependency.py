from sqlalchemy import Engine
from dataclasses import dataclass


@dataclass
class Dependencies:
    db_engine: Engine
