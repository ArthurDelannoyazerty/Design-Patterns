package patterns.behavioral.visitor;

class TreeNode {
    private String name;

    public TreeNode(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void accept(NodeVisitor v) {
        v.visit(this);
    }
}
