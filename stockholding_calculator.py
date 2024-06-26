import pandas as pd
import os
from math import ceil


def stockholding_calculator(sales_df,inventory_df):
    """Program should look at the last 'n' periods of sales data for each
    item, calculate the average period sales, standard deviation, and sum
    the two to reach a 'standard period sales' figure.
    Program then generates a csv of items and how over/under stocked each is."""

    # Query input periods and desired output
    period_dict = {"D": "days", "W": "weeks", "M": "months", "Q": "quarters"}
    while True:
        period = str(
            input(
                "What size period is your sales data in? [D]ays/[W]eeks/[M]onths,[Q]uarters: "
            )
        )[0].upper()
        try:
            period = period_dict[period]
        except KeyError:
            print("That is not an accepted value. Please try again.")
        else:
            break

    while True:
        try:
            prediction_period = int(
                input(
                    f"How many {period} worth of stock would you like me to suggest? "
                )
            )
        except ValueError:
            print("Please input a interger value.")
        else:
            break
    pd.options.mode.copy_on_write = True
    sales_df = sales_df[:-6]  # strip unneeded trailing information

    # sales_df contains 'n' periods worth of sales data, each column of which
    # is named after the date to which it pertains. These sales data columns
    # are column numbers 7 to -6(excusive)

    sales_data_column_names = list(sales_df.columns[7:-6])  # cast to list

    # create a new df of only the daily sales data; daily_sales_df to
    # call .mean on
    period_sales_df = sales_df[sales_data_column_names]

    # append the calculated mean value to original sales_df
    sales_df["average_sales"] = period_sales_df.mean(axis=1)

    # append calculated standard deviation to original sales_df
    sales_df["stdev_sales"] = period_sales_df.std(axis=1)

    # calculate standard period sales by summing mean and std columns
    sales_df[f"{period}_std_stock"] = (
        sales_df["average_sales"] + sales_df["stdev_sales"]
    )

    # calculate weekly standard sales by multiplying std_stock by the prediction_period
    sales_df["calculated_std_stock"] = (
        sales_df[f"{period}_std_stock"] * prediction_period
    )

    # round the callculated standard to a whole number
    sales_df["calculated_std_stock"] = sales_df["calculated_std_stock"].apply(
        lambda x: round(x)
    )

    sales_df.SKU = sales_df["SKU"].apply(lambda x: int(x))
    inventory_df[inventory_df["sku"].apply(lambda x: isinstance(x, int))]

    # merge the two dataframes into one, discarding any lines not sold
    # in the last eight weeks i.e. that are in inventory but not sales
    overstock_df = pd.merge(
        sales_df, inventory_df, how="left", left_on="SKU", right_on="sku"
    )

    # add quantity_to_order column using difference between inventory and std_weekly_stock
    overstock_df["quantity_to_order"] = (
        overstock_df["calculated_std_stock"]
        - overstock_df["inventory_Potters_of_Hockley"]
    )

    # strip out irrelevant columns from to_order_df
    overstock_df = overstock_df[
        [
            "Product",
            "SKU",
            "Supplier Code",
            "average_sales",
            "stdev_sales",
            f"{period}_std_stock",
            "calculated_std_stock",
            "inventory_Potters_of_Hockley",
            "quantity_to_order",
            "supply_price",
        ]
    ]

    # calculate the value of the suggested order (both over and under)
    overstock_df["suggested_line_stock_value"] = (
        overstock_df["quantity_to_order"] * overstock_df["supply_price"]
    )

    overstock_df = overstock_df.sort_values(
        by="quantity_to_order", axis=0, ascending=False
    )

    # export df to csv
    overstock_df.to_csv("over_under.csv")

    while True:
        delete_files = input("Do you want to delete files? [Y/N]: ").lower()

        if delete_files[0] == "y":
            os.remove("sales_data.csv")
            os.remove("product-export.csv")
            break
        elif delete_files[0] == "n":
            break
        else:
            continue

    print("Program complete; exiting to main menu\n\n")


if __name__ == "__main__":
    stockholding_calculator()
