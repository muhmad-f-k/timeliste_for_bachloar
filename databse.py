import os
import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, DATE, LargeBinary, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import UniqueConstraint
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_str = 'sqlite:///' + \
                 os.path.join(BASE_DIR, 'finaldata.db?check_same_thread=False')
engine = create_engine(connection_str)
base = declarative_base()


class User(base, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(200), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)



    @property
    def password(self):
        raise AttributeError('password is unreadable by humans ')

    @password.setter
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"{self.first_name} - {self.last_name} - {self.email} - {self.id}"

class Time_liste(base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    fra_dato = Column(DATE(), default=datetime.date.today(), nullable=False)
    til_dato = Column(DATE(), default=datetime.date.today(), nullable=False)
    type_arbeid = Column(String(255), nullable=False, unique=True)
    timer_per_type_arbeid = Column(String(255), nullable=False, unique=True)
    dato = Column(String(255), nullable=False, unique=True)
    start_tidspunkt =Column(DATE(), default=datetime.datetime.time(), nullable=False)
    slutt_tidspunkt = Column(DATE(), default=datetime.datetime.time(), nullable=False)
    antall_timer = Column(String(10), nullable=False)
    type_arbeid_forklaring = Column(String(255), nullable=False, unique=True)
    backlog_item = Column(String(10), nullable=False)
    oppsummering = Column(String(255), nullable=False, unique=True)












    def __repr__(self):
        return f"{self.name} - {self.id}"