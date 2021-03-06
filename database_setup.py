import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

########################## TABLES ###################################

class Ware(Base):
	__tablename__ = 'ware'
	name = Column(String(20), nullable=False)
	id = Column(String(3),primary_key=True)
	image = Column(String(200), nullable=False)


class Product(Base):
	__tablename__ = 'product'
	
	name = Column(String(500), nullable=False)
	catagory = Column(Integer, ForeignKey('ware.id'))
	ware = relationship(Ware)
	id = Column(String(6), primary_key=True)
	size = Column(String(50), nullable=False)
	material = 'stainless steel'
	price = Column(Integer, nullable=False)
	polish = Column(String(500), nullable=False)
	image = Column(String(200), nullable=False)
# We added this ser function to be able to send JSON objects in a
# serializable format
	@property
	def ser(self):

		return {
			'name': self.name,
			'id': self.id,
			'catagory': self.catagory,
			'size': self.size,
			'material': self.material,
			'price': self.price,
			'polish': self.polish,
			'image': self.image,
		}

class Event(Base):
	__tablename__ = 'event'

	name = Column(String(15), nullable=False)
	id = Column(Integer, primary_key=True)
	location = Column(String(15), nullable=False)
	month = Column(String(10), nullable=False)
	year = Column(String(5), nullable=False)
	image = Column(String(200), nullable=False)

class Bestseller(Base):
	__tablename__ = 'best'
	name = Column(String(500), primary_key=True)
	product_id = Column(String(6), ForeignKey('product.id'))
	product = relationship(Product)

class Catalog(Base):
	__tablename__ = 'catalog'
	id = Column(Integer,primary_key=True)
	image = Column(String(200), unique=True)
##############################################################################################


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))

# We added this ser function to be able to send JSON objects in a
# serializable format
	@property
	def ser(self):

		return {
			'name': self.name,
			'id': self.id,
		}


class Restaurant(Base):
	__tablename__ = 'restaurant'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	@property
	def ser(self):

		return {
			'name': self.name,
			'id': self.id,
		}
	

class MenuItems(Base):
	__tablename__ = 'menu_item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey(Restaurant.id))
	restaurant = relationship(Restaurant)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	@property
	def serialize(self):

		return {
			'name': self.name,
			'description': self.description,
			'id': self.id,
			'price': self.price,
			'course': self.course,
		}


	
	
############################# INIT ################################

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.create_all(engine)
