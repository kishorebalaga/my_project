for i in range(1,10):
         f = open("test_write.txt","a")
         name = input("enter name")
         f.write(name)
         f.write("\n")
