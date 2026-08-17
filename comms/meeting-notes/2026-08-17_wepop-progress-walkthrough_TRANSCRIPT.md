# Wepop progress walkthrough - verbatim transcript - 2026-08-17

> Verbatim record. Do not edit content. Fathom speaker labels are known to be swapped or
> mislabelled in places (for example an "Aakash Dhar (sorigin.com)" tag carries Elvis's design
> walkthrough lines). Speakers are normalized by role in the companion summary, not here.
> Source recording: https://fathom.video/share/vz8mFFBynigDhjxeMpMsq_HfZS7Kfnor (91 mins)
> Attendees: Aakash Dhar (PM), Elvis Ge (client and designer), Deepak Tewatia (tech lead).
> Note: the final section (from roughly 1:19:40) concerns a different engagement (Dan / Reflex
> SEO and a voice-tutor product), not Wepop. It is retained here verbatim but was set aside from
> the Wepop summary and proposals per the ingest scope decision.

---

Wepop progress discussion - August 17

VIEW RECORDING - 91 mins (No highlights): https://fathom.video/share/vz8mFFBynigDhjxeMpMsq_HfZS7Kfnor

[0:00] Deepak Tewatia
Hi, was logged out. Oh, I'm already signed to the calendar.

[0:09] Aakash Dhar (sorigin.com)
Hi, I'm Mark. Morning.

[0:16] Deepak Tewatia
Hey, guys.

[0:18] Aakash Dhar (sorigin.com)
So, did you get any, did you make any updates in terms of Re-pop?

[0:25] Elvis Ge (programination.com)
Yeah, I'm finishing off the onboarding. I can show that to you guys. I guess I also curious if you guys have any, uh, updates, like, questions. I know there's no updates because, you know, maybe there's nothing worked on yet. Yes. It's more in terms of, uh, if you guys have any questions and also, like, feedback, right? Um, so in terms of, uh, any ideas or any, um, how should I say, things that, uh, could be better, things that won't work kind of thing?

[0:58] Aakash Dhar (sorigin.com)
Yes.

[1:00] Elvis Ge (programination.com)
We are currently basically looking at the screens that we have designed so far, me and the other people looking at that.

[1:05] Aakash Dhar (sorigin.com)
And ideally what we have been doing is we were describing how we can modularize the thing so that when we actually get onto that bit, those things can be accelerated faster. So that's what were discussing purely in terms of the technical side of things. We didn't look much into, we didn't go into the critic mode of what can be better and what not. But ideally one thing which I would really want from you is like an entire project documentation. Just ask Cloud to generate it for me and if you can give it to me today, then in that case what I can do is I can set up a proper cloud-working flow for this.

[1:46] Elvis Ge (programination.com)
So it's easier to track things and reminders and progress and everything.

[1:50] Aakash Dhar (sorigin.com)
So then even I can share your well-nuanced report of the status and everything. So just... Can you please get me that documentation? Yeah, I'll work on that documentation. I mean, I have like a version of it. It's just because I wanted to finalize all the designs and then give it over.

[2:12] Elvis Ge (programination.com)
But I can give it to your version, but it may change until the... Yeah, that's fine.

[2:16] Aakash Dhar (sorigin.com)
That's perfectly fine. Even if it's that version, I can maintain the version in my co-working setup. So actually, that would be better as well. So at one point of time, even if you wanted to like have a mix of version one or version two, somewhere, a proper healthy mix of it, we can get those things sorted off as well. But just give me the documentation so that actually I can start building that co-working setup that I generally do for project management. So it would be really easy for me. Okay. Yeah.

[2:46] Elvis Ge (programination.com)
The other thing, because you're speaking about getting a document and version, is I know in the past for other projects like iSoftPole, Marish talked about creating a... And then maybe, harness is one thing, but I think also like, instead of me sending back and forth a document, I think I do have a GitHub account. Would it be better if we have a central location?

[3:16] Aakash Dhar (sorigin.com)
Perfect. What I would actually do for you is, once I set up the co-working setup, I would send you the GitHub link as well. Means in the sense like, you can, I'll give, I'll send across to you an invitation for the GitHub repo, that I set up for VPOP. Okay, you download it, and let's get on a call, I'll set up the co-work setup for you. It's easy, it's just a couple of steps, that's it, nothing else. So, once that is sorted out, then what we can do is, you can also push the changes there, and wherever you push the change, I can take a pull from the central GitHub repo, so that, that becomes the common source of truth for both of us. Yeah. So that way it would be easier. Ideally, so you don't have to share documents, I don't have to download and do all of those things. If there is a scenario where we actually might have to, you can just share it across and I'll push it to the GitHub repo. That's perfectly fine. So just share me your GitHub account, user ID first, second, or you would be sharing across the documentation, whatever is done so far. It's perfectly fine. Even if it's V1, we can call it V1. We can maintain versioning. That's perfectly natural. That's perfectly fine. Send across those to me and I'll set up the GitHub repo. I'll share across your GitHub request. Accept that. Once you have done with that, then we can get on a quick call. It's hardly fine to tell this job. We can get on a quick call and I can show you how the setup works. It's a very simple setup. You get that thing sorted off. Then whenever you make a change, let's assume that you decide on something else. You can just push... the update to that project repo, and whenever I need, whenever I'm, the next time when I'm back online, I can just take the pull, and I would have the updated version of the code, means, at least the repo-based setup, that's it. Yeah, okay. So that way, the coordination would be easier in those cases.

[5:17] Elvis Ge (programination.com)
Yeah, so, yeah, I'll get you the document, and then we'll set up the central GitHub to work off of.

[5:24] Aakash Dhar (sorigin.com)
Perfect, sounds good, sounds great. Okay, now, over to you, Lec. Yeah. So, so, some of these things are in the old version that we have, right, but design might be a change, but I still want to, because Deepak is somewhat new, I'll go over with them.

[5:39] Elvis Ge (programination.com)
So, in, in general, and I think also, Kashi, you're somewhat new because Behata was originally doing this project. So, in the beginning, so there, there are a lot of, kind of, event apps, right, in, in the world, in America, and then nowadays, they're more and more growing in Korea, as well.

[5:59] Aakash Dhar (sorigin.com)
So, yeah.

[6:01] Elvis Ge (programination.com)
So the app itself, how should I say, it's just 50% of the success of the business. The other part is kind of how we handle building the community and how we handle things off the app, right? And so one of the things is before I think we discussed is like we, it's not, it's not an app that anyone can join because once you join and the experience is bad, right? There's no one on the app in your location, there's no events, whatever, no friends on there, whatever, then you're more likely to drop out, right? So it's just like a, how should I say, the initial startup issue, right?

[6:38] Aakash Dhar (sorigin.com)
Any, any platform kind of issue.

[6:40] Elvis Ge (programination.com)
So we have here is like if you're in the beginning and we have, it's an invite only either from me directly or people from who are already in the platform that I invited, who then can invite other people to the platform via and.

[7:00] Aakash Dhar (sorigin.com)
existing event or idea.

[7:01] Elvis Ge (programination.com)
So it's not a generic invite. It's an invite to a specific event or an idea they created so that when the person joins that there's already someone they know and there's already something that exists that they can interact with. So knowing someone is not enough because then, you know, there's, you still need to, it's not like Instagram where you just view pictures or whatever, but you need to join an event or talk about some idea or event. So, so if you somehow, obviously on the app store, if they see it or in my marketing or landing page or whatever, they see it, they would just be joining a wait list. Okay. Okay. So we have the wait list, email, phone number, their location. So then as I build this data, I'll know kind of where to, what might be a good area to expand to next. And then, and here also like what university, if they're part of the university, right? Okay. Maybe if I don't expand to that university, if there's a lot of people, then I can, you know, reach out to them. Then normal onboarding, you have kind of this three-step process, three-step information on what this app is. Okay.

[8:12] Aakash Dhar (sorigin.com)
This one here is a little different, it's because you got invited to an event, right?

[8:17] Elvis Ge (programination.com)
So when you got invited, you see the thing you got invited, who invited you, what it was, and then either you can join or if you have an account, you log in, right? For required login, it's same as current app, phone number, or we can do this as well, social proof or social authentication. But at the end of the day, we still need to collect their phone number to verify that user. Okay. Okay. Then again, if you guys have any questions while I go through this or any feedback, that's, like, if I can't remember, let me know.

[8:57] Aakash Dhar (sorigin.com)
Definitely. Then... Yeah. So when you log, I'm sorry, there's more here.

[9:03] Elvis Ge (programination.com)
So this is scroll. Yeah. So phone number, phone number authentication, if you got invited, if they invited you via email, then you would see the email here as well. Birthday, because of just legal things for now, we're just going to have 18 or 19, whatever the, yeah.

[9:20] Aakash Dhar (sorigin.com)
Yeah.

[9:21] Elvis Ge (programination.com)
The thing is, let me know if it's, if we're able to change the logic via, I guess, the, I'm trying to figure out what the best way is, because every country has their own legal age.

[9:36] Aakash Dhar (sorigin.com)
Is there a way to do it based on their app store or whatever? Yeah. Generally, yes. But overall, like pan, like globally, 18 is like, I guess in some places it's 16, but 18 would be a safe number, wherein like you can consider the- is 19, that's why I'm saying this. Korea is 19? I know, 19. Yeah. Oh my God.

[9:58] Elvis Ge (programination.com)
Okay, then, then. That's why I'm saying the logic is a little different. America's 18, Korea's 19, so I'm just wondering.

[10:05] Aakash Dhar (sorigin.com)
India's also 18, by the way. You get the right to vote and everything starting at the age of 18. You can't drink until you're 19 or whatever here. Okay, then let's keep pointing them. But your college students would be 18. That's the thing, ideally. College students, like the first year of college, people, those who would be there, they would ideally be, I don't know about the Korean education system. We have 12 plus, 3 plus 3, purely in terms of engineering. You have 12 years of education, in a sense, like schooling. Then you have, if you're going for engineering, it's 4. If you're going for grads, it's 3. So ideally...

[10:45] Elvis Ge (programination.com)
question is more like, on the engineering end, is there a logic that can be built to change the stage? Yes, yes, yes, we can.

[10:55] Aakash Dhar (sorigin.com)
We can definitely, like, we can, we can get this thing. We have an admin panel, right, irrespectively. Okay, so... So... Oh, you can mention it there. Now, the question he means here is, based on your legal boundaries, do you want that to be geographically tied, right? Like, you should be able to select a country and the age limit. So when we are actually coming into this page and when we are signing up, we ask them to turn on the location. And we get their location based on the country that they're in. We can pull off the age. You're pulling off the location API. Okay, not from, like, the app store or their phone device?

