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
        print("\n", "\033[93m=" * 80, "\n")
        user_input = int(input("\n\033[95m\x1B[3m\033[1mWhat TV would you like to turn on?\033[0m\n" +
                                "\033[92m1. \033[97mTV 1\n" +
                                "\033[92m2. \033[97mTV 2\n\n" +
                                "\033[92m"))
        if user_input == 1:
            on_tv1() # should lead to TV 1
        elif user_input == 2:
            on_tv2() # should lead to TV 2
        else:
            print("\033[91mInvalid input.\033[97m\n")
    except ValueError:
        print("\033[91mOnly integers are allowed.\033[97m\n")
    print("\n", "\033[93m=" * 80, "\n")
    
# Create all the functions for TV 1
def on_tv1():
    '''Create def on_tv1 where it lets the user pick among
    setting a channel, setting a volume level, 
    increase and decrease the channel by 1, 
    increase and decrease the volume level by 1,
    and turn off the TV.'''
    
    # set the channel
    def set_channel():
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv1.channel) + ".")
        print("The current volume level is at " + str(tv1.volume_level) + ".")
        print("\n")

        try:
            tv1.channel = int(input("\033[95m\x1B[3m\033[1mChange the channel into: \033[0m\033[97m"))
            tv1.volume_level = tv1.volume_level
            tv1.on = tv1.on
            tv1.off = tv1.off
            print("\n", "\033[93m=" * 80, "\n")
            if tv1.channel in range(120):
                print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv1.channel)
                print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv1.volume_level)
                print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
            else:
                print("\033[91mChannel invalid or out of reach.\033[97m\n")
        except ValueError:
            print("\033[91mOnly integers are allowed.\033[97m\n")
        start_tv()
    
    # set the volume level
    def set_volumme():
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv1.channel) + ".")
        print("The current volume level is at " + str(tv1.volume_level) + ".")
        print("\n")

        try:
            tv1.volume_level = int(input("\033[95m\x1B[3m\033[1mChange the volume level into: \033[0m\033[97m"))
            tv1.channel = tv1.channel
            tv1.on = tv1.on
            tv1.off = tv1.off
            if tv1.volume_level in range(7):
                print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv1.channel)
                print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv1.volume_level)
                print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
            else:
                print("\033[91mChannel invalid or out of reach.\033[97m\n")
        except ValueError:
            print("\033[91mOnly integers are allowed.\033[97m\n")
        start_tv()
    
    # increase the channel by 1
    def inc_channel():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv1.channel) + ".")
        print("The current volume level is at " + str(tv1.volume_level) + ".")
        print("\n")
        tv1.channel = tv1.channel + 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv1.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv1.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()
    
    # decrease the channel by 1
    def dec_channel():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv1.channel) + ".")
        print("The current volume level is at " + str(tv1.volume_level) + ".")
        print("\n")
        tv1.channel = tv1.channel - 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv1.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv1.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()

    # increase the volume level by 1
    def inc_volume():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv1.channel) + ".")
        print("The current volume level is at " + str(tv1.volume_level) + ".")
        print("\n")
        tv1.volume_level = tv1.volume_level + 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv1.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv1.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()
    
    # decrease the volume level by 1
    def dec_volume():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv1.channel) + ".")
        print("The current volume level is at " + str(tv1.volume_level) + ".")
        print("\n")
        tv1.volume_level = tv1.volume_level - 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv1.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv1.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()

    # def start_tv to let the user pick what they would like to do on the TV
    def start_tv():
        try:
            print("\n", "\033[93m=" * 80, "\n")
            user_input = int(input("\n\033[92m\x1B[3m\033[1mWhat would you like to do?\033[0m\n\n" +
                                    "\033[96m1. \033[97mSet channel\n" +
                                    "\033[96m2. \033[97mSet volume level\n" +
                                    "\033[96m3. \033[97mIncrease channel\n" +
                                    "\033[96m4. \033[97mDecrease channel\n" +
                                    "\033[96m5. \033[97mIncrease volume level\n" +
                                    "\033[96m6. \033[97mDecerase volume level\n" +
                                    "\033[96m7. \033[97mTurn off TV\n\n" +
                                    "\033[96m"))
            print("\n", "\033[93m=" * 80, "\n")
            if user_input == 1:
                set_channel()
            elif user_input == 2:
                set_volumme()
            elif user_input == 3:
                inc_channel()
            elif user_input == 4:
                dec_channel()
            elif user_input == 5:
                inc_volume()
            elif user_input == 6:
                dec_volume()
            elif user_input == 7:
                print("\033[92m\x1B[3m\033YYou've turned off the TV.\033[0m")
                on_tv()
            else:
                print("\033[91mInvalid input.\033[97")
        except ValueError:
            print("\033[91mOnly integers are allowed.\033[97")
    start_tv()
        
