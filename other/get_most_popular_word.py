"""
Question:

Given an integer W that represents number of words and unlimited space complexity.
Write functions insert(word) and getMostPopularWord()
such that getMostPopularWord() will always return the most popular word in the last W number of words.
Create two solutions that will optimize run-time complexity for either function
while sacrificing the run-time for the other function.

example1:
let W = 2
insert('A')
getMostPopularWord() => 'A'
insert('B')
getMostPopularWord() => 'B'

example2:
let W = 3
insert('A')
insert('A')
getMostPopularWord() => 'A'
insert('B')
getMostPopularWord() => 'A'
insert('B')
getMostPopularWord() => 'B' // since the first inserted 'A' is out of the scope of the last 3 words

follow-up1: insert => O(1), getMostPopularWord => O(log w)
follow-up2: insert => O(log w), getMostPopularWord => O(1)
follow-up3: insert => O(1), getMostPopularWord => O(1)
"""
