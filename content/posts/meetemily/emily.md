title: Meet Emily: The Average Tinder Girl
slug: meet-emily
author: Dan Kolbman
date: 2014-12-27


![Emily]({attach}trans_avg.png)
Meet Emily. A 21 year old, white, brunette who uses Tinder. She drinks coffee and
enjoys music. She likes wine almost as much as she does beer, and she favors
whiskey as far as liquor is concerned. She prefers dogs to cats.

## Compiling an average Tinder girl

It turns out that the Tinder API is pretty easy to exploit. It only requires a 
Facebook account with a connected Tinder app to verify and get a auth token. 
After that, all the calls used by the actual app become available to us and we're
free to wreck whatever havok we like. My first antics was to create a bot that 
simply liked and downloaded users' profile photos. I then gave the bot the ability
to send some cheeky initial messages, chosen from a list, to new matches. But 
the best addition came when I started automating responses to matches using 
the cleverbot API. Needless to say, countless amusing conversations have come
out of the bot so far. But conversations were not the only products of the bot.
After a couple months of conversing, liking, and tweaking, I ended up gathering 
over a hundered thousand profiles totaling more than 5GB worth of profile data
and (only the primary) profile pictures. 

## What's her name

After a quick analysis, the most common name was Emily, followed closely by 
Nicole, Amanda, Sarah, and Jessica.

![Names]({attach}names.png)

This doesn't include any variations of the names. For example, I found seven 
variations of Emily: Emilie, Emilee, Emi, Emile, Emili, Emleigh, and Emillie.
To sort through all of the possible variations would be a pain, and considering 
each of the top five are all pretty variable, I'll assume that this list is 
a good representation of the distribution. It might be interesting to inspect 
each name and look at how many variates each one has, but again, that would 
require a lot of hand sifting, so I won't do that here.

## How old is she

The next obvious question is her age. Well the age distribution of female Tinder
profiles looks like this:

![Ages]({attach}ages.png)

So she's 21 according to the Tinder dates. However, I after inspecting bios, I 
found something that may challenge this. I looked at the mentions of the numbers
14-24 on Tinder bios. Now, Tinder users will know that there is often two
occasions in which a user wil mention a number like this. One is when mentioning
graduating class, ie 'nyu 16'. The other is when the user is correcting the age
shown on their profile, ie 'I'm actually 18' (I believe this is often due to users 
lieing about their age in order to create a Facebook account when their younger).
Either way, we could infer something about age from either of these cases. 
Here's what that distribution looks like across users:

![Numbers]({attach}numbers.png)

First thing we can note about this is the sudden drop in frequency when we get 
to 19. At first glance, I'd say that this is some supporting evidence that the
mention of these numbers in bios is mostly users mentioning class year. But if 
we consider that the class of 2018 also corresponds to a demographic of mostly 
18 year olds. We could either make the conclusion that 'Users tend to state their
class year in their profile with freshmen being more likely to than seniors' or
we could just as validly say that 'Users tend to correct their age on their profile
with 18 year olds doing so the most and 14 year olds the least'. Therefore, it's
inconclusive as to which statement is correct.

But there is one thing that this says that disagrees with the age reported by 
Tinder, and that's the fact that 18 is mentioned the most. Remember that 18 
corresponds to an age of 18 by either of the above cases. We should then think 
that the most common age shoud be 18, not 19. Of course there's a lot of other 
things to consider, like users who are 18 feel compelled to list their age. 
I would conclude that overall, the evidence points to the actual mean age being
lower than that reported by Tinder, but I'd take it with a grain of salt.

## What are her interests

![Interests]({attach}interests.png)

Well music is certainly far ahead of anything else, but just 'music' is rather
ambiguous. Here are some of the more popular genres I could find in the list.

![Music Genres]({attach}genres.png)

Country comes out with a strong lead with more than twice that of rock. Of course
country is also often used as a identifier, ie 'I'm just a country gal', but they
go hand in hand for the most part. Again, this popularity likely comes from one 
of the major demographics (upstate NY) in the data. Rock and punk could also be
used as adjectives unrelated to genre as well. Overall, we can get some deeper 
interpretation of popular genres from this, but it shouldn't be taken too seriously.

### Beverages
![Beverages]({attach}beverages.png)


![Liquor]({attach}liquor.png)

### Sports 
![Sports]({attach}sports.png)
![Pets]({attach}pets.png)
