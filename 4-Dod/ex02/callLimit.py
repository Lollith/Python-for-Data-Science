def callLimit(limit: int):
    '''takes as argument a call limit of another function and blocks
its execution above a limit.'''
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            try:
                if count >= limit:
                    raise TypeError(f"Error: {function} call too many times")
                else:
                    count += 1
                    return (function(*args, **kwds))
            except TypeError as e:
                print(e)
                return None
        return limit_function  # va executer la fonction limit_function
    return callLimiter


if __name__ == "__main__":
    @callLimit(3)
    def f():
        print("f()")
    # f = callLimit(3)
    # print(f())

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()
