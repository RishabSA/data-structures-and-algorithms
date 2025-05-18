import random
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def Insert(self, val):
        if self.root == None:
            self.root = Node(val=val)
        else:
            self._InsertNode(self.root, val)

        self.count += 1

    # O(log(N))
    def _InsertNode(self, currentNode, val):
        if val < currentNode.val:
            if currentNode.left == None:
                currentNode.left = Node(val=val)
            else:
                self._InsertNode(currentNode.left, val)
        else:
            if currentNode.right == None:
                currentNode.right = Node(val=val)
            else:
                self._InsertNode(currentNode.right, val)

    def FindNode(self, val):
        return self._FindNode(self.root, val)

    # O(log(N))
    def _FindNode(self, currentNode, val):
        if currentNode == None:
            return None

        if val == currentNode.val:
            return currentNode

        if val < currentNode.val:
            return self._FindNode(currentNode.left, val)
        else:
            return self._FindNode(currentNode.right, val)

    def FindParent(self, val):
        if self.root == None:
            return None
        else:
            return self._FindParent(self.root, val)

    def _FindParent(self, currentNode, val):
        if currentNode.val == val:
            return None

        if val < currentNode.val:
            if currentNode.left == None:
                return None
            elif currentNode.left.val == val:
                return currentNode
            else:
                return self._FindParent(currentNode.left, val)
        else:
            if currentNode.right == None:
                return None
            elif currentNode.right.val == val:
                return currentNode
            else:
                return self._FindParent(currentNode.right, val)

    # (O(log(N)))
    def Remove(self, val):
        if self.root == None:
            return False

        nodeToRemove = self.FindNode(val)
        if nodeToRemove == None:
            return False

        if self.count == 1:
            self.root = None
            self.count -= 1
            return True

        parent = self.FindParent(val)
        if nodeToRemove.left == None and nodeToRemove.right == None:
            # Case 1. the value to remove is a leaf node
            if nodeToRemove.val < parent.val:
                parent.left = None
            else:
                parent.right = None
        elif nodeToRemove.left == None and nodeToRemove.right != None:
            # Case 2. the value to remove has a right subtree, but no left subtree
            if nodeToRemove.val < parent.val:
                parent.left = nodeToRemove.right
            else:
                parent.right = nodeToRemove.right
        elif nodeToRemove.left != None and nodeToRemove.right == None:
            # Case 3. the value to remove has a left subtree, but no right subtree
            if nodeToRemove.val < parent.val:
                parent.left = nodeToRemove.left
            else:
                parent.right = nodeToRemove.left
        else:
            # Case 4. the value to remove has both a left and right subtree, so we promote the largest value in the left subtree.
            largestVal = nodeToRemove.left
            while largestVal.right != None:
                # find the largest value in the left subtree of nodeToRemove
                largestVal = largestVal.right

            self.FindParent(largestVal.val).right = None
            nodeToRemove.val = largestVal.val

        self.count -= 1
        return True

    # O(N)
    def PreOrder(self, currentNode):
        treeList = []

        if currentNode != None:
            treeList.append(currentNode.val)
            treeList.extend(self.PreOrder(currentNode.left))
            treeList.extend(self.PreOrder(currentNode.right))

        return treeList

    def PrintPreOrderTree(self):
        treeList = self.PreOrder(self.root)
        print(f"Pre Order Printed Tree: {treeList}")

    # O(N)
    def PostOrder(self, currentNode):
        treeList = []

        if currentNode != None:
            treeList.extend(self.PostOrder(currentNode.left))
            treeList.extend(self.PostOrder(currentNode.right))
            treeList.append(currentNode.val)

        return treeList

    def PrintPostOrderTree(self):
        treeList = self.PostOrder(self.root)
        print(f"Post Order Printed Tree: {treeList}")

    # O(N)
    def InOrder(self, currentNode):
        treeList = []

        if currentNode != None:
            treeList.extend(self.InOrder(currentNode.left))
            treeList.append(currentNode.val)
            treeList.extend(self.InOrder(currentNode.right))

        return treeList

    def PrintInOrderTree(self):
        treeList = self.InOrder(self.root)
        print(f"In Order Printed Tree: {treeList}")

    def BreadthFirst(self):
        if self.root != None:
            treeList = []

            queue = deque()
            currentNode = self.root
            while currentNode != None:
                treeList.append(currentNode.val)
                if currentNode.left != None:
                    queue.append(currentNode.left)

                if currentNode.right != None:
                    queue.append(currentNode.right)

                if len(queue) == 0:
                    currentNode = None
                else:
                    currentNode = queue.popleft()

            return treeList

        else:
            return []

    def PrintBreadthFirst(self):
        treeList = self.BreadthFirst()
        print(f"Breadth First Printed Tree: {treeList}")

    def MaxDepth(self):
        return self._MaxDepth(self.root)

    def _MaxDepth(self, currentNode):
        if currentNode == None:
            return 0

        return 1 + max(
            self._MaxDepth(currentNode.left), self._MaxDepth(currentNode.right)
        )

    def MinDepth(self):
        return self._MinDepth(self.root)

    def _MinDepth(self, currentNode):
        if currentNode == None:
            return 0
        elif currentNode.left == None:
            return 1 + self._MinDepth(currentNode.right)
        elif currentNode.right == None:
            return 1 + self._MinDepth(currentNode.left)
        else:
            return 1 + min(
                self._MinDepth(currentNode.left), self._MinDepth(currentNode.right)
            )

    def MaxVal(self):
        if self.root == None:
            return None

        return self._MaxVal(self.root)

    # O(log(N))
    def _MaxVal(self, currentNode):
        if currentNode.right == None:
            return currentNode.val
        else:
            return self._MaxVal(currentNode.right)

    def MinVal(self):
        if self.root == None:
            return None

        return self._MinVal(self.root)

    # O(log(N))
    def _MinVal(self, currentNode):
        if currentNode.left == None:
            return currentNode.val
        else:
            return self._MinVal(currentNode.left)


