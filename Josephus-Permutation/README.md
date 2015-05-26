Josephus-Permutation
======

##Description:##
This problem takes its name by arguably the most important event in the life of
the ancient historian Josephus: according to his tale, he and his 40 soldiers
were trapped in a cave by the Romans during a siege.

Refusing to surrender to the enemy, they instead opted for mass suicide, with a
twist: **they formed a circle and proceeded to kill one man every three, until
one last man was left (and that he was supposed to kill himself to end the
act).**

Well, Josephus and another man were the last two and, as we now know every
detail of the story, you may have correctly guessed that they didn't exactly
follow through with the original idea.

You are now to create a function that returns a Josephus permutation, taking as
parameters the initial _array/list of items_ to be permuted as if they were in a
circle and counted every _k_ places until none remain.

###Tips and Notes:###
It helps to start counting from 1 up to _n_, instead of the usual range: 0 to 
_n_ -1; _k_ will always be greater than or equal to 1.

###Example###
For example, with `n = 7` and `k = 3`, `josephus(7, 3)` should act like this:

```
[1, 2, 3, 4, 5, 6, 7] - initial sequence
[1, 2, 4, 5, 6, 7] => 3 is counted out and goes into the result [3]
[1, 2, 4, 5, 7] => 6 is counted out and goes into the result [3, 6]
[1, 4, 5, 7] => 2 is counted out and goes into the result [3, 6, 2]
[1, 4, 5] => 7 is counted out and goes into the result [3, 6, 2, 7]
[1, 4] => 5 is counted out and goes into the result [3, 6, 2, 7, 5]
[4] => 1 is counted out and goes into the result [3, 6, 2, 7, 5, 1]
[] => 4 is counted out and goes into the result [3, 6, 2, 7, 5, 1, 4]
```

So our final result is:
`josephus([1, 2, 3, 4, 5, 6, 7], 3) == [3, 6, 2, 7, 5, 1, 4]
