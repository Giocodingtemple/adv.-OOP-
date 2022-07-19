# Create a Class User
# Create Two Child class of User: Employee and Customer
# Follow The Rules Below to define the methods and attributes of your classes:

# Employees have:
    # first name [string]
    # last name [string]
    # email [string]
    # created_on [time stamp]
    # home_address [string]
    # security_level [int]
    # department [string]
    # id - which is made by taking the employee's full_name concatenating it with their department

    # Employees can:
    # change their first name
    # change their last name

    # change their department

# Customers have:
    # first name [string]
    # last name [string]
    # email [string]
    # created_on [time stamp]
    # shipping_address [string]
    # billing_address [string]
    # purchase_history [list]
    # id - which is made by taking the customers email and concatenating it with their shipping adress

    # Customers can:
    # change their first name
    # change their last name

    # change their billing_address
    # change their shipping_address

# Other Important Things to Note:
# All users should implement a __repr__ and a __str__ method
# Any Two Users are the same if they have the same email
# All Users should be hashable
# If I have a list of Users and sort them they should be sorted by there created_on date

# Things to Do After you Create the Classes
# Create 3 Instances of Employee and Customer
# Create a List of all your created users and have them sorted by creation date Newest Users first using .sort or sorted without a key lambda function
