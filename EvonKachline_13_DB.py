import matplotlib.pyplot as plt
import sqlite3

#Makes the name of the data base and the growth rate. 
DB_name = "population_EK.db"
Growth_rate = 0.02


def population_db():
#Creates a SQLite database.
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL,
            PRIMARY KEY (city, year)
        )
    """)

#The population of these cities in 2023.
    starting_population = [
        ("North Port", 2023, 88934),
        ("Fort Myers", 2023, 97372),
        ("Gainesville", 2023, 145812),
        ("Tallahassee", 2023, 196250),
        ("Cape Coral", 2023, 204788),
        ("Orlando", 2023, 310875),
        ("Tampa", 2023, 387450),
        ("Miami", 2023, 441713),
        ("Sarasota", 2023, 469013),
        ("Jacksonville", 2023, 955408),
         
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO population (city, year, population)
        VALUES (?, ?, ?)
    """, starting_population)

    conn.commit()
    conn.close()


def population_growth():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()


    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    data = cursor.fetchall()

#Calculate population growth for 20 years for each of the cites. 
    for city, population in data:
        new_population = population
        for year in range(2024, 2044):
#Calculate the population for each year.
            new_population = int(new_population * (1 + Growth_rate))

            cursor.execute("""
                INSERT OR IGNORE INTO population (city, year, population)
                VALUES (?, ?, ?)
            """, (city, year, new_population))

    conn.commit()
    conn.close()


def plot_population_growth():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    # Get list of cities from the database
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    while True:
        # Display available cities for user selection
        print("\n 10 Flordia Cities:")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")

        # Prompt user to select a city or exit
        choice = input("Select a city by number (type '0' when done): ").strip().lower()

        if choice == '0':
            break

        # Validate user input
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(cities):
            print("Invalid choice. Please try again.")
            continue

        # Retrieve the city based on the user's choice
        city = cities[int(choice) - 1]

        # Fetch population data for the selected city
        cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (city,))
        data = cursor.fetchall()

        # Extract years and population values for plot
        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        # Plot the population growth for the selected city
        plt.figure(figsize=(10, 6))  # Set figure size for better readability
        plt.plot(years, populations, marker='o')  # Use marker plot to emphasize individual data points
        plt.title(f"Population Growth for {city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()

    conn.close()


def main():
    # Initialize the database and populate initial data
    population_db()

    # Simulate 20 years of population growth
    population_growth()
    plot_population_growth()


main()
