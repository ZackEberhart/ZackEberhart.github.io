---
title: "Websterium"
excerpt: "A cooperative mystery game for the web."
header:
    teaser: websterium.png
collection: projects
---
Links:
[Game](https://mysterium-frontend.herokuapp.com/) | 
[GitHub](https://github.com/ZackEberhart/websterium)
<br>
Websterium is a webapp adaptation of the board game [Mysterium](https://en.wikipedia.org/wiki/Mysterium_(board_game)) by Libellud. Mysterium is a cooperative game in which one player is a recently-dead ghost, and the rest are psychics working together to solve the mystery of the ghost's murder. To do so, the psychics receive "visions" in the form of cards depicting abstract art, that the ghost must use to try to guide the individual psychics towards specific suspects, places, and murder weapons. 

The artwork in Mysterium is beautiful, but after playing it 10+ times, it becomes repetitive. You can buy $20 expansions if you want a change in scenery, but the truth is that the game mechanics are actually fairly agnostic about the content of the cards. Even the "suspect, place, weapon" structure is just theming. In truth, the fun of the game boils down to identifying weak patterns and similarities in dissimilar images and predicting what connections the other player(s) might draw. It certainly helps to have busy images that can be interpreted in several different ways, but anything would honestly work. 

I realized it could be fun to make a deck using your own custom images -- maybe use pictures of friends as suspects, or terrible drawings for dreams. And at that point it occurred to me that, by making it into a little web app, you could easily use any images you want.

So, unable to come up with any better name, I decided to make "Websterium". The frontend is a React app that lets you connect to a room with your friends, start a game with specified image sources, and play Mysterium with those images. As it stands, it's missing a couple of major features from the board game. The biggest omission: in Mysterium, after each player deciphers a different permutation of the ghost's murder, there is an additional phase in which they must all vote on the one "true" story.

But the game is still super fun, and you should try it out!

