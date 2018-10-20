from gurobipy import *
import os
import xlrd
import numpy

from settings import  ENV, PRODUCT_COUNT, STATION_COUNT, SHOPWIDTH, SHOPDEPTH, RESX, RESY

# Read data
use_case_file_path = os.path.join(r'C:\Users\TimKo\Desktop\Uni_7.0\4_WZL\MA\Use_Case', 'use-case_kaiquan_stator-assy_1.xlsx')

if ENV == 'local':
    use_case_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.xlsx')

usecase = xlrd.open_workbook(use_case_file_path)

#  Reading Products
products = list()

for i in range(PRODUCT_COUNT):
    sheet = usecase.sheet_by_name("product_%s" % (i + 1))
    product = list()

    for col_index in range(sheet.ncols):
        """
        product_id,
        task_id,
        task_type
        speed
        motion_factor
        due_date
        """
        column = sheet.col(col_index)
        product_property = list()
        for row_index in range(len(column) - 1):
            product_property.append(column[row_index + 1].value)
        
        product.append(product_property)
    
    products.append(product)

#  Reading Stations
stations = list()

for i in range(STATION_COUNT):
    sheet = usecase.sheet_by_name("station_%s" % (i + 1))
    station = list()

    for col_index in range(sheet.ncols):
        """
        station_id,
        operation_id,
        task_type
        processing_time
        speed
        motion_factor
        """
        column = sheet.col(col_index)
        station_property = list()
        for row_index in range(len(column) - 1):
            station_property.append(column[row_index + 1].value)
        
        station.append(station_property)
    
    stations.append(station)
    

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

shop_floor = DistanceCalculation(SHOPWIDTH,SHOPDEPTH,RESY,RESX)

# Instantiate positions
zonesCount = RESY * RESX
positions = []

for i in range(zonesCount):
    positions.append(i)
   
# Compute and sort distances
dist = dict()

for i in positions:
    for j in positions:
        dist[i,j] = shop_floor.GetDistance(i,j)

# Create list of shop-floor instances r
#shop_floors = [1,2,3,4,5,6]
shop_floors = []        
global_tasks = []

tasks = [i[1] for i in products]

for k in range(len(tasks)):
    for l in range(len(tasks[k])):
        global_tasks.append(tasks[k][l])

instances = range(len(global_tasks))

for i in instances:
    shop_floors.append(i+1)
   

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
        

# Step into allocation function
import allocation
allocation_params = allocation.solve(products,stations,positions,dist,a_ips,h_ijp,shop_floors)






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
        index4_zp = index[4]
        index5_zp = index[5]
        z_pfg_index_string = [index1_zp,index2_zp,index3_zp,index4_zp,index5_zp]
        z_pfg_index = [int(k) for k in z_pfg_index_string]
        zp_noVal.append(z_pfg_index)
        zp_values_float.append(allocation_params[1][params])
    elif index[0] == 'z_s':
        index1_zs = index[1]
        index2_zs = index[2]
        index3_zs = index[3]
        index4_zs = index[4]
        index5_zs = index[5]
        z_sfg_index_string = [index1_zs,index2_zs,index3_zs,index4_zs,index5_zs]
        z_sfg_index = [int(k) for k in z_sfg_index_string]
        zs_noVal.append(z_sfg_index)
        zs_values_float.append(allocation_params[1][params])
    elif index[0] == 'y':
        index1_y = index[1]
        index2_y = index[2]
        index3_y = index[3]
        index4_y = index[4]
        y_ipf_index_string = [index1_y,index2_y,index3_y,index4_y]
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

# Check results
y_indices = []

for i in range(len(y_ipf[1])):
    if y_ipf[1][i] == 1:
        y_indices.append(y_ipf[0][i])
        
zp_indices = []

for i in range(len(z_pfg[1])):
    if z_pfg[1][i] == 1:
        zp_indices.append(z_pfg[0][i])
        
zs_indices = []

for i in range(len(z_sfg[1])):
    if z_sfg[1][i] == 1:
        zs_indices.append(z_sfg[0][i])


# Include and sort products' due dates
D_p_float = []

D_p_list = [i[5] for i in products]


for i in range(len(D_p_list)):
    D_p_float.append(D_p_list[i][0])
D_p = [round(x) for x in D_p_float]

# Big M
M = 2000




# Step into scheduling function
import scheduling
scheduling.solve(products,stations,positions,dist,a_ips,z_pfg,z_sfg,y_ipf,h_ijp,D_p,M)


