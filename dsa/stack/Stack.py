class Stack:
    def __init__(self) -> None:
        self.maxsize = 3
        self.size = 0
        self.stack = []
        pass

    def isempty(self):
        if self.size == 0:
            return True
        return False

    def isfull(self):
        if self.size==self.maxsize:
            return True
        return False

    def push(self, ele):
        if self.isfull():
            return "max limit reached for stack, can't add more"
        else:
            self.stack.append(ele)
            self.size+=1
            return "element pushed successfully"
    
    def pop(self):
        if self.isempty():
            return "no element to pop, stack is empty"
        else:
            ele = self.stack[self.size-1]
            del self.stack[self.size-1]
            self.size -= 1
            return ele

    def peek(self):
        if not self.isempty():
            print("element at top")
            return self.stack[self.size-1]
        else:
            return "stack is empty"

    def display(self):
        if not self.isempty():
            print("elements in stack")
            for i in range (self.size-1,-1,-1):
                print(self.stack[i])
        else:
            print("stack is empty")



if __name__ == "__main__":
    stack = Stack()
    want_to_continue = True
    while want_to_continue:
        choice = int(input("enter your choice \n 1. Push\n 2. Pop\n 3. Peek\n 4. Display\n 5. Exit\n"))
        match choice:
            case 1 :
                ele = int(input("enter element to push: "))
                print(stack.push(ele))
            case 2:
                print(stack.pop())
            case 3:
                print(stack.peek())
            case 4:
                stack.display()
            case 5:
                want_to_continue = False





        









        
