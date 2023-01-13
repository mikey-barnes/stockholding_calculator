"""Program should look at the last six periods of sales data for each 
item, calculate the average period sales, standard deviation, and sum
the two to reach a 'standard period sales' figure. This should be
compared to the current stock level and if it below a period's worth of
standard period sales prompt an order."""

import pandas as pd
sales_df = pd.read_csv("sales_data.csv")[:-6] #sales data
inventory_df = pd.read_csv("inventory_data.csv") #inventory data
#sales_df = sales_df[:-6] #strip unneeded trailing information

#sales_df contains n periods worth of sales data, each column of which
#is named after the period to which it pertains. These sales data columns
#are column numbers 7 to -6(excusive)
sales_data_column_names = list(sales_df.columns[7:-6]) #cast to list
 
#create a new df of only the period's sales data; period_sales_df to call .mean on
period_sales_df = sales_df[sales_data_column_names]

#append the calculated mean value to original sales_df
sales_df["average_period_sales"] = period_sales_df.mean(axis = 1)

#append calculated standard deviation to original sales_df
sales_df["stdev_sales"] = period_sales_df.std(axis=1)

#calculate standard period's sales by summing mean and std columns
sales_df["period_std_stock"] = sales_df["average_period_sales"] + sales_df["stdev_sales"]

#round the weekly standard to a whole number
sales_df["period_std_stock"] = sales_df["period_std_stock"]\
                               .apply(lambda x : round(x, 0))

sales_df.SKU = sales_df["SKU"].apply(lambda x : int(x))

inventory_df[inventory_df['sku'].apply(lambda x: isinstance(x, int))]

#merge the two dataframes into one, discarding any lines that are in
#inventory but not sales
sales_and_inventory_merged_df = pd.merge(sales_df, inventory_df,
                                how="left", left_on="SKU", right_on="sku")

#create to_order_df from rows where std_period_stock is < inventory
to_order_df = sales_and_inventory_merged_df[sales_and_inventory_merged_df\
                            ["period_std_stock"] > \
                            sales_and_inventory_merged_df["inventory_Potters_of_Hockley"]]

#add quantity_to_order column using difference between inventory and std_weekly_stock
to_order_df["quantity_to_order"] = to_order_df["period_std_stock"] - to_order_df["inventory_Potters_of_Hockley"]

#strip out irrelevant columns from to_order_df
to_order_df = to_order_df[["Product","SKU","average_period_sales","stdev_sales",\
                           "period_std_stock","inventory_Potters_of_Hockley","quantity_to_order"]]

to_order_df.to_csv('to_order.csv')

exit()



                                             
