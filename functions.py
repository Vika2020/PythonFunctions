
# Defining a Function
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
# greet_user()

# Passing Information to a Function

# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}")
# greet_user('Vika')

# Positional Arguments and  Multiple Function Calls

# def describe_my_city(country_name, city_name):
#     """Display information about my city. """
#     print(f"\tI am from " + city_name + ".")
#     print(city_name + " is the capital of " + country_name + ".")
#
# describe_my_city('Uzbekistan', 'Tashkent')
# describe_my_city('Russia', 'Moscow')

# Keyword Arguments
# def describe_my_city(country_name, city_name):
#     """Display information about my city. """
#     print(f"\tI am from " + city_name + ".")
#     print(city_name + " is the capital of " + country_name + ".")
#
# describe_my_city(country_name = 'Uzbekistan', city_name =  'Tashkent')

# Default Values
# def describe_my_city(country_name, city_name="Tashkent"):
#     """Display information about my city. """
#     print(f"\tI am from " + city_name + ".")
#     print(city_name + " is the capital of " + country_name + ".")

# describe_my_city(country_name = 'Uzbekistan')

# Ex. 8-3
# def make_shirt(size, text):
#     """Summarizing the size of the shirt and the message printed"""
#     print(f"This shirt is " + size + " size with message:  " + text + "  on it.")
#
# make_shirt('s', 'I am the best')
#
# make_shirt(size='m', text='Cool Girl')

# Ex. 8-4
# def make_shirt(message, size='L'):
#     """Summarizing the size of the shirt and the message printed"""
#     print(f"This shirt is " + size + " size with message:  " + message + "!")
#
# make_shirt(message='I love Python')


# def make_shirt(size='L', text='I love Python'):
#     """Summarizing the size of the shirt and the message printed"""
#     print(f"This shirt is " + size + " size with message:  " + text + "!")
#
# make_shirt()

# Ex. 8-5

def describe_city(city, country='Iceland'):
    print(city + " is in " + country + ".")

describe_city(city='Reykjavik')





