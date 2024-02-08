    
In honor of my instructors who are going through the trouble of teaching me data analytics, I have decided to take on the exciting world of sports gambling. WOW 🤩

In all seriousness though, I am going through the process of collecting and gathering as much data as I can from the 

### General notes:

The statistics I am collecting is coming from the proballers API. It's one of the website's I found that offer detailed stats on both teams in a detailed recording of player's performance and final score. As well as home teams, and the date. All in a HTML table. Very easy to scrape. Especially with my new found skills on performing such a task. 

Some pattern that I found, all game statistics for the first team is found inside of a div with class name **class="home-game__content__entry home-game__content__team-stats__content-team-1"**. Inside that div, another div with class name **class="table__outer"** which for some reason only serves the purpose of holding another div with the name of **class="table__inner** I mean I can't say I would've been able to make something better, but it seems pointless to nest a div like that. Anyhoo.

We can find divs with these exact same class names inside of the second div for the second table with class name **class="home-game__content__entry home-game__content__team-stats__content-team-2"**. These tables show all I wish to know for know. Most of these are beyond what I know in terms of basketball. The first table shows either the home team or the winning team. 

Let me make a table for these classes hold on...

| element                           | class name                                                                       |
| --------------------------------- | -------------------------------------------------------------------------------- |
| div for team 1                    | class="home-game__content__entry home-game__content__team-stats__content-team-1" |
| div for team 2                    | class="home-game__content__entry home-game__content__team-stats__content-team-2" |
| table parent                      | class="table__outer"                                                             |
| table container (child of parent) | class="table__inner"                                                             |

Without further a do. Let's get scraping.

- [Webscraping](/webscraping_notebook.ipynb)

- [Link scraping](/URL_fetcher.ipynb)
