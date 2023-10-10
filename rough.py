# # # code
# # # string = "$Gee*k;s..fo, r'Ge^eks?"
# # # print("".join(filter(lambda x : x.isalpha(),string)))

# # # # ----------------------------------------------------------------------------------------------------------
# # # List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# # # # Sort each sublist
# # # sortList = lambda x: (sorted(i) for i in x)
 
# # # # Get the second largest element
# # # secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
# # # res = secondLargest(List, sortList)
 
# # # print(res)
# # # ------------------------------------------------------------------------------------------------------------------

# # # f1 = open("file1.txt" , "r")
# # # f2 = open("file2.txt","r")
# # # f = open("file.txt" , "a")
# # # for i in f1:
# # #     if i!='EOL':
# # #         f.write(i)
# # # f.write('\n')
# # # for i in f2:
# # #     if i!='EOL':
# # #         f.write(i)
# # # f1.close()
# # # f2.close()
# # # f.close()
# # # -------------------------------------------------------------------------------------------------------------------------------------------------------------

# # # import csv
# # # fields=[]
# # # rows=[]
# # # with open("hotel_bookings.csv",'r') as csvfile:
# # #     csvreader = csv.reader(csvfile)
# # #     fields = next(csvreader)
# # #     for row in csvreader:
# # #         rows.append(row)
# # #     print("Total no of rows :%d " %(csvreader.line_num))
# # # for row in rows[:10]:
# # #     for col in row:
# # #         print("%10s"%col,end=" "),
# # #     print('\n')

# # # -----------------------------------------------------------------------------------------------------------------------
# # # import csv
# # # fields=['UserName'+ "\t" +'Password']
# # # rows=[['Dev'+ "\t" + "ddr123"] , ["Hetanshi"+"\t" +"het345"],["MAnsi"+"\t\t" + "rankm19"]]
# # # filename = "user_pwd.csv"
# # # with open("user_pwd.csv","w") as csvfile:
# # #     csvwriter = csv.writer(csvfile)
# # #     csvwriter.writerow(fields)
# # #     csvwriter.writerows(rows)
# # # csvfile.close()
# # # uid = input("Enter User name : ")
# # # pwd = input("Enter password : ")
# # # with open("user_pwd.csv","r") as csvfile:
# # #     csvreader = csv.reader(csvfile)
# # #     fields = next(csvreader)
# # #     for row in csvreader:
# # #         rows.append(row)
# # #     for row in rows[:3]:
# # #         for col in row:
# # #             print("%10s"%col,end=" "),
# # #         print('\n')
# # #     for row in rows[:3]:
# # #         for col in row:
# # #             if col==uid or col==pwd:
# # #                 print("True")
# # #             else:
# # #                 print("False")
# # #         print("\n")




# # # import csv
# # # with open("7.csv", "w") as obj:
# # #     fileobj = csv.writer(obj)
# # #     fileobj.writerow(["User Id", "password"])
# # #     while(True):
# # #         user_id = input("enter id: ")
# # #         password = input("enter password: ")
# # #         record = [user_id, password]
# # #         fileobj.writerow(record)
# # #         x = input("press Y/y to continue and N/n to terminate the program\n")
# # #         if x in "Nn":
# # #             break
# # #         elif x in "Yy":
# # #             continue
# # # with open("7.csv", "r") as obj2:
# # #     fileobj2 = csv.reader(obj2)
# # #     given = input("enter the user id to be searched\n")

# # #     for i in fileobj2:
# # #         next(fileobj2)

# # #         # print(i,given)
# # #         if i[0] == given:
# # #             print("YES it exists")
# # #             break

# # # ----------------------------------------------------------------------------------------------------------------------------------

# # # # importing csv module
# # # import csv
 
# # # # csv file name
# # # filename = "Shares.csv"
 
# # # # initializing the titles and rows list
# # # fields = []
# # # rows = []
 
# # # # reading csv file
# # # with open(filename, 'r') as csvfile:
# # #     # creating a csv reader object
# # #     csvreader = csv.reader(csvfile)
     
# # #     # extracting field names through first row
# # #     fields = next(csvreader)
 
# # #     # extracting each data row one by one
# # #     for row in csvreader:
# # #         rows.append(row)
 
