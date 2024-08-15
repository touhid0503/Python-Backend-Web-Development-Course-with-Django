try:
    x = int(input("Enter a number: "))
    print(x, "this is an integer number")
except ValueError:
    print("Wrong... Please try again")
else:
    print("nothing went wrong")
finally:
    print("done")