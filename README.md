PickMeUp
========
This started as a 3am idea where we decided "you know what would be cool? if my phone could tell that im having a bad day and call an uber to send me to the bar". That's when we started coding, but the more we thought about it, we wanted to make it more than just a bar ride app. 

Various people have asked us the question "what if I'm sad all the time? Could I just get free rides to the bar then?". Our answer has always been "No, if you are sad all the time, you need professional help and we can't help you, And if you are pretending, we would implement a fraud detection scheme where it doesn't measure your sadness level overall, but rather normalizes your profile over time and if you have a particularly bad day (spike in your mood), we'd send you a 'pickmeup' that picks you up." 

NLP is a massive field and emotion detection is a largely untapped market at the moment. The bar ride was just one use case: we could use this for REAL TIME marketing of brick and mortar businesses! It doesn't have to be a bar, but a local music venue for your favorite genre, a restraunt/coffee shop that is having a special, anything. Lets say there is a cafe that paid for live music, and your cafe is empty...this kinda sucks cause the shop is gonna lose some money and the band isn't really helping the community by sharing their music with them, well the coffee shop now has an easy way of tapping into who might be having a bad day and could give a deal to those customers who were accessed with this service. The point is that your mood affects what you want, and if we can figure that out, and give you what you want, it makes your day, businesses get paid, and everyone is happy.

So how do we accomplish this? We trained a naive bayes classifier using Python SKLearn and we fed it a set of what was going to be 1.6 million tweets but for time's sake we only used 400,000 tweets from the set. The training and test data came from this website: http://help.sentiment140.com/for-students. Tweets made the most sense in this case because they are efficient textual forms designed to specifically convey updates and emotions. To start we classified on 1-grams and 2-grams for its analysis. This is a very hard NLP problem of which we have only scratched the surface, but it made for some fun experimentation. Enjoy!