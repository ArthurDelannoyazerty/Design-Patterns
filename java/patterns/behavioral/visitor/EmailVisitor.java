package patterns.behavioral.visitor;

class EmailVisitor implements NodeVisitor {
    @Override
    public void visit(TreeNode n) {
        System.out.println("email:" + n.getName());
    }
}
