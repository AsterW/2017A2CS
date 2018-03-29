student(simon).
student(andy).
school(gt).
school(washu).
school(emory).

studentAdmittedTo(simon, gt).
studentAdmittedTo(andy, washu).
studentAdmittedTo(ken, emory)

match(X, Y) :- student(X), school(Y); student(Y), school(X).


vegetable(tomato).
vegetable(egg).
addOn(cheese).
addOn(pepperoni).
meat(beef).
meat(chicken).
ingredients(pizza, tomato, 100).
Ingredients(pizza, cheese, 50).
ingredients(pizza, egg, 75).


male(carl).
male(ken).
male(simon).
male(andy).

female(candice).
female(linda).
female(katherine).

/* Factorial */
factorial(0,1).
factorial(N, F) :-
	X is N - 1,
	factorial(X, Y),
	F is N * Y.

/* BunnyEars */
bunnyEars(0, 0).
bunnyEars(N, E) :-
	X is N - 1,
	bunnyEars(X, Y),
	E is 2 + Y.

/* Fibonacci */
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :-
	X is N - 1,
	fibonacci(X, Y),
	R is N - 2,
	fibonacci(R, Z),
	F is Y + Z.

/* List */
len([], 0).
len([_|T], L) :-
	len(T, X),
	L is X + 1.

/* reverse list */
rev([], []).
rev([A|B], R) :-
	rev(B, X),
	append(X, A, R).

eq([], []).
eq([A|B], [A|C]) :-
	eq(B, C).


