#!/usr/bin/python3
"""
insurance module
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from models.base_model import BaseModel, Base
import sys
sys.path.insert(0, '..')


class Insurance(BaseModel, Base):
    """
        insurance details
    """
    __tablename__ = "insurance"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    insuranceID = Column(String(128), nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)

