'''
Models
'''

import dataclasses
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Table)
from db import engine

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)

@dataclasses.dataclass
class User(Base):
    '''
    User model (linked to projects via association table)
    '''
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    projects = relationship('Project',
        secondary=association_table,
        back_populates='users')

@dataclasses.dataclass
class Profile(Base):
    '''
    Profile model (linked to user)
    '''
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    bio = Column(String(255), nullable=False, unique=True)
    phone = Column(String(255), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship('User', backref='profile', uselist=False)


@dataclasses.dataclass
class Project(Base):
    '''
    Project model (linked to users via association table)
    '''
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=False, unique=True)
    users = relationship('User',
        secondary=association_table,
        back_populates='project')

@dataclasses.dataclass
class Task(Base):
    '''
    Task modedel (linked to project)
    '''
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    status = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey('projects.id'), unique=True)
    project = relationship('Project', backref='task', uselist=False)

Base.metadata.create_all(engine)
