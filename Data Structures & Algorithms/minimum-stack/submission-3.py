class MinStack:

    def __init__(self):
        self.stack = [None]
        self.sp = 0
        self.min_val = []
        self.min_val_sp = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sp += 1
        if self.min_val:
            if val <= self.min_val[self.min_val_sp]:
                self.min_val.append(val)
                self.min_val_sp += 1
        else:
            self.min_val.append(val)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.min_val[self.min_val_sp]:
            self.min_val.pop()
            if self.min_val_sp != 0:
                self.min_val_sp -= 1                                                                
        self.sp -= 1

    def top(self) -> int:
        return self.stack[self.sp]

    def getMin(self) -> int:
        return self.min_val[self.min_val_sp]
