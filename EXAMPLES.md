# Syntax for 2Language

### Boilerplate for 2Language example program:
```
terminal.print("Hello, world!");
```

### Random number generator:
```
var rand = Random.new();
terminal.print(rand.nextDouble()); && (nextDouble() returns a double between the random number and a number (defaults to 1000 if no number is given))
```
### Random number game:

No conditionals in 2Language yet, so...

If you try now, that means you can win **all the time**, which is _not_ what you want.

### Define and call another function:

There is no way to do it yet. Even if you tried to do it, at best, you would have [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code). And at worst, you would have several [years](https://en.wikipedia.org/wiki/century) of [debugging](https://en.wikipedia.org/wiki/Debugging) to do.

### FizzBuzz:

There currently isn't a way to loop a specific bit of code in 2Language OR to check if a variable is equal to a specific value.

This means the closest thing to FizzBuzz is this:

```
var i = 0;
terminal.print(i)
```

Which will just print the number.

## That's all for now.