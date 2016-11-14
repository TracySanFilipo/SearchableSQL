import psycopg2


conn = psycopg2.connect("dbname=animals user=TracySanFilipo host=/tmp/")


cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS species (id serial PRIMARY KEY, scientific_name VARCHAR(40) NOT NULL, common_name VARCHAR(25) NOT NULL, current_population INTEGER, historic_population INTEGER, historic_year INTEGER, percent_decline float, native_range VARCHAR(60), last_updated DATE, sci_kingdom VARCHAR(30), sci_phylum VARCHAR(30), sci_class VARCHAR(30), sci_order VARCHAR(30), sci_family varchar(30), pop_trend VARCHAR(15), upper_weight INTEGER, weight_units VARCHAR(12), unique (scientific_name, common_name));""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Camelus ferus', 'Wild Bactrian Camel', 950, 1200, 1980, 20, 'China, Mongolia', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Cetartiodactyla', 'Camelidae', 'Decreasing', 450, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Acinonyx jubatus', 'Cheetah', 9000, 100000, 1900, 91, 'Africa, Asia', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Felidae', 'Decreasing', 72, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Pan troglodytes', 'Chimpanzee', 150000, 1000000, 1950, 85, 'Africa', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Primates', 'Hominidae', 'Decreasing', 65, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Pan paniscus', 'Bonobo', 30000, 60000, 1980, 50, 'Africa', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Primates', 'Hominidae', 'Decreasing', 60, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Gymnogyps californianus', 'Calafornia Condor', 435, 1000, 1900, 56, 'North America', '2016-11-11', 'Animalia', 'Chordata', 'Aves', 'Cathartiformes', 'Cathartidae', 'Increasing', 12, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Platanista gangetica', 'South Asian River Dolphin', 1000, 5000, 1982, 80, 'Asia', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Cetartiodactyla', 'Platanistidae', 'Unknown', 89, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Elephas maximus', 'Asian Elephant', 40000, 100000, 1900, 40, 'Asia', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Proboscidea', 'Elephantidae', 'Decreasing', 7000, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Loxodonta africana', 'African Elephant', 470000, 2000000, 1900, 76, 'Africa', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Proboscidea', 'Elephantidae', 'Increasing', 7000, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Ursus maritimus', 'Polar Bear', 20000, 25000, 1990, 5, 'North America, Greenland, Europe', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Ursidae', 'Unknown', 700, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Bison bison', 'American Bison', 30000, 60000000, 1700, 99, 'North America', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Cetartiodactyla', 'Bovidae', 'Stable', 1000, 'kg')""")


cur.execute("""INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES ('Panthera uncia', 'Snow Leopard', 5000, 7500, 2000, 33, 'Asia, Europe', '2016-11-11', 'Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Felidae', 'Decreasing', 55, 'kg')""")


conn.commit()


cur.close()


conn.close()
