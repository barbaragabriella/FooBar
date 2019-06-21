import FooBarProgram

test1 = '1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 FooBar 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 FooBar 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 FooBar 46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 FooBar 61 62 Foo 64 Bar Foo 67 68 Foo Bar 71 Foo 73 74 FooBar 76 77 Foo 79 Bar Foo 82 83 Foo Bar 86 Foo 88 89 FooBar 91 92 Foo 94 Bar Foo 97 98 Foo Bar'
test2 = ''
test3 = '4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 FooBar 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 FooBar 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 FooBar 46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 FooBar 61 62 Foo 64 Bar Foo 67 68 Foo Bar 71 Foo 73 74 FooBar 76 77 Foo 79 Bar Foo 82 83 Foo Bar 86 Foo 88 89 FooBar 91 92 Foo 94 Bar Foo 97 98 Foo'
test4 = '1'
test5 = 'FooBar'

test = [test1, test2, test3, test4, test5]
testRange = [[1,100],[19,15],[4,99],[1,1],[75,75]]
j = 0
for i in test:
    print(i == FooBarProgram.FooBarOutput(testRange[j][0],testRange[j][1]))
    j = j + 1