[11:36] Elvis Ge (programination.com)
Not from the app store. So, like, unless and until they register, they are not part of your application.

[11:43] Aakash Dhar (sorigin.com)
You can have the app on your phone. That doesn't change anything. But, like, what to say, your, this thing, like, when they start using the app, that is when your legal boundaries step in, right? So, before the register, we get the location, we get the age. The legal age of that country. And if they are above it, good enough, we allow them to register. If not, we tell them that, sorry, based on the country that you're in, your legal age does not qualify. That's it. I understand that part.

[12:17] Elvis Ge (programination.com)
I'm just wondering because this requires them to turn on their location versus if we can grab it more passively.

[12:28] Aakash Dhar (sorigin.com)
Because the reason why is, I don't know, actually, I have to talk to a lawyer for this.

[12:35] Elvis Ge (programination.com)
I guess like, you know, let's say, let's say, you know, in some countries, you said like the legal age is 16, right? So I guess the, I guess you have to, even if I'm from the US and I travel to a country where the drinking age is 16, I can, I follow the, the country's legal, right? So if I can't drink, I can, let's say in America, I can't drink until I'm 21. But if I go to. I don't know which country. India is 16? 18.

[13:05] Aakash Dhar (sorigin.com)
India is 18. Germany is 16.

[13:09] Elvis Ge (programination.com)
Okay. Let's say I traveled to Germany. If I'm 16, I can't drink in America, but I can drink in Germany if I'm American.

[13:16] Aakash Dhar (sorigin.com)
Yes, you can. That doesn't matter.

[13:20] Elvis Ge (programination.com)
Because when you're in the country, that country's rules apply.

[13:26] Aakash Dhar (sorigin.com)
It's kind of a messy domain. So it would be better if we can get that thing sorted off with a lawyer. Okay. They would be actually be able to help. I'll, I'll, yeah, I'll check.

[13:35] Elvis Ge (programination.com)
Um, okay. I guess we can, then maybe, because we do ask location later. So maybe we can turn down the, if they're under, let's say whatever the age is, instead of, it will suck, but I guess it's okay.

[13:51] Aakash Dhar (sorigin.com)
Okay.

[13:51] Elvis Ge (programination.com)
We'll, we will let them continue the path. And then at the very.

[13:59] Aakash Dhar (sorigin.com)
Great. Great. Great. Great. Great. Great. Great. Thank At the very end, say, maybe continue after the required stuff, maybe.

[14:08] Elvis Ge (programination.com)
So like location, maybe a location. Because I don't want them, like, if they go through everything, I'm worried that they will get a little angry at the end.

[14:20] Aakash Dhar (sorigin.com)
It is true. So if you are not allowing them to go ahead, stop them right at the first step. If not, you have to allow them. Because the thing is, like, if I'm going through 10 screens, and at the end, if I'm getting to know that, oh, shoot, I cannot register because I'm not of the correct legal age, then that becomes a hassle. And that actually runs against your favor. In the sense, like, I have spent so much time getting all these things set up. So either you have to do it before, or, like, something else. Yeah, guess we'll trigger... ... ...

[15:00] Elvis Ge (programination.com)
I guess we'll do this. If they mark their age under, let's say 19 or something, we'll trigger the location permission. Like if their age is a certain limit, like if it's obviously if their age is over, whatever, 19 or 20, because for now I'm just focused on Korea and the U.S., and then like you said, most countries are probably not going to be like, are probably under 19, know what mean? Like they're probably most countries we deal with are not going to be like 20 or 21 or whatever. So, so we'll trigger that logic if it's under to ask for location early. And then if their location doesn't, isn't that, then we'll say sorry. It's only for people under whatever in this country. Well, we'll mention the country, I guess, so that they know.

[15:49] Aakash Dhar (sorigin.com)
Okay.

[15:50] Elvis Ge (programination.com)
And then, yeah, and then you have the name and username.

[15:56] Aakash Dhar (sorigin.com)
Username generator, some suggestions based off maybe what you typed if it doesn't.

[16:00] Elvis Ge (programination.com)
it's already taken. Then you have the location.

[16:04] Aakash Dhar (sorigin.com)
Okay. And then it's just a map.

[16:07] Elvis Ge (programination.com)
I don't know if we, I don't know if this, this pop-up is this, or just be a map current location. I, I showed before, I think Dheeraj wasn't able to do it, but hopefully now with AI, maybe we can figure out how to do it easier. So a lot of the maps, when you choose a location, what I like that you can do is on like, you know, using your fingers, you can move around the map and then you can kind of, it's either, or either when you move around, like kind of when you use Uber or whatever, driving service, that you can choose the location to pick you up. It's similar, right? So either you can tap on, I think different maps do differently. I don't care either way. Either you tap on, you can move the map and then tap the new location or the location marker is always like in the center. And then when you move the map, it, this, you know, when you move the map, the center, the pin. It's always there, so it just moves with you. And then you choose that location, whatever it lands on, right?

[17:06] Aakash Dhar (sorigin.com)
That's the standard procedure, right? For some reason, Dheeraj wasn't able to do it. he, like, you know, when you do, on Google Maps, that's not it. On Google Maps, you have to tap on the map to pick a new point, right? Yes. I think Uber is, you move the map and the marker moves with you. Okay. Okay.

[17:31] Elvis Ge (programination.com)
Other option, the other option is, as you just said, marker stays as is.

[17:36] Aakash Dhar (sorigin.com)
There is no change in the marker. You move the map underneath it. Yeah, that's Uber, think. That's, yeah, that's Uber, that's Ola, that's the ride-sharing apps that we have in India, Ola over Rapido.

[17:47] Elvis Ge (programination.com)
They have that. It could be, it could honestly be both, too. I think you could, if you don't touch the pin, right, then it just stays and you can move the map and the pin moves around with you. Right? Mm-hmm. Mm Or, and then if you, if it's not, for some reason, getting exactly, I guess you could tap the map, and then it'll move that pin to that area. Okay, so, so, so, so that's one important thing that Deepak and I need to figure out.

[18:16] Aakash Dhar (sorigin.com)
I'm just saying this out so that it's in my recorder, and I can actually take note out of that. Okay, yeah, that's fine. Okay, okay, next.

[18:23] Elvis Ge (programination.com)
The reason, there's, there's pros and cons, I think, right? So, for example, on Google, it makes sense to me, right? So, if you have this map, and then you're like, oh, I want to go to this location, right? I want to go to this restaurant. I think it's easier than, instead of moving around the map so that the point goes exactly to the restaurant's location, if you see the restaurant on the map, it's easier to tap the restaurant, and then it goes there. You know what mean? Yeah, I got that. Right. So, I think it depends. Depends on the use case. I think for this one, I think, just off the top of my head, I think the map moving and the marker stays in the center without you tapping, I think is a better experience, I think.

[19:19] Aakash Dhar (sorigin.com)
I would rather say, let's keep the more, what to say, the behavior around people, ride-sharing app is one of the things which people mostly use, right? So if you keep this map's behavior as close to that, it would actually help the user to understand the thing far easier because that's something they're accustomed to doing it. That's what I'm saying, Aakash. I'm saying both use cases are very common.

[19:47] Elvis Ge (programination.com)
So I don't know what you guys use in India, but I use Google Maps a lot and I use other Korean apps, map apps a lot. And so those apps, you touch, you tap the map to choose.

[20:00] Aakash Dhar (sorigin.com)
Choose the location, okay?

[20:02] Elvis Ge (programination.com)
But like you said, ride-sharing apps like Uber and Lyft, I think the map moves with the marker, right?

[20:10] Aakash Dhar (sorigin.com)
Sorry, like... marker stays.

[20:12] Elvis Ge (programination.com)
The marker stays, yeah, and the map moves, right? So I'm saying both are very common use cases. I think it depends on the use case we're trying to go with because there's a couple times we're going to be using this map.

[20:26] Aakash Dhar (sorigin.com)
And I'm just thinking, do we use the same way throughout or do we use both different ways depending on the use case?

[20:36] Elvis Ge (programination.com)
Different ways may confuse the user because they're using the same app, so maybe they expect the same behavior when they see a map, right? But then like later when you're creating an event, right? And you're like, oh, this event is going to be at this park. My opinion, that functionality is more like Google.

[20:57] Aakash Dhar (sorigin.com)
Okay, because let's say here, right? You see... You see here this map, right?

[21:02] Elvis Ge (programination.com)
And then let's say I want to meet here for the event. I'm meeting at this park. Exact location. Right? So I think the reason why Uber ride-sharing does it is because they care more about the specific latitude, longitude, right? Exact location.

[21:23] Aakash Dhar (sorigin.com)
But for event, it's more like let's meet at the park, I think, right?

[21:28] Elvis Ge (programination.com)
Or let's meet at the restaurant. So you can search the restaurant. But like if you see the store, you just tap like on Google Maps, right?

[21:34] Aakash Dhar (sorigin.com)
You just tap on the store, right? You tap on the park and it just marks the park as the...

[21:40] Elvis Ge (programination.com)
So I think that's a better user experience. Even for this one, what your location is, this is your like location for your profile for yourself.

[21:49] Aakash Dhar (sorigin.com)
I don't need to grab this, like we don't need to know your home, right?

[21:52] Elvis Ge (programination.com)
I don't want anyone to know your latitude, longitude of your home. I just need to know the general city that you live in.

[21:59] Aakash Dhar (sorigin.com)
All right. All right.

[22:01] Elvis Ge (programination.com)
So I think the Google use case is better, like Google Maps use case, but I think, Deepak, you unmuted, so don't know if you want to say something earlier you unmuted.

[22:13] Deepak Tewatia
The main thing, like, if you are a person about some place, like, users, like, persons can be, choose a street too, right?

[22:24] Aakash Dhar (sorigin.com)
So, for example, a street, a street would have, can I lack multiple? There addresses within that area. So pinpointing to a particular location, for example, like, I stay in a society, there are, like, A to N wings, N to N buildings. So if I type in my society's name, it will give a very general idea of that space. But if I, if I am able to pinpoint a particular building, let's say that I know that this is A wing. Okay, if I can move the mouse over to that point, it would be easier. You can tap, right? You can search and you can tap, right? Yeah, but the point is like, for example, if I'm searching for my apartment, I don't get all the wings in Google Maps. Anyone who has actually added, those I can select. Not all of them. I can select my society in general. That's perfectly fine. I cannot select the exact building. So then in that case, what you would have to do is, we can do both. Ideally, we should be having both the features. Both the features are better in their own sense, in terms of uses. So we can have an option where they can very specifically mention where the location is. Yeah, so I was thinking this. So one is obviously you can search.

