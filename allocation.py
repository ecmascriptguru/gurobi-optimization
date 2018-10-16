from gurobipy import *
import os
import xlrd
import numpy

def solve(products,stations,positions,dist,a_ips):
  # Model
  model = Model("Allocation")
  
  # stations
  no_s = []
  no_stations = []
  c_s_list = []
  c_s = []
  motion_factor_s1 = []
  motion_factor_s2 = []
  motion_factor_s3 = []
  motion_factor_s4 = []
  motion_factor_s5 = []
  motion_factor_s6 = []
  motion_factor_s7 = []
  motion_factor_s8 = []
  station_IDs_s1 = [stations[0][0]]
  station_IDs_s2 = [stations[1][0]]
  station_IDs_s3 = [stations[2][0]]
  station_IDs_s4 = [stations[3][0]]
  station_IDs_s5 = [stations[4][0]]
  station_IDs_s6 = [stations[5][0]]
  station_IDs_s7 = [stations[6][0]]
  station_IDs_s8 = [stations[7][0]]
  motion_factor_s1 = [stations[0][5]]
  motion_factor_s2 = [stations[1][5]]
  motion_factor_s3 = [stations[1][5]]
  motion_factor_s4 = [stations[3][5]]
  motion_factor_s5 = [stations[4][5]]
  motion_factor_s6 = [stations[5][5]]
  motion_factor_s7 = [stations[6][5]]
  motion_factor_s8 = [stations[7][5]]
  c_s_list = motion_factor_s1+motion_factor_s2+motion_factor_s3+motion_factor_s4+motion_factor_s5+motion_factor_s6+motion_factor_s7+motion_factor_s8 
  IDs_s = station_IDs_s1+station_IDs_s2+station_IDs_s3+station_IDs_s4+station_IDs_s5+station_IDs_s6+station_IDs_s7+station_IDs_s8
  
  
  # products
  task_types_p = []
  product_IDs = []
  no_p = []
  no_products = []
  c_p_list = []
  c_p = []
  task_types_p1 = []
  task_types_p2 = []
  task_types_p3 = []
  task_types_p4 = []
  task_types_p5 = []
  task_types_p6 = []
  task_types_p7 = []
  task_types_p8 = []
  motion_factor_p1 = []
  motion_factor_p2 = []
  motion_factor_p3 = []
  motion_factor_p4 = []
  motion_factor_p5 = []
  motion_factor_p6 = []
  motion_factor_p7 = []
  motion_factor_p8 = []
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
  motion_factor_p1 = [products[0][4]]
  motion_factor_p2 = [products[1][4]]
  motion_factor_p3 = [products[2][4]]
  motion_factor_p4 = [products[3][4]]
  motion_factor_p5 = [products[4][4]]
  motion_factor_p6 = [products[5][4]]
  motion_factor_p7 = [products[6][4]]
  motion_factor_p8 = [products[7][4]]
  c_p_list = motion_factor_p1+motion_factor_p2+motion_factor_p3+motion_factor_p4+motion_factor_p5+motion_factor_p6+motion_factor_p7+motion_factor_p8
  IDs_p = product_IDs_p1+product_IDs_p2+product_IDs_p3+product_IDs_p4+product_IDs_p5+product_IDs_p6+product_IDs_p7+product_IDs_p8
  task_types_p_float = task_types_p1+task_types_p2+task_types_p3+task_types_p4+task_types_p5+task_types_p6+task_types_p7+task_types_p8
  
  # Constructing handover parameters
  a = dict()
  task_types = []
  product_IDs = []
  station_IDs = []
  
  # Sorting parameters
  for i in range(len(IDs_s)):
      no_s.append(IDs_s[i][0])
  no_stations = [int(x) for x in no_s] 
  
  for i in range(len(IDs_p)):
      no_p.append(IDs_p[i][0])
  no_products = [int(x) for x in no_p]
  
  for i in range(len(c_s_list)):
      c_s.append(c_s_list[i][0])

  for i in range(len(c_p_list)):
      c_p.append(c_p_list[i][0])      

  for p in range(len(no_products)):
      c = [int(x) for x in task_types_p_float[p]]
      task_types_p.append(c)
  
  # Sorting handover parameters a[i,p,s]
  indices = a_ips[0]
  values = a_ips[1]
  
  for i in range(len(indices)):
      task_types.append(indices[i][0])
      product_IDs.append(indices[i][1])
      station_IDs.append(indices[i][2]) 
      
  for k in range(len(task_types)):
      a[task_types[k],product_IDs[k],station_IDs[k]] = values[k]
  
  #task_types = [int(x) for x in task_types_float]
  
  
  # Add decision variables
  # Continuous decision variable Dmax, that is maximal distance traveled by assembly participants, shall be minimized
  Dmax = model.addVar(obj=1, vtype = "C", name = "Dmax")

  # Binary decision variable z_pfg indicates whether product p is moved from postion f to g
  z_p = {}
  for p in no_products:
    for f in positions:
        for g in positions:
            # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
            z_p[p,f,g] = model.addVar(obj = 0, vtype=GRB.BINARY, name = "z_p,%s,%s,%s" % (p,g,f))

  # Binary decision variable z_sfg indicates whether product p is moved from postion f to g
  z_s = {}
  for s in no_stations:
    for f in positions:
        for g in positions:
            # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
            z_s[s,f,g] = model.addVar(obj = 0, vtype = GRB.BINARY, name = "z_s,%s,%s,%s" % (s,g,f))


  # Binary decision variable y_i indicates whether student i is a leader (value = 1) or not (value = 0).
  y = {}
  for f in positions:
      for p in no_products:
          for i in task_types_p[p-1]:
              # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
              y[i,p,f] = model.addVar(obj = 0, vtype=GRB.BINARY, name="y,%s,%s,%s" % (i,p,f))


  # MINIMIZE Dmax
  model.modelSense = GRB.MINIMIZE
  
  # Update the model to make variables known. 
  # Update the model to make variables known. From now on, no variables should be added.
  model.update()


  # Add constraints
  # Max travelled distance Dmax is not exceeded
  model.addConstr(quicksum(dist[f,g]*c_p[p-1]*z_p[p,f,g] for p in no_products for f in positions for g in positions)+
                  quicksum(dist[f,g]*c_s[s-1]*z_s[s,f,g] for s in no_stations for f in positions for g in positions) <= Dmax)
  
  # Every job is assigned to exactly one position   
  for p in no_products:    
      for i in task_types_p[p-1]:
          model.addConstr(quicksum(y[i,p,f] for f in positions) == 1)
          
  # Different jobs (tasks of different products) are not assigned to the same position if they are assigned to different stations
  for s in no_stations:
