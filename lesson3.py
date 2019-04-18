#This is Exercise 3.3.1
#inches->cm

cm = 2.54

def inches_to_cm(inches):
    return cm * inches

inc=2

print(inches_to_cm(inc))

#feet to inches
#create a function that turns the an input which will be in feet to inches
#ft = 12in
inch = 12
def ft_to_inches(ft):
    return ft * inch

feet = 5
print(f"{feet} feet is equal to {ft_to_inches(feet)} inches")

#yards to feet
#1 yard = 3ft
ft = 3
def yard_to_feet(y):
    return y * ft

print(f"{yard_to_feet(5)} feet")

#rod to feet
#1 rod = 5.5 yards
yd = 5.5
def rods_to_yards(rod):
    return  rod * yd

#furlong to rods
rd = 40
def furlong_to_rods(furlong):
     return furlong * rd
print(f"{furlong_to_rods(2)} rods")

#mile to furlong
#1  mile is equal to 8 furlong
fl = 8
def miles_to_furlong(mile):
    return mile * fl

print(f"{miles_to_furlong(2)} furlongs")

#feet to centimeters

#test 12 * 2.54 = 30.48
#     2 * 12 * 2.54 = 60.96
def ft_to_centimeter(ft):
    feet_converted_inches = ft_to_inches(ft)
    return inches_to_cm(feet_converted_inches)

print(ft_to_centimeter(2))


#rods to inches
#test 5.5*3*12 = 198
def rod_to_inches(rods):
    #first convert rod to yd and assign it a variable
    converted_to_yards = rods_to_yards(rods)
    #Then convert yards to feet
    converted_to_feet = yard_to_feet(converted_to_yards)
    #lastly convert feet to inches
    return ft_to_inches(converted_to_feet)

print(rod_to_inches(1))

#def miles_to_feet

#Exercise 3.3.2.
#volume of a cylinder = 3.14r*r*h
pi = 3.14

def volume_cylinder(r,h):
    return pi*r*r*h

print(f" the volume of this cylinder is {volume_cylinder(2,2)}")

#this is to see if the a change will happen