[23:52] Elvis Ge (programination.com)
So let's say I'm searching a building. So, and then the other thing maybe to note is you can use your... -finger to zoom and zoom out, right?

[24:03] Aakash Dhar (sorigin.com)
So obviously if you zoom out, you're going to see more, less detail, right? More generic area, right?

[24:12] Elvis Ge (programination.com)
And then if you want a specific building, then you can zoom in, right?

[24:19] Aakash Dhar (sorigin.com)
So I would zoom in and then, yeah, so obviously not, you know, these buildings are not marked, right? Not all these buildings, some of these might be like apartments or whatever.

[24:30] Elvis Ge (programination.com)
yeah, so I would, you know, yes, you can choose these, but if you're like, no, we're meeting here, then yeah, you should be able to drop your location in there.

[24:42] Deepak Tewatia
Like currently, how we doing like food ordering app and these apps, we, instead of location, we also take text as an address. So that would be good too, if we can do that. So you can come on location and then you can like, suppose we. We have eight wings, right? So you can mention in that address that is C4 2003. So that's kind of thing like that's C4 is the wing, the wing number.

[25:14] Aakash Dhar (sorigin.com)
Oh, yeah, yeah, yeah.

[25:16] Elvis Ge (programination.com)
the event, obviously, it doesn't make sense for your profile. don't need to know you, right?

[25:24] Aakash Dhar (sorigin.com)
But for the event, there will be an optional note section. That you can tie to the event. Give exactly the location. to the location, yeah.

[25:35] Elvis Ge (programination.com)
you can, on the map, you choose like the building or whatever, right? And then on the optional note, you can say third floor, whatever.

[25:43] Aakash Dhar (sorigin.com)
Correct, exactly. Exactly, exactly. That's the one, that's the thing.

[25:47] Elvis Ge (programination.com)
Yeah, yeah. But either way, I'm just saying how the map would work. I think it's more, so instead of having like the location in the middle here, and then you move the map and it stays, space, You're I think my ...

[26:00] Aakash Dhar (sorigin.com)
Kinion is obviously zoom in, zoom out for how detailed you want, and then you would just click, you know, click on the thing, and then that's the location, right? That, I think, functionality is better than the Uber one where you're just moving around.

[26:15] Deepak Tewatia
Yeah.

[26:15] Elvis Ge (programination.com)
Because that one, I think, needs a very specific, but the problem with that is the very specific one is good for Uber because you don't, the driver doesn't need to know, like, this latitude, longitude is a, building called, whatever, building called, uh, McDonald's, let's say, right? It doesn't, I don't think it shows you that on, on Uber, right? It just tells you latitude, longitude, but it doesn't say, like, oh, this building is McDonald's. But for an event app, I think latitude, longitude is obviously not good for normal humans to read. So they want to see, like, oh, this is, this is at McDonald's. This is the McDonald's near the subway station, right?

[26:56] Aakash Dhar (sorigin.com)
I think, like, we need to show the, the name. I Uber's, sorry, Google's style, map style is better than Uber's location.

[27:08] Elvis Ge (programination.com)
So ideally the thing is Uber's use cases, it needs a very specific point.

[27:14] Aakash Dhar (sorigin.com)
So if I'm picking someone up, I need that exact location where I need to pick up. So in that case, that would make sense. But as we mentioned in this, you can select, if your event is happening somewhere, you can very well say the event is happening here, then give it extra details. And that should be perfectly fine. Yeah. Yeah. Sure. That, that, that locks it up. Okay. Okay. All right. So, okay. So it's, goes to map, then you have the profile photo, upload or choose.

[27:42] Elvis Ge (programination.com)
Then you have, these start getting kind of, all these are optional. The only thing we really need to create a person's account is just name, username. And we have their phone number, right? So they can log in with their phone number. I guess, do we need to ask for password? So, okay. See No, we went for that, no?

[28:02] Aakash Dhar (sorigin.com)
Security codes. That's OTP, right? Yeah, this is OTP, but I'm guessing, should we ask for password in case? In case, in the sense, generally, a lot of these apps nowadays, they go directly for the OTP thing. I guess it's an edge case, like if they've lost, I don't know, like some other security method.

[28:28] Elvis Ge (programination.com)
In a recent app that I worked on, we had a problem where like SMS sending and your SMS or WhatsApp sending was blocked by location.

[28:40] Aakash Dhar (sorigin.com)
So basically, the business was registered in USA. So WhatsApp or Twilio, they were not able to function in that particular geographic area until and unless you have a registered business over there. I'm assuming for your Korea and US, it should be fine. It should be perfectly fine. But if you expand into a location, which does which For which you would need a business over there, then it's better to have both the options. Like you can ask the user, which one do you want to co-write with, OTP or a regular password. If they allow, if they select a password as well, let them add a password. That's all good. But we need the OTP to verify their phone number. That's also there. Yeah. Yeah. Yeah, because I'm just seeing in many use cases that sometimes, yes, the phone's not working.

[29:32] Elvis Ge (programination.com)
Like, I don't know in India and in Korea, I feel people still like using pass, typing passwords in.

[29:42] Aakash Dhar (sorigin.com)
And I'm sure maybe a lot of other countries still do. Yes. And I think it's good safety measure. Like you said, if one login method doesn't work, right? The problem here is OTP doesn't allow you to forgot password, right?

[29:58] Elvis Ge (programination.com)
So it's not like I forgot my phone. Or I don't have access to my phone, right? So at least the password, if you've got your password, you can reset it and still get it. So anyways, what I mean is I think I will put a password here, field.

[30:12] Aakash Dhar (sorigin.com)
Then everything else here is optional, technically. I'm debating if location should be required because I guess we need location for age.

[30:23] Elvis Ge (programination.com)
Yeah, age, but we're going to ask here anyway, so Trigger wants the logic. But I guess here is, technically, this app would really suck without your location, right? Because we can't really recommend you anything if we don't have your location.

[30:37] Aakash Dhar (sorigin.com)
So I'm just wondering if we make it a requirement versus asking the agent. Make it a requirement. Make it a requirement. Because as you said, since your app is very location-centric, if you don't have that, it's pretty much anything down the line will not, we cannot get them things right from the get-go. For example, if we get the location... Once they register, we can actually show them something like in your area, in your city, in this area. Yeah, I mean, even if we don't have that location, we're going to show them something.

[31:11] Elvis Ge (programination.com)
We'll pick a default location anyways. I guess the point is some, I assume, there will be some people who are very hesitant to share too many things and they just want to kind of log in, like her account and just to play around, just to see the app. And then once they're like, oh, this looks good, they'll do it. The other use case is if you got invited, right, then we don't need your location, technically. We just need you to create a council and you can quickly go to the event that you're invited to, right, and you can always turn on your location later. So I think that was the reason. It's not the best experience, but it's not required, that's why.

[31:52] Aakash Dhar (sorigin.com)
You can actually start as a city, right? You can ask the city. The city. The point is, I guess it's like.

[32:00] Elvis Ge (programination.com)
Like you're still requiring someone to do something, right? You're still requiring someone to give you more info than what is this. Like my general thought process, my general thinking with asking for information usually is more about ask it at the point that they need it or at the point that they see the value kind of thing, right? So unless you can clearly explain why, which, you know, we're trying to talk here maybe, a little pop-up, why you should turn it on. Unless you can clearly explain the value, it's more like they're so, how should I say, like, let's say they use the app without the location. They're just going to see, let's say, we just say, for example, we'll put default is India, right? And we show all these India events and they're like, why am I seeing these India events, right? And then they see this little pop-up that says, you know, turn on your location for more personalized results. I think there's a better use, how should I say, selling point than... Asking them right away when they don't see the value yet.

[33:04] Aakash Dhar (sorigin.com)
Does that make sense? So cause and a result kind of an approach. You see this, this is not what you need, and we refined it for you.

[33:12] Elvis Ge (programination.com)
Yeah, but it's still, everything is still optional, right? Technically, you can still, the reason why I'm saying the difference between optional and required is like, required is like, we can't create your account without like a, yeah, without username or password or something, you know, I mean, something to identify you, right?

[33:28] Aakash Dhar (sorigin.com)
That's the bare minimum.

[33:30] Elvis Ge (programination.com)
Technically though, without your location, you could still search events, could still create an event, right? You can still look at people.

[33:38] Aakash Dhar (sorigin.com)
So there's nothing stopping you from using the app. That's why I was saying it's optional, right?

[33:43] Elvis Ge (programination.com)
And then it's like, then you're trying to sell the person, like these days, right? Especially in America, I don't know about India and Korea. I think it's Asia is a little different, but in America, we're so sensitive about giving information, right?

[33:59] Aakash Dhar (sorigin.com)
And so

[34:00] Elvis Ge (programination.com)
It's more like, yeah, so I'm like trying to, in a way, we're like trying to sell them, oh, you should give us, because of this, you should, not like, just be like, assuming that they should give it to us, right? It's more like, this is why you should give it to us, because, you know, it will enhance your experience at the app, you get to, whatever it is, right? So I'm just general, general thinking, usually, for my, when I decide these things.

[34:25] Aakash Dhar (sorigin.com)
I think, at least what they're thinking is actually very correct for us, they are very hesitant, sort of, people, very, very, yeah. Unlike, uh, the Asians of content, it's okay, fine, it's just efficient. Yeah, China is very open to giving all the information because of the government. They, they feel like the more information to give, the better, that the government can protect them or something, or it's, it's more efficient. Like, they find, I think these days in China, I haven't been in a while, but like, you, you don't even need to, pay with card or phone or anything, like, they just scan your face, and your face is connected. So obviously in America that would never happen, like we don't, no one, everyone would be so scared to have your face in the, even though it probably, they probably already have it technically, I feel, they have a lot of your info anyways, but I think if the people interacting, yeah, yeah, don't know, India, don't know, maybe you guys are in the middle between the two, like, we are, we are in the middle, we are definitely in middle, yeah, okay, got it. Right, sure, that, that makes sense.

[35:32] Elvis Ge (programination.com)
So, so you have the, yeah, profile, then you have a little bit more information about you, which is your gender, this is, the reason why we need this is more, again, for the recommendation algorithm. Yes, yes, yes, yes, for discussion. So what languages you speak, I think instead of MBTI, I was gonna, I'm debating, instead of MBTI, it's just gonna be a list of tags that you can, Fun personality traits.

[36:02] Aakash Dhar (sorigin.com)
Including the MBTI. And then you can add your own.

[36:06] Elvis Ge (programination.com)
So then there will be a list of maybe the top, whatever, 10 or 20 most common ones, I think. And then people can, as they search, the other ones will exist.

[36:16] Aakash Dhar (sorigin.com)
And if there doesn't exist, they can just add it. And so now just create a language.

