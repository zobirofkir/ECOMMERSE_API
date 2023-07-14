from pydantic import BaseModel

class Diapering_Changings(BaseModel):
    Disposable_diapers:str
    Cloth_diapers:str
    Diaper_rash_creams:str
    Changing_mats_or_pads:str
    Diaper_bags:str



class Feeding_and_Nursings(BaseModel):
    Baby_bottles :str
    Breast_pumps :str
    Formula_milk :str
    Nursing_pillows :str
    Bottle_sterilizers :str
    Baby_food_makers :str


class Bathing_and_Groomings(BaseModel):
    Baby_bathtubs :str
    Baby_shampoo_and_body_wash :str
    Hooded_towels :str
    Baby_brushes_and_combs :str
    Nail_clippers :str
    Baby_lotion_and_oil :str


class Clothing_and_Accessoriess(BaseModel):
    Onesies_and_bodysuits :str
    Baby_pajamas :str
    Socks_and_booties :str
    Hats_and_mittens :str
    Bibs_and_burp_cloths :str
    Baby_blankets :str


class Nursery_and_Sleeps(BaseModel):
    Baby_cribs :str
    Bassinets :str
    Changing_tables :str
    Baby_monitors :str
    Swaddles_and_sleep_sacks :str
    Mobiles_and_nightlights :str




class Safety_and_Healths(BaseModel):
    Baby_gates :str
    Outlet_covers :str
    Cabinet_locks :str
    Baby_thermometers :str
    Nasal_aspirators :str
    Baby_first_aid_kits :str


class Travel_and_Transportations(BaseModel):
    Strollers :str
    Car_seats :str
    Baby_carriers :str
    Diaper_backpacks :str
    Travel_cribs :str
    Portable_high_chairs :str



class Toys_and_Entertainments(BaseModel):
    Rattles_and_teethers :str
    Soft_toys :str
    Activity_gyms :str
    Musical_toys :str
    Books_for_infants :str
    Stacking_toys :str


class Descriptionss(BaseModel):
    username:str
    email:str
    descriptions:str



class Productss(BaseModel):
    name :str
    category :str
    photos :str
    video :str
    prix :int


class Userss(BaseModel):
    username:str
    email:str
    password:str

