def FooBarOutput(start, end):
    output = ""
    for i in range(start, end + 1):
        if i % 3 == 0:
            output += "Foo"
        if i % 5 == 0:
            output += "Bar"
        if i % 3 != 0 and i % 5 != 0:
            output += str(i)
        output += " "
    return output[:-1]


print('FooBarOutput: ', FooBarOutput(1,100))