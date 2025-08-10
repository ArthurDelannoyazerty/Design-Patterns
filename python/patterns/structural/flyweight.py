import random


class TreeType:
    """The Flyweight: Stores the intrinsic (shared) state"""
    def __init__(self, model: str, texture: str, color: str):
        self.model = model
        self.texture = texture
        self.color = color

    def render(self, x: int, y: int):
        print(f"Rendering {self.color} {self.model} at ({x}, {y}) (using texture: {self.texture})")


class TreeFactory:
    """The Flyweight Factory"""
    def __init__(self):
        self._tree_types = {}

    def get_tree_type(self, model: str, texture: str, color: str) -> TreeType:
        key = (model, texture, color)
        if key not in self._tree_types:
            print(f"Creating new TreeType: {model}")
            self._tree_types[key] = TreeType(model, texture, color)
        return self._tree_types[key]


class Tree:
    """The Context: stores extrinsic (unique) state  ((x, y) and a reference to a TreeType (flyweight))"""
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def render(self):
        # Delegate the rendering logic to the flyweight, passing the extrinsic state.
        self.tree_type.render(self.x, self.y)



# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
class Forest:
    """The Client"""
    def __init__(self, factory: TreeFactory):
        self._factory = factory
        self._trees:list[Tree] = []

    def plant_tree(self, x: int, y: int, model: str, texture: str, color: str):
        # The factory provides the flyweight (intrinsic state)
        tree_type = self._factory.get_tree_type(model, texture, color)
        
        # We create a new Tree (context) with the extrinsic state
        new_tree = Tree(x, y, tree_type)
        self._trees.append(new_tree)

    def render_forest(self):
        print(f"\n--- Rendering Forest ({len(self._trees)} trees) ---")
        for tree in self._trees:
            tree.render()
        print(f"Total unique TreeTypes in memory: {len(self._factory._tree_types)}")



if __name__ == "__main__":
    factory = TreeFactory()
    forest = Forest(factory)

    tree_configs = [
        ("Oak", "Oak Texture 1", "Green"),
        ("Pine", "Pine Texture 1", "Dark Green"),
        ("Maple", "Maple Texture 1", "Yellow")
    ]
    
    num_trees = 1000
    print(f"Planting {num_trees} trees...")
    
    for _ in range(num_trees):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        model, texture, color = random.choice(tree_configs)
        forest.plant_tree(x, y, model, texture, color)

    forest.render_forest()

# ---------------------------------- Output ---------------------------------- #

# ...
# Rendering Dark Green Pine at (183, 156) (using texture: Pine Texture 1)
# Rendering Dark Green Pine at (101, 659) (using texture: Pine Texture 1)
# Rendering Yellow Maple at (824, 975) (using texture: Maple Texture 1)
# Rendering Dark Green Pine at (980, 806) (using texture: Pine Texture 1)
# Total unique TreeTypes in memory: 3