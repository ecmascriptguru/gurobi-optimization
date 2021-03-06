# from gurobipy import *
import os
import xlrd
import numpy

from settings import  ENV
# Read data

use_case_file_path = os.path.join(r'C:\Users\TimKo\Desktop\Uni_7.0\4_WZL\MA\Use_Case', 'use-case_kaiquan_stator-assy.xlsx')

if ENV == 'local':
    use_case_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.xlsx')

usecase = xlrd.open_workbook(use_case_file_path)

# Sort data for products
sheet_1 = usecase.sheet_by_name(r'product_1')
sheet_2 = usecase.sheet_by_name(r'product_2')
sheet_3 = usecase.sheet_by_name(r'product_3')
sheet_4 = usecase.sheet_by_name(r'product_4')
sheet_5 = usecase.sheet_by_name(r'product_5')
sheet_6 = usecase.sheet_by_name(r'product_6')
sheet_7 = usecase.sheet_by_name(r'product_7')
sheet_8 = usecase.sheet_by_name(r'product_8')
#global_sheet = [sheet_1, sheet_2, sheet_3, sheet_4, sheet_5, sheet_6, sheet_7, sheet_8]
product_1 = []
product_2 = []
product_3 = []
product_4 = []
product_5 = []
product_6 = []
product_7 = []
product_8 = []
products = []
product_ID_1 = []
task_ID_1 = []
task_type_1 = []
speed_1 = []
motion_factor_1 = []
product_due_date_1 = []
product_parameter_1 = [product_ID_1, task_ID_1, task_type_1, speed_1,motion_factor_1, product_due_date_1]
product_ID_2 = []
task_ID_2 = []
task_type_2 = []
speed_2 = []
motion_factor_2 = []
product_due_date_2 = []
product_parameter_2 = [product_ID_2, task_ID_2, task_type_2, speed_2,motion_factor_2, product_due_date_2]
product_ID_3 = []
task_ID_3 = []
task_type_3 = []
speed_3 = []
motion_factor_3 = []
product_due_date_3 = []
product_parameter_3 = [product_ID_3, task_ID_3, task_type_3, speed_3,motion_factor_3, product_due_date_3]
product_ID_4 = []
task_ID_4 = []
task_type_4 = []
speed_4 = []
motion_factor_4 = []
product_due_date_4 = []
product_parameter_4 = [product_ID_4, task_ID_4, task_type_4, speed_4,motion_factor_4, product_due_date_4]
product_ID_5 = []
task_ID_5 = []
task_type_5 = []
speed_5 = []
motion_factor_5 = []
product_due_date_5 = []
product_parameter_5 = [product_ID_5, task_ID_5, task_type_5, speed_5,motion_factor_5, product_due_date_5]
product_ID_6 = []
task_ID_6 = []
task_type_6 = []
speed_6 = []
motion_factor_6 = []
product_due_date_6 = []
product_parameter_6 = [product_ID_6, task_ID_6, task_type_6, speed_6,motion_factor_6, product_due_date_6]
product_ID_7 = []
task_ID_7 = []
task_type_7 = []
speed_7 = []
motion_factor_7 = []
product_due_date_7 = []
product_parameter_7 = [product_ID_7, task_ID_7, task_type_7, speed_7,motion_factor_7, product_due_date_7]
product_ID_8 = []
task_ID_8 = []
task_type_8 = []
speed_8 = []
motion_factor_8 = []
product_due_date_8 = []
product_parameter_8 = [product_ID_8, task_ID_8, task_type_8, speed_8,motion_factor_8, product_due_date_8]

