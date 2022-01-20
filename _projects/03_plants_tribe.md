---
title: "Custom Hearthstone Tribe"
excerpt: "\"We warned you to stay off the grass...\""
header:
    teaser: JungleUpdate.png
    overlay_image: https://cdn.hearthstonetopdecks.com/wp-content/uploads/2017/04/featured-junglegiants.jpg
    overlay_filter: rgba(0,0,0,.3)
collection: projects
description: "A \"Plant\" tribe concept for Hearthstone Battlegrounds"
---


<p style="text-align: center; font-weight: bold;">Introducing the Plant tribe in Hearthstone Battlegrounds, consisting of 17 brand-new pesticide-free minions! Will you nurture your plants into a symbiotic garden, or feed into their carnivorous overgrowth? Take a look at the image gallery to see the cards, and if you're curious to hear how they came together, read through my bizarrely comprehensive write-up below.</p>

{% include image-gallery.html folder="images/battlegrounds" %}

## Page Contents
1. [Introduction](#Introduction)
2. [Background](#Background)
3. [Concept](#Concept)
4. [Design Pillars](#Pillars)
5. [Individual Card Breakdown](#Breakdown)
6. [Challenges](#Challenges)
7. [Opportunities](#Opportunities)
8. [Final Bits](#Final)


## Introduction <a name="Introduction"></a>

This was a concept I developed over the course of a weekend. I'm a big fan of [Hearthstone](https://playhearthstone.com/en-us), and the Battlegrounds mode in particular. I also dabble in game design, and I constantly have ideas kicking around for ways to theoretically build on the games I love. Of course, taking those ideas and turning them into a cohesive design document is always easier said than done.

I had a blast coming up with ideas and envisioning how they would mesh with existing game mechanics.  I do wish it was feasible to actually test the tribe out *in vivo* -- nevertheless, I was able to come away with a deeper understanding of how one of my favorite games operates, and I'm excited to carry those insights with me as I bring [my own board game's](/projects/01_mysterywizard) development to a close.

This write-up describes how the new tribe works, how it was developed, and the challenges I faced along the way. It's going to assume that the reader is familiar with Battlegrounds' core mechanics and general balance, so if you're not... I guess, go play the game first? Come back once you've accidentally killed yourself with **Wrath Weaver**.


## Background and Related Work

There are some incredibly creative fan-made tribes out there. If I had to critique them, I'd say that a common flaw is that they're creatively *expensive*. By that I mean, the cool, creative concepts that they introduce are outweighed by the complexity they add in the form of new keywords, new mechanics, new decisions the player has to make, etc. Simplicity is at the core of Hearthstone's design philosophy, doubly so for Battlegrounds (a bit old, but check out [Eric Dodd's talk](https://www.youtube.com/watch?v=pyjDMPTgxxk). Tl;dw: Complexity should come from rich interactions among simple cards and mechanics  -- prioritize depth over breadth. 

I'll quickly* give my thoughts on a few fan-tribes, feel free to skip. 
  
<br/>

<img src="https://preview.redd.it/tklhv2zbpnn71.png?width=1600&format=png&auto=webp&s=aedff93af6fc319e010fc872ee472661afdf0436" alt="Trolo lolo lol" style="width: 50%"/>
### Troll tribe [posted by u/AYYLMAO2281337](https://www.reddit.com/r/customhearthstone/comments/pooo3b/complete_overhaul_of_trolls_hearthstone/)

This concept is packed to the brim with creative ideas, but I think the sheer quantity of NEW it brings to the table would prevent it from getting a seat at the table in the first place. The core concept is that Trolls give  and receive temporary buffs that remain permanent if they survive combat. Also, there's  a broad array of new overkill- and refresh-triggered mechanics. Also, half of the trolls have unique bonus "Requiem" abilities that are triggered by selecting a new troll-buff option that always pops up when you get a triple (whether you have trolls or not). Most minions have two or more of these new things going on.

Compare it to the Quilboar tribe, the only officially-released expansion tribe so far. Their core mechanic is the blood gem -- just a lil' 1/1 buff card that you get sometimes. Yes, I consider it expensive to add a keyword and mechanic like this (though at least there is some precedence for the 1/1 buff mechanic in King Mukla's delicious banana), but they pull a lot of weight. The blood gems themselves are about as straightforward as possible. Every single Quilboar has an ability either producing blood gems, or granting buffs when blood gems are played. The tribe's complexity doesn't come from having elaborate new triggers or buffs, but creating one simple mechanic that can interact with familiar systems in fresh ways.

<br/>

<img src="https://preview.redd.it/mdjxeli0um981.jpg?width=1125&format=pjpg&auto=webp&s=bc6a01f477acfef862d75edf9ab6191678b6735f" alt="Checkmate" style="width: 50%"/>
### Chess tribe [posted by u/rhernhdz12](https://www.reddit.com/r/customhearthstone/comments/rvpn7v/new_battlegrounds_update_introducing_chess_pieces/)

This is another well-developed concept. It introduces two new keywords (auto-attack and auto-defend) as shorthand for existing triggers. Like the Quilboar, all of the Chess pieces make use of these mechanics, and like the blood gems, they are used for other purposes too (e.g. triggering effects only on minions with one keyword or the other). It also introduces repositioning during combat -- an interesting mechanic that gets a lot of mileage, and doesn't even require a keyword! Taken as a whole, these mechanics aren't overly broad; the problem is that the tribe lacks depth. It relies extensively on automatic triggers and automatic permanent buffs -- no battlecries or active triggers, no interplay with other mechanics. There aren't enough interesting ways to use a Chess piece. Furthermore, because black and white pieces mirror each other's effects, the new ideas being introduced only get about half the mileage that they should. "The Chess update" was clearly meant as more of a creative exercise than a serious tribe design concept, but that makes its feasible qualities all the more impressive. 

<br/>

<img src="https://preview.redd.it/bfyuy69ysdi71.jpg?width=1280&format=pjpg&auto=webp&s=1b243919f558190fd3518d307d7f26b0c9d434e5" alt="It's not a cult!" style="width: 50%"/>
### Cultist tribe, [also by u/AYYLMAO2281337](https://www.reddit.com/r/customhearthstone/comments/p7nxeu/hearthstone_battlegrounds_cultists_update/)

I love this concept, because it does so much with so little. There are two core mechanics at play: Taunt buffs, and card hoarding. The former largely reuses or retools existing minions and concepts, unifying key players from most Taunt builds under a single banner. The latter taps into the game's existing mechanics in ways that haven't previously been done, shifting  the player's decision-making priorities without creating *new* decisions. I.e., players have always had to ask "should I play this card now or later," but this tribe shines a spotlight on that question and makes either decision interesting. The balancing act between pumping out tough Taunters now and nurturing an army for later seems like it could be very fun.

Here are some more things I like, in no particular order:
* The theming is so cool. I love the fact that you get this feeling of growing your cult in the shadows, and I love how it's translated for the Tier-6 boss monster (C'Thun's Body).
* Speaking of which, Chromie, the 1-cost minion that puts C'Thun in your hand, is great. Cements the theme, great secondary ability, allows you to start pursuing a Cultist build without locking you in.
* The Tier 5 minion General Rajaxx is just \*chef's kiss\*. The problem with hoarding cards in your hand is that you're... not playing them.   This allows you to pursue a strategy of growing some very large boy in your hand without worrying about the opportunity costs.

... All that said, I do see some flaws in the set.

* First and foremost: Taunt is one of the key pillars of the tribe, but the ability itself is essentially irrelevant. If "Taunt" didn't actually confer any ability, and just served as a tag for some minions, this tribe would play exactly the same. 
* The Tier 2 minion Vessel of Evil is... meh. It has the same ability as the tier 3 dragon Tarecgosa, but only synergizes with a single  Cultist... It doesn't really do much *for the tribe*, and insofar as it synergizes with other tribes, it's a (nearly) strict upgrade to Tarecgosa.
* The other Tier 6 minion, Kill Suit Cultist, seems out of place and underpowered (except for when he happens to be the exact card you need to win the game) compared to the rest of the set.
* The Tier 5 minion General Rajaxx is just \*foghorn\*. Yes, I also said it was great. The idea of what it does is awesome, but the execution is off.

Despite the flaws, I could totally see a form of the Cultist tribe working in the game! 

Phew, okay, with all of that out of the way, let me tell you about these Plants.


## Concept <a name="Concept"></a>
<br/>
<img src="https://tempandtea.files.wordpress.com/2016/09/tumblr_m3a6dylvtk1qko769o1_500.gif" alt="He's a mean green mother!" style="width: 60%; display: block;margin-left: auto; margin-right: auto;"/>
<br/>
<br/>

My goal was to create a tribe that **I could imagine existing in the game** -- something that felt both instantly familiar and utterly distinct from existing tribes, without introducing complexity in the form of long effect descriptions or new keywords. And I got pretty close! Read on.

The Plant tribe's core mechanic is **stat-draining**. Plants have to get their nutrients from somewhere, after all! Some plants just take little sips, while others devour minions whole. The draining mechanic works exactly like it sounds: when a Plant drains another minion, that minion's stats  are transferred to the Plant. If a minion's stats are lower than the amount being drained, it gives what it can. If its health reaches 0, it dies.  Like the "consume" mechanic used by by the Demon tribe, I felt that "draining" was intuitive enough to not require its own keyword.

So, how is draining implemented in a way that is deep, simple, exciting, balanced, and fun? Very carefully. From the get-go, I decided that plants would *not* drain from enemy minions. Could draining from enemies be fun? Maybe. Would it be hard to balance? Probably. Is it too obvious a direction? Absolutely.  

Instead, **your plants drain health from each other** -- the idea being that they're connected by a network of roots (and, I guess, mycelia [yes, this tribe counts fungi as plants {shut up}]), and they can drain or distribute their power as needed. Throw in a couple of primary producers, man-eaters, and gardeners to tend to the fields, and this network can readily grow into a behemoth (or grow a behemoth!).


## Design Pillars <a name="Pillars"></a>

OK, so plants drain plants -- great, how does the tribe actually *work* though?  Through trial and error, I whittled down 2 design pillars.

### Suck 'Em Dry! (Or: Using the Whole Minion).  

Other tribes have minions with effects like "Battlecry: Give a friendly Beast +2/+2". That's great and all, but when it inevitably comes time to sell that minion, its lasting value will have been only 2/2 (and when you sell the beast that got the buff, all you'll have left are memories). But when you can drain a minion dry, its value can live on forever.

In the late game, its obvious why draining is strong; board space is limited, so you need a way to consolidate your stats as much as possible. Late game Plants work by facilitating more concentrated draining, so you can grow your Big Boys and Beefsteaks more efficiently.

In the early game, board space is abundant, but what matters is stacking on enough stats to stay in the game. Friendly minions draining each other don't produce more stats, so they need some way to pick up momentum early on. Therefore, early game minions have abilities that allow you to derive additional value from  draining and from selling nearly-empty husks.

### Engine-building! 

Like most other tribes, the mid game is spent searching for Plants to build and fuel your stat engine. Unlike other tribes, simply playing a Plant seldom yields an immediate benefit; this engine is a garden that must be fertilized, tilled, and allowed to grow.

A fully-functional plant engine will be draining non-stop. There are a few ways the engine can be configured:
- *Suck 'em dry* -- Back to Pillar 1 baybeeee! A high-performance engine should allow you to quickly drain minions, so you can absorb their power as soon as you play them.
- *Collect little buffs* -- Some cards grant small buffs when a minion is drained. By draining as frequently as possible, your minions can stack up little buffs along the way.
-   *Drainserker* -- A variation on the little buff config that prioritizes maximizing drain frequency *during combat*. The buffs gained this way aren't permanent, but drains proc much more frequently!

Non-plant minions like **Plantsitter Seymour** and **Florist Friar** can provide the stats and cards needed to keep an engine running nicely.


## Individual Card Breakdown <a name="Breakdown"></a>

### Tier One
In-game tribes tend to use Tier 1 minions to introduce toned-down versions of their core concepts (e.g., **Alleycat** and Beast summoning, **Rockpool Hunter** and one-off Murloc buffs, both Quilboars and their delicious gems). But for plants, I didn't see an elegant way to make Tier 1 drains work. Drains are rather weak on their own early game, since they don't directly bring more stats to the board. Of course, Tier 1 minions also get play in the mid and even late game (especially as engine fodder for Elementals, pirates, etc.), but they still need to be viable early game if the tribe as a whole is going to be viable. Looking at the set, it seems that every single Tier 1 minion does something to bring value in the first few turns beyond it's vanilla stats.

So, rather than dwell on making a Tier 1 drain work, I opted for making minions that serve as valuable early-game choices in their own rights, while also feeding into a mid-late game Plant build. They are definitely on the weaker side in rounds 1 and 2, but they start to shine after that. They are plants, after all -- they take a while to grow!

<img src="/images/bg_cards/1_ancientbaby.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Ancient Baby**

Starting off weak: **Ancient Baby** is practically the same as **Micro Machine**, a minion that was retired last fall. In general, I don't think it bodes well for a card idea to resemble one that has already been removed, but I think the context of the rest of the tribe matters. 

 Micro Machine could offer decent value to any early-game build if you purchased in on turn 1 or 2 and kept it around for the next 4 or 5, after which it would just start taking up board space. It had no particular synergy with the Mech tribe -- the best one could do would be to attach an annoy-o-module to it to have a very slow-growing divine shield.

Like **M.M.** **Ancient Baby** offers decent value to all early-game builds (with slightly greater longevity, due to its additional health buff). But importantly, it also serves a synergistic role for a decent chunk of the early-mid game as a renewable drain source. The only Plant that serves a similar role is the Tier 2 minion **Primary Producer**. And while that minion does outclass this one as a drain source, A.B.'s versatility makes it a worthwhile inclusion.

<img src="/images/bg_cards/1_seedpod.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Seedpod**

This is another minion that is weak in Tier 1, but quickly picks up the slack. On its own, it has a weak, but viable body. Unlike **Ancient Baby**, this can hold its own against a few T1 minions on the first turn. The only benefit you get from playing it is a guaranteed A.B. or additional Seedpod in the tavern. That's not much, but if you want to start committing to the Plant tribe early, this can be a ticket in. In T2 and beyond, **Seedpod** can help you find minions to being building your plant engine, and once it's built, it can help you procure the fuel to keep it running.

Observations: this card's effect is the same as **Frost Elementals**' minus the freeze. It's stats are half of Frosty's, and it comes in two tiers lower. The balance feels appropriate to me -- if anything, it's just a little boring to have another nearly-identical effect to one already in game. Luckily, we're getting fresh effects from here on out.


<br/>

### Tier Two
Tier 1 is just an appetizer -- a starter salad, if you will -- something to whet your appetite. Tier 2 is the real first course. It doesn't quite commit you to a full-on plant build, but it's where you start to get the plant tribe experience. Hopefully, the progression should feel familiar to the other tribes.

<img src="/images/bg_cards/2_oaky.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Oaky Dokey**

At last, we have a drainer! This card serves a lot of different purposes over the course of the game.  When you play it in T2, it serves as an instant powerhouse. It's initial stats are 2/4, but assuming you can get a full drain, that'll bring it up to 5/7. The highest vanilla stats on a T2 minion are 3/5 (and 5/3). Access to a 5/7  taunter straight onto the board in T2 is pretty cool, and synergizes well with some other T2 minions  (e.g. **Selfless Hero**, **Glyph Guardian**). It also has a modest yet effective synergy with **Primary Producer**, if you can grab one of those first. Finally, it grants you some versatility by consolidating stats from a minion that you can choose to sell at a later point. 

Later on, that stat consolidation will become more important as you run out of space for new minions, and the Taunt will be able to help some of your supports survive in combat. And old **Oaky Dokeys** that had previously served as powerhouses make good candidates for subsequent drain sources.

<img src="/images/bg_cards/2_berserker.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Infested Berserker**

This minion is one of two plants that drains during combat. With its Windfury, it can drain up to four times when it attacks. On its own, this ability is not particularly impressive -- at best, it can be useful for taking out pesky cards like **Monstrous Macaw** and **Soul Juggler**. But combined with Plants that grant drain buffs, this can become devastating.

Well, relatively devastating. How devastating exactly? I'm going to jump ahead and see how strong I can make this card by mid-late game if I pull every  Plant minion I need.

No golds:
- 1x **Infested Berserker**, draining 1 from adjacent 2 times,
- 2x **Primary Producer**, each generating +1/+1 when drained,
- 2x **Fungal Enchanter**, each granting +1/+1 on drain,
- 1x **Lichen King**, doubling all drains

I.B. will net 12/4, while the Producers each lose 2 Attack but gain 2 Defense. Total net gain is +8/+8.

All golds:
- 1x **Infested Berserker**, draining 1 from each adjacent 4 times (mega Windfury),
- 2x **Primary Producer**, each generating +2/+2 when drained,
- 2x **Fungal Enchanter**, each granting +2/+2 on drain,
- 1x **Lichen King**, tripling all drains.

I.B. will net 40/16, while the Producers each lose 4 Attack but gain 8 Defense. Total net gain is +32/+32.

It definitely takes some setting up, but this is a pretty rad combo. Other Plants can help I.B. drain some Health along the way to help it survive these attacks. Throw in the T6 minion **Ixlid, Fungal Lord**, and  the attack drained by I.B. is redistributed to the other friendly minions once he dies.

<img src="/images/bg_cards/2_producer.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Primary Producer**

This is the first "engine-building" minion, gaining a small buff whenever it's drained. 

It has modest synergies with both ok the other T2 minions. It's stats are just high enough that it can survive a drain from **Oaky Dokey** (playing the pair nets +1/+1), and it can net at least a temporary +2/+2  during combat by synergizing with **Infested Berserker** (see above).

Its true power comes out in T3 and beyond, with minions that can repeatedly tap it for small permanent buffs, and minions that can help it recharge its stats should they get too low.



### Write-ups on Tier 3 and above coming soon.

### Tier Three

<img src="/images/bg_cards/3_enchanter.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Fungal Enchanter**

<img src="/images/bg_cards/3_guardian.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Twisted Guardian**

<img src="/images/bg_cards/3_festerroot.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Splitting Festerroot**

<img src="/images/bg_cards/3_seymour.png" style="display: block;margin-left: auto; margin-right: auto;"/>

* **Plantsitter Seymour**


### Tier Four

<img src="/images/bg_cards/4_spitter.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Vilespawn Spitter**


<img src="/images/bg_cards/4_ancient.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Ancient of Foresight**


### Tier Five

<img src="/images/bg_cards/5_manager.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Branch Manager**


<img src="/images/bg_cards/5_conduit.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Living Conduit**


<img src="/images/bg_cards/5_friar.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Florist Friar**


<img src="/images/bg_cards/5_king.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **The Lichen King**


### Tier Six

<img src="/images/bg_cards/6_ixlid.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Ixlid, Fungal Lord**


<img src="/images/bg_cards/6_audrey.png" style="display: block;margin-left: auto; margin-right: auto;"/>
* **Audrey 2000**



## Challenges <a name="Challenges"></a>

I ran into a lot of challenges putting the design together, but I decided to see it through to the end. Ultimately I feel like I've come away with a deeper understanding of and appreciation for evaluation and iteration in game design.


### Reinventing the wheel (Or: On the backs of giants)
When designing new cards, you're at least vaguely aware that you're working in the context of every other card that's ever existed. What should you take from that knowledge? Should you try to replicate the feeling of existing cards since you know they work, or should you try to make sure every card does something completely new? What about old cards that have been retired -- do you avoid them like the plague, or would copying aspects of those actually be preferable, since they're not represented in the current ensemble? It's definitely a balancing act. I think anyone would lean towards bringing in fresh ideas, but for me, it was also important to maintain some perspective. Not every Tier-1 or Tier-2 minion is utterly unique -- several of them have some variation of "Deathrattle: Summon a small friend." I felt comfortable giving Ancient Baby a familiar ability, because it seemed to work and do something fresh in this context.

### Undefined Behavior (Or: ... So, minions can die outside of combat?)
To the best of my knowledge, there don't seem to be any BG cards with effects that can reduce your own minions' Health during downtime. There are a number of cards that "remove" friendly minions from the board or "consume" tavern minions, but in those cases, it's clear that any abilities that proc on damage or death will not apply.

So, what would happen if you drain a Deathrattle minion to death? I'm not sure if the logic built into the game would even know how to handle something like this! There are a few abilities that you can proc in and out of combat, e.g.  "when you summon" triggers and **Whelp Smuggler**'s "when you gain Attack" trigger. But Deathrattlers aren't all built in the same way, and quite a lot of them have effects that only apply during combat (e.g., dealing damage to enemies).

So what *should* happen? On the one hand, draining to 0 health sure looks a lot like damage and death, so it would make sense to proc those triggers. Unfortunately, I imagine that giving players that ability would really throw off the balance of some existing cards, e.g. killing **Selfless Hero** for a permanent shield, killing **Nadina** for permanent shields on ALL of your dragons, spawning infinite demons with **Imp Mama**.

For a time, I tried avoiding having any Plant cards that drained Health from a "minion" target outside of combat (only ever from other Plant targets). But as the tribe evolved, the configuration of the drain mechanic I found to work best was having temporary in-combat drains prioritize Attack, and permanent out-of-combat drains prioritize Health. That meant that Plants wouldn't have any/many opportunities to permanently drain from non-Plant minions -- which was a core design pillar!

I considered just giving up and making **Drain** into a keyword with the caveat that a minion cannot be drained lower than 1 Health. Not only did adding a keyword rub me the wrong way, but that caveat didn't feel intuitive enough -- even if it was defined for the player, it would seem like an arbitrary rule, and it wouldn't be easy to remember.

I also considered just allowing minions with 0 Health to just stay on the board until combat, whereupon they would instantly die. But, no, that was bad.

Ultimately, I decided that since the mechanic was currently undefined, I would just give it a definition: being drained and dying out of combat do **not** proc damage triggers or Deathrattles. It's not ideal, but it's not completely unintuitive either. Thematically, consensual draining does not feel like the same activity as taking damage, so players won't *necessarily* expect it to act as such (this could be reinforced in-game with animations and sound that distinguish it). As for Deathrattles, there is a precedent for "removing" friendly minions from the board without triggering effects. Most importantly, I observed that the game draws a distinction between "Playing" minions and "Summoning" minions (the distinction being that minions summoned automatically do not proc "Play" triggers). In the same way, I feel it's fair to institute that being drained of life and "dying" fall into different categories. If need be, the definition for Deathrattles in BG could be amended to specify dying "in combat."

When a concept for a game mechanic leads to undefined behavior, it's often best to just [turn 360 degrees and walk away](https://i.kym-cdn.com/photos/images/newsfeed/001/265/714/fd1.gif). But there is a trade off here -- if the idea is good enough, and you can provide a definition that is intuitive, easy to define, easy to learn, and easy to remember, you may as well go for it. Of course, I'm not sure how well users would *actually* take to this rendition of the draining mechanic in practice -- would need to run some experiments!



### Unintended Consequences (Or: Uh oh, that low-tier [Divine Shield/Poisonous/Attacks Adjacent Minions/Attack Doubling] minion just got really high stats!?)

Thanks to the decision not to have drains trigger Deathrattles, I didn't need to worry about letting players get permanent divine shields from every **Selfless Hero** they came across. But some of my early ideas would have led to things nearly as strong.

At various points, there were Plants that allowed non-Plant minions to drain stats, as well as Plants that granted their stats to random minions when sold. These seemed like reasonable concepts, until it occurred to me that some minions are only kept in check by their low stats and limited access to permanent buffs. Take **Cave Hydra**. If an arbitrary Hydra could absorb a buffed Plant's stats, potentially as early as Tier 4, it would be an absolute beast (!).

There were a number of ways to keep the general concepts while curbing the consequences. For the stats-given-on-sale mechanic, rather than giving all stats to a random minion, it could just give half -- or even a constant value. I could have made the stat-granting card a Tier 6 to ensure that plays like that would only be possible in the late game. Really, there were countless ways to work around it, but few of them had the simplicity and thematic appeal of the first, broken iteration. In the end, a form of that mechanic did make it into the tribe -- instead of a random tavern minion absorbing a Plant's stats, the Tier 6 minion **Audrey 2000** absorbs the stats of any minions sold while it's in the tavern.

On the one hand, stumbling upon unintended consequences like this can help you define the boundaries of your playing field -- I can now see that the ability to grant arbitrarily large stats to ANY minion is incredibly strong, no matter the cost.

On the other hand, consequences like this can sometimes challenge your conception of your game's existing balance and mechanics altogether. At some point, I realized that as crazy as this power had seemed, there was already something in-game that did the same thing, but stronger: **Vol'jin**. His Hero Power lets you swap any two minion's stats EVERY TURN! FOR FREE! Reading over player comments from when he was first announced, people were, in fact, worried that he would be absolutely busted. And, uh, he is pretty strong. But no, he doesn't quite rise to game-breaking levels. And most importantly: he's really fun to play! In addition to bringing this strong new ability, he also introduced the first effect in BG that required the player to select two targets. That's one of those mechanics that would seem almost too heavy to even have in BG, but in practice, it works just fine. The ability itself is so straightforward that selecting two targets is second nature.

I have to imagine that there were some heated conversations about **Vol'jin**, and some heavy playtesting before he was introduced. I decided to back away from what I perceived to be an overpowered ability, but in some cases, it's worth it to go down the rabbit hole.


### Balance? Balance!

Balance was at the front of my mind during a lot of the tribe's development. Early on, I didn't want to seriously consider any mechanics or abilities that seemed like they would break the game's existing balance. I was constantly checking the Battlegrounds cards list, tweaking individual stats up and down 1 at a time to make sure a card didn't feel over/underpowered compared to existing cards.

About halfway through the development, I realized that I simply could not use static analysis to balance against every card in the game. There are so many factors at play, so many unforeseen interactions, that it is silly to attempt to get everything right the first time. If I wanted to balance these cards, I would need to playtest them extensively -- not gonna happen. 

To an extent, balance needs to be separate from design. Rather than base stats around the entire set of existing cards, I limited my scope to the tribe alone, basing stats and abilities on synergies with other Plants. The exact magnitudes may need to be tweaked in practice, but focusing on the fun synergies was what mattered.


### Fun! Fun?
Speaking of fun... what is fun? On the one hand, fun is something that people tend to agree upon; after all, there are millions of people who seem to think Hearthstone is fun. On the other hand, fun is different from person to person. We all have our own favorite fun activities; even within a shared "fun" experience like BG, different people may have the most "fun" with different tribes. Personally, I prefer to play the slow engine-building tribes like Elementals and Quilboar. I know that the more dynamic tribes like Beasts and Demons can be fun too (and definitely beat me a fair amount of the time), but I prefer a playstyle where I'm more in control.

As with balance, I spent a lot of time early on trying to optimize for fun. I threw out ideas that may have seemed interesting, creative, and balanced, because they just weren't *fun* enough. One card I threw out was a Tier 2 4/8 with "Can't attack." This card complemented a lot of the Plant tribe synergies, but it... just wasn't fun. There are only \~11-18 minions in a tribe, and I couldn't justify including one whose entire gimmick was the lack of an ability.

Another one I threw out was a Gardener concept, who simply gave all plants +1/1 at the end of each turn. I think a card like that could work just fine. It's a bit familiar to, e.g., **Charlga**, but different enough to not feel like a clone. Nevertheless, it just didn't seem fun enough to afford its spot. **Charlga** at least gets interactions with cards that buff blood gems -- the "balanced" version of a gardener I had presented had nothing.

I built the tribe like this: thinking of what other interesting BG interactions look like, thinking about what I'd like to play, thinking about what others might like to play. But occasionally, I would step back, and view it through the eyes of someoneI hadn't considered before -- someone coming from a different card game, a non-gamer, someone who would only ever play Beasts and nothing else. Through these lenses, cards that had previously seemed fun could seem far too intimidating, or confusing, or just plane boring. 

"Immediate fun" is another pillar of Hearthstone's design philosophy, but when you're optimizing for fun, what's the actual function? Should you aim for the most fun for a moderate crowd, or a little fun for everyone? Ultimately, this is another question that you can only really answer with playtests, so in the meantime I decided to trust my instincts, understanding that in practice this would not be the end. 


### Iterating without iterating
The essential challenge underlying this exercise was that I couldn't actually test the cards. You can imagine as many scenarios as you want, but without empirical results it's very tough to know how cards will work in practice.

That said, iteration was not only possible, but critical to the design. Whenever I came up with a good card concept, I would take a look through the existing Plants to see how it would fit in. There would often be interesting interactions or blatant incompatibilities, and identifying synergies and fixes would lead to ideas for new cards.  Once the set resembled a full-size tribe, I found myself going round and round, modifying or replacing cards, and then dealing with the repercussions of those changes. While this definitely helped to an extent, this design phase could be dragged out forever with greatly diminishing returns. At a certain point, I had to say that the tribe had gone as far as it could, would, or should go without proper testing.

I am curious if this resembles the process used by actual Hearthstone/CCG designers. A common motto in the industry is "fail fast," but for something like a BG tribe, I'd love to know if that takes the form of prototyping an entire set of cards at once, or if individual cards start to be tested right away. I tend to spend too long in the design stage, but I'd say this exercise has helped me recognize when enough is enough.


## Final Bits <a name="Final"></a>
I haven't done many write ups like this for topics other than [my research](/about), but I hope to do more in the future. All of my projects, be they research, web dev, or game design, involve breaking down problems to their base components and building up solutions piece by piece. It can be easy to lose sight of the countless tiny decisions that go into a system, but it's important to reflect on those decisions in order to learn and grow. 

(Still might've gone a little overboard with this one though -- I'll reign it in next time)


