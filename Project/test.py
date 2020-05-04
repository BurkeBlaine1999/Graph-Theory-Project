from match import * 


"""A set of premade tests in order to determine 
if the code is working properly.
"""
def runTests():
        tests = [
                ["a.b|b*","bbbbbb",True],
                ["a.b|b*","bbbbbbx",False],
                ["a.b","ab",True],
                ["b**","b",True],
                ["b*","",True],
                ["a|b","a",True],
                ["a|b","ab",False],
                ["a.b|c","ab",True],
                ["a.b|c","c",True],
                ["a.b|c","ac",False]
            ]

        for test in tests:
            assert match(test[0],test[1]) == test[2],test[0] + \
            (" should match " if test[2] else " should not ") + test[1]

        print("\n All tests were completed successfully!\n ")



if __name__ == "__main__":
        tests = [
                ["a.b|b*","bbbbbb",True],
                ["a.b|b*","bbbbbbx",False],
                ["a.b","ab",True],
                ["b**","b",True],
                ["b*","",True],
                ["a|b","a",True],
                ["a|b","ab",False],
                ["a.b|c","ab",True],
                ["a.b|c","c",True],
                ["a.b|c","ac",False]
            ]

        for test in tests:
            assert match(test[0],test[1]) == test[2],test[0] + \
            (" should match " if test[2] else " should not ") + test[1]

        print("\n All tests were completed successfully! \n")
