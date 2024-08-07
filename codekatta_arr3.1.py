
#get length of the list
len_list = int(input())

#get list of passports
list_of_passport = input().strip()

#convert list of passport to a proper list
given_list = list(list_of_passport.split(" "))
res = ''

#check for duplicates and find the result
for i in given_list:
    if i not in res:
        res = res +" "+ i
#print the results
print(res.strip())


"""You are a passport issuer, but due to some problems in the system, there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers. You are given a list of passport numbers.

Input Description:
You are given length of list.Second line,You are given with a list.

Output Description:
Print the list of passport numbers without duplicates.

Sample Input :
5
A23 B56 B56 C79 D16

Sample Output :
A23 B56 C79 D16"""
