# PABUNA, KATRINA B. 

# Create class TV
class TV:
    # constructor
    def __init__(self, channel, volume_level, on, off):
        '''Create a TV instance where
        channel = int(channel of TV)
        volume_level = int(volume level of TV)
        on = bool(if the TV is on or not)
        off = bool(if the TV is on or not)'''

        # instance variables
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
        self.off = off
    
tv1 = TV(30, 3, True, False)
tv2 = TV(3, 2, True, False)

# Create a function that lets the user to choose between TV1 and TV2
def on_tv():
    '''Create def on_tv where it asks the user
    to turn on either TV 1 or TV 2.'''

    try:
        user_input = int(input("\nWhat TV would you like to turn on?\n" +
                                "1. TV 1\n" +
                                "2. TV 2\n\n"))
        if user_input == 1:
            on_tv1() # should lead to TV 1
        elif user_input == 2:
            print("") # should lead to TV 2
        else:
            print("Invalid input.")
    except ValueError:
        print("Only integers are allowed.")
    
# Create all the functions for TV 1
def on_tv1():
    '''Create def on_tv1 where it lets the user pick among
    setting a channel, setting a volume level, 
    increase and decrease the channel by 1, 
    increase and decrease the volume level by 1,
    and turn off the TV.'''

    # for setting the channel
    print("\n")
    print("The current channel is at " + str(tv1.channel) + ".")
    print("The current volue level is at " + str(tv1.volume_level) + ".")
    print("\n")

    try:
        tv1.channel = int(input("Change the channel into: "))
        tv1.volume_level = tv1.volume_level
        tv1.on = tv1.on
        tv1.off = tv1.off
        if tv1.channel in range(120):
            print("\nCurrent channel:", tv1.channel)
            print("Current volume level:", tv1.volume_level)
            print("The TV is on.")
        else:
            print("Channel invalid or out of reach.")
    except ValueError:
        print("Only integers are allowed.")


on_tv()
