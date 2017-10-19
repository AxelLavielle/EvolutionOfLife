# EvolutionOfLife
Game of life that is going to evolve in order to conquer his world.

This project have for aim to train myself with machine learning and evolution AI.
The project can be resumed easily:

Consider a map with a (in theory) infinite size.
- Every cell of this map have 4 neighbor.
- Every cell can be alive or dead, no schrodinger here,

The rules are those of a Conway's game of life:
- If a dead cell is surrounded by three living cell (Yeah, normally we do child as two, but you don't know cells, trust me), it becomes alive at the iteration + 1
- If a living cell is surrounded by 0 (Mr Lonely) or 4 (so famous) living cells, it dies at the iteration + 1

At the center of this map, allow a 10x10 (at first, I'll maybe grow it if my model is okay for 10x10) square that the artificial intelligence will fill. for example, a random initialisation could be:
```
1011000001
0010100001
1010000011
0100000000
0000000000
0000000000
1000100100
0110010010
0000000000
0000101010 (<- yeah, this one is 42 in binary in purpose)
```

I want to make the AI evolves in order to have the best initialisation possible to beat this challenge:
- Have the maximum propagation in 100 iteration (largest number of cells alive) (100 is totally arbitrary and may change)

For the artificial intelligence, I want two important part:
- Deep learning model to compute the inputs (10x10 map of initialisation) and the outputs (integer value representing the number of cells alive at the end of the 100 iterations) and gives the let's say 10 best differents initialisations it can find (there is 2^100 possible initialisations).
- Evolution, that will, from the 10 result of the DL Model, give a new batch of 100 iterations, modifying them a little bit randomly.
