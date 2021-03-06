abstract class Polygonal {
    private long index = 0;
    protected long current = 0;

    public abstract long function(long index);

    long reset() {
        index = 0;
        current = 0;
        return current;
    }

    public long current() {
        return current;
    }

    public long next() {
        index++;
        current = function(index);
        return current;
    }

    boolean isPolygonal(long number) {
        long index = 1;
        while (function(index) < number) index++;
        return function(index) == number;
    }
}

class Triangular extends Polygonal {
    public long function(long index) {
        return index * (index + 1) / 2;
    }
}

class Pentagonal extends Polygonal {
    public long function(long index) {
        return index * (3 * index - 1) / 2;
    }
}

class Hexagonal extends Pentagonal {
    public long function(long index) {
        return index * (2 * index - 1);
    }
}
