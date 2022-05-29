from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, GLPK

model = LpProblem(name="small-problem", sense=LpMaximize)

x = LpVariable(name="x", lowBound=0, cat="Integer")
y = LpVariable(name="y", lowBound=0)

model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

model += lpSum([x, 2 * y])

status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
  print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
  print(f"{name}: {constraint.value()}")

model.solver


