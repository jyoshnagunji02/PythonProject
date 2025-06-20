#Example1: Writing Data to text file
file=open("C:/Users/Jyoshna/OneDrive/Documents/DemoFile/textfile.txt",'w')
file.write("this is my first text\n")
file.write("this is my second text\n")
file.write("this is my third text\n")
file.close()
print("completed")

#Example2: Read Data from text file
file=open("C:/Users/Jyoshna/OneDrive/Documents/DemoFile/textfile.txt",'r')
print(file.readline())  # first line will read
print(file.read())  # next lines will read
print(file.readline())   # once all lines are read, again it wont read
file.close()

#Example3: Append the data to existing file
file=open("C:/Users/Jyoshna/OneDrive/Documents/DemoFile/textfile.txt",'a')
file.write("\nthis is fourth text\n")
file.write("this is fifth text\n")
file.close()
print(" append completed")





