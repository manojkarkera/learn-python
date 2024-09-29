# https://tradewithpython.com/download-end-of-day-stock-prices-for-national-stock-exchange-of-india-using-python
#Making all necessary imports for the code
from datetime import date
from jugaad_data.nse import bhavcopy_save
import pandas as pd
from jugaad_data.holidays import holidays

# date_range = pd.bdate_range(start='10/09/2023', end = '10/13/2023', 
#                          freq='C', holidays = holidays(2023,10))


# dates_2023 = [x.date() for x in date_range]

# print(dates_2023)

#Saving the Bhavcopy file for 01-01-2021
bhavcopy_save(date(2023,10,4), ".")
# YYYYMMDD