# # #     # get total number of rows
# # #     print("Total no. of rows: %d"%(csvreader.line_num))
 
# # # # printing the field names
# # # print('Field names are:' + ', '.join(field for field in fields))
 
# # # # printing first 5 rows
# # # print('\nFirst 5 rows are:\n')
# # # for row in rows[:5]:
# # #     # parsing each column of a row
# # #     for col in row:
# # #         print("%10s"%col,end=" "),
# # #     print('\n')

# # # importing OrderedDict class from collections library
# # # An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted


# # # from collections import OrderedDict

# # # # defining a function 
# # # def checkOrder(input,pattern):
# # #     dict = OrderedDict.fromkeys(input)
# # #     ptrlen = 0
# # #     for key,value in dict.items():
# # #         if (key == pattern[ptrlen]):
# # #             ptrlen = ptrlen+1
# # #             if(ptrlen==(len(pattern))):
# # #                 return 'true'
# # #             return 'false'
# # # if __name__=="__main__":
# # #     input='engineers rock'
# # #     pattern='er'
# # #     print(checkOrder(input,pattern))


# # # # Python3 code to demonstrate working of
# # # # Group Similar items to Dictionary Values List
# # # # Using defaultdict + loop
# # # from collections import defaultdict,Counter
 
# # # # initializing list
# # # test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
 
# # # # printing original list
# # # print("The original list : " + str(test_list))
 
# # # # using defaultdict for default list
# # # res = defaultdict(list)
# # # for ele in test_list:
     
# # #     # appending Similar values
# # #     res[ele].append(ele)
 
# # # # printing result
# # # print("Similar grouped dictionary : " + str(dict(res)))
# # # print(Counter(test_list))

# # full_name=lambda fn,ln: "Hello !!! \n" + fn.strip().title() + " " +ln.strip().title()
# # # full name is func name
# # # strip method will discrad the spaces that are not needed
# # # tile will do first letter capital
# # # so lamba has made a fubnction full name with fn and ln as variable that will take input from user
# # # fun_name=lambda parameters : execution
# # # after colon the statement is 
# # print(full_name("   dev","MEHTA")) 
# # names=["dev mehta","  Dev  Mehta ","Dev Mehta","DEV MEHTA" ]
# # names.sort(key=lambda n :n.split(" ")[-1].lower())
# # print(names)
# # def build_quad_fun(a,b,c):
# #     return lambda x : a*x**2  + b*x  + c
# # f=build_quad_fun(2,3,-5)
# # print(f(0))
# # # we are returning lambda to f it has become a function of parameter x

# # warm = ['red', 'yellow', 'orange']

# # sortedwarm = warm.sort()

# # print(warm)

# # print(sortedwarm)



# # cool = ['grey', 'green', 'blue']

# # sortedcool = sorted(cool)

# # print(cool)

# # print(sortedcool)

# import matplotlib.pyplot as plt
# import pandas as pd

# icici = pd.read_csv("ICICIBANK.csv")
# axis = pd.read_csv("AXISBANK.csv")
# hdfc = pd.read_csv("HDFCBANK.csv")
# kotak = pd.read_csv("KOTAKBANK.csv")
# fig = plt.figure(figsize=(20,7),facecolor='white')
# #create a subplot with transparent facecolor
# ax = fig.add_subplot(111, facecolor='none')
# #plot thr data with different colors
# ax.plot(icici['Date'],icici['Trades'] , color='blue', label='ICICI')
# ax.plot(axis['Date'],axis['Trades'] , color='red', label='AXIS')
# ax.plot(hdfc['Date'],hdfc['Trades'] , color='grey', label='HDFC')
# ax.plot(kotak['Date'],kotak['Trades'] , color='green', label='KOTAK')
# # set titile,x-label,y-label
# ax.set_xlabel("year" , color='black')
# ax.set_ylabel("Price" , color='black')
# # set legend title color
# ax.legend(title='' , facecolor='white' , edgecolor='black' , labelcolor='black')
# # set tick color 
# ax.tick_params(colors='black')
# plt.show().

from collections import defaultdict
str=list('srusti')
print(str)
d=defaultdict()
for i in str:
    d[i].append[i]
print((dict(d)))