[36:24] Elvis Ge (programination.com)
This will create a more database of tags that people can associate with. And we can use this to also help match with events that might fit these tags. Your language. So you put the language and then your efficiency level. You know, the tags. Then you have the categories, like what kind of things you're interested in. I'm interested in music and sports and blah, blah, blah. And then if you are, you can skip.

[36:51] Aakash Dhar (sorigin.com)
I should maybe use the word skip. Yeah. Then it's, you know, what university you're a part of. If your university doesn't exist. You can raise it, right? Yeah, you can raise it. So this is suggested school.

[37:05] Elvis Ge (programination.com)
So school name, what city they're in, and it's an option of the URL so that I can reach out to them or something. Okay. Yeah, and then that's it. And then I guess here it's like if any, if it's already been turned on, like they are maybe already turned on the locations, a location, then this would be switched on. But the ones that, I don't think we need all these, it's just the AI creating all of them, but maybe notifications we need.

[37:34] Aakash Dhar (sorigin.com)
These photos we need too, because if they're uploading from the gallery.

[37:38] Elvis Ge (programination.com)
Context, not yet. I think maybe in phase, you know, a little later phase, once there are more users, then we can ask for context and search context. And then calendar, not yet. I don't even know how this calendar would work.

[37:52] Aakash Dhar (sorigin.com)
This basically connects to your Google Calendar. So if your Google Calendar has meetings or something. between that meeting or event that time. For example, I have a meeting that is happening at like 11 o'clock. But I have a meeting at 11 o'clock.

[38:08] Elvis Ge (programination.com)
You said Google Calendar. Isn't this whatever your device, this is connected to your device, right? These are all device specific. So this is whatever calendar is on your device, right?

[38:18] Aakash Dhar (sorigin.com)
Correct, yes. Your Google Accounts calendar, basically. Well, if I have an iPhone, I also have an iCalendar. Yes, yes. Whichever calendar you have in that case. So whatever device default calendar it is, yeah. Then, yeah, that might be useful too, so. Oh, why is this happening?

[38:41] Elvis Ge (programination.com)
Okay, anyways.

[38:44] Aakash Dhar (sorigin.com)
Okay. So that was, so that was the onboarding login. It's much simpler, obviously. have just the, here, if they register with any of these things before, if we have the username, email, phone.

[38:57] Elvis Ge (programination.com)
I think I'll make this a drop-down here. But basically, if you're typing a phone number, hopefully we can detect, like once you're done, we'll detect if it's a phone number. Email, obviously, if it has an add symbol, then we'll know when you're done if it's an email and a username. I don't think this would need to be here. This will remove, but yeah. So we'll detect, but if they can change it, I'll make this a drop-down so they can choose between the phone, email, or username. Then, obviously, I'm used to these days never logging in, so using biometrics instead, if we can.

[39:35] Aakash Dhar (sorigin.com)
I don't know how hard it is to build those things. Forgot password flow, and then... does it do this? Location permissions and everything, yeah. Yeah, permissions, access, things like that.

[39:50] Elvis Ge (programination.com)
I don't think there's anything to discuss on these screens. Sorry, I want to use a different mouse.

[39:57] Aakash Dhar (sorigin.com)
Like giving drop-down there.

[40:00] Deepak Tewatia
It doesn't feel like a good UX.

[40:03] Aakash Dhar (sorigin.com)
Instead, we can get things on our end of self.

[40:07] Deepak Tewatia
Here's a telephone number or email or email.

[40:13] Aakash Dhar (sorigin.com)
What do you mean? So what the book is saying is, in the welcome back screen, you've mentioned, right? Like on the left side, you would drop down. Like, which one is it? Yeah, if they want to change it, right?

[40:25] Elvis Ge (programination.com)
Obviously, we would auto-detect and then we would select it for them. But if they want to change it, if it's for some reason, our detection was incorrect, is what I was saying.

[40:37] Aakash Dhar (sorigin.com)
Okay. Honestly, it's been evoked for me. But Deepak, what are you? So I think, I'm hoping it's similar to this here, here as well.

[40:48] Elvis Ge (programination.com)
When you tap this, right, the country code, the screen doesn't have it. But in the previous, I had an, I have an, on a different design. When you tap this, it gives you a list, a search and a list. of all the countries. So you can either tap or search the country. But it's similar. I mean, we can make it a little bigger so it's more obvious that this is tappable.

[41:10] Aakash Dhar (sorigin.com)
But what was your concern?

[41:12] Elvis Ge (programination.com)
Is it still a fixture concern or not really? Is it still a bad experience, you think? Yeah.

[41:17] Deepak Tewatia
Okay, okay.

[41:18] Elvis Ge (programination.com)
Because the other one that the AI created was three navigation at the top.

[41:27] Aakash Dhar (sorigin.com)
Yeah. I thought it was ugly.

[41:29] Elvis Ge (programination.com)
Ugly. It was more of an ugly design, not necessarily functional. Functional? Yes. Very easy. A phone, email, password.

[41:35] Aakash Dhar (sorigin.com)
But I felt like it was unnecessary to instead just put it here. That is only the same brand that is this thing. So get your phone number, email, or even from the same input. by default, like based on whatever the type we get that thing. Yeah. Okay. And I think that's already built that in.

[41:58] Elvis Ge (programination.com)
don't know, again, I don't know how much of the old Who we're using, or we're just going to rebuild everything with AI, don't know. But technically, think that logic exists.

[42:05] Aakash Dhar (sorigin.com)
We will salvage whatever.

[42:07] Elvis Ge (programination.com)
Like we have been working on it.

[42:10] Aakash Dhar (sorigin.com)
So we are salvaging whatever we can from the older code and building on top of it. So that will reduce the timeline. Primarily, that's the primary concern. Reduce the timeline and also get things sorted faster. Okay.

[42:27] Elvis Ge (programination.com)
These are just other screens in terms of all the error states and whatever connection, like things are not connected. This is the old, yeah, this is the older design. Okay. So that's the onboarding login for Graphics with Flow. Then you have the idea is done. I don't know if I showed you guys this last time. So the, one of the differences, I don't know if it was there. So remember how we got all the information out of a person in terms of like their age, their location, their gender and stuff. So this would, so before you join something, we'll just give you a summary, right? And then that's it.

[43:08] Aakash Dhar (sorigin.com)
So you can't see all the people who are interested. You can just see your mutual, so your friends basically. You can see if they're going or they're interested, stuff like that. But you can't see all, right?

[43:20] Elvis Ge (programination.com)
So this is locked until, so I'm trying to force people to, to at least join the event or say they're interested in an idea before they can see more info about the thing.

[43:32] Aakash Dhar (sorigin.com)
But here you can see like, I'm hoping like this summary is enough to like, you see what the event, so I think there's two parts usually for like, what makes you decide.

[43:40] Elvis Ge (programination.com)
It's more like the event itself or the idea, whatever.

[43:44] Aakash Dhar (sorigin.com)
So you see like the pictures, you see what the title, description, right?

[43:48] Elvis Ge (programination.com)
You know what it's about. And then the other part is like the people, right? I think a lot of times people choose an event or idea based on the people. I do myself. I do myself.

[43:59] Aakash Dhar (sorigin.com)
Yeah.

[44:00] Elvis Ge (programination.com)
But I don't want it to, how should I say, I know it's humans, but we also choose based off of people's looks, but it's not a dating app. So that's why I'm not showing the app for all the people, I'm just showing, you know, like, oh, there's people around your age, there's people from your area, there's people that like similar things that you like, right? That kind of thing, as opposed to like, you can stalk and look at all the people's photos and like, oh, there's this hot girl, I want to go see, I want to go to this event or idea. Make sense, make sense.

[44:37] Aakash Dhar (sorigin.com)
It becomes more of a security hazard, means liability, more of a liability.

[44:43] Deepak Tewatia
Yeah, like, ideally, the people can see someone's profile, So it can go over there and see, it can see his or her picture, actually, right?

[44:55] Aakash Dhar (sorigin.com)
You can see, you can see that your mutuals, right? The people that you're already.

[45:02] Deepak Tewatia
On Instagram or any other platform, can go on any profile and I can see only the profile picture at least so that I can connect. Likewise, we are in Google Meet, So I can see Elvis, the photos and other pictures, same thing.

[45:20] Aakash Dhar (sorigin.com)
Profile pic, that's what it Profile pic action, yeah. You want to show the list of all the profile pic but not let them do anything with it?

[45:28] Elvis Ge (programination.com)
Like they can't click it? Yeah, they cannot click it, they cannot take screenshots and things like that.

[45:38] Aakash Dhar (sorigin.com)
Maybe, maybe.

[45:39] Deepak Tewatia
But ah, that's a different thing, we can discuss it later, but just to let you know that these things.

[45:46] Elvis Ge (programination.com)
Yeah, maybe the other reason, how should I say, one of the reasons why I'm making this business is not, I should say, not only to make a business. My, my, my actual, like, my goal, my goal with this, I had this idea for a long time, my goal of this was really to bring people together, like two parts, bring people together that you wouldn't normally meet, right? And I think like, I think this world would be a better place if you talk with new people and meet new people, you understand more different types of people. And so one way to meet new people is by doing stuff together, right? Doing events or activities together. And so like, maybe by going to this cooking class, you meet someone new that you would never have met, right?

[46:37] Aakash Dhar (sorigin.com)
That's one. And then two is like, just in general, over these past 10 years, I had this idea was like, there's this growing, growing dependency on like technology and kind of just using, like being absorbed with technology, like social media, YouTube, whatever, TikTok, whatever it is, right?

[46:54] Elvis Ge (programination.com)
And not actually being part of the world. Yeah. Right. And I think that, I think timing is somewhat good because this new generation understands both, like they're using AI, they love TikTok and whatnot, but at the same time, I've been reading articles and listening, like this generation also understands that like, hey, I want to also be happy and enjoy this world and like experience the world around me as well. So, the reason why this is designed this way, in my opinion, looks a lot like Instagram. It's kind of on purpose, right? And I'm thinking like, don't want, how should I, I don't think I want to go complete opposite and be like, oh, we're not going to use AI or tech or anything. We're going to do everything manual from now on. And like, you know, like I still want to be, it still needs to be a successful business, but using a lot of the design and principles of maybe addicting or whatever. Social media apps, but for a good reason, right? To get people to go out and try new things and meet new people. So one of the reasons why I was like, oh, maybe we don't show, right? I don't even, I'm debating also like showing gender or not, right? Is showing pictures and gender because we're so used to judging people based on their looks before we decide that I'm like, maybe we should, you know, just focus on the activity, focus, and then like once you, because sometimes when you meet someone and talk to them, then you realize, you know, it's like, you know, unless you're looking for a girlfriend, boyfriend, fine, right?

