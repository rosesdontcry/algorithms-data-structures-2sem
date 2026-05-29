from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def search(self, value):
        return self._search(self.root, value, 0)

    def _search(self, node, value, comparisons):
        if node is None:
            return None, comparisons

        comparisons += 1

        if value == node.value:
            return node, comparisons
        if value < node.value:
            return self._search(node.left, value, comparisons)
        else:
            return self._search(node.right, value, comparisons)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def level_order(self):
        if self.root is None:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return node

    def draw(self):
        self._draw(self.root, 0, "root -> ")

    def _draw(self, node, level, prefix):
        if node:
            print("  " * level + prefix + str(node.value))
            self._draw(node.left, level + 1, "L ─> ")
            self._draw(node.right, level + 1, "R ─> ")

    @staticmethod
    def _find_min(node):
        while node.left is not None:
            node = node.left
        return node


def test1(data, keys_to_search, keys_to_delete):
    tree = BST()
    for val in data:
        tree.insert(val)

    print(f"Inorder: {' '.join(map(str, tree.inorder()))}")
    print(f"Preorder: {' '.join(map(str, tree.preorder()))}")
    print(f"Postorder: {' '.join(map(str, tree.postorder()))}")
    print(f"Level-order: {' '.join(map(str, tree.level_order()))}\n")
    tree.draw()

    print(f"\nTree height: {tree.get_height()}\n")

    for key in keys_to_search:
        _, comparisons = tree.search(key)
        print(f"Search: {key} -> {comparisons}")


    for key in keys_to_delete:
        tree.delete(key)
        print(f"\nAfter delete {key}:")
        print(f"Inorder: {' '.join(map(str, tree.inorder()))}")
        print(f"Level-order: {' '.join(map(str, tree.level_order()))}\n")
        tree.draw()

    print("\n" + "-"*50 + '\n')

def main():
    nods_sorted = [20, 30, 40, 50, 60, 70, 80, 90, 120]
    nods_random = [50, 30, 120, 70, 20, 90, 40, 60, 80]
    keys_to_search = [20, 80, 120]
    keys_to_delete = [20, 30, 50]

    test1(nods_random, keys_to_search, keys_to_delete)
    test1(nods_sorted, keys_to_search, keys_to_delete)


if __name__ == "__main__":
    main()
