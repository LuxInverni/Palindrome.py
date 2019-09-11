string = input("Please write a number or word:  ")
string2 = string[::-1]
print("Your answer and it reversed is: ", string, string2)

####Takes user input as string, makes a reversed copy string2

list1 = [string];
list2 = [string2];

n = 0
while n < len(list1):
    if list1[n] == list2[n]:
        n = n+1
        print(f"{string} is a Palindrome!")
    else:
        print("not Palindrome!")
        n = n+1
        
       
####Puts the strings into lists and does a While loop to compare the individual characters against each other.