[48:42] Aakash Dhar (sorigin.com)
But this is not a dating app. This is just doing something and making friends, hopefully, right? If you happen to date, that's up to you, but like, it's not a dating app.

[48:49] Elvis Ge (programination.com)
That's why I'm like debating about showing too much. Deepak, do want say something? I think you're saying something. No, no, no, no.

[48:57] Deepak Tewatia
I get it. Yeah.

[49:00] Elvis Ge (programination.com)
That's kind of like a lot of the reasons I'm like doing these things is partially that underlying goal for myself for this app. It's not just about like how do I make this app the most successful, addicting, you know, because then we could do a lot, right, to make it more like, I was like, one thing that someone asked me is like, hey, we should show like on your profile, we should show what events you're going to, right? And then people can, because then people would love that, right? If I, if I was stalking you, right, I can see all the events you're going, like, it's like Instagram used to have this feature. If you remember a long time ago, Instagram in the notifications used to show you what your follow or like what your mutuals liked or what posts they like.

[49:42] Aakash Dhar (sorigin.com)
Yeah, exactly. And it took it down. But now they brought something very similar. It's very addicting. They brought very similar. I don't know if you use Instagram, but like now they brought in like all the reels that your friends like.

[49:55] Elvis Ge (programination.com)
But like, it doesn't show you like an easy format, you just scroll. So when When you scroll, you can see, like, oh, my friend liked this, or my friend follows this, right? Correct, correct, correct, correct, correct, yes.

[50:05] Aakash Dhar (sorigin.com)
And it's like, I agree, it's addicting.

[50:07] Elvis Ge (programination.com)
Like, one for me, it's like, oh, I like this girl that I like, likes this post, right?

[50:12] Aakash Dhar (sorigin.com)
And I get to know what kind of stuff she likes. But, like, I don't know if it's better, like, even though it's addicting, is it better for us as a society, as a human? I'm not sure, so that's why I'm, like, trying to... Ideally, the way you are doing anything, this makes sense, because you don't want, like, a dating app. It's not a dating app, it's a meetup app. Okay, so that way, that logic stays very clear. Like, let's keep that grounded in that itself. And when it comes to showing profile of pics, I go with, I side with your thoughts on this. Like, let's let people beat. Let people beat and decide, rather than judging people right off the bat.

[50:53] Elvis Ge (programination.com)
Yeah, so I'm showing, obviously, like I said, I'm still showing the mutual because they're your friends. So it's more... not for judging like, oh, is this cute or whatever person going?

[51:03] Aakash Dhar (sorigin.com)
It's more like, oh, my friends are going too. It's more like a social proof, right? Less about like, oh, this cute girl is going and I want to follow. Exactly, exactly. It becomes a stalking app then. Yeah. So, and then it's mutual.

[51:17] Elvis Ge (programination.com)
So hopefully mutual people, if they agree to follow you and you follow them, then hopefully it's, you know, you trust them, I guess. You trust each other.

[51:28] Aakash Dhar (sorigin.com)
And if not, I guess they can. Block you, but yeah.

[51:32] Elvis Ge (programination.com)
So I'm trying to, I'm trying to do this balance game, I guess, right? Between what, what makes a good app, you know, there's a lot to learn from all these existing apps and all these addictive TikTok, Instagram, all these apps, right? They do many things well, but like, I'm trying to balance between what is good, I guess, and what is bad. I don't know if you have, I don't have kids, but, you know, I have a lot of friends that have kids. I I know that they, I They see a lot of the negative effects, right? I think Facebook just got sued because of all the, you know, all the stuff they did, but yeah. Anyways, so just, sorry, I was painting a picture so that you guys can kind of understand where I'm coming from.

[52:14] Aakash Dhar (sorigin.com)
Yeah, I get it.

[52:16] Elvis Ge (programination.com)
So, yeah, so if you're not interested, you say interested, and once you're interested, it becomes this heart, and then you can make it happen.

[52:23] Aakash Dhar (sorigin.com)
So these are ideas.

[52:25] Elvis Ge (programination.com)
Ideas, basically, it's just, you know, something you want to do, but you don't want to be the one planning it or whatever. So people can create events out of your idea, okay?

[52:35] Aakash Dhar (sorigin.com)
That's basically the concept. Then you have, like, you know, it's very similar to the event.

[52:41] Elvis Ge (programination.com)
You have the details, you have the discussion board, and here is going to be, in the event, this was the media. But I don't know if we, I'm debating if we need any media. Here, for ideas, like, for people to upload pictures, because there's no event, you're just. It's idea, but I don't know. Maybe people want to upload pictures for ideas? don't know.

[53:04] Aakash Dhar (sorigin.com)
We'll see. Maybe in later phases. don't know. But would you put an image to an idea? I don't know.

[53:13] Elvis Ge (programination.com)
Maybe like, hey, I want to do a cooking class and maybe someone's uploading like what they want to cook. I don't know.

[53:20] Aakash Dhar (sorigin.com)
But they could do it in the discussion.

[53:22] Elvis Ge (programination.com)
Like they can upload photos in discussion.

[53:24] Aakash Dhar (sorigin.com)
So I don't know. For now, it's not there. That's why I wasn't sure. Okay, okay, okay. People generally ads currently, AI-generated images are really so. AI-generated images are really serious. Like I really hate them. They look really very, very, very predictive. Like I can see an image, I can say that this is chargeability. Chargeability. It cannot be a real image. Yeah, I decided for now not to allow.

[53:51] Elvis Ge (programination.com)
So here, like obviously you do have some photos. It's just the cover, like the photo up here, right? When you create the idea.

[53:57] Aakash Dhar (sorigin.com)
So you can create, I want to do, I want to go hike. Who's interested in hiking?

[54:02] Elvis Ge (programination.com)
You can upload a bunch of hiking features. Obviously, we can't stop people from uploading AI-generated images that they made separately, but for now, in this app, there's no, the only AI in here that the user interfaces with is creating the, like, when they write the prompt, it'll create the idea event for them, right?

[54:24] Aakash Dhar (sorigin.com)
But we won't generate the video or images for them. It's on the podcast.

[54:32] Elvis Ge (programination.com)
Because one, the main reason is because these days, I don't know, I know it's the future maybe, but I don't know, who knows, maybe there's, like, the internet. Some people hated the internet, didn't think the internet was going to be big, and then, obviously, they were wrong. I don't know, like you said, Akash, like, when I see AI-generated images, it just makes me feel a little weird.

[54:54] Aakash Dhar (sorigin.com)
It's very sloppy. It's very sloppy. I know it'll get better. It's going to get better, for sure, but... Irrespectively, like, they don't have that charm, don't have that appeal, like, you would love to interact with it. They don't have that, irrespectively.

[55:09] Deepak Tewatia
I don't know, I find, yeah, I'm just, uh, I was, uh, saying not to, like, generate in the app, but the user then wait outside the app, and they upload it.

[55:19] Aakash Dhar (sorigin.com)
Yeah, no one I can't control, I can't control that, right?

[55:22] Elvis Ge (programination.com)
So I'm just not making it easy for them.

[55:24] Deepak Tewatia
And also, I think it'll save us on tokens, as well. So it's a site, business situation.

[55:30] Elvis Ge (programination.com)
but yeah, it's mainly because, I don't know, there was, like, this new, uh, uh, I think they generated some movie with some...

[55:38] Aakash Dhar (sorigin.com)
C-Dans?

[55:39] Elvis Ge (programination.com)
Oh, C-Dans, I don't know, C-Dans, I don't know which one, but there was, like, using some YouTube, uh, influencers, like, they agreed to sign their faces to be used, uh, and then they generally, it's just, like, it's just so, it's still off. I know it'll get better, but I think, I don't know, I'm, I'm debating if, if people... C-Dans, don't know.-Dans, Because there's already like a big, like a lot of artists and whatnot are against it, so I'm not sure. Like it's a tool, I agree. It's a good tool to use, but I don't know if you should replace what you do. But anyways, so that was the, so those are the three parts.

[56:15] Aakash Dhar (sorigin.com)
You have the details, you have the discussion, and you have the events, the details here.

[56:21] Elvis Ge (programination.com)
So the details are basically like, again, these are an idea, so you don't have to follow it. So they could either post a specific location or a specific date and time, or they can create a poll, okay. But at the end of the day, people can create any types of events, like it doesn't have to follow this, right. So here's the event, there's no events here, these are the polls, right. So you choose a time, you choose the place, then there's like the more options that that's up here. Okay, so you have the save, the share, the more options, more options.

[57:00] Aakash Dhar (sorigin.com)
It's for the host, for each person to create the idea, and more options for the user who's interested in the idea.

[57:09] Elvis Ge (programination.com)
And this is very similar to the creation flow that we have, but so if you create an event from the idea, we would probably, you don't need a prompt anymore because we kind of have the general where it came from. So inspired from this idea, and then we can create, and then obviously you can change, right, if the date is wrong or whatever is wrong, you can change it. And this is if, I was thinking this is useful, I'm not sure, if for some reason the host, the person who created the idea was like, okay, we have too many people in this idea now, talking about so many things in creating, so I'm going to close it to new people. I just want to, I only want it for this, for these people now. So that's this right here, so they closed it, so no one can join anymore, basically, is the concept here. Okay. Okay. Okay. And then. then. That holds close to new interest, like hold it up at least for the initial hits.

[58:05] Aakash Dhar (sorigin.com)
We can keep it built. We don't expose that yet because this would be a new app. So you would want more people to join in, right? Yeah, we can have this for later phases. For later phases. So that idea is good because generally when we go for bike rides, that is something that we look forward to. If someone has joined, we say, no, it's close. It's better to have that feature, but at a later stage.

[58:30] Elvis Ge (programination.com)
When you have people using it. agree. Because we probably don't have that many users anyway.

[58:35] Aakash Dhar (sorigin.com)
So that can be a later phase. then this is, so we have the locate, so this is the time voting. I think it's much simpler. You have the location voting. It's a little more complicated because maybe I want to see it in a map.

[58:50] Elvis Ge (programination.com)
So if you click map view, you will see it on the map like this, right? And if you click on the specific location. It'll take you to, you know, zoom in, maybe whatever. And then here is the little note we said before, right? So you can add a little note to that location. And then you're like, okay, yeah, I like this place.

[59:11] Aakash Dhar (sorigin.com)
I'm going to vote it.

[59:11] Elvis Ge (programination.com)
Or you can go back and see all the locations.

[59:16] Aakash Dhar (sorigin.com)
So that's the idea.

