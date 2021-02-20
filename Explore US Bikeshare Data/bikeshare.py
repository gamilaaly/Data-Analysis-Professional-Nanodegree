import time
import pandas as pd

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city, month, day = " ", " ", " "
    while True:
        try:
            city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()
            if city.replace(" ", "").isalpha():
                if city in CITY_DATA:
                    print("You will get data about {}".format(city.title()))
                    break
                else:
                    print("Please choose one of the following cities: Chicago, New York City or Washington.\n")
            else:
                raise TypeError
        except TypeError:
            print("Letters only please!")
            continue  
        except EOFError:
            print("Please input the name of the city.")
            continue  
        except KeyboardInterrupt:
            print("There was an in interruption!")
            continue  

    # choosing to filter by month or day or no time filter at all
    while True:
        try:
            time_filter = input("Would you like to filter the data by month, day, both or no filter at all? For no filter at all, please type: no filter\n ").lower()
            if time_filter.replace(" ", "").isalpha():
                if time_filter in ['month', 'day']:
                    print("Your data will be filtered by {}".format(time_filter))
                    break
                elif time_filter == 'both':
                    print("Your data will be filtered by both month and day.")
                    break
                elif time_filter == "no filter":
                    print("Your data will not be filtered by time.")
                    break
                else:
                    print("Please choose one of the following time filters: month, day, both, no filter. \n")
            else:
                raise TypeError
        except TypeError:
            print("Letters only please!")
            continue  
        except EOFError:
            print("Please input one of this options: month, day, both, no filter.")
            continue  
        except KeyboardInterrupt:
            print("There was an in interruption!")
            continue  

    # get user input for month (all, january, february, ... , june)

    if time_filter == 'month':
        day = "none"
        valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
        while True:
            try:
                month = input("Which month? January, February, March, April, May, June or all.\n").lower()
                if month.isalpha():
                    if month == "all":
                        print("You will get data from all the months.")
                        break
                    if month in valid_months:
                        print("You will get data from {}".format(month.title()))
                        break
                    else:
                        print(
                            "Please choose one of the following months: January, February, March, April, May, June or all.\n ")
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please!")
                continue  
            except EOFError:
                print(
                    "Please input the name of the month as one of the following, January, February, March, April, May, June or all.\n ")
                continue  
            except KeyboardInterrupt:
                print("There was an in interruption!")
                continue  


    # get user input for day of week (all, monday, tuesday, ... sunday)
    elif time_filter == 'day':
        month = "none"
        valid_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        while True:
            try:
                day = input(
                    "Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all. \n").lower()
                if day.isalpha():
                    if day == "all":
                        print("You will get data from all the days.")
                        break
                    if day in valid_days:
                        print("You will get data from {}".format(day.title()))
                        break
                    else:
                        print(
                            "Please choose one of the following days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all.\n ")
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please.")
                continue  # This causes it to continue
            except EOFError:
                print(
                    "Please input the name of the days as one of the following, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all. \n")
                continue  # This causes it to continue
            except KeyboardInterrupt:
                print("There was an in interruption.")
                continue  # This causes it to continue

    elif time_filter == "both":
        valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
        while True:
            try:
                month = input("Which month? January, February, March, April, May, June or all. \n").lower()
                if month.isalpha():
                    if month == "all":
                        print("You will get data from all the months.")
                        break
                    if month in valid_months:
                        print("You will get data from {}".format(month.title()))
                        break
                    else:
                        print(
                            "Please choose one of the following months: January, February, March, April, May, June or all.\n")
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please!")
                continue  
            except EOFError:
                print(
                    "Please input the name of the month as one of the following, January, February, March, April, May, June or all. \n")
                continue  # This causes it to continue
            except KeyboardInterrupt:
                print("There was an in interruption.")
                continue  # This causes it to continue

        valid_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        while True:
            try:
                day = input(
                    "Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all.\n").lower()
                if day.isalpha():
                    if day == "all":
                        print("You will get data from all the days.")
                        break
                    if day in valid_days:
                        print("You will get data from {}".format(day.title()))
                        break
                    else:
                        print(
                            "Please choose one of the following days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all.\n")
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please!")
                continue
            except EOFError:
                print(
                    "Please input the name of the days as one of the following, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all.")
                continue  
            except KeyboardInterrupt:
                print("There was an in interruption!")
                continue  

    else:
        month, day = 'none', 'none'

    print('-' * 40)
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all' and month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all' and day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        (str) month - name of the month which we filtered by or all or nono for no month filter
        (str) day - name of the day of week which we filtered by or all or nono for no day filter

    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # this works only if the data isn't already filtered by a month
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month.lower() in valid_months:
        print(
            "There is no most popular month as the data already includes one month which is {}.".format(month.title()))
    else:
        most_common_month = df['month'].value_counts().idxmax()
        print("Most popular month: ", valid_months[most_common_month - 1].title())

    # display the most common day of week
    # this works only if the data isn't already filtered by a day
    valid_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    if day.lower() in valid_days:
        print("There is no most popular day as the data already includes one day which is {}.".format(day.title()))
    else:
        most_common_day = df['day_of_week'].value_counts().idxmax()
        print("Most popular day: ", most_common_day.title())

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print("Most popular hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args: 
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most popular start station: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("Most popular end station: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    df["route"] = df["Start Station"] + "-" + df["End Station"]
    most_common_trip = df['route'].value_counts().idxmax()
    print("Most popular trip is between " + most_common_trip.split("-")[0] + " station and " +
          most_common_trip.split("-")[1] + " station.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travelling duration = {} seconds,  which is equal to {} hours.".format(total_travel_time, total_travel_time /3600))

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("Average travelling duration = {} seconds, which is equal to {} hours.".format(average_travel_time,
                                                                                         average_travel_time / 3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.
    
    Args:
    df - Pandas DataFrame containing city data filtered by month and day
    str (city) - name of the city to analyze, if the city is Washington, so there are no data for gender or birth year
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts().to_frame()
    print("\n Count of each user type: \n", user_types)

    # Display counts of gender
    if city.lower() == "washington":
        print("\n There are not any available data about gender in the Washington dataset.")
    else:
        user_gender = df['Gender'].value_counts().to_frame()
        print("\n Count of each user gender: \n", user_gender)

    # Display earliest, most recent, and most common year of birth
    if city.lower() == "washington":
        print("\n There are not any available data about birth years in the Washington dataset.")
    else:

        print("\n The earliest birth year is:", int(df['Birth Year'].min()))
        print("\n The most recent birth year is:", int(df['Birth Year'].max()))
        print("\n The most common birth year is:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(city):
    """ 
    Displays chunks of row data to the user upon its request
    
    Args:
        (str) city - name of the city to analyze 
    """
    print('\nThere is raw data available to check.')
    display_raw_data_option = input('\nWould you like to view a chunk (5 lines) of the raw data? Enter yes or no.\n')
    while display_raw_data_option.lower() not in ['yes', 'no']:
        print('Invalid input! please enter your selection as yes or no only.')
        display_raw_data_option = input('\nWould you like to view a chunk (5 lines) of the raw data? Enter yes or no.\n')
    if display_raw_data_option.lower() == "no":
        print(
            'Your analysis is done, if you want to do more analysis or to show more raw data, please restart the program.')
    while display_raw_data_option.lower() == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col=0, chunksize=5):
                print(chunk)
                display_raw_data_option = input('\nWould you like to view a chunk (5 lines) of the raw data? Enter yes or no.\n')
                if display_raw_data_option != "yes":
                    print(
                        'Your analysis is done, if you want to do more analysis or to show more raw data, please restart the program.')
                    break
            break

        except KeyboardInterrupt:
            print('There was an interruption.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
