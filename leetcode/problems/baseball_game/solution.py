class Solution:
    def calPoints(self, ops: List[str]) -> int:
        self.stack = []
        
        for op in ops:
            op_result = self.do_operation(op)
            if op_result and isinstance(op_result, int):
                self.stack.append(op_result)
        
        return sum(self.stack)
        
    def do_operation(self, op):
        try:
            return int(op)
        except ValueError as e:
            if op == "+":
                return int(self.stack[len(self.stack)-1]) + int(self.stack[len(self.stack)-2])
            elif op == "D":
                return int(self.stack[len(self.stack)-1]) * 2
            elif op == "C":
                self.stack.pop()
            return