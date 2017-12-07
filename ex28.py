#True
True and True

#False
False and True

#False
1 == 1 and 2 == 1

#True
"test" == "test"

#True
1 == 1 or 2 != 1

#True
True and 1 == 1

#False
False and 0 != 0

#True
True or 1 == 1

#False
"test" == "testing"

#False
1 != 0 and 2 == 1

#True
"test" != "testing"

#False
"test" == 1

#True
not (True and False)

#False
not (1 == 1 and 0 != 1)

#False
not (10 == 1 or 1000 == 1000)

#False
not (1 != 10 or 3 == 4)

#True
not ("testing" == "testing" and "Zed" == "Cool Guy")

#True
1 == 1 and (not ("testing" == 1 or 1 == 0))

#False
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))

#False
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

True and (not (True))


