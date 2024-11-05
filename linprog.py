## PROGRAMACION LINEAL Y ENTERA:
from scipy.optimize import linprog
#Problema original:
#max -x_1+x_2
# sujeto a 
#x_1,x_2 positivos, 12x_1+11x_2<=63 y -22x_1+4x_2<=-33 
# pg 180 del libro de Jon Lee "Combinatorial Optimization"

#linprog siempre es minimización asi que multiplicamos por -1
obj = [1, -1]
lhs_ineq = [[12, 11],
            [-22,4],
            [-1,0],
            [0,-1]
            ]
rhs_ineq =[63,-33,0,0]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
(-1)* opt.fun #objective value (lprog upper bound)
opt.x# actual optimal point


#We do branch and bound...

#Branch along x_1
obj = [1, -1]
lhs_ineq = [[12, 11],
            [-22,4],
            [-1,0],
            [0,-1],
            [1,0],
            ]
rhs_ineq =[63,-33,0,0,2]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
(-1)* opt.fun #objective value
opt.x# actual optimal point
#other constraint on x_1
obj = [1, -1]
lhs_ineq = [[12, 11],
            [-22,4],
            [-1,0],
            [0,-1],
            [-1,0],
            ]
rhs_ineq =[63,-33,0,0,-3]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
(-1)* opt.fun #objective value
opt.x# actual optimal point

#We further branch the first subprogram
obj = [1, -1]
lhs_ineq = [[12, 11],
            [-22,4],
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
            ]
rhs_ineq =[63,-33,0,0,2,2]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
(-1)*opt.fun #objective value
opt.x# actual optimal point


obj = [1, -1]
lhs_ineq = [[12, 11],
            [-22,4],
            [-1,0],
            [0,-1],
            [1,0],
            [0,-1],
            ]
rhs_ineq =[63,-33,0,0,2,-3]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
(-1)*opt.fun #objective value
assert opt.success
opt.x# actual optimal point

#Ejercicio: 
#Complete el árbol de Branch and Bound para el problema original dibujando la región factible y el optimo en cada paso.
