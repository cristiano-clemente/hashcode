# Practice Round: [Pizza Problem](practice-round/pizza.pdf)

## Problem Statement:

The goal is to,

```
cut correct slices out of the pizza maximizing the total number of cells in all slices.
```

## How we tackled the problem:

- The pizza is mapped onto a grid.

- Each of the grid lines are scanned from left to right.

- When a valid pizza slice is encountered, it is added to the output file and the scanning of the line restarts from where it left off. 
