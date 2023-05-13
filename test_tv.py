# PABUNA, KATRINA B.

# Import class
import tv_class

# Create first object of class TV
tv1 = tv_class.TV(30, 2, True, False)

# Create second object of class TV

# call instance methods and parameters
print("Channel:", tv1.get_channel())
print("Volume level:", tv1.get_volume_level())

if tv1.turn_on() == True:
    print("The TV is on.")
else:
    print("The TV is off.")