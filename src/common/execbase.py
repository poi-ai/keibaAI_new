from access import Access
from db import Db
from entity import Entity
from base import Base

class ExecBase(Base):
    def __init__(self):
        self.access = Access()
        self.db = Db()
        self.entity = Entity()
