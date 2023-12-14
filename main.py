import stockholding_calculator
import sys
def main():
    print(
        r"""
  _____      _   _                   _____ _             _       _____           _                 
 |  __ \    | | | |                 / ____| |           | |     / ____|         | |                
 | |__) |__ | |_| |_ ___ _ __ ___  | (___ | |_ ___   ___| | __ | (___  _   _ ___| |_ ___ _ __ ___  
 |  ___/ _ \| __| __/ _ \ '__/ __|  \___ \| __/ _ \ / __| |/ /  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |  | (_) | |_| ||  __/ |  \__ \  ____) | || (_) | (__|   <   ____) | |_| \__ \ ||  __/ | | | | |
 |_|   \___/ \__|\__\___|_|  |___/ |_____/ \__\___/ \___|_|\_\ |_____/ \__, |___/\__\___|_| |_| |_|
                                                                        __/ |                      
                                                                       |___/                       
"""
    )
    while True:
        try:
            selection = int(
                input(
                    """Please choose from the following:
    1. Update catalogue.
    2. List suppliers.
    3. Suggest purchases. 
    0. Exit\n\n"""
                )
            )
        except ValueError:
            print("Please only input numbers listed.\n")
        else:
            if selection == 0:
                sys.exit("Exiting")
            if selection == 3:
                stockholding_calculator.main()


if __name__ == "__main__":
    main()
