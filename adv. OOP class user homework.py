from datetime import date

today = date.today()

class User:
    """User"""
    def __init__(self, fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory):
        self.fname = fname
        self.last_name = last_name
        self.email = email
        self.id = id
        self.hadd = hadd
        self.seclvl = seclvl
        self.edepart = edepart
        self.cshipping = cshipping
        self.cbilling = cbilling
        self.chistory = chistory
        

class Customer(User):
    #Customer
    def __init__(self, fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory):
        super().__init__(fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory)
        
class Employee(User):
    #Employee
    def __init__(self, fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory):
        super().__init__(fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory)


class EmployeeInfo(Employee):
    #Employee Info
    def __init__(self, fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory):
        super().__init__(fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory)
        
class CustomerInfo(Customer):
    #Customer Info
    def __init__(self, fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory):
        super().__init__(fname, last_name, email, id, hadd, seclvl, edepart, cshipping, cbilling, chistory)
       

#Fname, Lname, email, "year - not defined only instanced", ID, Home Add, Security Level, Depart, " " - empty"
ei = EmployeeInfo("Andrea", "Harrison |", "aharrison@walkingdead.com |", "harrisonandrea,guns |", "220 Victoria Trace, Senoia, GA 30276 |", 3, "| Guns", "", "", "")
ei2 = EmployeeInfo("Beth", "Greene |", "bgreene@walkingdead.com |", "greenebeth, morguetechician |", "220 Victoria Trace, Senoia, GA 30276 |", 5, "| Morgue technician", "", "", "")
ei3 = EmployeeInfo("Daryl", "Dixon |", "ddixon@walkingdead.com |", "dixondaryl, crossbow's |", "220 Victoria Trace, Senoia, GA 30276 |", 4, "| Crossbow's", "", "", "")

#Fname, Lname, email, "year - not defined only instanced", Home Add, Shipping, Billing, History" " - empty"
ci = CustomerInfo("Rick", "Grimes |", "rgrimes@walkingdead.com |", " rgrimes@victoriatrace", "| 220 Victoria Trace, Senoia, GA 30276 |", "", "", "220 Victoria Trace, Senoia, GA 30276 |", "220 Victoria Trace, Senoia, GA 30276 |", "Guns, Ammo, Knives |")
ci2 = CustomerInfo("Maggie", "Rhea |", "mrhea@walkingdead.com |", " mrhea@victoriatrace", "| 220 Victoria Trace, Senoia, GA 30276 |", "", "", "220 Victoria Trace, Senoia, GA 30276 |", "220 Victoria Trace, Senoia, GA 30276 |", "Guns, Ammo, Knives |")
ci3 = CustomerInfo("Meryl", "Dixon |", "mdixon@walkingdead.com |", " mdixon@victoriatrace", "| 220 Victoria Trace, Senoia, GA 30276 |", "", "", "220 Victoria Trace, Senoia, GA 30276 |", "220 Victoria Trace, Senoia, GA 30276 |", "Guns, Ammo, Knife Hand Attachment |")

#print(Employee Info)
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("Employees")
print("---------------------------------------------------------------------------------------------------------------------------------------")
         #first, last, email, "year", ID, HomeAddress, Security Level, Depart, empty, empty, empty
print(ei.fname, ei.last_name, ei.email, today.year,"| Employee ID:", ei.id, ei.hadd, "Security Level:", ei.seclvl, ei.edepart, ei.cshipping, ei.cbilling, ei.chistory)
print("---------------------------------------------------------------------------------------------------------------------------------------")
print(ei2.fname, ei2.last_name, ei2.email, today.year,"| Employee ID:", ei2.id, ei2.hadd, "Security Level:", ei2.seclvl, ei2.edepart, ei2.cshipping, ei2.cbilling, ei2.chistory)
print("---------------------------------------------------------------------------------------------------------------------------------------")
print(ei3.fname, ei3.last_name, ei3.email, today.year,"| Employee ID:", ei3.id, ei3.hadd, "Security Level:", ei3.seclvl, ei3.edepart, ei3.cshipping, ei3.cbilling, ei3.chistory)
print("---------------------------------------------------------------------------------------------------------------------------------------")

#Space Seperation
print("")
print("")
print("")
print("")
print("")
print("")

#print(Customer Info)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Customer")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #first, last, email, "year", empty, HomeAddress, empty, empty, Shipping, Billing, History.
print(ci.fname, ci.last_name, ci.email, today.year, "| Customer ID:", ci.id, ci.hadd, ci.seclvl, ci.edepart, ci.cshipping, ci.cbilling, ci.chistory)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(ci2.fname, ci2.last_name, ci2.email, today.year,"| Customer ID:", ci2.id, ci2.hadd, ci2.seclvl, ci2.edepart, ci2.cshipping, ci2.cbilling, ci2.chistory)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(ci3.fname, ci3.last_name, ci3.email, today.year,"| Customer ID:", ci3.id, ci3.hadd, ci3.seclvl, ci3.edepart, ci3.cshipping, ci3.cbilling, ci3.chistory)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")