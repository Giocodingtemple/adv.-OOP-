from datetime import datetime as dt


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
        return f'<User | {self.email}>'

    def __repr__(self):
        return f'<User | {self.email}>'

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, __o):                                                         
        return self.created_on == __o.created_on
    
    def __lt__(self, __o):
        return self.created_on < __o.created_on

    def __gt__(self, __o):
        return self.created_on > __o.created_on

    def __le__(self, __o):
        return self.created_on <= __o.created_on

    def __ge__(self, __o):
        return self.created_on >= __o.created_on 

    def first_name_change(self):
        self.first_name.append()
        return input(f"new first name")
    
    def last_name_change(self):
        self.last_name.append()
        return input(f"new last name")        
            


class Employee(User):
    def __init__(self, first_name, last_name, email, home_address, security_level, department, id):
        super().__init__(self, first_name, last_name, email, id)
        self.home_address = home_address 
        self.security_level = security_level
        self.department = department
        self.created_on = dt.now().strftime("%c")


    @property
    def id(self):
        return self.first_name + '.' + self.last_name + '.' + self.department

    def department_change(self):
        self.department.append()
        return input(f"new department section")
    

    
class Customer(User):
    def __init__(self, first_name, last_name, email, shipping_address, billing_address, purchase_history, id):
        super().__init__(self, first_name, last_name, email, id)
        self.shipping_address = shipping_address 
        self.billing_address = billing_address
        self.purchase_address = purchase_history 
        self.created_on = dt.now().strftime("%c")

    @property
    def id(self):
        return self.email + '.' + self.shipping_address

    def billing_address_change(self):
        self.billing_address.append()
        return input(f"new billing address")

    def shipping_address_change(self):
        self.shipping_address.append()
        return input(f"new shipping address")



andrea = Employee("andrea", "Harrison", "aharrison@walkingdead.com", "220 Victoria Trace, Senoia, GA 30276",  3, "guns",  "harrisonandrea,guns") 
beth = Employee("beth", "greene", "bgreene@walkingdead.com", "220 Victoria Trace, Senoia, GA 30276",  5, "Morgue technician", "greenebeth, morguetechician") 
daryl = Employee("daryl", "dixon", "ddixon@walkingdead.com", "220 Victoria Trace, Senoia, GA 30276",  11, "crossbows", "dixondaryl, crossbows")

rick = Customer("rick", "grimes", "rgrimes@walkingdead.com" , "220 Victoria Trace, Senoia, GA 30276", "220 Victoria Trace, Senoia, GA 30276","guns ammo and knives", "rgrimes@victoriatrace")
maggie = Customer("maggie", "rhea", "mrhea@walkingdead.com" , "220 Victoria Trace, Senoia, GA 30276", "220 Victoria Trace, Senoia, GA 30276", "guns ammo and knives", "mrhea@victoriatrace")
meryl = Customer("meryl", "dixon", "mdixon@walkingdead.com" , "220 Victoria Trace, Senoia, GA 30276", "220 Victoria Trace, Senoia, GA 30276", "guns ammo and knives", "mdixon@victoriatrace")

print(andrea.full_name)
print(beth.full_name)
print(daryl.full_name)

print(rick.full_name)
print(maggie.full_name)
print(meryl.full_name)
