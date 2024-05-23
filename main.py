from stockholding_calculator import stockholding_calculator
import non_movers_report
import sys
import pandas as pd


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
    print("\nPlease wait; loading resources.\n")

    # Import resources
    try:
        sales_df = pd.read_csv("sales_data.csv")  # this is sales data for each item
        inventory_df = pd.read_csv(
            "product-export.csv"
        )  # this is current inventory figures for each item
    except FileNotFoundError:
        print(
            "One or more files missing. You will need to rectify this before progressing.\n"
        )
    else:
        print("Resources loaded.\n")

    while True:
        try:
            selection = int(
                input(
                    """Please choose from the following:
    1. Update catalogue.
    2. List suppliers.
    3. Suggest purchases.
    4. Run non-movers report.
    0. Exit\n\n"""
                )
            )
        except ValueError:
            print("Please only input numbers listed.\n")
        else:
            if selection == 0:
                sys.exit("Exiting")
            if selection == 3:
                stockholding_calculator(sales_df,inventory_df)
            if selection == 4:
                non_movers_report.main()


if __name__ == "__main__":
    main()