[59:17] Elvis Ge (programination.com)
Again, the general concept is just someone has an idea of something they want to do, but maybe they don't want to be hosting or creating the event. They just want to see who's interested and stuff like that, right? Events, I think we talked about. Do we need to go over events again? I think this is fine.

[59:35] Aakash Dhar (sorigin.com)
No, we went over the events. Yeah. Yeah.

[59:40] Deepak Tewatia
I think the only...

[59:41] Elvis Ge (programination.com)
But you have this in document, right?

[59:43] Aakash Dhar (sorigin.com)
You have...

[59:44] Elvis Ge (programination.com)
This would be all there in the document. Yeah, I'll share the HR file when this is done.

[59:49] Aakash Dhar (sorigin.com)
I'm screenshotting this and putting it in Figma. So the event and idea and creation flow is already in Figma. The only thing I realized was missing is it's probably just one screen.

[59:59] Elvis Ge (programination.com)
one screen. I I I Uh, the screen to save your event or idea as a draft. Okay. That's the only thing. The only thing if like you, if you, you want to leave in the middle or whatever, you can leave a, kind of like Instagram, when you're about to upload something and you leave, it asks you, do you want to save as a draft or do you want to cancel, you know, do you want to delete all, everything you've done?

[1:00:19] Aakash Dhar (sorigin.com)
Okay. Okay.

[1:00:22] Elvis Ge (programination.com)
yeah, the rest is, the home is nothing special. The Explorer is basically, I think done. I just need to screenshot, put it up.

[1:00:31] Aakash Dhar (sorigin.com)
Explorer is also, I mean, it's just, um, I'm thinking, I'm thinking of one thing since we are already moving to that, uh, co-working setup, right? Like we have that GitHub and you can push it, push those. I was thinking, can we do it this way that we can also push from design to a repo? So in that way, it would be easier. Can you? don't know. I guess we can try. I can try. I can give The HTML files, and then you can try, I don't know. That is fine, that is fine, but I think it's like, I don't want to have that thing where you generate something and you share it with me, like, I have a central repo, where you can put, so it's easier, exactly.

[1:01:13] Elvis Ge (programination.com)
So I think the, so I don't know if you can do it here, this is limited, I think, this little chat here.

[1:01:19] Aakash Dhar (sorigin.com)
I don't if in code, I know, I do know you can do it in code, I don't know whether you can do it in design or not, and this is a design, it's not a code. So I look at it, I look at that.

[1:01:31] Elvis Ge (programination.com)
The desktop version, they updated the desktop cloud version to also include a design there. Yes, yes, yes. So maybe you can do it from the desktop version, I don't know if you can do it from the browser version, because this, I don't know, this is. No, no, we use the desktop version.

[1:01:46] Aakash Dhar (sorigin.com)
We are losing the desktop version.

[1:01:48] Elvis Ge (programination.com)
So I don't think there's much to say about Explore, it's just like, you know, main, the main thing, I don't know, because I use a lot of Korean math, apps now, so I don't know if Google does this. Basically, can switch, you can kind of do two types of views. So normally it's a map view, right? And then, but you can also at the, for the map view, they also show like this little bottom tray window here. Yes.

[1:02:14] Aakash Dhar (sorigin.com)
That gives you a list of all the things on the map. Happening on the area, as well. Happening on the area. So for example, like if you search for location, so for example, if I search for Vimanaga, that's an area near my place. Okay. If I search for that area, like it gives me the highlights from that particular area. Yeah. Like this event is happening, this event is happening, like a food event is happening, or some singer is coming to the concert. So you can see those things as well. They call it local vibe. Okay.

[1:02:49] Elvis Ge (programination.com)
So, but yeah, basically, I mean, the feature that I see basically is like some people like to see it on the map. And some people, instead of seeing it, because they have to click everything to see all the details, some people like to

[1:03:00] Aakash Dhar (sorigin.com)
See it in a list view of what's on the map.

[1:03:02] Elvis Ge (programination.com)
So it's just, so you can, you can either drag this up or click list and then basically it's just showing you, yeah, it just shows you the list of things, right?

[1:03:10] Aakash Dhar (sorigin.com)
So this is the full screen version of that. So you can scroll, you could, you know, scroll the list if you wanted to see other things, or you can go back to the map version and you see it on the map, right? That's basically it.

[1:03:20] Elvis Ge (programination.com)
But on, I like this because then on this thing, you also have the filters, right? So you can filter by, you know, the date, the type, the distance, that kind of stuff.

[1:03:34] Aakash Dhar (sorigin.com)
So I like that.

[1:03:35] Elvis Ge (programination.com)
don't know, I'll do a recording of Karima. I don't know if India has a different kind of maps.

[1:03:39] Aakash Dhar (sorigin.com)
Maybe you got something similar. I don't think Google has, I don't know, I have to check again, Google Maps, I don't remember. But yeah, so that's it.

[1:03:46] Elvis Ge (programination.com)
But you can also search, like, so this is, the location is down here. You can change the location. Up here is more like, you know, if you're looking for events, ideas, or a user. Okay. So you can search like, you know, basketball or whatever, running a mobile NC.

[1:04:03] Aakash Dhar (sorigin.com)
Okay. But it'll be based off this location. Got it. Right. Yeah, let's explore. Home is also very, it's just showing you all the things that we recommend to you.

[1:04:16] Elvis Ge (programination.com)
And then the only two, the profile is the other big piece. I will try to get that to you guys. There's another, I'm debating, so there's the notification, where's the notification profile moments.

[1:04:30] Aakash Dhar (sorigin.com)
Chat 10, chat 10. Yeah. Okay.

[1:04:33] Elvis Ge (programination.com)
So there's the chat, where'd it go? Brief 10, brief 10, yes, that's the notification. Chat 1, I mean, it's just chat. So I, I tried again, designed it kind of similar to Instagram chat. So it'll just show you all the list of chats you have. So you, you, you might have chats for each of the events or ideas. Actually, there's no idea chat. There's only event chat. So event chats. And then obviously if you do some like group chat or DM chats with people, I don't like this can be, I don't know if it's easy to build all this. If not, group event chats are first, obviously. DMing a user or creating a group chat with a bunch of users can be later if it can't be done in one shot with AI. But I assume it's probably similar. If you can do an event chat, you can probably do. Ideally, yes.

[1:05:25] Aakash Dhar (sorigin.com)
Yeah, right.

[1:05:26] Elvis Ge (programination.com)
And then, yeah, mean, technically, yeah, so this one you're creating, you know, you can choose the people and then start to chat. You can go to a profile and do a DM, that kind of thing. Yeah, so that's chat. mean, and then the previous screen, previous event had the event chat.

[1:05:44] Aakash Dhar (sorigin.com)
It looked the same basically, right? So just like you have the chat, you have the ability to add photos to the chat. You can reply to a chat and you can like react to the chat. The general functionalities around chat. Yeah. Yeah. The only thing I guess Yeah.

[1:06:00] Elvis Ge (programination.com)
Other apps have, that we're not doing, obviously, is video chat at the moment, or audio, just curly text.

[1:06:09] Aakash Dhar (sorigin.com)
Yeah, let's get to that, least for the time being. Yeah.

[1:06:14] Elvis Ge (programination.com)
You have the notification screen, which is all the notifications. We'll have to define what they are, but we probably have many versions. So we'll have a simpler version for now and then more later. So, like, obviously, any, maybe, like, if people, any event or idea, anyone invited to an event or idea, people who follow you or whatever, that kind of stuff, general ones for now. And then you have the calendar view.

[1:06:37] Aakash Dhar (sorigin.com)
This one I would like to have, but I think this could be a later phase two.

[1:06:40] Elvis Ge (programination.com)
It doesn't have be exactly in phase one. But all the, this is to access, like, you know, all the things that you are going to or interested in, right? So, I guess going to, because ideas don't have a date.

[1:06:53] Aakash Dhar (sorigin.com)
So, all the things you're going to, right? And so you can see it in the, you know, view or list.

[1:07:03] Elvis Ge (programination.com)
That's about it. only thing, profile, I mean, I just need to review, generate it, just review it again. So there's two types. The other big feature was the organization, right?

[1:07:16] Aakash Dhar (sorigin.com)
So there's the human, the user profile.

[1:07:20] Elvis Ge (programination.com)
So you have your profile and the other person's profile, and then you have the organization profile or business profile, we can say.

[1:07:27] Aakash Dhar (sorigin.com)
So any user can create multiple business profiles.

[1:07:32] Elvis Ge (programination.com)
And it's just basically showing that this is my profile. So me, so all my followers, all the events I've created, all the, for now I thinking moments. Moments are like, after you go to an event, you do a reflection, you upload photos, talk about, that's here. I thought it would be something people can, instead of just seeing photos, people can kind of read into people's thoughts about their experience, right? It might be interesting.

[1:07:59] Aakash Dhar (sorigin.com)
Then you have.

[1:08:00] Elvis Ge (programination.com)
Yeah, I realized we're missing this in the onboarding, the description piece. So we might need to either ask that on onboarding or ask them to add it later.

[1:08:10] Aakash Dhar (sorigin.com)
This is how you access the calendar. This is how you edit a profile.

[1:08:13] Elvis Ge (programination.com)
This is how you share your profile to people. This is the more options. The businesses that you are a part of, that you join, like other people's organizations. These are the events that you, events and ideas that you're interested in going to.

[1:08:28] Aakash Dhar (sorigin.com)
These are the things that you save.

[1:08:29] Elvis Ge (programination.com)
These are your photos, photos that you uploaded, right, for, that's connected to all the things that you did. Yeah. So then you have the, I would say like the, I should say, like the full view versus the list view.

[1:08:48] Aakash Dhar (sorigin.com)
That's true. Okay. All right. So you just toggle with this here. Okay. You, you, these will increase the density of how the cards. Yeah. The reason why is.

[1:09:00] Elvis Ge (programination.com)
This is, for me, this is the typical event app style. It's like this kind of smaller card that has a really small picture and then that kind of thing. But I was, the reason why I designed, I was trying to balance again, is that I think people are very visual and so I wanted my app to be, has more visual components, right? To look a little bit more interesting. that's why there's this bigger card to see more of image. And then maybe not even like, this might not even be here. This might be below so the picture doesn't get covered. don't know. But like, that's why there's two.

[1:09:38] Aakash Dhar (sorigin.com)
Some people prefer one. You can have like a small pull-up icon over there, right? So when the people click on that, that particular detail shows up. The, the, the, thing, uh, the Friday, 7 p.m. Chinchon free. That can be like the one, the one below. Yeah. This, details. Since, as you mentioned, people are more visual, right? So you can have just one line of detail over there, like the Make Jolly Plus page on Friday. You can have that one line, and when people click on it, that section expands and grows to this site and gives all the details. So your images won't be cut, and your details would also be cut. Okay. Yeah.

