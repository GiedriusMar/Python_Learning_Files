URL = 'database/mano_duomenu_baze.db'

TRANSMISSION_TABLE = """
CREATE TABLE IF NOT EXISTS transmission (
transmission_id INTEGER PRIMARY KEY,
transmission char,
transmission_type char);
"""

ENGINE_TABLE = """
CREATE TABLE IF NOT EXISTS engine (
engine_id INTEGER PRIMARY KEY,
engine_type char,
cc_displacement INTEGER,
power_bhp INTEGER,
torque_nm INTEGER,
fuel_type char);
"""


MODEL_TYPE_TABLE = """
CREATE TABLE IF NOT EXISTS model_type (
model_type_id INTEGER PRIMARY KEY,
make char,
body_type char,
seating_capacity INTEGER,
fuel_tank_capacity INTEGER);
"""


MODEL_TABLE = """
CREATE TABLE IF NOT EXISTS model (
model_id INTEGER PRIMARY KEY,
car_name char,
mileage_kmpl INTEGER,
model char,
model_type_id INTEGER,
transmission_id INTEGER,
engine_id INTEGER,
emission char
);
"""


MARKET_TABLE = """
CREATE TABLE IF NOT EXISTS market (
market_id INTEGER PRIMARY KEY,
price INTEGER,
make_year INTEGER,
color char,
mileage_run INTEGER,
no_of_owners char,
model_id INTEGER
);
"""

TABLES = [MARKET_TABLE]
# DROP_TABLES = ['transmission', 'engine', 'model_type', 'model', 'market']