# Baekjoon_1260
If you want to see this quiz, please click [here](https://www.acmicpc.net/problem/1260)\
It's about DFS/BFS

## what is DFS/BFS
DFS is Depth First Search. I solved this Quiz, using Stack.\
BFS is Breath First Search. I solved it by using deque.

## what i've had problems 
1.  `visited = [False] * 9` it must be changed to `visited = [False] * (n+1)` because we need visited check n+1. (n = the number of *vertaxs*)
2.  The quiz told me that the algorithm must print vertax smaller, if the vertax has nodes more than 1.\ 
But, I missed this condition.
