# def test_func(param1="Hello", param2="Welcome"):
#     print(param1, param2)

# test_func()            # no arguments
# test_func(100, 200)    # arguments given
# test_func(None, 1000)  # arguments given
def show(*args):
    return(args)

s = show(8, 8, 9, "swarup")
print (s)