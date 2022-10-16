package patterns.behavioral.interpreter;

class OrExpression implements Expression {

    private Expression expr1 = null;
    private Expression expr2 = null;

    public OrExpression(Expression expr1, Expression expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    public boolean evaluate(String context) {
        return expr1.evaluate(context) || expr2.evaluate(context);
    }
}
