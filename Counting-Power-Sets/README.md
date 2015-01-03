Counting Power Sets
======

##Description##
In this kata, you must create a function `powers` that takes an array, and
returns the number of subsets possible to create from that list. In other
words, counts the power sets.

For instance
`powers([1, 2, 3]) => 8`
due to
`powerSet([1, 2, 3]) => [[], [1], [2], [3], [1, 2], [2,3], [1,3], [1,2,3]]`

Your function should be able to count sets up to the size of 500, so watch
out; pretty big numbers occur there!

you should treat each array passed as a set of unique values for this kata.
