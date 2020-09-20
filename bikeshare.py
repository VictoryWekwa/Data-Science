#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[7]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter your choice city: ")
    # Creating the while loop to handle invalid input
    while city not in CITY_DATA.keys():
        print("Hello! Welcome to this program. Please choose your choice city: ")
        print("\n1. Chicago 2. New York City 3. Washington")
        if city not in CITY_DATA.keys():
            print("\nPlease check your input and try again")
            print("*" * 100)
    print("You have chose", city.capitalize(),"as your choice city.")

    # get user input for month (all, january, february, ... , june)
    Months_Available = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = input("Please enter a month from the available months to continue: ")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    Days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("You need to enter a day from the available days: ")


    print('-'*40)
    return city, month, day


# In[8]:


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
    df['day_of_week'] = df['Start Time'].dt.weekday
    
    # filter by month if applicable
                                                                       
    if month !='all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.capitalize()]

    
    return df
    


# In[9]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour

    # display the most common start hour
    common_hour = df['week'].mode()[0]

    #printing the time taken to get the results using the time module
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[10]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print("The most common start station is", common_sstation)

    # display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print("The most common end station is", common_estation) 

    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combine = df['Start To End'].mode()[0]
    print("The most frequent combination of start station and end station trip is", combine)
    
    #Getting the time it takes to print the result
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[11]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is", total_travel_time)

    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    print("The mean travel time is", mean_travel_time)

    #Getting the time it took 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[14]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("The type of users by gender are", gender)
    except:
        print("There is no field called 'Gender' in this file.")


    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("The earliest year of birth: {},The most recent year of birth: {},The most common year of birth: {}").format(earliest,most_recent,most_common_year)
    except:
        print("No details")
        
    #printing out the time it takes to get the result
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


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


# In[ ]:




