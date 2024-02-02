import currencyapicom
from datetime import datetime

url = "https://api.currencyapi.com/v3/latest"

# this api key is currently not working. I checked whether the code works on its own key,
# so in order for the code to work you need to substitute the api key value
# of the with a key in which requests will not be exhausted
client = currencyapicom.Client('YOUR_API_KEY')


def converter(values_to_currency_list, amount, name_cur_var, date, name_currency_to_list):
    print("--- data from: ", date, " ---")
    # Conversion for each specified currency
    for i in range(0, len(values_to_currency_list), 1):
       res = float(amount)*float(values_to_currency_list[i])
       print("->>>", amount, name_cur_var, "  ==  ", round(res, 2), name_currency_to_list[i])
    return 0


def input_currency():
    while True:
        # Ask the user to input a currency
        currency = input("write a currency you want convert from: ").upper()
        # Check if the input is valid (i.e., a three-letter string)
        if len(currency) == 3 and currency.isalpha():
            # If valid, return the currency
            return currency
        else:
            # If invalid, inform the user and loop again
            print("\nInvalid currency. Please use the 3-letter currency code (e.g. USD).")


def input_date():
    while True:
        # Ask the user to input a date
        date_str = input("Please enter a date (e.g. 2022-12-01): ")
        try:
            # Try to parse the input to a datetime object
            date = datetime.strptime(date_str, '%Y-%m-%d')
            # Check if the date is valid (i.e., not in the future and in the correct format)
            if date_str != datetime.strftime(date, '%Y-%m-%d') or date > datetime.now():
                raise ValueError()
            # If valid, return the date
            return date_str
        except ValueError:
            # If invalid, inform the user and loop again
            print("\nInvalid date. Please enter a past or present date in the following format: YYYY-MM-DD (e.g. 2022-12-01).")


def input_amount():
    while True:
        try:
            # Ask the user to input an amount and try to convert it to a float
            return float(input("Enter the amount to be converted: "))
        except ValueError:
            # If the input cannot be converted to a float, inform the user and loop again
            print("Invalid amount. Please enter a number.")


def input_to_currency():
    while True:
        # Ask the user to input currencies
        currencies_input = input("Currencies to convert (comma-separated): ").upper()

        # Split the input by commas and remove any leading/trailing whitespaces
        currencies_list = [currency.strip() for currency in currencies_input.split(',')]

        # Check if all currencies are valid (i.e., three-letter strings)
        if all(len(currency) == 3 and currency.isalpha() for currency in currencies_list):
            # If valid, return the list of currencies
            return currencies_list
        else:
            print(
                "\nInvalid currency or format. Please use 3-letter currency codes separated by commas (e.g., USD, EUR).")


date_variable = input_date()
currency_variable = input_currency()
amount_variable = input_amount()
currency_to_variable = input_to_currency()

# Request to api
result = client.historical(date_variable, currencies=[currency_variable]+currency_to_variable, base_currency= currency_variable)

# Get the rate value for each item specified by the user and write to new list
values_to_currency_list = []
for i in currency_to_variable:
    values_to_currency_list.append(result['data'][i]['value'])

# Conversation data and output of the work results
converter(values_to_currency_list, amount_variable, currency_variable, date_variable, currency_to_variable)





# Made by Viktoriia Dziadukh #





