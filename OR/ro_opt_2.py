# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:39:04 2024
v2 Rebuilt on 4/12/24 to correct errors and implemented attraction factor

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
attr = {1: 1, 2: 1, 3:1}  # attraction factor for RO, larger is more

# mu_lo = 3
# mu_hi = 12
mu = 7   # fixing # of recruiters per office for now
M = 5*c*mu  # larger than total supply from an RO
epsilon = .001  # small # to enforce delta_i = 0 if sum(x_i_j over j)=0


# Set the verbosity level
pulp.LpSolverDefault.msg = 0  # Set to 0 for minimal output, 1 for normal, -1 for silent


# data.load_file(open(file_name))
ro_opt_model = LpProblem('Recruiting_Office_Placement_&_Sizing',LpMaximize)

# Variables
x = LpVariable.dicts('x',(roffices, markets),0,cat=LpContinuous) 
# mu = LpVariable.dicts('mu',roffices,0,cat=LpInteger)
delta = LpVariable.dicts('delta',roffices,0,cat=LpBinary)

# Objective function
ro_opt_model += lpSum(x[i][j] for i in roffices for j in AR_mkts[i]) 

# Constraints
for i in roffices:
    ro_opt_model += lpSum(x[i][j] for j in AR_mkts[i]) <= c * mu,   \
                    f'RO_{i} staffing supply capacity'
    # ro_opt_model += mu[i] >= mu_lo * delta[i], f'RO_{i} staff lower bound'
    # ro_opt_model += mu[i] <= mu_hi * delta[i], f'RO_{i} staff upper bound'

for j in markets:
    tmp_sum = 0
    if j in IR_ros.keys():   # if this mkt is in IR of an RO
        tmp_sum += lpSum(attr[i]*x[i][j] for i in IR_ros[j])
    if j in OR_ros.keys():   # if this mkt is in OR of an RO
        tmp_sum += w_or * lpSum(attr[i]*x[i][j] for i in OR_ros[j])
    if tmp_sum:
        ro_opt_model += tmp_sum <= d[j],  \
          f'RO accessions do not exceed market {j} demand'
    
# add indicator variable for RO constraint
for i in roffices:
    ro_opt_model += delta[i] >= lpSum(x[i][j] for j in AR_mkts[i]) / M
    
    ro_opt_model += delta[i] <= lpSum(x[i][j] for j in AR_mkts[i]) / epsilon
    
    
    
print(ro_opt_model)

ro_opt_model.solve()

for variable in ro_opt_model.variables():
    print(f"{variable.name}: {variable.varValue}")
   
    
def get_inflation_str(attr,x,i,j):
    if attr[i] == 1:
        extra_str = ''
    else:
        extra_str = ', which is adjusted by attraction factor '
        extra_str += f'{attr[i]} to {attr[i]*x[i][j].varValue} units'
    return extra_str

for i in roffices:
 
    print(f'Of a total of {c*mu} units:')
    for j in markets:
        if attr[i] == 1:
            extra_str = ''
        else:
            extra_str = '\n which is adjusted by attraction factor '
            extra_str += f'{attr[i]} to service {attr[i]*x[i][j].varValue} '
            extra_str += 'units of demand'

        print(f'RO{i} ships {x[i][j].varValue} units to MKT{j}',
              extra_str)
        if j in OR_mkts[i]:
            print(f'MKT{j} is an outer market of RO{i}')
    print()
    
for j in markets:
    print(f'Of a total demand of {d[j]} units:')
    for i in roffices:
        if attr[i] == 1:
            extra_str = ''
        else:
            extra_str = '\n which is adjusted by attraction factor '
            extra_str += f'{attr[i]} to service {attr[i]*x[i][j].varValue} '
            extra_str += 'units of demand'
     
        print(f'MKT{j} receives {x[i][j].varValue} units from RO{i}',extra_str)
    print()