#      for u in no_stations:
#          if u!= s:
              for p in no_products:
                  for q in no_products:
                      if q != p:
                          for i in task_types_p[p-1]:
                              for j in task_types_p[q-1]:
                                  if a.get((i,p,s),0)+a.get((j,q,s),0)==1:
                                      for f in positions:
                                          model.addConstr(y[i,p,f]+y[j,q,f] <= 1) 

  # Move if the job is allocated, but only if two different jobs are assigned to different positions 
  #for s in no_stations:
  #    for p in no_products:
  #        for i in task_types_p[p-1]:
  #            if a.get((i,p,s),0)==1:
  #                for f in positions:
  #                    for g in positions:
  #                        for h in positions:
  #                            if h!=g!=f:
  #                               model.addConstr(z_p[p,f,g]+z_s[s,h,g] >= 2*y.get((i,p,g),0))
  #                               model.addConstr(z_s[s,f,g]+z_p[p,f,g] <= y.get((p,i,g),0))
  
  for p in no_products:
      for i in task_types_p[p-1]:
 #         for j in task_types_p[p-1]:
 #             if i == j-1:
                 for f in positions:
                     for g in positions:
                          if g != f:
                              model.addConstr((y.get((i-1,p,f),0)+y.get((i,p,g),0))-1 <= z_p[p,f,g])
                              
   
  for s in no_stations:                             
      for p in no_products:
          for q in no_products:
              if q!= p:
                  for i in task_types_p[p-1]:
                      for j in task_types_p[q-1]:
                          if a.get((i,p,s),0)==1 and a.get((q,j,s),0)==1:
                              for f in positions:
                                  for g in positions:
                                      if g!=f:
                                          model.addConstr((y.get((i,p,f),0)+y.get((j,q,g),0))-1 <= z_s[s,f,g])
  
  #for p in no_products:
  #    for i in task_types_p[p-1]:
  #        for f in positions:
 #             for g in positions:
  #                for h in positions:
  #                    model.addConstr(2*y.get((i,p,g),0) <= z_p[p,f,g]+z_p[p,g,h])

 # for p in no_products:
 #     for s in no_stations:
 #         for i in task_types_p[p-1]:
 #             for f in positions:
 #                 model.addConstr(z_p[p,f,f] + z_s[s,f,f] <= 2*y.get((i,p,f),0))  
              
  #for s in no_stations:
  #    for i in task_types_p[p-1]:
  #        for f in positions:
  #            model.addConstr(z_s[s,f,f] <= y.get((i,p,f),0))

    
  #for p in no_products:
  #    for f in positions:
  #        for g in positions:
  #            for h in positions:
  #                if h!=g!=f:
  #                    model.addConstr(z_p[p,g,h] <= z_p[p,f,g])
                      
  #for s in no_stations:
  #    for f in positions:
  #        for g in positions:
  #            for h in positions:
  #                if h!=g!=f:
  #                    model.addConstr(z_s[s,g,h] <= z_s[s,f,g])
    
    
  # Variable zp and zs need to be zero when object is not moved 
  #for p in no_products:
  #    for f in positions:
  #        for g in positions:
  #            if g == f:
  #                model.addConstr(z_p[p,f,g] == 0)
                  
  #for s in no_stations:
  #    for f in positions:
   #       for g in positions:
   #           if g == f:
   #               model.addConstr(z_s[s,f,g] == 0)
  
  #for p in no_products:
  #  for f in positions:
  #      model.addConstr(z_p[p,f,f] == 0)
       
  #for s in no_stations:
  #  for f in positions:
  #     model.addConstr(z_s[s,f,f] == 0)
                      
                      
  # Every product leaves the origin and approaches the exit
  #for p in no_products:
  #    for f in positions:
  #       for g in positions:
  #           model.addConstr(z_p[p,min(positions),f]+z_p[p,g,max(positions)] == 2)

  
  #for p in no_products:
  #    for f in positions:
  #        model.addConstr(z_p[p,min(positions),f] == 1)
          
  #for p in no_products:
  #    for g in positions:
  #        model.addConstr(z_p[p,g,max(positions)] == 1)
    

  # Update the model to make constraints known.
  model.update()

  # Solve
  model.optimize()
 # model.computeIIS()
  
  # Prepare output
  myvars = []
  myvars = model.getVars()
  myvars_list = [[],[]]
  
  for v in myvars:
      myvars_list[0].append(v.VarName)
      myvars_list[1].append(v.X)

  # Return relevant parameters
  return myvars_list