from gurobipy import *
from nge_fct import nge_fct as get_next_greatest

def solve(products, stations, positions, dist, a_ips, h_ijp, shop_floors, sampleData):
    # Model
    model = Model("Allocation")

    #Motion Factors for station list
    c_s = [s.motion_factor for s in sampleData.stations]

    #Motion factors for products
    c_p = [p.motion_factor for p in sampleData.products]

    no_stations = sampleData.get_station_ids()
    no_products = sampleData.get_product_ids()
    
    
    # Constructing handover parameters
    a = dict()
    a_another = dict()

    task_types_p = [p.tasks for p in sampleData.products]
    
    # Sorting handover parameters a[i,p,s]
    indices = a_ips[0]
    values = a_ips[1]
    
    for task_id in sampleData.get_task_ids():
        for product_id in sampleData.get_product_ids():
            for station_id in sampleData.get_station_ids():
                if [task_id, product_id, station_id] in indices:
                    a_another[task_id, product_id, station_id] = values[indices.index([task_id, product_id, station_id])]
                else:
                    a_another[task_id, product_id, station_id] = 0
    
    
    # Add decision variables
    # Continuous decision variable Dmax, that is maximal distance traveled by assembly participants, shall be minimized
    Dmax = model.addVar(obj=1, vtype = "C", name = "Dmax")

    # Binary decision variable z_pfg indicates whether product p is moved from postion f to g
    z_p = {}
    for p in no_products:
        for r in shop_floors:
            for v in shop_floors:
                if v > r:
                    for f in positions:
                        for g in positions:
                            if g!= f:
                                # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
                                z_p[p,f,r,g,v] = model.addVar(obj = 0, vtype=GRB.BINARY, name = "z_p,%s,%s,%s,%s,%s" % (p,f,r,g,r+1))

    # Binary decision variable z_sfg indicates whether product p is moved from postion f to g
    z_s = {}
    for s in no_stations:
        for r in shop_floors:
            for v in shop_floors:
                if v > r:
                    for f in positions:
                        for g in positions:
                            if g!=f:
                                # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
                                z_s[s,f,r,g,v] = model.addVar(obj = 0, vtype = GRB.BINARY, name = "z_s,%s,%s,%s,%s,%s" % (s,f,r,g,r+1))


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
    model.addConstr(quicksum(dist[f,g]*c_p[p-1]*z_p[p,f,r,g,v] for p in no_products for r in shop_floors for v in shop_floors if v>r for f in positions for g in positions if g!=f)+
                    quicksum(dist[f,g]*c_s[s-1]*z_s[s,f,r,g,v] for s in no_stations for r in shop_floors for v in shop_floors if v>r for f in positions for g in positions if g!=f) <= Dmax)
    
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
                for r in shop_floors:
                    for f in positions:
                        for g in positions:
                            if g != f:
                                nge_list = get_next_greatest(shop_floors, r, y[i, p, f, r], y[j, p, g, v])
                                if nge_list[0] == True:
                                    t = nge_list[1]
                                    model.addConstr((y.get((i,p,f,r),0)+y.get((j,p,g,t),0))-1 <= z_p[p,f,r,g,t])
                                
    # Station movement between steps 
    for s in no_stations:                             
        for p in no_products:
            for q in no_products:
                if q!= p:
                    for i in task_types_p[p-1]:
                        for j in task_types_p[q-1]:
                            for r in shop_floors:
                                for f in positions:
                                    for g in positions:
                                        if g!=f:
                                            nge_list = nge_fct(r,shop_floors,y[i,p,f,r],y[j,p,g,v])
                                            if nge_list[0] == True:
                                                t = nge_list[1]
                                                model.addConstr((y.get((i,p,f,r),0)+y.get((j,q,g,t),0))-1 <= z_s[s,f,r,g,t])
    
    
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