# pqueue implementation using python
class Prioritypqueue:
    def __init__(self,pqueue):
        '''constructor which takes the empty pqueue at initialization '''
        self.pqueue=pqueue
    def isEmpty(self):
        ''' function to check whether pqueue is empty or not'''
        if not self.pqueue:
            return True
        else:
            return False
    def traversal(self):
        '''function to traverse the pqueue '''
        if len(self.pqueue)==0:
            print('pqueue is empty at the moment , add some data first\n')
            return 
        for i in self.pqueue:
            print(i)
    def enpqueue(self):
        '''function to enter the new data at the top of the pqueue'''
        data=int(input('Enter the new element to add -> '))
        self.pqueue.append(data)
        
        print(f'{data} is added in the pqueue...\n')
    def depqueue(self):
        '''function to remove the top element from the pqueue'''
        if not self.pqueue:
            print('pqueue is empty you need to add first..\n')
        else:
            data=self.pqueue.pop(0)
            print(f'{data} is removed from the pqueue\n')



def menu():
    print('Enter 1 for Enpqueue')
    print('Enter 2 for Depqueue')
    print('Enter 3 for Traveesal')
    print('Enter 4 for check IsEmpty')
    print('Enter 0 for EXIT')
    try:
        num=int(input('Enter the choice you want\n -> '))
        return num
    except Exception as e:
            print('Enter only number .... you have enter character\n')
            
pqueue=[100,3,5,1,7,2,8,9]
if __name__=='__main__':
    print('\n\n\n\t\t\t\tpqueue Implementation using python\n\n')
    q=Prioritypqueue(pqueue)
    while 1:
        num=menu()
        # pqueue.sort(reverse=True)  #for arranging in ascending order 
        pqueue.sort()
        # as it is priority queue so we make the priority as the decending number 
        try:
            if num==1:
                q.enpqueue()
            elif num==2:
                q.depqueue()
            elif num==3:
                q.traversal()
            elif num==4:
                print(q.isEmpty())
            elif num==0:
                print('thank you for your time.... ')
                break
            else:
                print('Enter the correct option mention above.....\n')

            
            d=input('enter y for continue otherwise enter any key for exit()\n -> ' )
            if d.lower()!='y':
                break

        except Exception as e:
            print('Error:',e)
            





