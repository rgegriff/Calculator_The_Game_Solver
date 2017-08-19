# Calculator_The_Game_Solver
I hacked together a very simple solver for calculator the game

Arguments to solve():
  `moves` is the number of moves allowed in the level
  `goal` is the desired final value
  `function` is a list of transformation functions to apply to the value

example:
    allowed_functions = [
      append_digit(12), # adds 12 to the end of the value
      add(1), # adds 1 to the value
      replace(12, 2),
      reverse()
    ]
    solve(moves=5, start=12, goal=123, functions=allowed_functions)

## Supported Button Functions
All of the functions generate callable functions. This is to allow dynamic generation of transforms on the value

- add(x)
  Adds x to the value
- sub(x)
  Subtracts x from the value
- reverse()
  Reverses the value
- div_by(x)
  Divides the value by x
- mul_by(x)
  Multiplies the value by x
- append_digit(x)
  Appends x to the end of the value
- drop_last()
  Drops the final digit of the value
- replace(old, new)
  Replaces every instance of old in new
- sum_value()
  Sums all digits in value

You can also view the name of the transform functions with `.name`
Example:
    transform_function = add(3)
    transform_function(7) # returns 10
    transform_function.name # returns 'add(3)'
