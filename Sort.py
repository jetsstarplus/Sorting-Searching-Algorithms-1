class BubbleStringList():
    def __init__(self) -> None:
        self.list: list = []
    
    def add(self, string: str) -> list:
        self.list.append(string)
        return self.list

    def sort(self):
        for i in range(len(self.list)):
            for j in range(len(self.list) - 1, i, -1):
                if self.list[j] < self.list[j - 1]:
                    self.swap(j, j - 1)

    def swap(self, x, y):
        temp = self.list[x]
        self.list[x] = self.list[y]
        self.list[y] = temp

class MergeStringList():
    def __init__(self) -> None:
        self.list: list = []

    def add(self, string: str) -> list:
        self.list.append(string)
        return self.list

    def sort(self, listToSort: list) -> list:
        if len(listToSort) > 1:
            mid = len(listToSort)//2
            left = listToSort[:mid]
            right = listToSort[mid:]
            self.sort(left)
            self.sort(right)
            i = j = k = 0
            while i< len(left) and j < len(right):
                if left[i] < right[i]:
                    listToSort[k] = left[i]
                    i += 1
                else:
                    listToSort[k] = right[j]
                    j += 1
                k += 1
            while i< len(left):
                listToSort[k] = left[i]
                i += 1
                k += 1
            self.list = listToSort


class QuickStringList():
    def __init__(self) -> None:
        self.list: list = []

    def add(self, string: str) -> list:
        self.list.append(string)
        return self.list

    def swap(self,listToSort: list, x: int, y: int):
        temp = listToSort[x]
        listToSort[x] = listToSort[y]
        listToSort[y] = temp

    def sort(self, listToSort: list, low: int, high: int):
        if low < high:
            pivot = self.divide(listToSort, low, high)
            self.sort(listToSort, low, pivot - 1)
            self.sort(listToSort, pivot + 1, high)
        self.list = listToSort
            
    def divide(self, listToSort: list, low, high) -> int:
        pivot = low
        self.swap(listToSort, pivot, high)
        for i in range(low, high):
            if listToSort[i] <= listToSort[high]:
                self.swap(listToSort, i, low)
                low += 1
        self.swap(listToSort, low, high)
        return low

# sort_list = QuickStringList();
# sample_list = ["Swedish","McFish","Puff Daddy","Floater","Wave","Chips","Bob","Flotsam","Miso","Cod","Finley","Finneus",
# "Larry","Salmon","Sea Beast","Otto","Sardine","Pirate","Captain Jack Sparrow","Long John Silver"]

# for string in sample_list:
#     sort_list.add(string=string)

# sort_list.sort(sort_list.list, 0, len(sort_list.list)-1)
# print(sort_list.list)