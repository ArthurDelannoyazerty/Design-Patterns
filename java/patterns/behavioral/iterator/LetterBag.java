package patterns.behavioral.iterator;

class LetterBag {
    public String[] names = {"R" , "J" ,"A" , "L"};
    public Iterator getIterator() {
        return new NameIterator();
    }
    class NameIterator implements Iterator {
        int index;
        @Override
        public boolean hasNext() {
            return index < names.length;
        }
        @Override
        public Object next() {
            if(this.hasNext()){
                return names[index++];
            }
            return null;
        }
    }
}