[1:10:21] Elvis Ge (programination.com)
So there is a bunch of versions. The one I liked the most was this version. So you just have only the, you know, the person, the what type of, is it still planning, is it an idea, is it an event, that kind of stuff. And all the details without covering too much of the photo, because this is very, very minimal. And I think this would also go away when you're swiping. So there's multiple. This doesn't always need to be there. It's just the very first screen, maybe. And then also you can tap on it for full image view, right, if you just want to see the image itself.

[1:10:55] Aakash Dhar (sorigin.com)
Okay. Yeah, there's different versions. I was just like trying to play around.

[1:11:00] Elvis Ge (programination.com)
with which version I like the most. But I think there needs to be kind of two or three versions. One is like the bigger, you know, image view, and then one is like more of the smaller text view. Yeah, text, yeah, text.

[1:11:15] Aakash Dhar (sorigin.com)
There's one.

[1:11:19] Elvis Ge (programination.com)
This one here.

[1:11:22] Aakash Dhar (sorigin.com)
Which we saw, like.

[1:11:24] Elvis Ge (programination.com)
Yes, gotcha.

[1:11:25] Aakash Dhar (sorigin.com)
The different density. Like this one. Yeah, yeah, that's one. Right.

[1:11:29] Elvis Ge (programination.com)
So, yeah, um, so it has profiles. So this is my profile, and then, uh, this is like, yeah, if you see full profile, then you can see all the other info if they shared it, um, yeah, I think in the settings, they can choose what's displayed, but like, you know, age, gender, location, the languages to speak, the interests that they chose, like, all the stuff they were, they did on onboarding, all their stuff. Photo collage of their profile. They uploaded multiple things like that. Someone else's profile, you can follow a message. Otherwise, it's basically the same, right? If they, I think here, we're going to, so if we're going to, once we do feedback for events, I think we'll start adding some rating system for people.

[1:12:20] Aakash Dhar (sorigin.com)
So you can kind of see how they're doing in terms of events that they created. All right.

[1:12:27] Elvis Ge (programination.com)
Now this is another concept I was looking about. So here you have the, their kind of bigger background photos.

[1:12:36] Aakash Dhar (sorigin.com)
I'm like debating, obviously the first version I showed you for a very Instagram style. This one's a little different because of the background, right?

[1:12:44] Elvis Ge (programination.com)
Facebook or whatever.

[1:12:45] Aakash Dhar (sorigin.com)
So this allows people to be a little bit more, I guess, customized with their like profile, like to show a little more of their personality. So cover photo and a profile photo. Yeah.

[1:12:58] Elvis Ge (programination.com)
So I'm debating, I don't if you guys have any thoughts, but. Yeah, so that's kind of what this was. I like this style. I hear this style.

[1:13:04] Aakash Dhar (sorigin.com)
I generally have that. You guys like doing the cover photo? Yes. So that's, yeah, so that's what this is. Then you have the editing. And then, yeah, when you click followers, you can see more, like, followers following mutual. It's just, like, too much to, because we're not Instagram, so we can't do followers following mutual here, because there's so much other, I think, we're still an event app, so we should.

[1:13:31] Elvis Ge (programination.com)
Show all the events that this person created, that kind of stuff, you know, events, the ideas that they created. And this is the organizational profile, so.

[1:13:41] Aakash Dhar (sorigin.com)
Okay, This is the business profile.

[1:13:43] Elvis Ge (programination.com)
So you can switch when you click on your, like, up here, right, the little, I think same as Instagram, if you click on your username, right, you can switch the accounts, and then these are blocking settings stuff, but where's the. Organization tonight.

[1:14:05] Aakash Dhar (sorigin.com)
Organization, organization, or profile. guess, yeah, this is follow-up line. It's not showing. I got to find where it was.

[1:14:16] Elvis Ge (programination.com)
But anyways, the slight difference with business profile is it's not just you, right? There's a bunch of people, right?

[1:14:23] Aakash Dhar (sorigin.com)
So you have members, right? Who are probably members.

[1:14:27] Elvis Ge (programination.com)
I think there's two types of members, like just regular members and admin, right? Like admin can do a bunch of things and then they can decide if they allow members to also create events or ideas. But like, so members, you know, can see and interact and then followers are just people following to see some, whatever their, whatever this business is showing to followers, right? Otherwise, if you need to, maybe it's like a member only business. So you need to join a member to like see all the events and all this stuff. So it depends on their setting, privacy setting, but basically. But yeah, the main difference is a business will have multiple people kind of running this business, right?

[1:15:09] Aakash Dhar (sorigin.com)
But it's like how I see it as like, I'm hoping like for now it's like university clubs, right? So obviously a club has multiple members.

[1:15:19] Elvis Ge (programination.com)
So I see this profile as like you have the like, people can suggest like, hey guys, who wants to study this weekend? Or there's this really cool, or it's a holiday, anyone want to travel to, you know, like, so it's like within this profile, people can share ideas and events, right?

[1:15:40] Aakash Dhar (sorigin.com)
And then people can like, you know, vote or want to choose, all this stuff. So like, that's how I'm seeing it. In the future, right, you can also see like internal for like Betacraft or whatever, like you guys, like all the employees can suggest things that they want to do, want to grab lunch together today or whatever. Like, let's have, we need to do whatever it is.

[1:16:01] Elvis Ge (programination.com)
But then, so you can use it as an internal thing, but maybe bigger companies like, I don't know, let's say Apple, they might use it more as a promotional profile, where they're like, hey, we have this event happening, or Spotify, we have this concert going out, so they would have a profile, a business profile for Spotify, and then they would create events.

[1:16:24] Aakash Dhar (sorigin.com)
so maybe they would be like, hey, we have this idea of something, just to see how many of their followers are interested, and then they would create the event after, kind of like a Kickstarter or whatever, once they get more validation that it's a good idea, then they would create the event.

[1:16:43] Elvis Ge (programination.com)
So that's kind of like the future, I imagine, but that's what a business organization profile is. But in general, it's, yeah, it's just a slight difference because of the, you have multiple people, so it has to change a little. But I think it still shows you, you know, the events, the media, maybe this one here, this was all the things that you shared back here. I didn't go over this. This is all like, so these are things you created, but these are things that you kind of interacted with. So things you're going to, interest saved, drafts, things like that.

[1:17:22] Aakash Dhar (sorigin.com)
Because I have to put that, but like this one, I don't think we're sharing to other people.

[1:17:26] Elvis Ge (programination.com)
But this is private to you. Okay. Right. Because I don't think you want to show people all the things that you saved.

[1:17:31] Aakash Dhar (sorigin.com)
No, no, definitely not. Definitely not.

[1:17:35] Elvis Ge (programination.com)
So yeah, that's, that's, is it. That's the whole app for now.

[1:17:40] Aakash Dhar (sorigin.com)
You can see, like most of the screens are done.

[1:17:41] Elvis Ge (programination.com)
I'm just like reviewing and like there's, the reason it takes so long is all these like small edge case or details or something. So I just wanted to like, come up with the screens or design. Makes sense. All finalized before you, but like I will. Yeah, I will go to a probably cafe or something at work today. Okay, and then I'll generate the file for you. You can work on the GitHub and whatnot.

[1:18:05] Aakash Dhar (sorigin.com)
Please generate the doc files for me. Doc file, MD file, anything is fine. I'm all okay with it. I'm Okay, so just generate them for me.

[1:18:13] Elvis Ge (programination.com)
Once you're done, I'll set up the repo, the harness for the PM part, and then I'll share it with you as well. And also share your GitHub account ID.

[1:18:24] Aakash Dhar (sorigin.com)
Okay. Put everything in. Can you just put it in Slack? I'll just create it. I'll just share it with you. Okay. Okay. Any questions, any thoughts?

[1:18:36] Elvis Ge (programination.com)
Again, I'm doing this all alone. So obviously, if, how should I say, like, the danger of working on a startup idea alone is sometimes you think everything is good. So if you guys have anything, comments, improvements, suggestions, please, Deepak or Akash, let me know.

[1:18:55] Aakash Dhar (sorigin.com)
Definitely, we'll do that. Yeah. Yeah. Yeah. As you know, like, I thought it was so long. So it's... Sometimes it's like, you just think everything's good or like, is great, but then like, you need, I need people's opinions, right? So feel free, feel free to push on me. Okay. Sure. Definitely. Definitely. Okay.

[1:19:11] Elvis Ge (programination.com)
Anything, any questions, comments, or any, any initial thing that was like, oh, this is bad or anything? Or this can be version one.

[1:19:20] Aakash Dhar (sorigin.com)
Yeah. None so far. Like, we'll go in a little bit more in-depth and like, and we can give you those details as soon as possible. Deepak? Anything from you?

[1:19:31] Elvis Ge (programination.com)
No.

[1:19:32] Deepak Tewatia
I pushed back to where I sent myself, so that's all from myself. Okay. The other thing, do you guys have like five more minutes? Yeah, yeah.

---

## Non-Wepop section (set aside from the Wepop summary and proposals)

> The remainder concerns a separate engagement: the Dan / Reflex (Preflex) website SEO work and a
> voice-tutor product. Retained verbatim for completeness; not part of the Wepop record.

[1:19:43] Aakash Dhar (sorigin.com)
Sure. Okay. The other thing is the prefix, right?

[1:19:46] Elvis Ge (programination.com)
we, Dan told me that, Dan told me like, we're taking over the SEO stuff, right? Yes. And then I think we suggested that WordPress is probably, we don't need to use WordPress. Is that correct? you. you. Thank Yes, that's where we went.

[1:20:02] Aakash Dhar (sorigin.com)
Okay.

[1:20:03] Elvis Ge (programination.com)
So, okay, I'm okay if we don't want to use WordPress anymore. So I think you said like we should turn on the, what was it for Google search? What was the thing we were trying? No, actually, we are already using Next.js under the hood.

[1:20:19] Deepak Tewatia
So this need to make the SEO-friendly meta tags and inject some meta variables inside the... AI, for AI, SEO, you need to start. Yes, yes.

[1:20:35] Elvis Ge (programination.com)
Yeah, so what I want to do is because, how should I say, like this is our first time with this client, with Dan, to be in charge of SEO and stuff.

[1:20:45] Deepak Tewatia
This is our first time, right?

[1:20:47] Aakash Dhar (sorigin.com)
So what I want to do is kind of show him kind of before and after, right?

