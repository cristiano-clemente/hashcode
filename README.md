# Google Hash Code 2019

## Practice Round: [Pizza Problem](practice-round/pizza.pdf)

Our results:

Final Score: xxxx points

The goal is to,

```
cut correct slices out of the pizza maximizing the total number of cells in all slices.
```

...


How we tackled the problem:

...


## Online Qualification Round + Extended Round: [Photo Slideshow](qualification-round/photo_slideshow.pdf)

Placements:

| Round                      | Score          | #Hub | #Country | #Worldwide |
| :------------------------- | :------------- | :--- | :------- | :--------- |
| Online Qualification Round | 1,483 points   | 7th  | 80th     | 4,768th    |
| Extended Round             | 872,966 points | 3rd  | 10th     | 779th      |

Submissions:

Online Qualification Round:

| Test                    | 09:06 PM |
| :---------------------- | :------- |
| A - Example             | 2        |
| B - Lovely Landscapes   | X        |
| C - Memorable Moments   | 1483     |
| D - Pet Pictures        | X        |
| E - Shiny Selfies       | X        |
| Total Submission Points | 1485     |

Extended Round:

| Test                    | 11:26 PM| 08:29 PM| 08:43 PM| 09:37 PM| 11:05 AM| 11:44 AM    | 09:11 AM    | 10:02 AM| 10:05 AM| Max
| :---------------------- | :------ | :------ | :------ | :------ | :------ | :---------- | :---------- | :------ | :----   | :----
| A - Example             | X       | 2       | 2       | 2       | 2       | **2**       | 2           | -       | -       | 2
| B - Lovely Landscapes   | X       | X       | 27      | 120     | 1,476   | 14733       | **205,485** | -       | -       | 205,485
| C - Memorable Moments   | X       | X       | 196     | 652     | 1,239   | **1530**    | -           | 1,464   | 1,530   | 1,530
| D - Pet Pictures        | X       | X       | 205,552 | 263,662 | 306,086 | **335,252** | -           | -       | -       | 335,252 
| E - Shiny Selfies       | X       | 112,768 | 112,768 | 203,172 | 275,456 | **330,697** | -           | -       | -       | 330,697
| Total Submission Points | 0       | 112,770 | 318,545 | 467,608 | 584,259 | 682,214     | 205,487     | 1,464   | 1,530   |

Final Score: 872,996 points

## Problem Statement

The idea is to,

```
Given a list of photos and the tags associated with each photo, arrange the photos into
a slideshow that is as interesting as possible.
```

The slideshow's total score depends on the score of each transition between slides.

The score of each transition between slides is the *minimum* of:
  * the number of common tags between two consecutive slides
  * the number of tags that only appear in the first slide
  * the number of tags that only appear in the second slide

 Each slide consists of:
  * one horizontal photo or
  * two vertical photos

...

## How we tackled the problem

We started with seperating photos into two lists; vertical photos and horizontal photos

We divided the problem into 3 parts
  1. Separating horizontal and vertical photos
  2. Grouping vertical photos to form a slide
  3. Arranging slides to form a slideshow

---------------

So, firstly, we ignored the vertical photos. We focused on how to arrange that maximize the score. 

One simple idea we found is that 
1. order all photos by its number of tags (just this you could get more than 100k points)
2. optimize it by using a **sliding window**

The sliding window N is that
* starting with position 0 then you are going to find the next slide which will maximize your score from the next N slides
* then move that slide to position 1
* do it again until the final slide

The bigger N will get the better score but I believe that it will be limited around 800k points

---------------

The second part is to group vertical photos into a slide

We also used a simple solution by
1. order all photos by its number of tags
2. group the largest with the smallest and the second largest with the second smallest and so on.

This will give you roughtly the same size photos (in term of the number of tags)

Then combine two part together; grouping all vertical photos into slides then arrange them.
...

**#HashCodeSolved**


# Our Team (πthon)
* Cristiano Clemente [@cpcmc](https://github.com/cpcmc)
* Hugo Pitorro [@xtwigs](https://github.com/xtwigs)
* Catarina Carreiro [@cmccarreiro](https://github.com/cmccarreiro)
* Mónica Jin [@mokita-j](https://github.com/Mokita-J)

hub: [GCE - IST](https://www.gce-neiist.org/)
from [Instituto Superior Técnico](https://tecnico.ulisboa.pt/en/) (Lisbon, Portugal)
