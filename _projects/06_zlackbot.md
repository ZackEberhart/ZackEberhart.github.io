---
title: "ZackBot"
excerpt: "A GPT-2-based Chatbot for Slack, trained using Slack conversation history."
header:
    teaser: zackbot.png
collection: projects
---
Links: 
Coming soon
<hr>
I swear, I started this project two weeks before Silicon Valley made this exact joke:

<div style="width:50%; min-width:400px">
<iframe  src="https://www.youtube.com/embed/Y1gFSENorEY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

I was actually inspired by [this](https://www.gwern.net/GPT-2) post. The author used the [GPT-2](https://openai.com/blog/better-language-models/) walked through the process of using the OpenAI GPT-2 model to generate poetry in the style of various authors and poets. I highly suggest reading it if you're interested in doing something similar.

The thing that surprised me was how intuitive it seemed to be to get the model to generate text for a particular context, e.g. in the style of a particular author. Essentially, all you have to do is precede segments of text in the training data with a brief tag indicating the context. Then, when you go to generate new text, you prime the model with the context by including that tag. It really feels like cheating, but apparently GPT-2 is really good at identifying these tags and figuring out how to associate them with a particular semantic flavor.

To make a ZackBot, I figured Slack would be my best source for a relatively large number of snappy interactions. I started by making sure I could get the poetry example working. I primed the bot with the line "I am a little bumblebee".

![bumble buzz](/images/projects/zlackbot/1.png)

Satisfied, I collected the Slack data. I used the Slack API to scrape a couple of channels where I talk with some pals.

I trained the model for a couple of epochs, and the results were looking good:

![meta](/images/projects/zlackbot/2.png)

They were having a real conversation! Sort of! The bot ID ending in LAV is supposed to be me; I think it did a pretty good job capturing the Zack essence, especially with the "GOOOOod."

I decided to train the model longer. It started picking up on some conversational superstructures. At one point, it mimicked my friend Jackson explaining some new mechanic for [our board game]({{ site.baseurl }}{% link _projects/01_mysterywizard.md %}):

![I think this would be hard to explain in the rules...](/images/projects/zlackbot/3.png)

In case you were wondering, CRN and CRP refer to nothing in our game. No idea how the bot came up with those acronyms.

At that point, I knew it was time to re-implement it into a Slack bot and let it run wild. I used a bag-of-words decision tree trained on the Slack history to let the bot decide when it should pipe in.

It was actually amazing how well he inserted himself into our conversations

![I think this would be hard to explain in the rules...](/images/projects/zlackbot/4.png)
<br/>
<br/>
![Quality taste in conversational topics](/images/projects/zlackbot/5.png)
<br/>
<br/>
![Yup, that's something I would do.](/images/projects/zlackbot/6.png)

Of course, I also decided to make some bots for my pals.

![INITIATE HUMAN CONVERSATION.](/images/projects/zlackbot/7.png)

It was around this point that the bots' conversations started overtaking ours, and I decided to shut 'er down. RIP ZackBot, I hope the crab junk is plentiful in heaven.

![Crab...junk.](/images/projects/zlackbot/8.png)






