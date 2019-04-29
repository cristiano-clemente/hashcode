# Google Hash Code 2019

## Practice Round: [Pizza Problem](practice-round/pizza.pdf)

### Problem Statement

The goal is to,

```
cut correct slices out of the pizza maximizing the total number of cells in all slices.
```

### How we tackled the problem

- The pizza is mapped onto a grid.

- Each of the grid lines are scanned from left to right.

- When a valid pizza slice is encountered, it is added to the output file and the scanning of the line restarts from where it left off. 


## Online Qualification Round / Extended Round: [Photo Slideshow](qualification-round/photo_slideshow.pdf)

### Placements:

| Round                      | Score          | #Hub | #Country | #Worldwide |
| :------------------------- | :------------- | :--- | :------- | :--------- |
| Online Qualification Round | 1,483 points   | 7th  | 80th     | 4,768th    |
| Extended Round             | 872,966 points | 3rd  | 10th     | 779th      |

### Submissions:

#### Online Qualification Round

| Test                    | 09:06 PM |
| :---------------------- | :------- |
| A - Example             | 2        |
| B - Lovely Landscapes   | X        |
| C - Memorable Moments   | 1,483    |
| D - Pet Pictures        | X        |
| E - Shiny Selfies       | X        |
| Total Submission Points | 1,485    |

Final Score: 1,485 points

#### Extended Round

| Test                    | 11:26 PM| 08:29 PM| 08:43 PM| 09:37 PM| 11:05 AM| 11:44 AM    | 09:11 AM    | 10:02 AM| 10:05 AM|
| :---------------------- | :------ | :------ | :------ | :------ | :------ | :---------- | :---------- | :------ | :----   |
| A - Example             | X       | 2       | 2       | 2       | 2       | **2**       | 2           | -       | -       |
| B - Lovely Landscapes   | X       | X       | 27      | 120     | 1,476   | 14733       | **205,485** | -       | -       |
| C - Memorable Moments   | X       | X       | 196     | 652     | 1,239   | **1530**    | -           | 1,464   | 1,530   |
| D - Pet Pictures        | X       | X       | 205,552 | 263,662 | 306,086 | **335,252** | -           | -       | -       |
| E - Shiny Selfies       | X       | 112,768 | 112,768 | 203,172 | 275,456 | **330,697** | -           | -       | -       |
| Total Submission Points | 0       | 112,770 | 318,545 | 467,608 | 584,259 | 682,214     | 205,487     | 1,464   | 1,530   |

Final Score: 872,996 points

### Problem Statement

The goal is to,

```
Given a list of photos and the tags associated with each photo, arrange the photos into
a slideshow that is as interesting as possible.
```

### How we tackled the problem

- The photos are divided up into 2 different lists: vertical and horizontal.

- The vertical photos are grouped into pairs, maxizing the combined number of tags.

-> The slideshow starts with the first horizontal photo.

-> All the remaining photos are scored against the current last photo in the slideshow.

-> The following photo is the one that maximizes the score when combined with the previous one.

**#HashCodeSolved**

# Our Team (πthon)
* Cristiano Clemente [@cpcmc](https://github.com/cpcmc)
* Hugo Pitorro [@xtwigs](https://github.com/xtwigs)
* Catarina Carreiro [@cmccarreiro](https://github.com/cmccarreiro)
* Mónica Jin [@mokita-j](https://github.com/Mokita-J)

hub: [GCE - IST](https://www.gce-neiist.org/)
from [Instituto Superior Técnico](https://tecnico.ulisboa.pt/en/) (Lisbon, Portugal)
