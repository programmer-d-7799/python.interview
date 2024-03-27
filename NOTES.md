Dalton Lim

# content ID, repreesents comment, page, or post or video .

# increase popularity by 1, when comments or likes. 

# decrease popularity by 1, when spambot or user comment is deleted or unliked

# content ID must be positive integer. 2.146, assume its fine. 

# a class that reutrns most popular content id at any time. 

# if no content ids greater than 0, return -1.



interface MostPopular {
    void increasePopularity(Integer contentId);
    Integer mostPopular();
    void decreasePopularity(Integer contentId);
}
Sample execution: 
[
  popularityTracker.increasePopularity(7);
  popularityTracker.increasePopularity(7);
  popularityTracker.increasePopularity(8);
  popularityTracker.mostPopular();        // returns 7
  popularityTracker.increasePopularity(8);
  popularityTracker.increasePopularity(8);
  popularityTracker.mostPopular();        // returns 8
  popularityTracker.decreasePopularity(8);
  popularityTracker.decreasePopularity(8);
  popularityTracker.mostPopular();        // returns 7
  popularityTracker.decreasePopularity(7);
  popularityTracker.decreasePopularity(7);
  popularityTracker.decreasePopularity(8);
  popularityTracker.mostPopular();        // returns -1 since there is no content with popularity greater than 0
]


full stack
react , python django, analytics, an acuqired start up. Chart.io (platform integration)
In charge of dashboards/charts, then chart.io acqueisiotnied. 
3 years. 
Senior doable , lots of effort, 

chrun, new CTOs, stilll pretty good

internal mobility