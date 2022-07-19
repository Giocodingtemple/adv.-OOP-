from datetime import datetime as dt

# Create a Class User
# Create Two Child class of User: Employee and Customer
# Follow The Rules Below to define the methods and attributes of your classes:

# Other Important Things to Note:
# All users should implement a __repr__ and a __str__ method
# Any Two Users are the same if they have the same email
# All Users should be hashable
# If I have a list of Users and sort them they should be sorted by there created_on date

# Things to Do After you Create the Classes
# Create 3 Instances of Employee and Customer
# Create a List of all your created users and have them sorted by creation date Newest Users first using .sort or sorted without a key lambda function
class User():
    def __init__(self, first_name, last_name, email, id):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email 
            self.id = id
            self.created_on = dt.now().strftime("%c")

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
        
    def __str__(self):
        '''Human Readable output'''
        return f'<User | {self.full_name}>'

    def __repr__(self):
        '''machine readable unique output'''
        return f'<User |{self.last_name} {self.created_on}>'

    def __hash__(self):
        return hash(self.last_name+self.created_on)

    def first_name_change(self):
        self.first_name.append()
        return input(f"new first name")
    
    def last_name_change(self):
        self.last_name.append()
        return input(f"new last name")        
            
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

class Employee(User):
    def __init__(self, first_name, last_name, email, home_address, security_level, department, id):
        super().__init__(self, first_name, last_name, email, id)
        self.home_address = home_address 
        self.security_level = security_level
        self.department = department
        self.created_on = dt.now().strftime("%c")
       
    def department_change(self):
        self.department.append()
        return input(f"new department section")
    
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
    
class Customer(User):
    def __init__(self, first_name, last_name, email, shipping_address, billing_address, purchase_history, id):
        super().__init__(self, first_name, last_name, email, id)
        self.shipping_address = shipping_address 
        self.billing_address = billing_address
        self.purchase_address = purchase_history 
        self.created_on = dt.now().strftime("%c")

    def billing_address_change(self):
        self.billing_address.append()
        return input(f"new billing address")

    def shipping_address_change(self):
        self.shipping_address.append()
        return input(f"new shipping address")

# Things to Do After you Create the Classes
# Create 3 Instances of Employee and Customer
# Create a List of all your created users and have them sorted by creation date Newest Users first using .sort or sorted without a key lambda function

andrea = User(first_name="andrea", last_name="Harrison", email="aharrison@walkingdead.com", home_address="220 Victoria Trace, Senoia, GA 30276", security_level = 3, department="guns", id= "harrisonandrea,guns") 
beth = User(first_name="beth", last_name="greene", email="bgreene@walkingdead.com", home_address="220 Victoria Trace, Senoia, GA 30276", security_level= 5, department="Morgue technician", id="greenebeth, morguetechician") 
daryl = User(first_name="daryl", last_name="dixon", email="ddixon@walkingdead.com", home_address="220 Victoria Trace, Senoia, GA 30276", security_level= 11, department="crossbows", id="dixondaryl, crossbows")

rick = User(first_name="rick", last_name="grimes", email="rgrimes@walkingdead.com" ,shipping_address="220 Victoria Trace, Senoia, GA 30276", billing_address="220 Victoria Trace, Senoia, GA 30276",purchase_history="guns ammo and knives",id="rgrimes@victoriatrace")
maggie = User(first_name="maggie", last_name="rhea", email="mrhea@walkingdead.com" ,shipping_address="220 Victoria Trace, Senoia, GA 30276", billing_address="220 Victoria Trace, Senoia, GA 30276",purchase_history="guns ammo and knives",id="mrhea@victoriatrace")
meryl = User(first_name="meryl", last_name="dixon", email="mdixon@walkingdead.com" ,shipping_address="220 Victoria Trace, Senoia, GA 30276", billing_address="220 Victoria Trace, Senoia, GA 30276",purchase_history="guns ammo and knives",id="mdixon@victoriatrace")

print(andrea.full_name)
print(beth.full_name)
print(daryl.full_name)

print(rick.full_name)
print(maggie.full_name)
print(meryl.full_name)
