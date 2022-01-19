---
title: "Custom Hearthstone Tribe"
excerpt: "\"We warned you to keep off the grass...\""
header:
    teaser: JungleUpdate.png
    overlay_image: https://cdn.hearthstonetopdecks.com/wp-content/uploads/2017/04/featured-junglegiants.jpg
    overlay_filter: rgba(0,0,0,.3)
collection: projects
description: "A \"Plant\" tribe concept for Hearthstone Battlegrounds"
---


Introducing the Plant tribe in Hearthstone Battlegrounds, consisting of 17 brand-new pesticide-free minions! Will you nurture your plants into a symbiotic garden, or feed into their carnivorous overgrowth? Take a look at the image gallery to see the cards, and if you're curious to hear how they came together, read through my bizarrely comprehensive write-up below.

{% include image-gallery.html folder="images/battlegrounds" %}

## Page Contents: 
1. [Introduction](#Introduction)
2. [Background](#Background)
3. [Concept](#Concept)
4. [Design Pillars](#Pillars)
5. [Individual Card Breakdown](#Breakdown)
6. [Challenges](#Challenges)
7. [Opportunities](#Opportunities)
8. [Final Bits](#Final)


## Introduction <a name="Introduction"></a>

This was a concept I developed over the course of a weekend. I'm a big fan of Hearthstone, and the Battlegrounds mode in particular. I also dabble in game design, and I constantly have ideas kicking around for ways to theoretically build on the games I love. Of course, taking those ideas and turning them into a cohesive design document is always easier said than done.

I had a blast coming up with ideas and envisioning how they would mesh with existing game mechanics.  I do wish it was feasible to actually test the tribe out in vivo -- nevertheless, I was able to come away with a deeper understanding of how one of my favorite games operates, and I'm excited to carry those insights with me as I bring my own board game's development to a close.

This write-up describes how the new tribe works, how it was developed, and the challenges I faced along the way. It's going to assume that the reader is familiar with Battlegrounds' core mechanics and general balance, so if you're not... I guess, go play the game first? Come back once you've accidentally killed yourself with Wrath Weaver.


## Background (Or: your tribe is bad and you should feel bad!)

There are some incredibly creative fan-made tribes out there. If I had to critique them, I'd say that a common flaw is that they're creatively expensive. By that I mean, the cool, creative concepts that they introduce are outweighed by the complexity they add in the form of new keywords, new mechanics, new decisions the player has to make, etc. Simplicity is at the core of Hearthstone's design philosophy, doubly so for Battlegrounds (a bit old, but check out Eric Dodd's talk https://www.youtube.com/watch?v=pyjDMPTgxxk). Tl;dw: Complexity should come from rich interactions among simple cards and mechanics  -- prioritize depth over breadth. 

I'll quickly* give my thoughts on a few fan-tribes, feel free to skip.  

* Troll tribe posted by u/AYYLMAO2281337 (https://www.reddit.com/r/customhearthstone/comments/pooo3b/complete_overhaul_of_trolls_hearthstone/)
This concept is packed to the brim with creative ideas, but I think the sheer quantity of NEW it brings to the table would prevent it from getting a sit at the table in the first place. The core concept is that Trolls give  and receive temporary buffs that remain permanent if they survive combat. Also, there's  a broad array of new overkill- and refresh-triggered mechanics. Also, half of the trolls have unique bonus "Requiem" abilities that are triggered by selecting a new troll-buff option that always pops up when you get a triple (whether you have trolls or not). Most minions have two or more of these new things going on.

Compare it to the only officially-released tribe expansion -- the Quilboar. The Quilboars' core mechanic is the blood gem -- just a lil' 1/1 buff card that you get sometimes. Yes, I consider it expensive to add a keyword and mechanic like this (there is some precedence for the 1/1 buff mechanic in King Mukla's delicious banana), but they pull a lot of weight. The blood gems themselves are about as straightforward as possible. Every single Quilboar has an ability either producing blood gems, or granting buffs when blood gems are played. The tribe's complexity doesn't come from having elaborate new triggers or buffs, but creating one simple mechanic that can interact with familiar systems in fresh ways.

* Chess tribe posted by u/rhernhdz12 (https://www.reddit.com/r/customhearthstone/comments/rvpn7v/new_battlegrounds_update_introducing_chess_pieces/)
This  is another well-developed concept, even though it wouldn't quite fit in the game. It introduces two new keywords (auto-attack and auto-defend) as shorthand for existing triggers. Like the Quilboar, all of the Chess pieces make use of these mechanics, and like the blood gems, they are used for other purposes too (e.g. triggering effects only on minions with one keyword or the other). It also introduces repositioning during combat -- an interesting mechanic that gets a lot of mileage, and doesn't even require a keyword! Taken as a whole, these mechanics aren't overly broad; the problem is that the tribe lacks depth. It relies extensively on automatic triggers and automatic permanent buffs -- no battlecries or active triggers, no interplay with other mechanics. There aren't enough interesting ways to use a Chess piece. Furthermore, because black and white pieces mirror each other's effects, the new ideas being introduced only get about half the mileage that they should. "The Chess update" was clearly meant as more of a creative exercise than a serious tribe design concept, but that makes its feasible qualities all the more impressive. 

* Cultist tribe, also by u/AYYLMAO2281337 (https://www.reddit.com/r/customhearthstone/comments/p7nxeu/hearthstone_battlegrounds_cultists_update/). 
* I love this concept, because it does so much with so little. There are two core mechanics at play: Taunt buffs, and card hoarding. The former largely reuses or retools existing minions and concepts, unifying key players from most Taunt builds under a single banner. The latter taps into the game's existing mechanics in ways that haven't previously been done, shifting  the player's decision-making priorities without creating *new* decisions. I.e., players have always had to ask "should I play this card now or later," but this tribe shines a spotlight on that question and makes either decision interesting. The balancing act between pumping out tough Taunters now and nurturing an army for later seems like it could be very fun.

Here are some more things I like, in no particular order:
* The theming is so cool. I love the fact that you get this feeling of growing your cult in the shadows, and I love how it's translated for the Tier-6 boss monster (C'Thun's Body).
* Speaking of which, Chromie, the 1-cost minion that puts C'Thun in your hand, is great. Cements the theme, great secondary ability, allows you to start pursuing a Cultist build without locking you in.
* The Tier 5 minion General Rajaxx is just *chef's kiss*. The problem with hoarding cards in your hand is that you're... not playing them.   This allows you to pursue a strategy of growing some very large boy in your hand without worrying about the opportunity costs.

... All that said, I do see some flaws in the set.

* First and foremost: Taunt is one of the key pillars of the tribe, but the ability itself is essentially irrelevant. If "Taunt" didn't actually confer any ability, and just served as a tag for some minions, this tribe would play exactly the same. The only difference would be that two minions granting buffs when Taunt minions are attacked would trigger slightly less often. 
* The Tier 2 minion Vessel of Evil is... meh. It has the same ability as the tier 3 dragon Tarecgosa, but only synergizes with a single  Cultist... Basically, it doesn't really do much of anything for the tribe, and insofar as it synergizes with other tribes, it's a (nearly) strict upgrade to Tarecgosa.
* The other Tier 6 minion, Kill Suit Cultist, seems out of place and underpowered (except for when he happens to be the exact card you need to win the game) compared to the rest of the set.
* The Tier 5 minion General Rajaxx is just *foghorn*. Yes, I also said it was great. The idea of what it does is awesome, but the execution is off.

Despite the flaws, I could totally see a form of the Cultist tribe working in the game! 

Phew, okay, with all of that out of the way, let me tell you about these Plants.


## Concept <a name="Concept"></a>


My goal was to create a tribe that I could imagine existing in the game -- something that feels both instantly familiar and utterly distinct from existing tribes, without introducing complexity in the form of long effect descriptions or new keywords. And I got pretty close! Read on.

The Plant tribe's fundamental mechanic is stat-draining. Plants have to get their nutrients from somewhere, after all! It works exactly like it sounds: when a Plant drains another minion's stats, that minion's stats  are transferred to the Plant. If a minion's stats are lower than the amount being drained, it gives what it can. If its health reaches 0, it dies.   Like the "consume" mechanic used by by the Demon tribe, I felt that "draining" was intuitive enough to not require its own keyword.

So, how is draining implemented in a way that is deep, simple, exciting, balanced, and fun? Very carefully. From the get-go, I decided that plants would *not* drain from enemy minions. Could draining from enemies be fun? Maybe. Would it be hard to balance? Probably.  Is it too obvious a direction? Absolutely.  

Instead, your plants drain health from each other -- the idea being that they're connected by a network of roots (and, I guess, mycelia [yes, this tribe counts fungi as plants {shut up}]), and they can drain or distribute their power as needed. Throw in a couple of primary producers, man-eaters, and gardeners to tend to the fields, and this network can readily grow into a behemoth (or grow a behemoth!).


## Design Pillars <a name="Pillars"></a>

Plants drain plants -- great, how does the tribe actually *work* though?  Through trial and error, I whittled down 2 design pillars.

* Suck 'Em Dry! (Or: Using the Whole Minion).  Other tribes have minions with effects like "Battlecry: Give a friendly Beast +2/+2". That's great and all, but when it inevitably comes time to sell that minion, its lasting value will have been only 2/2 (and when you sell the beast that got the buff, all you'll have left are memories). But when you can drain a minion dry, its value can live on forever.

In the late game, its obvious why draining is strong; board space is limited, so you need a way to consolidate your stats as much as possible. Late game Plants work by facilitating more concentrated draining, so you can grow your Big Boys and Beafsteaks more efficiently.

In the early game, board space is abundant, but what matters is stacking on enough stats to stay in the game. Friendly minions draining each other don't produce more stats, so they need some way to pick up momentum early on. Therefore, early game minions have abilities that allow you to derive additional value from  draining and from selling nearly-empty husks.

* Engine-building! Like most other tribes, the mid game is spent searching for Plants to build and fuel your stat engine. Unlike other tribes, simply playing a Plant seldom yields an immediate benefit; this engine is a garden that must be fertilized, tilled, and allowed to grow.

A fully-functional plant engine will be draining non-stop. There are a few ways the engine can be configured:
- Suck 'em dry -- Pillar 1 baybeeee! A high-performance engine should allow you to quickly drain minions, so you can cycle through even more!
- Collect little buffs -- Some cards grant small buffs when a minion is drained. By draining as frequently as possible, your minions can stack up little buffs along the way.
-   Drainserker -- A variation on the little buff config that prioritizes maximizing drain frequency during combat. The buffs gained this way aren't permanent, but drains proc much more frequently!

Non-plant minions like Plantsitter Seymour and Florist Friar can provide the stats and cards needed to keep an engine running nicely.


## Individual Card Breakdown <a name="Breakdown"></a>

Tier One
In-game tribes tend to use Tier 1 minions to introduce toned-down versions of their core concepts (e.g., Alleycat and Beast summoning, Rockpool Hunter and one-off Murloc buffs, both Quilboars and their delicious gems). But for plants, I didn't see an elegant way to make Tier 1 drains work. Drains are rather weak on their own early game, since they don't directly bring more stats to the board. Of course, Tier 1 minions also get play in the mid and even late game (especially as engine fodder for elementals, pirates, etc.), but they still need to be viable early game if the tribe as a whole is going to be viable. Looking at the set, it seems that every single Tier 1 minion does something to bring value in the first few turns beyond it's vanilla stats.

So, rather than dwell on making a Tier 1 drain work, I opted for making minions that serve as valuable early-game choices in their own rights, while also feeding into a mid-late game Plant build. They are definitely on the weaker side in rounds 1 and 2, but they start to shine after that. They are plants, after all -- they take a while to grow!

Ancient Baby
Starting off strong: Ancient Baby is practically the same as Micro Machine, a minion that was retired last fall. In general, I don't think it bodes well for a card idea to resemble one that has already been removed, but I think the context of the rest of the tribe matters. 

 Micro Machine could offer decent value to any early-game build if you purchased in on turn 1 or 2 and kept it around for the next 4 or 5, after which it would just start taking up board space. It had no particular synergy with the Mech tribe -- the best one could do would be to attach an annoy-o-module to it to have a very slow-growing divine shield.

Like M.M. Ancient Baby offers decent value to all early-game builds (with slightly greater longevity, due to its additional health buff). But importantly, it also serves a synergistic role for a decent chunk of the early-mid game as a renewable drain source. The only Plant that serves a similar role is the Tier 2 minion Primary Producer. And while that minion does outclass this one as a drain source, A.B.'s versatility makes it a worthwhile inclusion.

Seedpod
This is another minion that is weak in Tier 1, but quickly picks up the slack. On its own, it has a weak, but viable body. Unlike Ancient Baby, this can hold its own against a few T1 minions on the first turn. The only benefit you get from playing it is a guaranteed A.B. or additional Seedpod in the tavern. That's not much, but if you want to start committing to the Plant tribe early, this can be a ticket in. In T2 and beyond, Seedpod can help you find minions to being building your plant engine, and once it's built, it can help you procure the fuel to keep it running.

Observations: this card's effect is the same as Frost Elementals' minus the freeze. It's stats are half of frosty's, and it comes in two tiers lower. The balance feels appropriate to me -- if anything, it's just a little boring to have another nearly-identical effect to one already in game. Luckily, we're getting fresh effects from here on out.

Tier Two
Tier 1 is just an appetizer -- a starter salad, if you will -- something to whet your appetite. Tier 2 is the real first course. It doesn't quite commit you to a full-on plant build, but it's where you start to get the plant tribe experience. Hopefully, the progression should feel familiar to the other tribes.

Oaky Dokey
At last, we have a drainer! This card serves a lot of different purposes over the course of the game.  When you play it in T2, it serves as an instant powerhouse. It's initial stats are 2/4, but assuming you can get a full drain, that'll bring it up to 5/7. The highest vanilla stats on a T2 minion are 3/5 (and 5/3). Access to a 5/7  taunter straight onto the board in T2 is pretty cool, and synergizes well with some other T2 minions  (e.g. selfless hero, glyph guardian). It also has a modest yet effective synergy with Primary Producer, if you can grab one of those first. Finally, it grants you some versatility by consolidating stats from a minion that you can choose to sell at a later point. 

Later on, that stat consolidation will become more important as you run out of space for new minions, and the Taunt will be able to help some of your supports survive in combat. And old Oaky Dokeys that had previously served as powerhouses make good candidates for subsequent drain sources.

Infested Berserker
This minion is one of two plants that drains during combat. With its windfury, it can drain up to four times when it attacks. On its own, this ability is not particularly impressive -- at best, it can be useful for taking out pesky cards like Monstrous Macaw and Soul Juggler. But combined with Plants that grant drain buffs, this can become devastating.

Well, relatively devastating. How devastating exactly? I'm going to jump ahead and see how strong I can make this card by mid-late game if I pull every  Plant minion I need.

No golds:
1x Infested Berserker, draining 1 from adjacent 2 times
2x Primary Producer, each generating +1/+1 when drained
2x Gold Fungal Enchanter, each granting +1/+1 on drain.
1x Lichen King, doubling all drains

I.B. will net 12/4, while the Producers each lose 2 Attack but gain 2 Defense. Total net gain is +8/+8.

All golds:
1x Infested Berserker, draining 1 from each adjacent 4 times (mega windfury)
2x Primary Producer, each generating +2/+2 when drained
2x Gold Fungal Enchanter, each granting +2/+2 on drain.
1x Lichen King, tripling all drains

I.B. will net 40/16, while the Producers each lose 4 Attack but gain 8 Defense. Total net gain is +32/+32.

It definitely takes some setting up, but this is a pretty rad combo. Other Plants can help I.B. drain some Health along the way to help it survive these attacks. Throw in the T6 minion Ixlid, Fungal Lord, and  the attack drained by I.B. is redistributed to the other friendly minions once he dies.

Primary Producer
This is the first "engine-building" minion, gaining a small buff whenever it's drained. 

It has modest synergies with both ok the other T2 minions. It's stats are just high enough that it can survive a drain from Oaky Dokey (playing the pair nets +1/+1), and it can net at least a temporary +2/+2  during combat by synergizing with Infested Berserker (see above).

Its true power comes out in T3 and beyond, with minions that can repeatedly tap it for small permanent buffs, and minions that can help it recharge its stats should they get too low.


Tier Three
Fungal Enchanter


Twisted Guardian


Ancient of Foresight


Plantsitter Seymour


Tier Four
Vilespawn Spitter


Ancient of Foresight


Tier Five
Branch Manager


Living Conduit


Florist Friar


The Lichen King


Tier Six
Ixlid, Fungal Lord


Audrey 2000



## Challenges <a name="Challenges"></a>
* ... So, minions can die outside of combat?
* Uh oh, that low-tier [Divine Shield/Poisonous/Attacks Adjacent MinionsAttack Doubling] minion has just got really high stats!
* Balance? Balance!
* Fun! Fun?
* Iterating without iterating
* On the backs of giants.
* Press (X) to doubt

## Opportunities <a name="Opportunities"></a>

## Final Bits <a name="Final"></a>
