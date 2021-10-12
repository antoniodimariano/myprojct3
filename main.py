def myfunc(my_str):
    try:
        return my_str[::-1]
    except Exception as error:
        return False


if __name__ == '__main__':
    print(myfunc('ciao')) #pragma no cover
