'''
 Application1:Reverse String
'''
stack=[]
reverse=[]
n=int(input('Enter the length of senetence you want to enter -> '))
print('Enter the sentence :')
# taking the input from the user 
for i in range(n):
    stack.append(input(''))

 # for reverse the string 
for i in range(n):
    d=stack.pop()
    reverse.append(d)

print('Reverse Sting is as follow :')
# using loop to dispaly the reverse sting 
for i in reverse:
    print(i,end='')