i = 1
while True:
    try:
        c = sheet_1.cell_value(i, 0)
        product_parameter_1[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_1.cell_value(i, 1)
        product_parameter_1[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_1.cell_value(i, 2)
        product_parameter_1[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_1.cell_value(i, 3)
        product_parameter_1[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_1.cell_value(i, 4)
        product_parameter_1[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_1.cell_value(i,5)
        product_parameter_1[5].append(c)
        i = i + 1
    except IndexError:
        break
product_1 = [product_ID_1,task_ID_1,task_type_1,speed_1,motion_factor_1,product_due_date_1]

i = 1
while True:
    try:
        c = sheet_2.cell_value(i, 0)
        product_parameter_2[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_2.cell_value(i, 1)
        product_parameter_2[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_2.cell_value(i, 2)
        product_parameter_2[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_2.cell_value(i, 3)
        product_parameter_2[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_2.cell_value(i, 4)
        product_parameter_2[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_2.cell_value(i,5)
        product_parameter_2[5].append(c)
        i = i + 1
    except IndexError:
        break
product_2 = [product_ID_2,task_ID_2,task_type_2,speed_2,motion_factor_2,product_due_date_2]

i = 1
while True:
    try:
        c = sheet_3.cell_value(i, 0)
        product_parameter_3[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_3.cell_value(i, 1)
        product_parameter_3[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_3.cell_value(i, 2)
        product_parameter_3[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_3.cell_value(i, 3)
        product_parameter_3[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_3.cell_value(i, 4)
        product_parameter_3[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_3.cell_value(i,5)
        product_parameter_3[5].append(c)
        i = i + 1
    except IndexError:
        break
product_3 = [product_ID_3,task_ID_3,task_type_3,speed_3,motion_factor_3,product_due_date_3]

i = 1
while True:
    try:
        c = sheet_4.cell_value(i, 0)
        product_parameter_4[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_4.cell_value(i, 1)
        product_parameter_4[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_4.cell_value(i, 2)
        product_parameter_4[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_4.cell_value(i, 3)
        product_parameter_4[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_4.cell_value(i, 4)
        product_parameter_4[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_4.cell_value(i,5)
        product_parameter_4[5].append(c)
        i = i + 1
    except IndexError:
        break
product_4 = [product_ID_4,task_ID_4,task_type_4,speed_4,motion_factor_4,product_due_date_4]

i = 1
while True:
    try:
        c = sheet_5.cell_value(i, 0)
        product_parameter_5[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_5.cell_value(i, 1)
        product_parameter_5[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_5.cell_value(i, 2)
        product_parameter_5[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_5.cell_value(i, 3)
        product_parameter_5[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_5.cell_value(i, 4)
        product_parameter_5[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_5.cell_value(i,5)
        product_parameter_5[5].append(c)
        i = i + 1
    except IndexError:
        break
product_5 = [product_ID_5,task_ID_5,task_type_5,speed_5,motion_factor_5,product_due_date_5]

i = 1
while True:
    try:
        c = sheet_6.cell_value(i, 0)
        product_parameter_6[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_6.cell_value(i, 1)
        product_parameter_6[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_6.cell_value(i, 2)
        product_parameter_6[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_6.cell_value(i, 3)
        product_parameter_6[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_6.cell_value(i, 4)
        product_parameter_6[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_6.cell_value(i,5)
        product_parameter_6[5].append(c)
        i = i + 1
    except IndexError:
        break
product_6 = [product_ID_6,task_ID_6,task_type_6,speed_6,motion_factor_6,product_due_date_6]

i = 1
while True:
    try:
        c = sheet_7.cell_value(i, 0)
        product_parameter_7[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_7.cell_value(i, 1)
        product_parameter_7[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_7.cell_value(i, 2)
        product_parameter_7[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_7.cell_value(i, 3)
        product_parameter_7[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_7.cell_value(i, 4)
        product_parameter_7[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_7.cell_value(i,5)
        product_parameter_7[5].append(c)
        i = i + 1
    except IndexError:
        break
product_7 = [product_ID_7,task_ID_7,task_type_7,speed_7,motion_factor_7,product_due_date_7]

i = 1
while True:
    try:
        c = sheet_8.cell_value(i, 0)
        product_parameter_8[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_8.cell_value(i, 1)
        product_parameter_8[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_8.cell_value(i, 2)
        product_parameter_8[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_8.cell_value(i, 3)
        product_parameter_8[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_8.cell_value(i, 4)
        product_parameter_8[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_8.cell_value(i,5)
        product_parameter_8[5].append(c)
        i = i + 1
    except IndexError:
        break
product_8 = [product_ID_8,task_ID_8,task_type_8,speed_8,motion_factor_8,product_due_date_8]

products = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8]


# Sort data for stations
sheet_9 = usecase.sheet_by_name(r'station_1')
sheet_10 = usecase.sheet_by_name(r'station_2')
sheet_11 = usecase.sheet_by_name(r'station_3')
sheet_12 = usecase.sheet_by_name(r'station_4')
sheet_13 = usecase.sheet_by_name(r'station_5')
sheet_14 = usecase.sheet_by_name(r'station_6')
sheet_15 = usecase.sheet_by_name(r'station_7')
sheet_16 = usecase.sheet_by_name(r'station_8')
#global_sheet = [sheet_1, sheet_2, sheet_3, sheet_4, sheet_5, sheet_6, sheet_7, sheet_8]
station_1 = []
station_2 = []
station_3 = []
station_4 = []
station_5 = []
station_6 = []
station_7 = []
station_8 = []
stations = []
station_ID_1 = []
operation_ID_1 = []
task_type_1 = []
processing_time_1 = []
speed_1 = []
motion_factor_1 = []
station_parameter_1 = [station_ID_1, operation_ID_1, task_type_1, processing_time_1, speed_1, motion_factor_1]
station_ID_2 = []
operation_ID_2 = []
task_type_2 = []
processing_time_2 = []
speed_2 = []
motion_factor_2 = []
station_parameter_2 = [station_ID_2, operation_ID_2, task_type_2, processing_time_2, speed_2, motion_factor_2]
station_ID_3 = []
operation_ID_3 = []
task_type_3 = []
processing_time_3 = []
speed_3 = []
motion_factor_3 = []
station_parameter_3 = [station_ID_3, operation_ID_3, task_type_3, processing_time_3, speed_3, motion_factor_3]
station_ID_4 = []
operation_ID_4 = []
task_type_4 = []
processing_time_4 = []
speed_4 = []
motion_factor_4 = []
station_parameter_4 = [station_ID_4, operation_ID_4, task_type_4, processing_time_4, speed_4, motion_factor_4]
station_ID_5 = []
operation_ID_5 = []
task_type_5 = []
processing_time_5 = []
speed_5 = []
motion_factor_5 = []
station_parameter_5 = [station_ID_5, operation_ID_5, task_type_5, processing_time_5, speed_5, motion_factor_5]
station_ID_6 = []
operation_ID_6 = []
task_type_6 = []
processing_time_6 = []
speed_6 = []
motion_factor_6 = []
station_parameter_6 = [station_ID_6, operation_ID_6, task_type_6, processing_time_6, speed_6, motion_factor_6]
station_ID_7 = []
operation_ID_7 = []
task_type_7 = []
processing_time_7 = []
speed_7 = []
motion_factor_7 = []
station_parameter_7 = [station_ID_7, operation_ID_7, task_type_7, processing_time_7, speed_7, motion_factor_7]
station_ID_8 = []
operation_ID_8 = []
task_type_8 = []
processing_time_8 = []
speed_8 = []
motion_factor_8 = []
station_parameter_8 = [station_ID_8, operation_ID_8, task_type_8, processing_time_8, speed_8, motion_factor_8]

i = 1
while True:
    try:
        c = sheet_9.cell_value(i, 0)
        station_parameter_1[0].append(c)
        i = i + 1
    except IndexError:
        break   
i = 1
while True:
    try:
        c = sheet_9.cell_value(i, 1)
        station_parameter_1[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_9.cell_value(i, 2)
        station_parameter_1[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_9.cell_value(i, 3)
        station_parameter_1[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_9.cell_value(i, 4)
        station_parameter_1[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_9.cell_value(i,5)
        station_parameter_1[5].append(c)
        i = i + 1
    except IndexError:
        break
station_1 = [station_ID_1,operation_ID_1,task_type_1,processing_time_1,speed_1,motion_factor_1]

i = 1
while True:
    try:
        c = sheet_10.cell_value(i, 0)
        station_parameter_2[0].append(c)
        i = i + 1
    except IndexError:
        break     
i = 1
while True:
    try:
        c = sheet_10.cell_value(i, 1)
        station_parameter_2[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_10.cell_value(i, 2)
        station_parameter_2[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_10.cell_value(i, 3)
        station_parameter_2[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_10.cell_value(i, 4)
        station_parameter_2[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_10.cell_value(i,5)
        station_parameter_2[5].append(c)
        i = i + 1
    except IndexError:
        break
station_2 = [station_ID_2,operation_ID_2,task_type_2,processing_time_2,speed_2,motion_factor_2]

i = 1
while True:
    try:
        c = sheet_11.cell_value(i, 0)
        station_parameter_3[0].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_11.cell_value(i, 1)
        station_parameter_3[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_11.cell_value(i, 2)
        station_parameter_3[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_11.cell_value(i, 3)
        station_parameter_3[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_11.cell_value(i, 4)
        station_parameter_3[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_11.cell_value(i,5)
        station_parameter_3[5].append(c)
        i = i + 1
    except IndexError:
        break
station_3 = [station_ID_3,operation_ID_3,task_type_3,processing_time_3,speed_3,motion_factor_3]

i = 1
while True:
    try:
        c = sheet_12.cell_value(i, 0)
        station_parameter_4[0].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_12.cell_value(i, 1)
        station_parameter_4[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_12.cell_value(i, 2)
        station_parameter_4[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_12.cell_value(i, 3)
        station_parameter_4[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_12.cell_value(i, 4)
        station_parameter_4[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_12.cell_value(i,5)
        station_parameter_4[5].append(c)
        i = i + 1
    except IndexError:
        break
station_4 = [station_ID_4,operation_ID_4,task_type_4,processing_time_4,speed_4,motion_factor_4]

i = 1
while True:
    try:
        c = sheet_13.cell_value(i, 0)
        station_parameter_5[0].append(c)
        i = i + 1
    except IndexError:
        break    
i = 1
while True:
    try:
        c = sheet_13.cell_value(i, 1)
        station_parameter_5[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_13.cell_value(i, 2)
        station_parameter_5[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_13.cell_value(i, 3)
        station_parameter_5[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_13.cell_value(i, 4)
        station_parameter_5[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_13.cell_value(i,5)
        station_parameter_5[5].append(c)
        i = i + 1
    except IndexError:
        break
station_5 = [station_ID_5,operation_ID_5,task_type_5,processing_time_5,speed_5,motion_factor_5]

i = 1
while True:
    try:
        c = sheet_14.cell_value(i, 0)
        station_parameter_6[0].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_14.cell_value(i, 1)
        station_parameter_6[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_14.cell_value(i, 2)
        station_parameter_6[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_14.cell_value(i, 3)
        station_parameter_6[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_14.cell_value(i, 4)
        station_parameter_6[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_14.cell_value(i,5)
        station_parameter_6[5].append(c)
        i = i + 1
    except IndexError:
        break
station_6 = [station_ID_6,operation_ID_6,task_type_6,processing_time_6,speed_6,motion_factor_6]

i = 1
while True:
    try:
        c = sheet_15.cell_value(i, 0)
        station_parameter_7[0].append(c)
        i = i + 1
    except IndexError:
        break      
i = 1
while True:
    try:
        c = sheet_15.cell_value(i, 1)
        station_parameter_7[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_15.cell_value(i, 2)
        station_parameter_7[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_15.cell_value(i, 3)
        station_parameter_7[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_15.cell_value(i, 4)
        station_parameter_7[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_15.cell_value(i,5)
        station_parameter_7[5].append(c)
        i = i + 1
    except IndexError:
        break
station_7 = [station_ID_7,operation_ID_7,task_type_7,processing_time_7,speed_7,motion_factor_7]

i = 1
while True:
    try:
        c = sheet_16.cell_value(i, 0)
        station_parameter_8[0].append(c)
        i = i + 1
    except IndexError:
        break
      
i = 1
while True:
    try:
        c = sheet_16.cell_value(i, 1)
        station_parameter_8[1].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_16.cell_value(i, 2)
        station_parameter_8[2].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_16.cell_value(i, 3)
        station_parameter_8[3].append(c)
        i = i + 1
    except IndexError:
        break  
i = 1
while True:
    try:
        c = sheet_16.cell_value(i, 4)
        station_parameter_8[4].append(c)
        i = i + 1
    except IndexError:
        break
i = 1
while True:
    try:
        c = sheet_16.cell_value(i,5)
        station_parameter_8[5].append(c)
        i = i + 1
    except IndexError:
        break
station_8 = [station_ID_8,operation_ID_8,task_type_8,processing_time_8,speed_8,motion_factor_8]

stations = [station_1,station_2,station_3,station_4,station_5,station_6,station_7,station_8]

# Step into assignment function
import assignment
a_ips = assignment.solve(products,stations)






# Sort assignments for handover
indices_string = a_ips[0]
a_ips_values = []
indices = []

for ips in range(len(indices_string)):
    number_string = indices_string[ips]
    index = number_string.split(",")
    number_string = [int(k) for k in index]
    indices.append(number_string)

for f in a_ips[1]:
    a_ips_values.append(int(f))

a_ips = [indices, a_ips_values]


# Instantiate shop_floor
from DistanceCalculation import DistanceCalculation

shopWidth = 12
shopDepth = 9
cols = 4
rows = 3

shop_floor = DistanceCalculation(shopWidth,shopDepth,rows,cols)

# Instantiate positions
zonesCount = rows * cols
positions = []

for i in range(zonesCount):
    positions.append(i)
   
# Compute and sort distances
dist = dict()

for i in positions:
    for j in positions:
        dist[i,j] = shop_floor.GetDistance(i,j)

# Step into allocation function
import allocation
allocation_params = allocation.solve(products,stations,positions,dist,a_ips)






# Instantiate and sort allocation params for handover
indices_string = allocation_params[0]
zp_values_float = []
zp_noVal = []
zs_values_float = []
zs_noVal = []
y_values_float = []
y_noVal = []



for params in range(len(indices_string)):
    string = indices_string[params]
    index = string.split(",")
    #number_string = [int(k) for k in index]
    
    if index[0] == 'z_p':
        index1_zp = index[1]
        index2_zp = index[2]
        index3_zp = index[3]
        z_pfg_index_string = [index1_zp,index2_zp,index3_zp]
        z_pfg_index = [int(k) for k in z_pfg_index_string]
        zp_noVal.append(z_pfg_index)
        zp_values_float.append(allocation_params[1][params])
    elif index[0] == 'z_s':
        index1_zs = index[1]
        index2_zs = index[2]
        index3_zs = index[3]
        z_sfg_index_string = [index1_zs,index2_zs,index3_zs]
        z_sfg_index = [int(k) for k in z_sfg_index_string]
        zs_noVal.append(z_sfg_index)
        zs_values_float.append(allocation_params[1][params])
    elif index[0] == 'y':
        index1_y = index[1]
        index2_y = index[2]
        index3_y = index[3]
        y_ipf_index_string = [index1_y,index2_y,index3_y]
        y_ipf_index = [int(k) for k in y_ipf_index_string]
        y_noVal.append(y_ipf_index)
        y_values_float.append(allocation_params[1][params])
    else:
        Dmax = allocation_params[1][params]

zp_values = [int(f) for f in zp_values_float]
zs_values = [int(f) for f in zs_values_float]
y_values = [int(f) for f in y_values_float]
        
z_pfg = [zp_noVal,zp_values]
z_sfg = [zs_noVal,zs_values]
y_ipf = [y_noVal,y_values]
    

# Include precedence parameter h_ijp - intree precedence graph
# product variant 1 (product variant 10 poles)
# instantiation
h_p1 = dict()
h_p2 = dict()
h_p3 = dict()
h_p4 = dict()
h_p5 = dict()
h_p6 = dict()
h_p7 = dict()
h_p8 = dict()

# product 1
h_p1[1,8,1] = 1
h_p1[2,8,1] = 1
h_p1[3,5,1] = 1
h_p1[6,8,1] = 1
h_p1[5,8,1] = 1
h_p1[8,10,1] = 1
h_p1[10,12,1] = 1
h_p1[12,14,1] = 1
h_p1[14,16,1] = 1
h_p1[16,17,1] = 1

# product 2
h_p2[1,8,2] = 1
h_p2[2,8,2] = 1
h_p2[3,5,2] = 1
h_p2[6,8,2] = 1
h_p2[5,8,2] = 1
h_p2[8,10,2] = 1
h_p2[10,12,2] = 1
h_p2[12,14,2] = 1
h_p2[14,16,2] = 1
h_p2[16,17,2] = 1

h_ijp = h_p1.copy()
h_ijp.update(h_p2)

# product 3
h_p3[1,8,3] = 1
h_p3[2,8,3] = 1
h_p3[3,5,3] = 1
h_p3[6,8,3] = 1
h_p3[5,8,3] = 1
h_p3[8,10,3] = 1
h_p3[10,12,3] = 1
h_p3[12,14,3] = 1
h_p3[14,16,3] = 1
h_p3[16,17,3] = 1

h_ijp.update(h_p3)

# product 4
h_p4[1,8,4] = 1
h_p4[2,8,4] = 1
h_p4[3,5,4] = 1
h_p4[6,8,4] = 1
h_p4[5,8,4] = 1
h_p4[8,10,4] = 1
h_p4[10,12,4] = 1
h_p4[12,14,4] = 1
h_p4[14,16,4] = 1
h_p4[16,17,4] = 1

h_ijp.update(h_p4)

# product 5
h_p5[1,9,5] = 1
h_p5[2,9,5] = 1
h_p5[4,5,5] = 1
h_p5[7,9,5] = 1
h_p5[5,9,5] = 1
h_p5[9,11,5] = 1
h_p5[11,13,5] = 1
h_p5[13,15,5] = 1
h_p5[15,16,5] = 1
h_p5[16,18,5] = 1

h_ijp.update(h_p5)

# product 6
h_p6[1,9,6] = 1
h_p6[2,9,6] = 1
h_p6[4,5,6] = 1
h_p6[7,9,6] = 1
h_p6[5,9,6] = 1
h_p6[9,11,6] = 1
h_p6[11,13,6] = 1
h_p6[13,15,6] = 1
h_p6[15,16,6] = 1
h_p6[16,18,6] = 1

h_ijp.update(h_p6)

# product 7
h_p7[1,9,7] = 1
h_p7[2,9,7] = 1
h_p7[4,5,7] = 1
h_p7[7,9,7] = 1
h_p7[5,9,7] = 1
h_p7[9,11,7] = 1
h_p7[11,13,7] = 1
h_p7[13,15,7] = 1
h_p7[15,16,7] = 1
h_p7[16,18,7] = 1

h_ijp.update(h_p7)

# product 8
h_p8[1,9,8] = 1
h_p8[2,9,8] = 1
h_p8[4,5,8] = 1
h_p8[7,9,8] = 1
h_p8[5,9,8] = 1
h_p8[9,11,8] = 1
h_p8[11,13,8] = 1
h_p8[13,15,8] = 1
h_p8[15,16,8] = 1
h_p8[16,18,8] = 1

# global intree dict
h_ijp.update(h_p8)


# Include and sort products' due dates
D_p_list = []
D_p_float = []
D_p = []
due_date_p1 = [products[0][5]]
due_date_p2 = [products[1][5]]
due_date_p3 = [products[2][5]]
due_date_p4 = [products[3][5]]
due_date_p5 = [products[4][5]]
due_date_p6 = [products[5][5]]
due_date_p7 = [products[6][5]]
due_date_p8 = [products[7][5]]
D_p_list = due_date_p1+due_date_p2+due_date_p3+due_date_p4+due_date_p5+due_date_p6+due_date_p7+due_date_p8

for i in range(len(D_p_list)):
    D_p_float.append(D_p_list[i][0])
D_p = [round(x) for x in D_p_float]

# Big M
M = 2000




# Step into scheduling function
import scheduling
scheduling.solve(products,stations,positions,dist,a_ips,z_pfg,z_sfg,y_ipf,h_ijp,D_p,M)


