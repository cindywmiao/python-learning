def test_var_kwargs(**kwargs):
    #print("formal arg: %s" % farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

test_var_kwargs(myarg1=1, myarg2="two", myarg3=3)