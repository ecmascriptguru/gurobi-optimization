from gurobipy import *

def assign_products(data):
    model = Model('Product Assignment')

    d_is_p = dict()
    a_is_p = dict()
    for product in data.products:
        for task in data.get_tasks_from_IDs(product.tasks):
            for station in data.get_S_i_p(task, product):
                d_is_p[task.id, station.id, product.id] = data.get_d_is_p(task)
                a_is_p[task.id, station.id, product.id] = model.addVar(
                                                            obj=d_is_p[task.id, station.id, product.id], 
                                                            vtype=GRB.BINARY, 
                                                            name="%s,%s,%s" % (task.id, station.id, product.id))
            
            model.addConstr(quicksum(a_is_p[task.id, station.id, product.id] for s in data.get_S_i_p(task, product)) == 1)
    
    model.update()
    model.modelSense=GRB.MINIMIZE
    model.optimize()

    result = dict()
    for var in model.getVars():
        result[var.VarName] = var.X

    return result