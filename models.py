from database import engine, Base
from sqlalchemy import Column, String, Integer

class Diapering_and_Changing(Base):
    __tablename__='Diapering_ and_Changingse'
    id = Column(Integer, primary_key=True)
    Disposable_diapers = Column(String, nullable=False)
    Cloth_diapers = Column(String, nullable=False)
    Diaper_rash_creams = Column(String, nullable=False)
    Changing_mats_or_pads = Column(String, nullable=False)
    Diaper_bags = Column(String, nullable=False)


class Feeding_and_Nursing(Base):
    __tablename__="Feeding_and_Nursingse"
    id = Column(Integer, primary_key=True)
    Baby_bottles = Column(String, nullable=False)
    Breast_pumps = Column(String, nullable=False)
    Formula_milk = Column(String, nullable=False)
    Nursing_pillows = Column(String, nullable=False)
    Bottle_sterilizers = Column(String, nullable=False)
    Baby_food_makers = Column(String, nullable=False)


class Bathing_and_Grooming(Base):
    __tablename__="Bathing_and_Groomingse"
    id = Column(Integer, primary_key=True)
    Baby_bathtubs = Column(String, nullable=False)
    Baby_shampoo_and_body_wash = Column(String, nullable=False)
    Hooded_towels = Column(String, nullable=False)
    Baby_brushes_and_combs = Column(String, nullable=False)
    Nail_clippers = Column(String, nullable=False)
    Baby_lotion_and_oil = Column(String, nullable=False)
    
class Clothing_and_Accessories(Base):
    __tablename__='Clothing_and_Accessoriesse'
    id = Column(Integer, primary_key=True)
    Onesies_and_bodysuits = Column(String, nullable=False)
    Baby_pajamas = Column(String, nullable=False)
    Socks_and_booties = Column(String, nullable=False)
    Hats_and_mittens = Column(String, nullable=False)
    Bibs_and_burp_cloths = Column(String, nullable=False)
    Baby_blankets = Column(String, nullable=False)

class Nursery_and_Sleep(Base):
    __tablename__="Nursery_and_Sleepse"
    id = Column(Integer, primary_key=True)
    Baby_cribs = Column(String, nullable=False)
    Bassinets = Column(String, nullable=False)
    Changing_tables = Column(String, nullable=False)
    Baby_monitors = Column(String, nullable=False)
    Swaddles_and_sleep_sacks = Column(String, nullable=False)
    Mobiles_and_nightlights = Column(String, nullable=False)

class Safety_and_Health(Base):
    __tablename__="Safety_and_Healthse"
    id = Column(Integer, primary_key=True)
    Baby_gates = Column(String, nullable=False)
    Outlet_covers = Column(String, nullable=False)
    Cabinet_locks = Column(String, nullable=False)
    Baby_thermometers = Column(String, nullable=False)
    Nasal_aspirators = Column(String, nullable=False)
    Baby_first_aid_kits = Column(String, nullable=False)

class Travel_and_Transportation(Base):
    __tablename__="Travel_and_Transportationse"
    id = Column(Integer, primary_key=True)
    Strollers = Column(String, nullable=False)
    Car_seats = Column(String, nullable=False)
    Baby_carriers = Column(String, nullable=False)
    Diaper_backpacks = Column(String, nullable=False)
    Travel_cribs = Column(String, nullable=False)
    Portable_high_chairs = Column(String, nullable=False)



class Toys_and_Entertainment(Base):
    __tablename__='Toys_and_Entertainmentse'
    id = Column(Integer, primary_key=True)
    Rattles_and_teethers = Column(String, nullable=False)
    Soft_toys = Column(String, nullable=False)
    Activity_gyms = Column(String, nullable=False)
    Musical_toys = Column(String, nullable=False)
    Books_for_infants = Column(String, nullable=False)
    Stacking_toys = Column(String, nullable=False)




class Description(Base):
    __tablename__="Descriptionse"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    descriptions = Column(String, nullable=False)

class Product(Base):
    __tablename__="Productse"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    photos = Column(String, nullable=False)
    video = Column(String, nullable=False)
    prix = Column(Integer, nullable=False)


class User(Base):
    __tablename__='Usersse'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)




Base.metadata.create_all(bind=engine)

