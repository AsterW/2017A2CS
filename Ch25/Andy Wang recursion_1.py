#Andy Wang
#This is the solutions to recursion_1 in CodingBat
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def bunnyEars(n):
    if n == 0:
        return 0
    return bunnyEars(n-1) + 2

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def bunnyEars2(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return bunnyEars2(n-1) + 2
    else:
        return bunnyEars2(n-1) + 3

def triangle(n):
    if n == 0:
        return 0
    return n + triangle(n-1)

def sumDigits(n):
    if n == 0:
        return n
    return n % 10 + sumDigits(n//10)

def count7(n):
    if n == 0:
        return 0
    if n%10 == 7:
        return count7(n//10)+1
    return count7(n//10)

def count8(n):
    if n == 0:
        return 0
    if n%10 == 8:
        if (n//10)%10 == 8:
            return 2 + count8(n//10)
        else:
            return 1 + count8(n//10)
    return count8(n//10)

def powerN(n,p):
    if p == 0:
        return 1
    return n * powerN(n, p-1)

def countX(n):
    if len(n) == 0:
        return 0
    if n[len(n)-1] == "x":
        return 1 + countX(n[:-1])
    return countX(n[:-1])

def countHi(n):
    if len(n) == 1:
        return 0
    if n[len(n)-1] == "i" and n[len(n)-2] == "h":
        return 1 + countHi(n[:-1])
    return countHi(n[:-1])

def changeXY(n):
    if len(n) == 0:
        return ""
    if n[len(n)-1] == "x":
        return changeXY(n[:-1])+"y"
    return changeXY(n[:-1])+n[len(n)-1]

def changePi(n):
    if len(n) == 2:
        if n[len(n)-1] == "i":
            if n[len(n)-2] == "p":
                return "3.14"
        else:
            return n
    if n[len(n)-1] == "i":
        if n[len(n)-2] == "p":
            return changePi(n[:-2])+"3.14"
    return changePi(n[:-1])+n[len(n)-1]

def noX(n):
    if len(n) == 0:
        return ""
    if n[len(n)-1] == "x":
        return noX(n[:-1])
    else:
        return noX(n[:-1]) + n[len(n)-1]

def array6(n, i):
    if len(n) == 0:
        return False
    if n[i] == 6:
        return True
    return array6(n, i+1) 

def array11(n, i):
    if i == len(n):
        return 0
    if n[i] == 11:
        return 1 + array11(n, i+1)
    return array11(n, i+1)

def array220(n, i):
    if i == len(n)-1:
        return False
    if n[i+1] == 10 * n[i]:
        return True
    return array220(n, i+1)

def allStar(n):
    if len(n) == 1:
        return n
    return n[0] + "*" + allStar(n[1:])

def pairStar(n):
    if len(n) == 1:
        return n
    if n[0] == n[1]:
        return n[0] + "*" + n[1] + pairStar(n[2:])
    return n[0] + pairStar(n[1:])

def endX(n):
    if len(n) == 0:
        return ""
    if n[0] == "x":
        return endX(n[1:]) + "x"
    return n[0] + endX(n[1:])

def countPairs(n):
    if len(n) == 2:
        return 0
    if n[0] == n[2]:
        return 1 + countPairs(n[1:])
    return 0 + countPairs(n[1:])

def countAbc(n):
    if len(n) == 0:
        return 0
    if n[0:3] == "abc" or n[0:3] == "aba":
        return 1 + countAbc(n[2:])
    return 0 + countAbc(n[1:])

def count11(n):
    if len(n) == 0:
        return 0
    if n[0:2] == "11":
        return 1 + count11(n[2:])
    return 0 + count11(n[1:])

def stringClean(n):
    if len(n) == 0:
        return ""
    if len(n) == 1:
        return n
    if n[0] == n[1]:
        return stringClean(n[1:])
    return n[0] + stringClean(n[1:])

def countHi2(n):
    if len(n) == 0:
        return 0
    if n[0] == "x":
        if n[1:3] == "hi":
            return 0 + countHi2(n[3:])
    if n[0:2] == "hi":
            return 1 + countHi2(n[2:])
    return countHi2(n[1:])

def parenBit(n):
    if len(n) == 0:
        return ""
    if n[0] != "(":
        if n[len(n)-1] != ")":
            return parenBit(n[1:-1])
        return parenBit(n[1:])
    if n[len(n)-1] != ")":
        return parenBit(n[:-1])
    return n

def nestParen(n):
    if len(n) == 0:
        return True
    if n[0] == "(" and n[len(n)-1] == ")":
        return nestParen(n[1:-1])
    return False

def strCount(n, m):
    if len(n) == 0:
        return 0
    if n[0:len(m)] == m:
        return 1 + strCount(n[len(m):], m)
    return 0 + strCount(n[1:], m)

def strCopies(n, sub, d):
    if d <= 0:
        return True
    if len(n) < len(sub):
        return False
    if n[0:len(sub)] == sub:
        return strCopies(n[len(sub):], sub, d-1)
    return strCopies(n[1:], sub, d)

def strDist(string, sub):
    if len(string) == 0:
        return 0
    if string[0:len(sub)] != sub:
        return strDist(string[1:], sub)
    if string[-len(sub):] != sub:
        return strDist(string[:-1], sub)
    return len(string)

print("factorial(5)", factorial(5))
print("bunnyEars(8)", bunnyEars(8))
print("fibonacci(9)", fibonacci(9))
print("bunnyEars2(4)", bunnyEars2(4))
print("triangle(5)", triangle(5))
print("sumDigits(126)", sumDigits(126))
print("count7(717)", count7(717))
print("count8(8818)", count8(8818))
print("powerN(3,3)", powerN(3,3))
print("countX(xxixx)", countX("xxixx"))
print("countHi(xxhixx)", countHi("xxhixx"))
print("changeXY(xxhixx)", changeXY("xxhixx"))
print("changePi(pipixx)", changePi("pipixx"))
print("noX(xaxb)", noX("xaxb"))
print("array6([1,6,4], 0)", array6([1,6,4], 0))
print("array11([1,2,11,3,11,4], 0)", array11([1,2,11,3,11,4], 0))
print("arrau220([1,2,20,3], 0)", array220([1,2,20,3], 0))
print("allStar(hello)", allStar("hello"))
print("pairStar(xxyyhello)", pairStar("xxyyhello"))
print("endX(xhixhix)", endX("xhixhix"))
print("countPairs(AxAxA)", countPairs("AxAxA"))
print("countAbc(abaxxababc)", countAbc("abaxxababc"))
print("count11(11abc11)", count11("11abc11"))
print("stringClean(abbbcdd)", stringClean("abbbcdd"))
print("countHi2(hiahixhi)", countHi2("hiahixhi"))
print("parenBit(xxx(abc)xxx)", parenBit("xxx(abc)xxx"))
print("nestParen((((x)))", nestParen("(((x))"))
print("strCount(catcowcat, cat)", strCount("catcowcat", "cat"))
print("strCopies(catcowcat, cat, 2)", strCopies("catcowcat", "cat", 3))
print("strDist(cccatcowcatxxx, cat)", strDist("cccatcowcatxxx", "cat"))
