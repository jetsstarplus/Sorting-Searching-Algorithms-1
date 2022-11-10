from binary_tree import Node

class BinaryTreeStringList:
    def __init__(self) -> None:
        self.root: Node = None
        self.connections: int = 0
        self.stringList: list = []
    
    def find(self, data):
        '''
        Worst case time complexity is O(n) since we can navigate the whole tree
        '''
        currentNode: Node = self.root
        while currentNode:
            if data == currentNode.getData():
                return currentNode.getData()
            if data < currentNode.getData():
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
            self.connections += 1
        return None

    def all(self):
        currentNode: Node = self.root
        self.stringList: list = []
        self.allNodes(self.root)
        return self.stringList

    def allNodes(self, currentNode: Node):
        '''
        Worst case time complexity is O(n) since we can navigate the whole tree
        '''
        while currentNode:
            self.stringList.append(currentNode.getData())
            if not currentNode.getLeft() is None:
                return(self.allNodes(currentNode.getLeft()))
            else:
                return(self.allNodes(currentNode.getRight()))

    def add(self, data):
        self.insertNode(self.root, data)

    def insertNode(self, root: Node, data: str):
        node: Node = Node()
        node.setData(data)

        if self.root is None:
            self.root = node
        else:
            if root.getData() > node.getData():
                if root.getLeft() is None:
                    root.setLeft(node)
                else:
                    return(self.insertNode(root.left, data))
            else:
                if root.getRight() is None:
                    root.setRight(node)
                else:
                    return(self.insertNode(root.right, data))
