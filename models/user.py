from dataclasses import dataclass
from models.base import Base


@dataclass
class UserDTC(Base):
    email: str = None
    password: str = None
