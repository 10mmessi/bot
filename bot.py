import praw

# reddit api login
reddit = praw.Reddit(client_id='redacted',
                     client_secret='redacted',
                     username='not_yet_eh',
                     password='redacted',
                     user_agent='Eh')


# the subreddits you want your bot to live on
subreddit = reddit.subreddit('titanfolk+sandland')
# phrase to activate the bot

phrase0 = '?randomcharacter'

phas = '-randomcharacter'

phrase9 = '+randomcharacter'

phrase = '!randomcharacter'

phrase1 = '!randomtitan'

frase = '?randomtitan'

phrase2 = 'thanos car'

phrase3 = 'Thanos car'

phrase6 = 'gone'

phrase7 = '!randomship'

phrose = '?randomship'

phrase8 = '!randomleak'

phras = '?randomleak'


livin1 = '!randomalive'
livin2 = '?randomalive'
livin3 = '+randomalive'
livin4 = '-randomalive'
livin5 = '$randomalive'

rb1 = '!randomboy'
rb2 = '?randomboy'
rb3 = '+randomboy'
rb4 = '-randomboy'
rb5 = '$randomboy'

rg1 = '!randomgirl'
rg2 = '?randomgirl'
rg3 = '+randomgirl'
rg4 = '-randomgirl'
rg5 = '$randomgirl'

rlb1 = '!randomlivingboy'
rlb2 = '?randomlivingboy'
rlb3 = '+randomlivingboy'
rlb4 = '-randomlivingboy'
rlb5 = '$randomlivingboy'

rlg1 = '!randomlivinggirl'
rlg2 = '?randomlivinggirl'
rlg3 = '+randomlivinggirl'
rlg4 = '-randomlivinggirl'
rlg5 = '$randomlivinggirl'

import random



char1 = ["Reiner", "Levi", "Eren", "Mikasa", "Armin", "Gabeh", "Falco", "Zeke", "Sasha", "Yelena", "Floch", "Erwin", "Hange", "Historia", "Ymir", "Zackley", "Pieck", "Annie", "Jean", "Keith", "Grisha", "Hitch", "Kenny", "Frieda", "Marlowe", "Porco", "Onyankopon", "Bertholdt", "Baggy pants Leon", "Daz", "Pixis", "Marcel", "Original Ymir", "Carla", "Petra", "Mike", "Nifa", "Moblit", "Magath", "Rico", "Dina", "Xaver", "Nile", "Marco", "Willy", "Clitoris-chan", "Racist Mario", "Colt", "Hannes", "Nanaba", "Kaya"]

titan = ["Attack Titan", "Female Titan", "Beast Titan", "Armoured Titan", "Colossal Titan", "Jaw Titan", "The Founding Titan", "Warhammer Titan", "Cart Titan"]

living = ["Annie", "Armin", "Baggy-Pants Leon", "Connie", "Daz", "The Earth Devil", "Eren", "Falco", "Flegel Reeves", "Floch", "Gabi", "Hange", "Historia", "Hitch", "Jean", "Keith", "Kitz", "Kiyomi", "Levi", "Louise", "Mikasa", "Niccolo", "Onyankopon", "Pieck", "Reiner", "Rico", "Magath", "Yelena", "Lolimir", "Zeke", "Farmer-kun"]

boys = ["Armin", "Baggy-pants Leon", "Bertholdt", "General Calvi", "Colt", "Connie", "Zachary", "Daz", "Dimo Reeves", "Pyxis", "Eld", "Eren Kruger", "Eren", "Erwin", "Falco", "Flegel Reeves", "Floch", "Franz", "Gelgar", "Grisha", "Gross", "Gunther", "Hannes", "Ian", "Jean", "Keith","Kenny", "Kitz", "Levi", "Marcel", "Marco", "Marlowe", "Miche", "Mitabi", "Mobilt", "Niccolo", "Pastor Nick", "Nile","Oruo", "Onyankopon", "Porco", "Reiner", "Rod Reiss", "Rogue", "Magath", "Thomas", "Xaver", "Udo", "Uri","Willy Tybur", "Zeke", "Farmer-kun"]

