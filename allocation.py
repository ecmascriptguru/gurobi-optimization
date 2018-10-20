from gurobipy import *

def solve(products,stations,positions,dist,a_ips,h_ijp,shop_floors):
    # Model
    model = Model("Allocation")
    
    task_types_p = []
    product_IDs = []

    #Motion Factors for station list
    c_s = [s[5][0] for s in stations]
    no_stations = [int(s[0][0]) for s in stations]
    no_products = [int(p[0][0]) for p in products]
    
    #Motion factors for products
    c_p = [p[4][0] for p in products]
    task_types_p_float = [p[2] for p in products]
 
    
    # Constructing handover parameters
    a = dict()
    task_types = []
    station_IDs = []

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
    
    
    # Add decision variables
    # Continuous decision variable Dmax, that is maximal distance traveled by assembly participants, shall be minimized
    Dmax = model.addVar(obj=1, vtype = "C", name = "Dmax")

    # Binary decision variable z_pfg indicates whether product p is moved from postion f to g
    z_p = {}
    for p in no_products:
        for r in shop_floors:
            for f in positions:
                for g in positions:
                    # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
                    z_p[p,f,r,g,r+1] = model.addVar(obj = 0, vtype=GRB.BINARY, name = "z_p,%s,%s,%s,%s,%s" % (p,f,r,g,r+1))

    # Binary decision variable z_sfg indicates whether product p is moved from postion f to g
    z_s = {}
    for s in no_stations:
        for r in shop_floors:
            for f in positions:
                for g in positions:
                    # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
                    z_s[s,f,r,g,r+1] = model.addVar(obj = 0, vtype = GRB.BINARY, name = "z_s,%s,%s,%s,%s,%s" % (s,f,r,g,r+1))


    # Binary decision variable y_i indicates whether student i is a leader (value = 1) or not (value = 0).
    y = {}
    for r in shop_floors:
        for f in positions:
            for p in no_products:
                for i in task_types_p[p-1]:
                    # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
                    y[i,p,f,r] = model.addVar(obj = 0, vtype=GRB.BINARY, name="y,%s,%s,%s,%s" % (i,p,f,r))


    # MINIMIZE Dmax
    model.modelSense = GRB.MINIMIZE
    
    # Update the model to make variables known. 
    # Update the model to make variables known. From now on, no variables should be added.
    model.update()


    # Add constraints
    # Max travelled distance Dmax is not exceeded
    model.addConstr(quicksum(dist[f,g]*c_p[p-1]*z_p[p,f,r,g,r+1] for p in no_products for r in shop_floors for f in positions for g in positions)+
                    quicksum(dist[f,g]*c_s[s-1]*z_s[s,f,r,g,r+1] for s in no_stations for r in shop_floors for f in positions for g in positions) <= Dmax)
    
    # Every job is assigned to exactly one position     
    for p in no_products:
        for i in task_types_p[p-1]:
            model.addConstr(quicksum(y[i,p,f,r] for r in shop_floors for f in positions) == 1)
            
    # Different jobs (tasks of different products) are not assigned to the same position in shop-floor instance r
    for p in no_products:
        for q in no_products:
            if q != p:
                for i in task_types_p[p-1]:
                    for j in task_types_p[q-1]:
                        for r in shop_floors:
                            for f in positions:
                                model.addConstr(y[i,p,f,r]+y[j,q,f,r] <= 1) 
    
    # Only one task of a product can be executed at one shop floor instance 
    for r in shop_floors:
        for p in no_products:
            for i in task_types_p[p-1]:
                for j in task_types_p[p-1]:
                    if j!=i:
                        model.addConstr(quicksum(y[i,p,f,r]+y[j,p,f,r] for f in positions) <= 1)
            

    # Product movement between steps  
    for p in no_products:
        for i in task_types_p[p-1]:
          for j in task_types_p[p-1]:
 #             if i == j-1 and h_ijp.get((i,j,p),0)==1:
                  for r in shop_floors:
                     for f in positions:
                         for g in positions:
                                if g != f:
                                    model.addConstr((y.get((i,p,f,r),0)+y.get((j,p,g,r+1),0))-1 <= z_p[p,f,r,g,r+1])
                                
    # Station movement between steps 
    for s in no_stations:                             
        for p in no_products:
            for q in no_products:
                if q!= p:
                    for i in task_types_p[p-1]:
                        for j in task_types_p[q-1]:
#                            if a.get((i,p,s),0)==1 and a.get((q,j,s),0)==1:
                                for r in shop_floors:
                                    for f in positions:
                                        for g in positions:
                                            if g!=f:
                                                model.addConstr((y.get((i,p,f,r),0)+y.get((j,q,g,r+1),0))-1 <= z_s[s,f,r,g,r+1])
    
    
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