import sqlite3

from db_management.sql_queries_create_tables import URL


class DB:
    def __init__(self, url=URL):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def execute_sql_query(self, sql_query: str):
        self.cursor.execute(sql_query)
        self.connection.commit()

        print('Query executed')

    def drop_table(self, table: str):
        sql_query = f"DROP TABLE IF EXISTS {table};"
        self.execute_sql_query(sql_query=sql_query)

#    def add_values_to_transmission_table(self, **kwargs):
#        transmission = kwargs.get('transmission', '5 gears')
#        transmission_type = kwargs.get('transmission_type', 'Automatic')

#        sql_query = f"""
#        INSERT INTO transmission (transmission, transmission_type)
#        VALUES ("{transmission}", "{transmission_type}");
#        """
#        self.execute_sql_query(sql_query=sql_query)

#    def add_values_to_engine_table(self, **kwargs):
#        engine_type = kwargs.get('engine_type', '5.0L')
#        cc_displacement = kwargs.get('cc_displacement', 5000)
#        power_bhp = kwargs.get('power_bhp', 200)
#        torque_nm = kwargs.get('torque_nm', 300)
#        fuel_type = kwargs.get('fuel_type', 'Petrol')

#        sql_query = f"""
#        INSERT INTO engine (engine_type, cc_displacement, power_bhp, torque_nm, fuel_type)
#        VALUES ("{engine_type}", "{cc_displacement}", "{power_bhp}", "{torque_nm}", "{fuel_type}");
#        """
#        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_market_table(self, **kwargs):
        price = kwargs.get('price', 65700)
        make_year = kwargs.get('make_year', 2017)
        color = kwargs.get('color', 'silver')
        mileage_run = kwargs.get('mileage_run', 44444)
        no_of_owners = kwargs.get('no_of_owners', '1st')
        model_id = kwargs.get('model_id', 1)

        sql_query = f"""
        INSERT INTO market (price, make_year, color, mileage_run, no_of_owners, model_id) 
        VALUES ("{price}", "{make_year}", "{color}", "{mileage_run}", "{no_of_owners}", "{model_id}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_model_type_table(self, **kwargs):
        make = kwargs.get('make', 'VW')
        body_type = kwargs.get('body_type', 'sedan')
        seating_capacity = kwargs.get('seating_capacity', 5)
        fuel_tank_capacity = kwargs.get('fuel_tank_capacity', 45)

        sql_query = f"""
        INSERT INTO model_type (make, body_type, seating_capacity, fuel_tank_capacity)
        VALUES ("{make}", "{body_type}", "{seating_capacity}", "{fuel_tank_capacity}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_model_table(self, **kwargs):
        car_name = kwargs.get('car_name', 'Volkswagen Ameo')
        mileage_kmpl = kwargs.get('mileage_kmpl', 'Ameo')
        model = kwargs.get('model', 5)
        model_type_id = kwargs.get('model_type_id', 1)
        transmission_id = kwargs.get('transmission_id', 1)
        engine_id = kwargs.get('engine_id', 1)
        emission = kwargs.get('emission', 'BS IV')

        sql_query = f"""
        INSERT INTO model (car_name, mileage_kmpl, model, model_type_id, transmission_id, engine_id, emission)
        VALUES ("{car_name}", "{mileage_kmpl}", "{model}", "{model_type_id}", "{transmission_id}", "{engine_id}", "{emission}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def close_connection(self):
        self.connection.close()

