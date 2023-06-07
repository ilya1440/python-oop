class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj

    @classmethod
    def predict(cls, root, x):
        current_node = root
        while current_node.value is None:
            decision = x[current_node.indx]
            current_node = current_node.left if decision else current_node.right
        return current_node.value


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)


def main():
    print('Session started')


if __name__ == '__main__':
    main()