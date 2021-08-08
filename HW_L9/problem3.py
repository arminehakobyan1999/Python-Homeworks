class TreeFactory:
 
    tree_types = {}
 
    @staticmethod
    def get_tree_type(name, color, texture):
        key = '-'.join([name, color, texture])

        if key not in TreeFactory.tree_types:
            TreeFactory.tree_types[key] = TreeType(name, color, texture)

        return TreeFactory.tree_types[key]

    @staticmethod
    def show_tree_types():
        for (index, tree_type) in TreeFactory.tree_types.items():
            print(f'{index}: name = {tree_type.name}, color = {tree_type.color}, texture = {tree_type.texture}')


class TreeType:

    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f'Drawing a tree type with name = {self.name}, color = {self.color}, texture = {self.texture} at coordinates ({x}, {y}) on canvas = {canvas} ...')
        print('End drawing tree type.')

class Tree:

    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        print(f'Drawing a tree on canvas = {canvas} ...')

        self.tree_type.draw(canvas, self.x, self.y)

        print('End drawing tree.')


class Forest:

    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)

        self.trees.append(tree)

        return tree

    def draw(self, canvas):
        print(f'Drawing a forest on canvas = {canvas} ...')

        for tree in self.trees:
            tree.draw(canvas)

        print('End drawing forest.')


forest = Forest()
forest.plant_tree(0, 0, 'Sequoia', 'black', 'Texture1')
forest.plant_tree(0, 1, 'Sequoia', 'black', 'Texture2')
forest.plant_tree(1, 0, 'Japanese Maple', 'green', 'Texture1')
forest.plant_tree(1, 1, 'Sequoia', 'black', 'Texture1')
forest.plant_tree(1, 2, 'Japanese Maple', 'green', 'Texture1')

forest.draw('Canvas')

TreeFactory.show_tree_types()
