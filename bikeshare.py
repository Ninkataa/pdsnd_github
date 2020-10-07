import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('For which city you would like to see statistics(chicago, new york city, washington): ')
        if city.lower() in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Please enter correct data.')


    # TO DO: get user input for month (all, january, february, ... , june    )
    while True:
        month = input('For which month you would like to see statistics(all, january, february, ... , june): ')
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Please enter correct data.')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('For which day of the week you would like to see statistics(all, monday, tuesday, ... sunday): ')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Please enter correct data.')



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print('The most common day of the week is: {}'.format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print('The most common start hour is: {}'.format(df['Start Time'].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is: {}'.format((df['Start Station'] + ' - ' +  df['End Station']).mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: {}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('Mean travel time is: {}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types is:\n{}'.format(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    try:
        print('\nCount per gender is:\n{}'.format(df['Gender'].value_counts()))


        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth is: {}'.format(int(df['Birth Year'].min())))
        print('Most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
        print('Most common year of birth is: {}'.format(int(df['Birth Year'].mode()[0])))
    except:
        print('\nNo gender and year of birth data available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_raw(df):
    """Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'."""

    row = 0
    while True:

        if row >= len(df.index):
            break

        raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')

        if raw_data.lower() != 'yes':
            break
        else:
            print(df[row: (row+5)])
            row += 5



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