girls = ["Anka", "Annie", "Carla", "Dina", "Faye", "Freida", "Gabi", "Hange", "Hannah", "Historia", "Hitch", "Kiyomi", "Kuchel", "Louise", "Mikasa", "Mina", "Nanaba", "Nifa", "Petra", "Pieck", "Rico", "Sasha", "Caven", "Yelena", "Frecklemir", "Lolimir", "Zofia", "Emma Tybur"]

lb = ["Armin", "Baggy-Pants Leon", "Connie", "Daz", "Eren", "Falco", "Flegel Reeves", "Floch", "Jean", "Keith", "Kitz", "Levi", "Niccolo", "Onyankopon", "Reiner", "Zeke", "Farmer-kun", "Magath"]

lg = ["Annie", "Gabi", "Hange", "Historia", "Hitch", "Kiyomi", "Louise", "Mikasa", "Pieck", "Rico", "Yelena", "Lolimir"]

leak = ["dies", "becomes a shifter", "appears", "is the father", "changes sides", "is pregnant", "does nothing", "suffers more", "is secretly a traitor", "stops the war", "turns to a mindless titan", "gets eaten", "is the final villain", "breaks down the wall", "drank the wine", "gets rekt by the Yeagerists", "gets resurrected by paths", "lives happily ever after"]


# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if  any(c in comment.body and comment.author != 'not_yet_eh' for c in (phrase, phrase0, phrase1, phrase7, phrase8, phrase9, phrose, frase, phas, phras, livin1, livin2, livin3, livin4, livin5, rb1, rb2, rb3, rb4, rb5, rg1, rg2, rg3, rg4, rg5, rlb1, rlb2, rlb3, rlb4, rlb5, rlg1, rlg2, rlg3, rlg4, rlg5)):
          reply = comment.body.replace(phrase,str(random.choice(char1))).replace(phas,str(random.choice(char1))).replace(phrase9,str(random.choice(char1))).replace(phrase1,str(random.choice(titan))).replace(frase,str(random.choice(titan))).replace(phrase8, str(random.choice(char1)) + ' '  + str(random.choice(leak))).replace(phras, str(random.choice(char1)) + ' '  + str(random.choice(leak))).replace(phrase7, str(random.choice(char1)) + ' x '  + str(random.choice(char1))).replace(phrose, str(random.choice(char1)) + ' x '  + str(random.choice(char1))).replace(phrase0,str(random.choice(char1))).replace(livin1,str(random.choice(living))).replace(livin2,str(random.choice(living))).replace(livin3,str(random.choice(living))).replace(livin4,str(random.choice(living))).replace(livin5,str(random.choice(living))).replace(rb1,str(random.choice(boys))).replace(rb2,str(random.choice(boys))).replace(rb3,str(random.choice(boys))).replace(rb4,str(random.choice(boys))).replace(rb5,str(random.choice(boys))).replace(rg1,str(random.choice(girls))).replace(rg2,str(random.choice(girls))).replace(rg3,str(random.choice(girls))).replace(rg4,str(random.choice(girls))).replace(rg5,str(random.choice(girls))).replace(rlb1,str(random.choice(lb))).replace(rlb2,str(random.choice(lb))).replace(rlb3,str(random.choice(lb))).replace(rlb4,str(random.choice(lb))).replace(rlb5,str(random.choice(lb))).replace(rlg1,str(random.choice(lg))).replace(rlg2,str(random.choice(lg))).replace(rlg3,str(random.choice(lg))).replace(rlg4,str(random.choice(lg))).replace(rlg5,str(random.choice(lg)))
          comment.reply(reply)
          print('posted')
    if phrase2 in comment.body and comment.author != 'not_yet_eh' :
         reply = '[Mada ka na?](https://i.imgur.com/q8PK2tl.png)'
         comment.reply(reply)
         print('posted')
    if phrase3 in comment.body and comment.author != 'not_yet_eh' :
         reply = '[Mada ka na?](https://i.imgur.com/q8PK2tl.png)'
         comment.reply(reply)
         print('posted')
    if phrase6 in comment.body and comment.author != 'not_yet_eh' :
         reply = '>[gone](https://www.youtube.com/watch?v=pwSsT8IU0WE)'
         comment.reply(reply)
         print('posted')
