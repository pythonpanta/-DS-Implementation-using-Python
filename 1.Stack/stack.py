
# stack implementation using python 
class Stack:
    def __init__(self,stack):
        '''constructor which takes the empty stack at initialization '''
        self.stack=stack
    def isEmpty(self):
        ''' function to check whether stack is empty or not'''
        if not self.stack:
            return True
        else:
            return False
    def traversal(self):
        '''function to traverse the stack '''
        if len(self.stack)==0:
            print('Stack is empty at the moment , add some data first\n')
            return 
        for i in self.stack:
            print(i)
    def push(self):
        '''function to enter the new data at the top of the stack'''
        data=int(input('Enter the new element to add -> '))
        self.stack.append(data)
    def pop(self):
        '''function to remove the top element from the stack'''
        if len(self.stack) ==0:
            print('Stack is empty you need to add first..')
        else:
            data=self.stack.pop()
            print(f'{data} is removed from the stack')

stack=[]

def menu():
    print('Enter 1 for PUSH')
    print('Enter 2 for POP')
    print('Enter 3 for Traveesal')
    print('Enter 4 for check IsEmpty')
    print('Enter 0 for EXIT')
    num=int(input('Enter the choice you want\n -> '))
    return num

if __name__=='__main__':
    print('\n\n\n\t\t\t\tStack Implementation using python\n\n')
    s=Stack(stack)
    while 1:
        num=menu()
        try:
            if num==1:
                s.push()
            elif num==2:
                s.pop()
            elif num==3:
                s.traversal()
            elif num==4:
                print(s.isEmpty())
            elif num==0:
                print('thank you for your time.... ')
                break
            else:
                print('Enter the correct option mention above.....')

            
            d=input('enter y for continue otherwise enter any key for exit()\n -> ' )
            if d.lower()!='y':
                break

        except Exception as e:
            print('Error:',e)
            