[1:20:54] Elvis Ge (programination.com)
So that's why I was asking if we can create, I don't know if it's SEMrush or some other tool. Obviously, I don't. We can show our, I think in my restaurant someone built a tool as well to assess the website. We can show that report, that's fine. But I would say it's an internal tool, so I also want to use a third-party tool to assess whether it's S&M or something, right?

[1:21:18] Aakash Dhar (sorigin.com)
Because the internal tool could be from the client, would be like, well, it's your tool, so who knows if it's like, how accurate it is. I'm okay with using both, right? Just as long as there's a third-party external tool. But I know that we didn't turn, what was the thing called? I just asked, I forgot, sorry.

[1:21:35] Elvis Ge (programination.com)
The search, like, to turn on so that, yeah.

[1:21:39] Aakash Dhar (sorigin.com)
No index, no index. No index, right?

[1:21:41] Elvis Ge (programination.com)
So we didn't turn it on for hours, but they turned it on for their WordPress, right? Correct, correct. For our WordPress. So technically, we should still be able to generate a report for how Reflex is currently doing, right?

[1:21:54] Aakash Dhar (sorigin.com)
I can get you the page spreader indexes and other details. Or like anything which I can get done in the free tier, I can get those information up for you. Okay.

[1:22:08] Elvis Ge (programination.com)
So yeah, try to like, yeah, try to get a report on currently how Reflex is doing.

[1:22:13] Aakash Dhar (sorigin.com)
Okay.

[1:22:14] Elvis Ge (programination.com)
And then on Wednesday, is it Wednesday? Yeah, Wednesday, Wednesday we meet again, right? So Wednesday, let's go to the report and then go over what we plan to do. Okay.

[1:22:26] Aakash Dhar (sorigin.com)
And then we can, yeah, and then we can work on that.

[1:22:28] Elvis Ge (programination.com)
So for now though, I don't, Deepak, I think you're, you can still work on, you know, like our current landing page, the non-WordPress version doesn't have any of those blogs, right?

[1:22:41] Aakash Dhar (sorigin.com)
Blogs. Yeah, resources, right?

[1:22:43] Elvis Ge (programination.com)
So I think a few things, I think one is we'll have to create those for our version.

[1:22:48] Aakash Dhar (sorigin.com)
And then I think we'll also, I agree with, how should I say, MyRash and whatnot is for SEO and whatnot, I think it's not just, I believe it's not just how.

[1:23:00] Elvis Ge (programination.com)
Well, the site is currently doing, but we have to constantly add new content.

[1:23:06] Aakash Dhar (sorigin.com)
So I assume we're not going to be writing it, I don't think.

[1:23:10] Elvis Ge (programination.com)
We might review it, but at the end of the day, I think AI is going to be doing it. I don't think Dan expects us to write any content for the blogs. But I think just something to think about, like, enabling our, if we're going to build these resources and blog, we should also somehow enable some blog generator, and then we can work on that separately, like in the future, right? We can create some plan and some prompt for AI to create a blog, and then we can have a...

[1:23:43] Aakash Dhar (sorigin.com)
I have one for mine. This is the one I, like, if you go to my profile, in my profile, I have a complete blog. I write generally mostly about, like, PM side of the stuff. So, like, I have a AI, like, a co-work set. I've completely built for my blogging, along with your, based on how I write, or like my voice, or my style of, so I already have that, if you need it for brieflets, do let me know, I can build one for brieflets. I just need a couple of samples of older blogs, that's it. Sure.

[1:24:18] Elvis Ge (programination.com)
So yeah, what I'm saying is like, we'll discuss what the details for that would be, like in terms of what it's going to blog about, the voice, all that kind of stuff. I think now, it's just like, just preparing for building that workflow, I guess, right? So if you're going to work on building the resources and the blogs right now, from the current WordPress version into ours, if it's related, then you can also start working on just building the foundation for, in the future, when we do create some AI blogging. Okay, sure, sure. I think the only thing I require is in this, in the AI blogging, is there should be some manual. A review, I think would be nice.

[1:25:02] Aakash Dhar (sorigin.com)
Definitely, definitely.

[1:25:04] Elvis Ge (programination.com)
At least in the beginning. And then we can see if we can remove the manual later. But yeah, I don't think Dan's paying us to write the content.

[1:25:12] Aakash Dhar (sorigin.com)
We're just trying to improve. But I assume content, like blogging, will increase our SEO, right? Yes, yes. So just work on that report. then, Deepak, is there anything else on Preflex besides the landing page stuff that you're working on?

[1:25:30] Deepak Tewatia
Voice? Do I need to review voice?

[1:25:32] Aakash Dhar (sorigin.com)
mode is actually the notes and testing phase.

[1:25:36] Deepak Tewatia
So Swati will be testing it out. Okay. Okay. there are a couple of questions that I already put to the group and you respond with, right? Yeah, I'll review those today. Yeah, what was like that prompt? Because I was trying to get it.

[1:25:49] Elvis Ge (programination.com)
So like one thing I didn't like, like the voice was doing it. The voice would talk to me first, which is great. But the non-voice version, like just the chat room, it was just empty. Bye.

[1:25:59] Deepak Tewatia
Bye. out. I wish it would say something to me first. Like, give me some, like, hi, and then like, hi, you know, how you're doing?

[1:26:07] Aakash Dhar (sorigin.com)
And then like, you know, what do you want to talk about today? Or like, here's some things.

[1:26:10] Elvis Ge (programination.com)
But at the end of the day, I think the tutor, I, sorry, I didn't test, I'll test it later. But the tutor should be like a tutor, right? I'm a student. So when I walk into a class, the tutor doesn't wait for me to tell them what to do, right?

[1:26:26] Aakash Dhar (sorigin.com)
Usually the tutor is like, here's, you know, here's what we're going to do today.

[1:26:30] Elvis Ge (programination.com)
Well, here's what we're going to talk about, right?

[1:26:31] Aakash Dhar (sorigin.com)
Of course, you know, it's not exactly like a tutor.

[1:26:34] Elvis Ge (programination.com)
So if I say I disagree, I want to talk about this specific thing, then yeah, the AI should adjust. But I think, you know, because you're selecting the rules, right, before generating the tutor room. So the tutor should kind of start with something, right? So that's why the, in the prompt, if you saw, I mentioned something called the Socratic method.

[1:26:57] Aakash Dhar (sorigin.com)
Dan said this a lot, so that's why I'm emphasizing.

[1:27:00] Elvis Ge (programination.com)
Credit method, he really likes this teaching style, which is basically, I think what they do is ask, give you some example or some question that you need to answer, and then give feedback, and then keep repeating, basically.

[1:27:16] Aakash Dhar (sorigin.com)
Okay. That's what the soccer team is teaching.

[1:27:23] Deepak Tewatia
So this is the default stream, even if you land on the page comes, like, ask about any rule or concept, to your firm, UFS method, like, explain formalizations, explain DT, give me hypothetical forward formation. So if you clean one of those, so it will be to ask them.

[1:27:42] Aakash Dhar (sorigin.com)
So that's... you... I don't know why. I saw this.

[1:27:49] Elvis Ge (programination.com)
Yeah, I saw that initial screen. And I guess, when I look at it, I don't know why, but when I look at it, it makes me feel like it's just... It's just a back, like, it's just like a, a default background thing.

[1:28:08] Aakash Dhar (sorigin.com)
Like, so I didn't, I didn't really think about clicking it. I don't know why. I didn't, I didn't really think about interacting with it. Okay, okay, okay, okay. Let's do one thing. Let's encapsulate it within a border. Well, that's one.

[1:28:21] Deepak Tewatia
The other thing I was like thinking, click, click on one of the options again, click on it. Instead of just, it's more about changing of view.

[1:28:28] Elvis Ge (programination.com)
Can you, so if it's like this, where it's like already in a chat state and then like, so here, here, here. So what about making the view this way, where you have the AI already saying something and then be like, you know, like, hey, welcome, blah, blah, blah.

[1:28:47] Aakash Dhar (sorigin.com)
And then please choose one of the three, like, choose some of these options that you want to go first or let, or type below.

[1:28:54] Elvis Ge (programination.com)
You know what mean? Like, it's already, Yeah, yeah. Understood the concept.

[1:28:57] Aakash Dhar (sorigin.com)
It's already in the dialogue format. Where, as opposed to that previous view, I don't know why. I don't know if other people or Swati or whatever experienced this. I just didn't think about quick. I don't know why.

[1:29:10] Elvis Ge (programination.com)
I didn't know that each of those screens are generated differently. I thought it just a generic to-to-to-room screen. Yeah, I noticed those. I just noticed those options were generated based on the rules that you chose.

[1:29:23] Deepak Tewatia
Yeah. Yeah, I didn't notice that. So I will try to put it on this side, if you can see my cursor, this one. So it is predictable that, like, you need to select it. But I will try to do something that is, like, more predictable that I need to click these or not. Yeah, I think two parts. Make it look part of maybe, like, a dialogue and then make it, like, dialogue-based.

[1:29:49] Elvis Ge (programination.com)
So, like, you know, welcome. And then, like, please, you know, like, give me, give the person instructions. So, like, choose one of the options below or please type what you want to discuss, right?

[1:29:59] Deepak Tewatia
Sure. Okay.

[1:30:03] Elvis Ge (programination.com)
Yeah. Okay. Does this give you... So this is just... Yeah. Give me... Okay.

[1:30:13] Aakash Dhar (sorigin.com)
How would you determine... Okay. Okay. All right. That's fine. Okay. Yeah.

[1:30:21] Elvis Ge (programination.com)
I will get... I will test it today and see if I have any more feedback. Sure. Sure.

[1:30:27] Aakash Dhar (sorigin.com)
And for that...

[1:30:30] Deepak Tewatia
For those prompts changes, right? If you ever do, there are two things. Like I... If I change something, first I need to publish draft and then...

[1:30:40] Aakash Dhar (sorigin.com)
No, sorry. First I say draft and then publish.

[1:30:44] Deepak Tewatia
Correct. Yeah. I did... I think I did that because there's a bunch of versions now.

[1:30:48] Elvis Ge (programination.com)
You can see my version... I think version 3 and 4 are my versions.

[1:30:54] Deepak Tewatia
Yeah. Yeah. Yeah. won't let... Yeah.

[1:30:56] Elvis Ge (programination.com)
It didn't let me publish until I saved it. So it was fine. Yeah, yeah.

[1:31:00] Deepak Tewatia
Okay. Okay. That's all from myself. Yeah.

[1:31:05] Aakash Dhar (sorigin.com)
All Okay. Thanks, guys. Sure. Sorry about the long meeting. No, no, Thank you, sir.

[1:31:11] Deepak Tewatia
Thank you. guys. Bye. Have a good day. Bye. Bye. You too.
