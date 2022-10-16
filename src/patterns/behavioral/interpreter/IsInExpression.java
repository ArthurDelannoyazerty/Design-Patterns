package patterns.behavioral.interpreter;

class IsInExpression implements Expression {
    private String data;

    public IsInExpression(String data) {
        this.data = data;
    }

    @Override
    public boolean evaluate(String context) {
        return context.contains(data);
    }
}
