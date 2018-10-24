from gurobipy import *

def solve(products, stations, data):
    # Model
    model = Model("Assignment")
    
    
    station_IDs = list()
    processing_times = list()
    durations = dict()
    d_ips = dict()
    
    # Sorting Parameters
    # Stations
    capabilities = [s[2] for s in stations]
    times = [s[3] for s in stations]
    
    # Products
    task_types_p = []
    task_types_float = []
    task_types = []
    product_IDs = []

    no_stations = data.get_station_ids()
    no_products = data.get_product_ids()
    task_types_p = data.get_task_ids()
    
    d_is_p = dict()
    for station in data.stations:
        for product in data.products:
            for task in data.tasks:
                d_is_p[station.id, product.id, task.id] = 0

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
