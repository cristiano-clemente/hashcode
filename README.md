# Google Hash Code 2019

Practice Round

Our results:

Score: ???

Pizza Problem:

---

*** for a more detailed explanation read the [Problem Statement](practice-round/pizza.pdf)

How we tackled the problem:

---




## Online Qualification Round Problem

Our results:

Score: 1,483 points

Hub#: 7th

Country#: 80th

Worldwide#: 4,768th

Extended Round

Score: 872,966 points

Hub#: 3rd

Country#: 10th

Worldwide#: 779th



Photo Slideshow:

The idea is to,

> Given a list of photos and the tags associated with each photo, arrange the photos into
a slideshow that is as interesting as possible.

They score a slideshow by considering each transition between slides. The score will *minimum* of these three values 
  * the number of common tags between two consecutive slides or
  * the number of tags that only appears in the first slide or
  * the number of tags that only appears in the next slide
 
 Each slide could consist of
  * one horizontal photo
  * two vertical photos 

*** for a more detailed explanation read the [Problem Statement](qualification-round/photo_slideshow.pdf)

How we tackled the problem:

---

The idea behide this is a simple greedy algorithm.

To maximize score; we found that the optimal solution is that the consecutive slides A, B should have these properties.
  * n(A) = n(B)
  * n(A intersect B) = n(A-B) = n(B-A)
  * so only about half of tags in A should be found in B
  
** n(A) = a number of tags in photo A

So we knew that a number of tags is quite useful.

### How did we solve it?
We started with seperating photos into two lists; vertical photos and horizontal photos

We thought that it would be easier to seperate problem into two parts
* Arranging Slides 
* Grouping Vertical Photos to form a slide

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

Hope it helps. **#HashCodeSolved**

---content!---

hub: GCE - Instituto Superior Técnico


# Our Team (πthon)
* Cristiano Clemente [@cpcmc](https://github.com/cpcmc)
* Hugo Pitorro [@xtwigs](https://github.com/xtwigs)
* Catarina Carreiro [@cmccarreiro](https://github.com/cmccarreiro)
* Mónica Jin [@mokita-j](https://github.com/Mokita-J)

from [Instituto Superior Técnico](https://tecnico.ulisboa.pt/en/) (Lisbon, Portugal)
