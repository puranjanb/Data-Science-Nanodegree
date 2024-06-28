import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
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
    city = input('Enter a city\t').strip()
    #checking whether city is a valid name
    while city.lower() not in CITY_DATA:
        city = input('Enter a valid city\t').strip()
    city = city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter a month\t').strip()
    #checking if month is a valid name
    while month.lower() not in months:
        month = input('Enter a valid month\t').strip()
    month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a day\t').strip()
    #checking if day is a valid name
    while day.lower() not in days:
        day = input('Enter a valid day\t').strip()
    day = day.lower()
    
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
    #reading from excel file
    df = pd.read_csv(CITY_DATA[city])
    #converting start time to date time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #storing month
    df['month'] = df['Start Time'].dt.month
    #storing day
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #filtering by month        
    if month != 'all':
        month = months.index(month)
        df = df[df['month']==month]
    #filtering by day
    if day != 'all':
        day = day.title()
        df = df[df['day_of_week']==day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]#finding max value using mode
    print('Most Frequent Month: ', months[popular_month],'\n')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day: ', popular_day,'\n')

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Frequent Start Hour: ', popular_hour,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Frequent Start Station: ', popular_start,'\n')
    
    # TO DO: display most commonly used end station
    popular_stop = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_stop,'\n')
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('Most Frequent Trip:', popular_trip,'\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time: ',total,'\n')
    
    # TO DO: display mean travel time
    print('Mean travel time: ',total/df['Trip Duration'].count(),'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("No of user types:\n",df['User Type'].value_counts(),'\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns.values:#checking if gender column is present
        print("No of gender types:\n",df['Gender'].value_counts(),'\n')

    if 'Birth Year' in df.columns.values:#checking if gender column is present    
        # TO DO: Display earliest, most recent, and most common year of birth
        ser = pd.Series(df['Birth Year'].values)
        #saving the birth year in a pandas series
        print("Earliest year of birth: ",ser.min(),'\nRecent year of birth: ',ser.max(),'\n')
        print('Common year of birth: ',ser.mode()[0],'\n')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()    
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
