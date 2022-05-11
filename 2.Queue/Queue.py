
# Queue implementation using python 
# it follow the FIFO rule 
class Queue:
    def __init__(self,queue):
        '''constructor which takes the empty queue at initialization '''
        self.queue=queue
    def isEmpty(self):
        ''' function to check whether queue is empty or not'''
        if not self.queue:
            return True
        else:
            return False
    def traversal(self):
        '''function to traverse the queue '''
        if len(self.queue)==0:
            print('queue is empty at the moment , add some data first\n')
            return 
        for i in self.queue:
            print(i)
    def enqueue(self):
        '''function to enter the new data at the top of the queue'''
        data=int(input('Enter the new element to add -> '))
        self.queue.append(data)
        print(f'{data} is added in the queue...\n')
    def dequeue(self):
        '''function to remove the top element from the queue'''
        if not self.queue:
            print('queue is empty you need to add first..\n')
        else:
            data=self.queue.pop(0)
            print(f'{data} is removed from the queue\n')



def menu():
    print('Enter 1 for Enqueue')
    print('Enter 2 for Dequeue')
    print('Enter 3 for Traveesal')
    print('Enter 4 for check IsEmpty')
    print('Enter 0 for EXIT')
    try:
        num=int(input('Enter the choice you want\n -> '))
        return num
    except Exception as e:
            print('Enter only number .... you have enter character\n')
            
queue=[]
if __name__=='__main__':
    print('\n\n\n\t\t\t\tqueue Implementation using python\n\n')
    q=Queue(queue)
    while 1:
        num=menu()
        try:
            if num==1:
                q.enqueue()
            elif num==2:
                q.dequeue()
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
            