if __name__ == "__main__":
    bst = BinarySearchTree()

    minimum, maximum, size = -100, 100, 10
    random.seed()
    insertedNums = [random.randint(minimum, maximum) for num in range(size)]
    print(f"Inserted Nums: {insertedNums}")

    for num in insertedNums:
        bst.Insert(num)

    print("\n")

    bst.PrintPreOrderTree()
    bst.PrintPostOrderTree()
    bst.PrintInOrderTree()
    bst.PrintBreadthFirst()

    print("\n")

    print(f"The Min Value of the BST is: {bst.MinVal()}")
    print(f"The Max Value of the BST is: {bst.MaxVal()}")

    print("\n")

    print(f"The Min Depth of the BST is: {bst.MinDepth()}")
    print(f"The Max Depth of the BST is: {bst.MaxDepth()}")

    bstNode5 = bst.FindNode(insertedNums[4])
    print(f"Found Node val: {bstNode5.val if bstNode5 else bstNode5}")

    bstNode2 = bst.FindNode(insertedNums[1])
    print(f"Found Node val: {bstNode2.val if bstNode2 else bstNode2}")

    bstNodeNone = bst.FindNode(200)
    print(f"Found Node val: {bstNodeNone.val if bstNodeNone else bstNodeNone}")

    print("\n")

    parentVals = []

    for num in insertedNums:
        parentNode = bst.FindParent(num)
        parentVals.append((num, parentNode.val if parentNode else parentNode))

    print(f"Parents of Inserted Nodes: {parentVals}")

    print("\n")
    bst.PrintInOrderTree()

    print(
        f"Successfully removed {insertedNums[2]}"
        if bst.Remove(insertedNums[2])
        else f"Failed to remove {insertedNums[2]}"
    )
    print(
        f"Successfully removed {103}" if bst.Remove(103) else f"Failed to remove {103}"
    )

    bst.PrintInOrderTree()

    print("\n")
