class Logger:

    def __init__(self):
        self.msg = {}
        self.printed_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg.keys():
            self.msg.update({message : timestamp + 10})
            self.printed_timestamp.update({message: []})
            self.printed_timestamp[message].append(timestamp)
            return True
        
        if (timestamp >= self.msg[message]) and (timestamp not in self.printed_timestamp[message]):
            self.printed_timestamp[message].append(timestamp)
            self.msg.update({message : timestamp + 10})
            return True
        
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)