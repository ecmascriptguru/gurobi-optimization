from gurobipy import *
import os
import xlrd
import numpy



def solve(products, stations, positions, dist, a_ips, z_pfg, z_sfg, y_ipf, h_ijp, D_p, M):        
    # Model
    model = Model("Scheduling")
    
    # stations
    station_IDs = []
    processing_times = []
    durations = dict()
    d_ips = dict()
    
    
    capabilities = [s[2] for s in stations]
    times = [s[3] for s in stations]
    
    # products
    task_types_p = []
    task_types_float = []
    product_IDs = []
    
    
    task_types_p_float = [p[2] for p in products]
    
    
    # Constructing handover parameters
    a = dict()
    task_types_a = []
    product_IDs_a = []
    station_IDs_a = []
    
    zp = dict()
    product_IDs_z = []
    positions_pf = []
    positions_pg = []
    
    zs = dict()
    station_IDs_z = []
    positions_sf = []
    positions_sg = []
    
    y = dict()
    task_types_y = []
    product_IDs_y = []
    positions_y = []
    
    
    # Sorting parameters
    no_stations = [int(s[0][0]) for s in stations] 
    no_products = [int(p[0][0]) for p in products]
    v_p = [p[3][0] for p in products]


    for p in range(len(no_products)):
        c = [int(x) for x in task_types_p_float[p]]
        task_types_p.append(c)
        
    for s in range(len(no_stations)):
      for i in range(len(capabilities[s])):
          durations[capabilities[s][i],s+1] = times[s][i]
        
    # d_ips = [task_types_p,product_IDs,station_IDs]= duration 
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
    
    
    # Sorting handover parameters a[i,p,s]
    indices = a_ips[0]
    values = a_ips[1]
  
    for i in range(len(indices)):
        task_types_a.append(indices[i][0])
        product_IDs_a.append(indices[i][1])
        station_IDs_a.append(indices[i][2]) 
      
    for k in range(len(task_types_a)):
        a[task_types_a[k],product_IDs_a[k],station_IDs_a[k]] = values[k]
        
    # Sorting handover parameters zp[p,f,g]
    indices = z_pfg[0]
    values = z_pfg[1]
  
    for i in range(len(indices)):
        product_IDs_z.append(indices[i][0])
        positions_pf.append(indices[i][1])
        positions_pg.append(indices[i][2])
      
    for k in range(len(product_IDs_z)):
        zp[product_IDs_z[k],positions_pf[k],positions_pg[k]] = values[k]
    
    # Sorting handover parameters zs[s,f,g]
    indices = z_sfg[0]
    values = z_sfg[1]
  
    for i in range(len(indices)):
        station_IDs_z.append(indices[i][0])
        positions_sf.append(indices[i][1])
        positions_sg.append(indices[i][2])
      
    for k in range(len(station_IDs_z)):
        zs[station_IDs_z[k],positions_sf[k],positions_sg[k]] = values[k]
    
    # Sorting handover parameters y[i,p,f]
    indices = y_ipf[0]
    values = y_ipf[1]
  
    for i in range(len(indices)):
        task_types_y.append(indices[i][0])
        product_IDs_y.append(indices[i][1])
        positions_y.append(indices[i][2])
      
    for k in range(len(task_types_y)):
        y[task_types_y[k],product_IDs_y[k],positions_y[k]] = values[k]
    
    
    # Add decision variables
    # Continuous decision variable Cmax, that is maximal completion time/makespan for all jobs, shall be minimized
    Cmax = model.addVar(obj = 1, vtype = "C", name = "Cmax")
    
    # Continuous decision variable t_ip decides at which time point job ip is started
    t = {}
    for s in no_stations:
        for p in no_products:
            for i in task_types_p[p-1]:
                t[i,p,s] = model.addVar(obj = 0, vtype = "C", name = "t,%s,%s,%s" % (i,p,s))
     
    # Binary decision variable x_ijpq decides whether job ip is performed before jq or not
    x = {}
    for q in no_products:
        for p in no_products:
            if p != q:
                for j in task_types_p[q-1]:
                    for i in task_types_p[p-1]:
                        x[i,j,p,q] = model.addVar(obj = 0, vtype = GRB.BINARY, name = "x,%s,%s,%s,%s" % (i,j,p,q))
    
    # Binary decision variable c_ijpq decides whether job ip is performed concurrently to job jp or not
    #c = {}
    #for q in no_products:
    #    for p in no_products:
    #        if p != q:
    #            for j in task_types_p[q-1]:
    #                for i in task_types_p[p-1]:
    #                    c[i,j,p,q] = model.addVar(obj = 0, vtype = GRB.BINARY, name = "c,%s,%s,%s,%s" % (i,j,p,q))
        
    
    # Minimize Cmax
    model.modelSense = GRB.MINIMIZE
    
    # Update the model to make variables known. 
    # Update the model to make variables known. From now on, no variables should be added.
    model.update()
   
    
    # Add constraints
    # Cmax is smaller or equal to every prooducts' due date
   # for p in no_products:
   #     model.addConstr(Cmax <= D_p[p-1])
     
        
    # Every job finishes/reaches exit earlier than Cmax
    for s in no_stations:
        for p in no_products:
            for i in task_types_p[p-1]:
                if a.get((i,p,s),0)==1:
                    for f in positions:
                        for g in positions:
                            if g!=f:
                                model.addConstr(t[i,p,s]+d_ips[i,p,s] <= Cmax)


    # Job jp can only start when job ip has been finished and jp is a successor of ip (in tree precedence constraint)
    for s in no_stations:
        for u in no_stations:
            for p in no_products:
                for i in task_types_p[p-1]:
                    for j in task_types_p[p-1]:
                       if h_ijp.get((i,j,p),0)==1 and a.get((i,p,s),0)==1 and a.get((j,p,u),0)==1:
                            for f in positions:
                                for g in positions:
                                    if g!=f:
                                        model.addConstr(t[i,p,s]+d_ips[i,p,s]-(dist[f,g]/(1/v_p[p-1]))*zp[p,f,g] <= t[j,p,u])
                        

    # Job jq can only be started when job ip has been completed
    for s in no_stations:
        for p in no_products:
            for q in no_products:
                if q!=p:
                    for i in task_types_p[p-1]:
                        for j in task_types_p[q-1]:
                            if a.get((i,p,s),0)==1 and a.get((j,q,s),0)==1:
                                for f in positions:
                                    for g in positions:
                                        if g!=f:
                                            model.addConstr((t[i,p,s]+d_ips[i,p,s]-dist[f,g]/(1/v_p[q-1]))*zp[q,f,g] <= t[j,q,s])
                
    # Big M constraints
    #for s in no_stations:
    #    for p in no_products:
    #        for q in no_products:
    #            if q!=p:
    #                for i in task_types_p[p-1]:
    #                    for j in task_types_p[q-1]:
    #                        if a.get((i,p,s),0)==1 and a.get((j,q,s),0)==1:
    #                            for f in positions:
    #                                for g in positions:
    #                                    if g!=f:
    #                                        model.addConstr((t[i,p,s]+d_ips[i,p,s]-dist[f,g]/(1/v_p[q-1]))*zp[q,f,g]*y.get((j-1,q,f),0) <= (t[j,q,s]+M*(1-x[i,j,p,q]))*y.get((j,q,g),0))    
    #                                        model.addConstr((t[j,q,s]+d_ips[j,q,s]-dist[f,g]/(1/v_p[p-1]))*zp[p,f,g]*y.get((i-1,p,f),0) <= (t[i,p,s]+M*x[i,j,p,q])*y.get((i,p,g),0))
                          
                                                                 
                                            
    
    # Every job ip can only start after leaving the origin at time point zero
    #for s in no_stations:
    #    for p in no_products:
    #        for i in task_types_p[p-1]:
    #            if a.get((i,p,s),0)==1:
    #                for f in positions:
    #                    model.addConstr(dist[min(positions),f]*(1/v_p[p-1])*zp.get((p,min(positions),f),0) <= t[i,p,s])
                        
    # Job ip and jq can be processed in parallel, when they are performed on different stations, s and u, respectively 
    #for s in no_stations:
    #    for u in no_stations:
    #        if u!=s:
    #            for p in no_products:
    #                for q in no_products:
    #                    if q!=p:
    #                        for i in task_types_p[p-1]:
    #                            for j in task_types_p[q-1]:
    #                                if a.get((i,p,s),0)==1 and a.get((j,q,u),0)==1:
    #                                    model.addConstr(t[i,p,s]+d_ips[i,p,s] >= t[j,q,u]+M*c[i,j,p,q])
    #                                    model.addConstr(t[j,q,u]+d_ips[j,q,u] >= t[i,p,s]+M*c[i,j,p,q])
                                        
    # Either jobs are processed consecutively on the same stations (x_ijpq) or in parallel on different stations (c_ijpq)
    #for q in no_products:
    #    for p in no_products:
    #        if p != q:
    #            for j in task_types_p[q-1]:
    #                for i in task_types_p[p-1]:
    #                    model.addConstr(x[i,j,p,q]+c[i,j,p,q] == 1)
    
    # Update the model to make constraints known.
    model.update()

    # Solve
    model.optimize()
    
    # Prepare output
    myvars = []
    myvars = model.getVars()
    myvars_list = [[],[]]
  
    for v in myvars:
        myvars_list[0].append(v.VarName)
        myvars_list[1].append(v.X)

    # Return relevant parameters
    return myvars_list
