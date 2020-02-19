---
title: "TSŪKU"
excerpt: "An asbtract strategy game for Android."
header:
    teaser: tsuku.png
collection: projects
---
Links: 
[Google Play Store](https://play.google.com/store/apps/details?id=io.ciaos.tsuku&hl=en_US) | 
[GitHub](https://github.com/ZackEberhart/tsuku)
<br>

![Tsuku logo](/images/logo3.png)
TSŪKU is an abstract strategy game based on the board game ["SHōBU"](https://www.smirkandlaughter.com/shobu) by Smirk and Laughter Games. Tsūku is a Japanese word that means "poke" or "prod." The game inolves setting up attacks with mirror moves to push your opponent's pieces off of a board.

I built the Tsüku app in about two weeks using React Native and the Expo framework. There are two important features that I still need to add: online multiplayer, and better singleplayer AI. For multiplayer, I initially wanted to use a service like Pusher, but I think I will wind up writing a simple server to connect players. I would also include bluetooth multiplayer, but Expo doesn't support that (yet). For the AI, I want to leverage some of my experience with Reinforcement Learning to learn strategies. There are a lot of important considerations that will go into that model, one large one being deciding how to best represent the game state. I'm going to have to review similar RL applications to board games like chess to see what they have done.