### Date created
Project created on 07.10.2020

### Project Title
Explore US Bikeshare Data

### Description
This project can assist you to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.

### Code Example
~~~~
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
~~~~

### Files used
Data files used:
    chicago.csv
    new_york_city.csv
    washington.csv

### Credits
Thank you Udacity for the really good training!
