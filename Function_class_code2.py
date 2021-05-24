import datetime
def circle_radius(radius):
   area=(22/7)*radius**2
   print(f"Radius of circle is {radius} and area of circle is :{str(area)}")

def reverse(fname,lname):
    print(f"First Name:{fname}\nLast Name:{lname}")
    print("---------------reverse------------------ ")
    print(f"{lname}"+"   "+f"{fname}")

def current_date():
    print("Current date is:"+str(datetime.datetime.now()))