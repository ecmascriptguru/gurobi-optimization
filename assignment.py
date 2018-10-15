from gurobipy import *

def solve(products, stations):
  # Model
  model = Model("Assignment")
  
  # Stations
  station_IDs = []
  no_s = []
  no_stations = []
  capabilities = []
  processing_times = []
  durations = dict()
  d_ips = dict()
  task_types_s1 = []
  task_types_s2 = []
  task_types_s3 = []
  task_types_s4 = []
  task_types_s5 = []
  task_types_s6 = []
  task_types_s7 = []
  task_types_s8 = []
  processing_times_1 = []
  processing_times_2 = []
  processing_times_3 = []
  processing_times_4 = []
  processing_times_5 = []
  processing_times_6 = []
  processing_times_7 = []
  processing_times_8 = []
  station_IDs_s1 = [stations[0][0]]
  station_IDs_s2 = [stations[1][0]]
  station_IDs_s3 = [stations[2][0]]
  station_IDs_s4 = [stations[3][0]]
  station_IDs_s5 = [stations[4][0]]
  station_IDs_s6 = [stations[5][0]]
  station_IDs_s7 = [stations[6][0]]
  station_IDs_s8 = [stations[7][0]]
  task_types_s1 = [stations[0][2]]
  task_types_s2 = [stations[1][2]]
  task_types_s3 = [stations[2][2]]
  task_types_s4 = [stations[3][2]]
  task_types_s5 = [stations[4][2]]
  task_types_s6 = [stations[5][2]]
  task_types_s7 = [stations[6][2]]
  task_types_s8 = [stations[7][2]]
  processing_times_1 = [stations[0][3]]
  processing_times_2 = [stations[1][3]]
  processing_times_3 = [stations[2][3]]
  processing_times_4 = [stations[3][3]]
  processing_times_5 = [stations[4][3]]
  processing_times_6 = [stations[5][3]]
  processing_times_7 = [stations[6][3]]
  processing_times_8 = [stations[7][3]]
  IDs_s = station_IDs_s1+station_IDs_s2+station_IDs_s3+station_IDs_s4+station_IDs_s5+station_IDs_s6+station_IDs_s7+station_IDs_s8
  capabilities = task_types_s1+task_types_s2+task_types_s3+task_types_s4+task_types_s5+task_types_s6+task_types_s7+task_types_s8
  times = processing_times_1+processing_times_2+processing_times_3+processing_times_4+processing_times_5+processing_times_6+processing_times_7+processing_times_8
  
  # Products
  task_types_p = []
  task_types_float = []
  task_types = []
  product_IDs = []
  no_p = []
  no_products = []
  task_types_p1 = []
  task_types_p2 = []
  task_types_p3 = []
  task_types_p4 = []
  task_types_p5 = []
  task_types_p6 = []
  task_types_p7 = []
  task_types_p8 = []
  product_IDs_p1 = [products[0][0]]
  product_IDs_p2 = [products[1][0]]
  product_IDs_p3 = [products[2][0]]
  product_IDs_p4 = [products[3][0]]
  product_IDs_p5 = [products[4][0]]
  product_IDs_p6 = [products[5][0]]
  product_IDs_p7 = [products[6][0]]
  product_IDs_p8 = [products[7][0]]
  task_types_p1 = [products[0][2]]
  task_types_p2 = [products[1][2]]
  task_types_p3 = [products[2][2]]
  task_types_p4 = [products[3][2]]
  task_types_p5 = [products[4][2]]
  task_types_p6 = [products[5][2]]
  task_types_p7 = [products[6][2]]
  task_types_p8 = [products[7][2]]
  IDs_p = product_IDs_p1+product_IDs_p2+product_IDs_p3+product_IDs_p4+product_IDs_p5+product_IDs_p6+product_IDs_p7+product_IDs_p8
  task_types_p_float = task_types_p1+task_types_p2+task_types_p3+task_types_p4+task_types_p5+task_types_p6+task_types_p7+task_types_p8
  #task_types = [task_types_1 task_types_2 task_types_3 task_types_4 task_types_5 task_types_6 task_types_7 task_types_8]
  
  
  # Sorting parameters
  for i in range(len(IDs_s)):
      no_s.append(IDs_s[i][0])
  no_stations = [int(x) for x in no_s] 
    
  for i in range(len(IDs_p)):
      no_p.append(IDs_p[i][0])
  no_products = [int(x) for x in no_p] 

  for p in range(len(no_products)):
      c = [int(x) for x in task_types_p_float[p]]
      task_types_p.append(c) 


  for s in range(len(no_stations)):
      for i in range(len(capabilities[s])):
          durations[capabilities[s][i],s+1] = times[s][i]

  # d_ips = [task_types_p,product_IDs,station_IDs] = duration 
  for s in range(len(no_stations)):
      for p in range(len(no_products)):
          for i in task_types_p[p]:
            if i in capabilities[s]:
              task_types_float.append(i)
              product_IDs.append(p+1)
              station_IDs.append(s+1)
              processing_times.append(durations.get((i,s+1),))
          
  task_types = [int(x) for x in task_types_float]
          
  for k in range(len(task_types)):
      d_ips[task_types[k],product_IDs[k],station_IDs[k]] = processing_times[k]
    

  # Binary decision variable a[i,p,s] indicates whether task_type ip is executed on station s or not
  a = {}
  for s in no_stations:
      for p in no_products:
          for i in task_types_p[p-1]:
              # Adjust additional attributes (lb, ub, vtype, obj)
              a[i,p,s] = model.addVar(obj=d_ips.get((i,p,s),2000), vtype=GRB.BINARY, name="%s,%s,%s" % (i,p,s))


  # Update the model to make variables known. From now on, no variables should be added.
  model.update()
  model.modelSense=GRB.MINIMIZE
  
  # Add constraints
  # For every job exactly one station
  for p in no_products:    
      for i in task_types_p[p-1]:
          model.addConstr(quicksum(a[i,p,s] for s in no_stations) == 1)
  
  # Update the model to make constraints known.
  model.update()

  # Solve
  model.optimize()
    
  # Prepare output
  myvars = []
  myvars = model.getVars()
  assignments = [[],[]]
  
  for v in myvars:
      assignments[0].append(v.VarName)
      assignments[1].append(v.X)
     
  # Return relevant parameters
  return assignments

