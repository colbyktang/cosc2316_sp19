stringList = [["Dave", "Johnson"], ["John", "Johnson"], ["Rick", "Johnson"]]
for x in stringList:
    for y in x:
        print (y)
        if y == "John":
            print ("Found John!")
    print ("")