# Create all the functions for TV 2
def on_tv2():
    '''Create def on_tv1 where it lets the user pick among
    setting a channel, setting a volume level, 
    increase and decrease the channel by 1, 
    increase and decrease the volume level by 1,
    and turn off the TV.'''
    
    # set the channel
    def set_channel():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv2.channel) + ".")
        print("The current volume level is at " + str(tv2.volume_level) + ".")
        print("\n")

        try:
            tv2.channel = int(input("\033[95m\x1B[3m\033[1mChange the channel into: \033[0m\033[97m"))
            tv2.volume_level = tv2.volume_level
            tv2.on = tv2.on
            tv2.off = tv2.off
            print("\n", "\033[93m=" * 80, "\n")
            if tv2.channel in range(120):
                print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv2.channel)
                print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv2.volume_level)
                print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
            else:
                print("\033[91mChannel invalid or out of reach.\033[97m\n")
        except ValueError:
            print("\033[91mOnly integers are allowed.\033[97m\n")
        start_tv()

    # set the volume level
    def set_volumme():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv2.channel) + ".")
        print("The current volume level is at " + str(tv2.volume_level) + ".")
        print("\n")

        try:
            tv2.volume_level = int(input("\033[95m\x1B[3m\033[1mChange the volume level into: \033[0m\033[97m"))
            tv2.channel = tv2.channel
            tv2.on = tv2.on
            tv2.off = tv2.off
            if tv2.volume_level in range(7):
                print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv2.channel)
                print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv2.volume_level)
                print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
            else:
                print("\033[91mChannel invalid or out of reach.\033[97m\n")
        except ValueError:
            print("\033[91mOnly integers are allowed.\033[97m\n")
        start_tv()


    # increase the channel by 1
    def inc_channel():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv2.channel) + ".")
        print("The current volume level is at " + str(tv2.volume_level) + ".")
        print("\n")
        tv2.channel = tv2.channel + 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv2.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv2.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()
    
    # decrease the channel by 1
    def dec_channel():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv2.channel) + ".")
        print("The current volume level is at " + str(tv2.volume_level) + ".")
        print("\n")
        tv2.channel = tv2.channel - 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv2.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv2.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()

    # increase the volume level by 1
    def inc_volume():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv2.channel) + ".")
        print("The current volume level is at " + str(tv2.volume_level) + ".")
        print("\n")
        tv2.volume_level = tv2.volume_level + 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv2.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv2.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()
    
    # decrease the volume level by 1
    def dec_volume():
        print("\n")
        print("\033[92m\x1B[3m\033[1mThe current channel is at " + str(tv2.channel) + ".")
        print("The current volume level is at " + str(tv2.volume_level) + ".")
        print("\n")
        tv2.volume_level = tv2.volume_level - 1
        print("\n\033[96m\x1B[3m\033[1mCurrent channel:\033[0m\033[97m", tv2.channel)
        print("\033[96m\x1B[3m\033[1mCurrent volume level:\033[0m\033[97m", tv2.volume_level)
        print("\033[96m\x1B[3m\033[1mThe TV is on.\033[0m")
        start_tv()

    # def start_tv to let the user pick what they would like to do on the TV
    def start_tv():
        try:
            print("\n", "\033[93m=" * 80, "\n")
            user_input = int(input("\n\033[92m\x1B[3m\033[1mWhat would you like to do?\033[0m\n\n" +
                                    "\033[96m1. \033[97mSet channel\n" +
                                    "\033[96m2. \033[97mSet volume level\n" +
                                    "\033[96m3. \033[97mIncrease channel\n" +
                                    "\033[96m4. \033[97mDecrease channel\n" +
                                    "\033[96m5. \033[97mIncrease volume level\n" +
                                    "\033[96m6. \033[97mDecerase volume level\n" +
                                    "\033[96m7. \033[97mTurn off TV\n\n" +
                                    "\033[96m"))
            print("\n", "\033[93m=" * 80, "\n")
            if user_input == 1:
                set_channel()
            elif user_input == 2:
                set_volumme()
            elif user_input == 3:
                inc_channel()
            elif user_input == 4:
                dec_channel()
            elif user_input == 5:
                inc_volume()
            elif user_input == 6:
                dec_volume()
            elif user_input == 7:
                print("\033[92m\x1B[3m\033YYou've turned off the TV.\033[0m")
                on_tv()
            else:
                print("\033[91mInvalid input.\2033[97")
        except ValueError:
            print("\033[91mOnly integers are allowed.\033[97")
    start_tv()

on_tv()