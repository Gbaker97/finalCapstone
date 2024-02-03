def hotel_cost(nights):
    '''Function takes parameter of number of nights stay in hotel and returns total cost by looking up value in 'hotel_prices' list.'''
    if nights <= 10:
        cost = hotel_prices[nights - 1]
    # Applying base rate to hotel price for number of nights exceeding 10.
    else:
        cost = hotel_prices[-1] + ((nights - 10) * 40)
    return cost

def plane_cost(city):
    '''Function takes parameter of flight destination and returns cost by looking up city in 'flight_prices' dictionary.'''
    cost = flight_prices[city]
    return cost

def car_rental(days):
    '''Function takes parameter of number of days car rental and returns total cost by looking up value in 'car_prices' list.'''
    if days <= 10:
       cost = car_prices[days - 1]
    # Applying base rate to car rental price for number of days exceeding 10.
    else:
       cost = car_prices[-1] + ((days - 10) * 20)
    return cost

def holiday_cost():
    '''Function called to determine holiday requirements, costs and print to user.'''
    # Asking for user to input required details for holiday, and storing to variables.
    city_flight = input("Which city are you flying to? Type: 'Paris', 'Athens', 'Lisbon', 'Berlin' or 'Oslo': ").lower()
    num_nights = int(input(f"How many nights are you staying in {city_flight}? "))
    rental_days = int(input("How many days are you renting a car for? "))
    
    # Calling functions to determine costs, then calculating sum of these to give total cost.
    cost_of_flight = plane_cost(city_flight)
    cost_of_hotel = hotel_cost(num_nights)
    cost_of_car = car_rental(rental_days)
    total_cost = cost_of_flight + cost_of_hotel + cost_of_car

    # Printing the holiday details to the console.
    print(f"\nHere is the itinery for your holiday to {city_flight}:\n"
          "                ...............\n"
          f"The flight to {city_flight} will cost: £{cost_of_flight}.\n"
          f"Staying for {num_nights} nights in the hotel will cost: £{cost_of_hotel}.\n"
          f"Renting a car for {rental_days} days will cost: £{cost_of_car}.\n"
          "                ...............\n"
          f"The total cost of your holiday is: £{total_cost}.\n"
          f"---> To book your holiday please call us on: +44 7894563452. <---\n")

    # Restarting the function if the user wants to plan another holiday.
    start_again = input("Would you like to plan another holiday? Type 'y' for yes, or 'n' for no: ").upper()
    if start_again == 'Y':
        holiday_cost()
    else: 
        return

# List of prices for hotel stay in order of total nights stay. 
hotel_prices = [95, 180, 268, 359, 450, 530, 620, 710, 800, 875]
# Dictionary of flight prices for each city.
flight_prices = {'paris': 195, 'athens': 270, 'lisbon': 124, 'berlin': 182, 'oslo': 310}
# List of prices for car rental in order of total days hire.
car_prices = [45, 88, 135, 170, 205, 235, 265, 295, 325, 355]

# Calling the 'holiday_cost' function to start the program for the user.
holiday_cost()
