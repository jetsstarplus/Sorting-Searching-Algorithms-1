class SequentialStringList():
    def __init__(self) -> None:
        self.list: list = []
    
    def add(self, string: str) -> list:
        self.list.append(string)
        return self.list

    def find(self, string: str):
        for i in range(len(self.list)):
            if self.list[i] == string:
                return self.list[i]
        return None

class BinaryStringList():
    def __init__(self) -> None:
        self.list: list = []

    def add(self, string: str) -> list:
        self.list.append(string)
        return self.list

    def find(self, string: str):
        low: int = 0;
        high: int = len(self.list)-1
        while low < high:
            mid = (low + high)//2
            if self.list[mid] == string:
                return string
            if string > self.list[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return None