# PABUNA, KATRINA B.

# Import class
import tv_class

# Create first object of class TV
tv1 = tv_class.TV(30, 3, True, False)

# Create second object of class TV
tv2 = tv_class.TV(3, 2, True, False)

# Call instance methods and parameters
# TV 1
print("\nTV 1")
print("Channel:", tv1.get_channel())
print("Volume level:", tv1.get_volume_level())

if tv1.turn_on() == True:
    print("The TV is on.\n")
else:
    print("The TV is off.\n")

# TV 2
print("TV 2")
print("Channel:", tv2.get_channel())
print("Volume level:", tv2.get_volume_level())

if tv2.turn_on() == True:
    print("The TV is on.\n")
else:
    print("The TV is off.\n")

# Modify instance variables
# Modify TV 1
print("TV 1")
try:
    tv1.get_channel = int(input("Set new channel: "))
    print("New channel:", tv1.get_channel)
except ValueError:
    print("Only integers are allowed.")

try:
    tv1.get_volume_level = int(input("Set volume level: "))
    print("Volume level:", tv1.get_volume_level)
except ValueError:
    print("Only integers are allowed.")

# Modify TV 2
print("TV 2")
try:
    tv2.get_channel = int(input("Set new channel: "))
    print("New channel:", tv2.get_channel)
except ValueError:
    print("Only integers are allowed.")

try:
    tv2.get_volume_level = int(input("Set volume level: "))
    print("Volume level:", tv2.get_volume_level)
except ValueError:
    print("Only integers are allowed.")