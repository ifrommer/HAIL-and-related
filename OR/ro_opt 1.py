# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:39:04 2024

@author: ifrommer
"""
from pulp import *
from amply import *

data = Amply("""
set parts;
param prodRate{parts, machines};
param yields{parts};
""")

M = 2  # Markets
R = 3  # Recruiting offices
markets = range(1,M+1)
roffices = range(1,R+1)

# Market sets relative to ROs
IR_mkts = {1:[1], 2:[1,2], 3:[2]}  # mkts within inner ring of RO i
OR_mkts = {1:[2], 2:[], 3:[]}  # mkts outside inner ring of R0 i, but
                                     #  inside outer ring of RO i
AR_mkts = {i:list(set(IR_mkts[i]+OR_mkts[i])) for i in IR_mkts.keys() }

# RO sets relative to markets
def make_inv_dict(input_dict):
    inv_dict = {}
    for k,v in input_dict.items():
        for x in v:
            inv_dict.setdefault(x, []).append(k)
    return inv_dict

IR_ros = make_inv_dict(IR_mkts)
OR_ros = make_inv_dict(OR_mkts)
AR_ros = make_inv_dict(AR_mkts)

d = {1: 200, 2: 200}  # potential accessions
c = 20  # recruits accessed per recruiter
w_or = 0.5  # outer ring recruiter reduction factor

# mu_lo = 3
# mu_hi = 12
mu = 7   # fixing # of recruiters per office for now

# data.load_file(open(file_name))
ro_opt_model = LpProblem('Recruiting_Office_Placement_&_Sizing',LpMaximize)


#x = LpVariable.dicts('x',(data.parts,data.machines),0,cat=LpContinuous) #LpInteger)
x = LpVariable.dicts('x',(roffices, markets),0,cat=LpContinuous) 
# mu = LpVariable.dicts('mu',roffices,0,cat=LpInteger)
delta = LpVariable.dicts('delta',roffices,0,cat=LpBinary)

# Objective function
ro_opt_model += lpSum(x[i][j] for i in roffices for j in AR_mkts[i])

# Constraints
for i in roffices:
    ro_opt_model += (             lpSum(x[i][j] for j in IR_mkts[i]) + 
                        (1./w_or)* lpSum(x[i][j] for j in OR_mkts[i])
                     )  <= c*mu, f'RO_{i} staffing supply capacity'
    # ro_opt_model += mu[i] >= mu_lo * delta[i], f'RO_{i} staff lower bound'
    # ro_opt_model += mu[i] <= mu_hi * delta[i], f'RO_{i} staff upper bound'

for j in markets:
    ro_opt_model += lpSum(x[i][j] for i in AR_ros[j]) <= d[j], \
        f'RO accessions do not exceed market {j} demand'
    
    
print(ro_opt_model)

ro_opt_model.solve()

for variable in ro_opt_model.variables():
    print(f"{variable.name}: {variable.varValue}")