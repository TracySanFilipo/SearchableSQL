import psycopg2


conn = psycopg2.connect("dbname=animals user=TracySanFilipo host=/tmp/")


cur = conn.cursor()


def display_table(cells):
    whole_table = cells
    headinglist = ['Scientific name', 'Common name', 'Pop', 'Ref Pop', 'Ref Year', 'Drop', 'Geo Range', 'Updated', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Trend', 'Weight', 'Unit']
    widths = [18, 19, 7, 10, 8, 5, 10, 10, 8, 8, 8, 12, 9, 10, 7, 5]
    vert = '|'
    horizontal = '+'
    for w in widths:
        vert += " %-"+"%ss |" % (w,)
        horizontal += '-'*w + '--+'
    print(horizontal)
    print(vert % tuple(headinglist))
    print(horizontal)
    for row in whole_table:
        print(vert % tuple(row))
        print(horizontal)


def view_whole_table():
    vwtsql = "SELECT * FROM species"
    cur.execute(vwtsql)
    whole_table = cur.fetchall()
    print(whole_table)
    headinglist = ['Scientific name', 'Common name', 'Pop', 'Ref Pop', 'Ref Year', 'Drop', 'Geo Range', 'Updated', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Trend', 'Weight', 'Unit']
    widths = [18, 19, 7, 10, 8, 5, 10, 10, 8, 8, 8, 12, 9, 10, 7, 5]
    vert = '|'
    horizontal = '+'
    for w in widths:
        vert += " %-"+"%ss |" % (w,)
        horizontal += '-'*w + '--+'
    print(horizontal)
    print(vert % tuple(headinglist))
    print(horizontal)
    for row in whole_table:
        print(vert % tuple(row))
        print(horizontal)

def search_by_common_name():
    while True:
        interest_name = str(input("Please enter a name to search for: "))
        ifsql = "SELECT common_name FROM species WHERE common_name = %s"
        if cur.execute(ifsql, (interest_name,)):
            ifsql2 = "SELECT scientific_name AS Scientific_name, common_name AS Common_name, current_population AS Current_Population_Estimate, historic_population AS Earlier_Reference_Estimated_Population, historic_year AS Approximate_Year_of_Reference_Population, percent_decline AS Percent_Drop_between_Current_and_Reference_Populations, native_range AS General_Region_Species_From, last_updated AS Date_Data_Last_Updated, sci_kingdom AS Kingdom, sci_phylum AS Phylum, sci_class AS Class, sci_order AS Order, sci_family AS Family, pop_trend AS Trend, upper_weight AS Maximum_Weight, weight_units AS Unit FROM species WHERE common_name = %s"
            cur.execute(ifsql2, (interest_name,))
            namecells = cur.fetchall()
            display_table(namecells)
            break
        else:
            print("That is not currently in the database.")


def search_by_sci_name():
    while True:
        interest_sci_name = input("Please enter a scientific name to search for: ")
        ifsql3 = "SELECT scientific_name FROM species WHERE scientific_name = %s"
        if cur.execute(ifsql3, (interest_sci_name,)):
            ifsql4 = "SELECT scientific_name AS 'Scientific name', common_name AS 'Common name', current_population AS 'Current Population Estimate', historic_population AS 'Earlier Reference Estimated Population', historic_year AS 'Approximate Year of Reference Population', percent_decline AS 'Percent Drop between Current and Reference Populations', native_range AS 'General Region Species From', last_updated AS 'Date Data Last Updated', sci_kingdom AS Kingdom, sci_phylum AS Phylum, sci_class AS Class, sci_order AS Order, sci_family AS Family, pop_trend AS Trend, upper_weight AS 'Maximum Weight', weight_units AS Unit FROM species WHERE scientific_name = %s"
            cur.execute(ifsql4, (interest_sci_name,))
            scinamecells = cur.fetchall()
            display_table(scinamecells)
            break
        else:
            print("That is not currently in the database.")


def searchlist():
    while True:
        interest = input("Please choose to search by common name (name), "
                         "to search by scientific name (sci), "
                         "or to view all records (all): ")
        if interest.lower() == "all":
            view_whole_table()
            break
        elif interest.lower() == "name":
            search_by_common_name()
            break
        elif interest.lower() == "sci":
            search_by_sci_name()
            break
        else:
            print("That is not a valid selection.")


def add_row():
    while True:
        speciesadd = input("Enter scientific name of species: ")
        commonadd = input("Enter the common name of the species: ")
        current_popadd = int(input("Enter the current population of the "
                                   "species: "))
        histpopadd = int(input("Enter the historical population of the "
                               "species: "))
        histyear = int(input("Enter a four digit year associated with the"
                             " historical population: "))
        percentdecline = float(input("Subtract the current population from the"
                                     " historical population, then divide this"
                                     " by the historical population, and enter"
                                     " that number: "))
        range_of_species = input("Enter the native range of the species: ")
        dateadded = input("Enter today's date as year-month-day: ")
        kingdom_species = input("Enter the Kingdom the species is in: ")
        phylum_species = input("Enter the Phylum the species is in: ")
        class_species = input("Enter the Class the species is in: ")
        order_species = input("Enter the Order the species is in: ")
        family_species = input("Enter the Family the species is in: ")
        trend_of_pop = input("Enter whether the population tred is increasing,"
                             " decreasing, stable, or unknown: ")
        max_weight = int(input("Enter the maximum number of kilograms a member"
                               " of the species might weigh, or an integer of "
                               "another unit that could accuratly represent "
                               "this weight: "))
        weight_unit = input("Enter kg if kilograms were just used, or the "
                            "alternate unit chosen if applicable: ")
        sqlif6 = "SELECT scientific_name FROM species WHERE scientific_name = %s"
        if cur.execute(sqlif6, (speciesadd,)):
            print("That species is already in the database.")
        else:
            sqlinsert = "INSERT INTO species (scientific_name, common_name, current_population, historic_population, historic_year, percent_decline, native_range, last_updated, sci_kingdom, sci_phylum, sci_class, sci_order, sci_family, pop_trend, upper_weight, weight_units) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sqlinsert, (speciesadd, commonadd, current_popadd, histpopadd, histyear, percentdecline, range_of_species, dateadded, kingdom_species, phylum_species, class_species, order_species, family_species, trend_of_pop, max_weight, weight_unit))
            addedcells = cur.fetchall()
            display_table(addedcells)

def see_top_declines():
    cur.execute("SELECT * from species ORDER BY percent_decline DESC")
    orderedcells = cur.fetchall()
    display_table(orderedcells)


def edit_rows():
    row_to_edit = input("Provide the full species name that you wish to"
                        " update: ")
    today = input("Enter today's date as year-month-day: ")
    current_number = int(input("Enter the current population of the species as"
                               " an integer: "))
    per_decline = float(input("Enter the result of the following calucation as"
                              " an interger: ((The historic population - the "
                              "current population) divided by the historic "
                              "population) multiplied by 100: "))
    population_trend = input("Enter whether the population tred is increasing,"
                             " decreasing, stable, or unknown: ")
    sqlif7 = "SELECT scientific_name FROM species WHERE scientific_name = %s;"
    if cur.execute(sqlif7, (row_to_edit,)):
        sqlif8 = "UPDATE species SET current_population = %s, last_updated = %s, percent_decline = %s, pop_trend = %s WHERE scientific_name = %s"
        cur.execute = (sqlif8, (current_number, today, per_decline, population_trend, row_to_edit))
        editedcells = cur.fetchall()
        display_table(editedcells)
    else:
        print("That species is not yet in the database.")


def main():
    while True:
        selection = input("Please choose to search (s), append (a), view a "
                          "desending list of percent declines (v),"
                          " update data (u), or exit (e): ")
        if selection.lower() == 's' or selection.lower() == "search":
            searchlist()
        elif selection.lower() == 'a' or selection.lower() == 'append':
            add_row()
        elif selection.lower() == 'v' or selection.lower() == 'view':
            see_top_declines()
        elif selection.lower() == 'u' or selection.lower() == 'update':
            edit_rows()
        elif selection.lower() == 'e' or selection.lower() == 'exit':
            exit()
        else:
            print("That is not a recognized selection.")
            continue
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
