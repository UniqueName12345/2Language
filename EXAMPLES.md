# Syntax for 2Language

### Boilerplate for 2Language example program:
```
terminal.print("Hello, world!");
```

### Random number generator:
```
var rand = Random.new();
terminal.print(rand.nextDouble()); (nextDouble() returns a double between the random number and a number (defaults to 1000 if no number is given))
```
### Random number game:
```
var rand = Random.new();
var guess = readInt("Guess a number between 1 and 100: ");
if the (guess) is (rand.nextInt(100)) {
    terminal.print("You guessed correctly!");
}
else if not {
    terminal.print("You guessed incorrectly!");
}
}
```

### Define and call another function:
Not implemented yet.

### FizzBuzz:
```
variable i = 1;
while (i) is less than or equal to (100) {
    if (i) is divisible by (3) and (5) {
        terminal.print("FizzBuzz");
    }
    else if (i) is divisible by (3) {
        terminal.print("Fizz");
    }
    else if (i) is divisible by (5) {
        terminal.print("Buzz");
    }
    else {
        terminal.print(i);
    }
    i = i + 1;
}
```