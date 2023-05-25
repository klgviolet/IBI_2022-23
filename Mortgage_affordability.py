def calculator(house_price,annual_salary):
    # buy a house worth no more than five times	your annual	salary
    if house_price <= annual_salary * 5:
        return 'Yes'
    else:
        return 'No'

print(calculator(180000,35000))  # It returns"No"
