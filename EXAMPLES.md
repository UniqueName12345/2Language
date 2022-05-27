# ------ Syntax for 2Language ----------

### Boilerplate for 2Language example program:

```
public prog <progname>() {
    terminal.print("Hello, world!");
}
```

result: 0.30000000000000004

### Random number generator:

var rand = Random.new();
terminal.print(rand.nextDouble()); (nextDouble() returns a double between the random number and a number (defaults to 1000 if no number is given))

### Random number game:

public prog RNGGame() {
    var rand = Random.new();
    var guess = readInt("Guess a number between 1 and 100: ");
    if the (guess) is (rand.nextInt(100)) {
        terminal.print("You guessed correctly!");
    }
    else if not {
        terminal.print("You guessed incorrectly!");
    }
}

### Define and call another function:

public prog Test() {
    function()
}
public func function(){
    terminal.print("Hello, world!");
}


### FizzBuzz:

public prog FizzBuzz() {
    var i = 1;
    while the (i) is less than or equal to (100) {
        if the (i) is divisible by (3) and (5) {
            terminal.print("FizzBuzz");
            var i = i + 1; && (can also use i++ instead of var i = i + 1;)
        }
        else if the (i) is divisible by (3) {
            terminal.print("Fizz");
            var i = i + 1;
        }
        else if the (i) is divisible by (5) {
            terminal.print("Buzz");
            var i = i + 1;
        }
        else if not {
            terminal.print(i);
            var i = i + 1;
        }


That's all for now!