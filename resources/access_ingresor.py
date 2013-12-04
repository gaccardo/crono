#!/usr/bin/env python

import sqlalchemy
import tldextract
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import insert 

engine = sqlalchemy.create_engine('mysql://crono:ppp123@localhost/crono')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Access(Base):

  __tablename__ = 'crono_access'
  id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
  time = sqlalchemy.Column(sqlalchemy.String)
  elapsed = sqlalchemy.Column(sqlalchemy.Integer)
  ip = sqlalchemy.Column(sqlalchemy.String)
  code = sqlalchemy.Column(sqlalchemy.String)
  data = sqlalchemy.Column(sqlalchemy.Integer)
  method = sqlalchemy.Column(sqlalchemy.String)
  url = sqlalchemy.Column(sqlalchemy.String)
  date = sqlalchemy.Column(sqlalchemy.String)

  def __repr__(self):
    return "<Access(ip='%s')>" % self.ip


class LastKey(Base):
  __tablename__ = 'crono_lastkey'
  id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
  time = sqlalchemy.Column(sqlalchemy.String)

  def __repr__(self):
    return "<LastKey(time='%s')>" % self.time


class SquidLogParser( object ):
    
  def get_last_key(self):
    q = session.query(LastKey).order_by(LastKey.id.desc()).first()
    return q.time
      
  def set_last_key(self, last_key):
    new_last_key = LastKey(time=last_key)
    session.add(new_last_key)
    session.commit()

  def add_access(self, access):
    session.add(access)

  def save_logs(self):
    file_pointer = open('access_real.log', 'r')
    file_buffer = file_pointer.readlines()
    file_pointer.close()

    last_key = 0

    for rawline in file_buffer:
      r = [line for line in rawline.split(' ') if line]
      if r[0] > self.get_last_key():
        url = tldextract.extract(r[6])
        access = Access(time=r[0], elapsed=r[1], ip=r[2], 
                code=r[3], data=r[4], method=r[5], 
                url='%s.%s' % (url.domain, url.suffix), date=datetime.datetime.now())
        self.add_access(access)
        last_key = r[0]

    if last_key != 0:
      self.set_last_key(last_key)
      session.commit()


if __name__ == '__main__':
  slp = SquidLogParser()
  slp.save_logs()
