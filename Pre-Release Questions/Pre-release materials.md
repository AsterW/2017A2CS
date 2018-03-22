# Pre-release materials
## Task 1
### task 1.1
JSP structure diagrams show the basic structure of the program and functions within it. Basic operations like comparisons and if statement are also shown.

### task 1.2
The * sign means an iteration takes place.
The o sign means a selection takes place between two conditions.

### task 1.3
``NOT EOF
Salary > 50
Salary >= 90
"Project Manager."
"Lead Developer."
"Manager."
``

### task 1.4
Under the condition `Salary > 50` is `FALSE`, add a condition `Salary > 70`. Under this new condition, add an operation called "Assign Consultant".

### task 1.5
Add under line 9:
``IF Salary > 70
	THEN Role <- "Consultant."
	ELSE Role <- "Lead Developer."
ENDIF``
Delete line 9.

### task 1.6
``def role(salary):
	s = salary
	role = ""
	if s > 50:
		if s >= 90:
			role = "Project Manager."
		elif s > 70:
			role = "Consultant."
		else:
			role = "Lead Developer."
	else:
		role =  "Manager."
	return role``
