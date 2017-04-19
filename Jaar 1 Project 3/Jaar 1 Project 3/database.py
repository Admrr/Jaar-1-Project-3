import psycopg2

class Database:  
    def interact_with_database(command):
        connection = psycopg2.connect(host = "localhost", dbname = "Jaar 1 Project 3", user = "postgres", password = "DatThaBeast3636")
        cursor = connection.cursor()
        # Execute the command
        cursor.execute(command)
        connection.commit()
        # Save results
        results = None
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:
            # Nothing to fetch
            pass
        # Close connection
        cursor.close()
        connection.close()
        return results

    def get_crime_data(result, jaar, wijk):
        return Database.interact_with_database("SELECT " + str(result) + " FROM criminaliteit WHERE jaar = " + str(jaar) + " AND wijk = " + str(wijk))[0][0]

    def politie_coordinaten():
        return Database.interact_with_database("SELECT X, Y FROM politiebureaus")

    def get_areas(tabel):
        return Database.interact_with_database("SELECT DISTINCT(wijk) FROM " + str(tabel))

    def get_metro_info(wijk):
        return Database.interact_with_database("SELECT wijkoppervlakte_km2, aantal_stations FROM metro WHERE wijk = " + str(wijk))

    def metro_coordinaten():
        return Database.interact_with_database("SELECT X, Y FROM metrostations")

    def get_police_data(wijk):
        return Database.interact_with_database("SELECT COUNT(politiebureau) FROM politiebureaus WHERE wijk = " + str(wijk))[0][0]

    def get_markt_data():
        return Database.interact_with_database("SELECT m.wijk, m.aantal_markten, COUNT(p.wijk) FROM markten m, parkeerautomaten p WHERE m.wijk = p.wijk GROUP BY m.wijk, m.aantal_markten")

    def markt_coordinaten():
        return Database.interact_with_database("SELECT X, Y FROM marktlocaties")