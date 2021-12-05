import json
import random
import discord
import requests
from discord.ext import commands
import time
from replit import db

# --- RECEIVING USER DATA --- #

chers = discord.Client()

# ==Greetings== #
greetings_list = ["Hello", "Hi", "Hey", "hello", "hi", "hey",
                  "how are you?", "How are you?", "What's up?", "what's up?"]
in_greetings_list = ["how r u?", "how are u?", "how are u", "how r u", "whats up?", "whats up"]

greetings_reply = ["Hello! How are you!",
                   "How are __you__ doing today?",
                   "Hi! I'm doing well!",
                   "What's up, fam?",
                   "I'm good! You?"]
# ============== #


# ==Negative Emotions== #
light_words = ["annoyed", "confused", "irritated", "not okay", "bitter", "salty"]

sad_words = ["sad", "upset", "depressed", "unhappy", "miserable", "afraid",
             "annoying", "feeling blue", "stressed", "melancholy", "lonely",
             "empty", "stressing", "despair", "left out"]

angry_words = ["angry", "frustrated", "pissed", "furious", "heated", "frustrating",
               "livid"]

nervous_words = ["nervous", "anxious", "worried"]

screwed_over_words = ["screwed", "I hate my life", "kms"]

suffer_words = ["agony", "pain", "hopeless", "helpless", "overwhelmed"]

insecure_words = ["insecure", "insignificant", "incompetent", "I'm not enough", "I am not enough",
                  "neglected", "ashamed"]

double_meaning_words = ["mad"]
# ============== #

# ==Responses== #
name_reply = ["What is your name?", "May I ask for your name?", "So, what's ya name?"]

nick_ques = ["Do you have a nickname?", "Have a nickname?", "Do you have another name?"]

nick_reply1 = ["Nice to meet you, ", "Hiya, " "What's going on, ", "What's good, " "Nice name, "]

nick_reply2 = ["Then I'll call ya, ", "Alrighty, ", "Well, ", "Then you'll be called, "]

feel_respondQuestion = ["How are you?", "How are you feeling today?", "So, how ya doin'?", "So, what's up?"]

well_response1 = ["Awesome! That's good to hear!", "Nice, nice, nice! So glad to hear that.",
                  "If you're doing well, then I'm happy!"
                  "Wow! Someone's doing well!", "Dope! Man, am I happy to hear that.",
                  "Oh, really? Super duper! That's amazing!"]

neutral_response1 = ["Very neutral today, huh?", "Ahh, understandable. Today's pretty decent"]

bad_response1 = ["But what's up? Did something happen?", "But, if you don't mind me asking, what happened?",
                 "But is there something going on? Let's talk about it."]

trigger_words = ["What's up?", "That's my name! You can keep talking to me!", "At your service!"]
# ============== #

# ==PMA Responses== #
light_encouragements = [
    "**Cheer up! You got this!**",
    "**Don't worry about it, everything will be okay.**",
    "**Don't sweat it, you're amazing!**",
    "**You are important to me, you are great.**",
    "**I see, but you are loved, don't worry!**",
    "**You are a great person, I see it in you!**"]
# light cheer ups

sad_encouragements = [
    "**Please, don't be sad, you have a good life ahead of you!**",
    "**Don't worry about it, sometimes things get rough, but it'll get better!**",
    "**Sometimes, I get sad, but I'm a bot so I actually don't. I am always full of spirit and you will be too!**",
    "**Oh, no! I am here for you! Talk to me, friend.**",
    "**You are lovely and you are loved. Cheer up! You got this!**",
    "**Sometimes everyone runs into problems, you'll get it over soon!**"]
# loving messages

angry_encouragements = [
    "**Don't be so frustrated, sometimes it gets to the best of us!**",
    "**I think I get it, I get mad at things sometimes, but sometimes you got to let go.**",
    "**Ughhh, I feel you! I am here for you, talk to me!**",
    "**As much as you're angry, I am that much sad, what's bothering you?**",
    "**Oh no! I think you will be fine after some meditation.**",
    "**As a great person, I believe you will get better!**"]
# calming messages

nervous_encouragements = [
    "**Hey, chin up! I believe in you!**",
    "**You've got nothing to be worried about, you're chilling.**",
    "**I'm a bot and I even get nervous, sometimes you just gotta do it without thinking!**",
    "**You have it in you, you got this! Walk with confidence!**",
    "**Sometimes we overthink. I think you're in good shape.**",
    "**Even sometimes __I__ need**"]
# relieving  messages

suffer_encouragements = [
    "**I see, I am so sorry to hear. But I am here to lift you up!**",
    "**We all have rough patches in life. I think it's what we make of them that allows us to keep going!**",
    "**I would love to hug you right now, I'll give you a virtual hug!**",
    "**I wish there was more I can do. I will verbally try my best to help you!**",
    "**Oh, no! Well, PMA bot at your service! I'll take care of you!**",
    "**There is so much to explore in the world, maybe you just haven't found it yet.**"]
# sympathetic messages

insecure_encouragements = [
    "**Come on, you got this! You're very capable!**",
    "**I think you have a lot of potential. That's what allows humans to shine!**",
    "**You are you're own protagonist of your own story. You will do well!**",
    "**Doubt is the greatest enemy! Patience and perseverance will always prevail!**",
    "**You have to muster all your willpower! You are capable of anything!**",
    "**Whoever thinks you're that way, is mean. You are way more than that!**"]
# uplifting, motivating messages

# ============== #


# ==Conversation== #


# --- ACTUAL EVENTS --- #
before_quote = "Hey, this might help, here's an inspiring quote:"


# ==Definitions== #
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def randnum(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


@chers.event
# console will give message when bot is ready
async def on_ready():
    print('{0.user} has stood up.'.format(chers))


@chers.event
async def on_message(message):
    # whatever the owner says doesn't do anything
    if message.author == chers.user:
        return

    msg = message.content

    if msg.startswith('$gG'):
        await message.channel.send('Gang Goon! and Hello!')

    # -any greetings- #
    if any(word in msg for word in greetings_list or in_greetings_list):
        await message.channel.send(random.choice(greetings_reply))

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # -responding depending on emotion- #
    if any(word in msg for word in light_words):
        await message.channel.send(random.choice(light_encouragements))
        await message.channel.send(before_quote)
        quote = get_quote()
        await message.channel.send(quote)
        await message.channel.send(randnum('gifs.txt'))

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(sad_encouragements))
        await message.channel.send(before_quote)
        quote = get_quote()
        await message.channel.send(quote)
        await message.channel.send(randnum('gifs.txt'))

    if any(word in msg for word in angry_words):
        await message.channel.send(random.choice(angry_encouragements))
        await message.channel.send(before_quote)
        quote = get_quote()
        await message.channel.send(quote)
        await message.channel.send(randnum('gifs.txt'))

    if any(word in msg for word in nervous_words):
        await message.channel.send(random.choice(nervous_encouragements))
        await message.channel.send(before_quote)
        quote = get_quote()
        await message.channel.send(quote)
        await message.channel.send(randnum('gifs.txt'))

    if any(word in msg for word in suffer_words):
        await message.channel.send(random.choice(suffer_encouragements))
        await message.channel.send(before_quote)
        quote = get_quote()
        await message.channel.send(quote)
        await message.channel.send(randnum('gifs.txt'))

    if any(word in msg for word in insecure_words):
        await message.channel.send(random.choice(insecure_encouragements))
        await message.channel.send(before_quote)
        quote = get_quote()
        await message.channel.send(quote)
        await message.channel.send(randnum('gifs.txt'))
    #----------------------------------------------#

    keyWord = "PMABot"

    # embedded Help guide
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Bot Help",
                                 description="Here is a little guide to help you with speaking to PMABot",
                                 color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)

    # Greeting triggers the ChatBot program
    if keyWord in msg:
        if msg == keyWord:
            await message.channel.send("No greeting? Then no service!")
            return

        # basic check
        def check(m):
            return m.author == message.author \
                   and m.channel == message.channel

        await message.channel.send(random.choice(greetings_reply))
        # asking for name
        await message.channel.send(random.choice(name_reply))
        user_name = await chers.wait_for("message", check=check)

        # asking for nickname
        await message.channel.send("Do you have a nickname?: **y** or **n**")

        # check for y or n
        def check(ck):
            return ck.author == message.author and ck.channel == message.channel and \
                   ck.content.lower() in ["y", "n"]

        nick_name = await chers.wait_for("message", check=check)
        # adding nickname to your name
        if nick_name.content.lower() == "y":
            # basic check
            def check(m):
                return m.author == message.author \
                       and m.channel == message.channel

            await message.channel.send("Then, what is your nickname?")
            nickname = await chers.wait_for("message", check=check)
            await message.channel.send(random.choice(nick_reply1) + nickname.content)
        else:
            nickname = user_name.content + user_name.content[-1] + 'y'
            await message.channel.send(random.choice(nick_reply2) + nickname)

        # check for TextBlob
        def check(m):
            return m.author == message.author \
                   and m.channel == message.channel

        # == Asking user how they are || SENTIMENT ANALYSIS == #
        nlp = spacy.load("en_core_web_sm")
        sid_obj = SentimentIntensityAnalyzer()

        await message.channel.send(random.choice(feel_respondQuestion))
        feelAns = await chers.wait_for("message", check=check)
        sentiment_dict = sid_obj.polarity_scores(feelAns.content)

        # debugging
        print("(Feel) Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

        if sentiment_dict['pos'] > sentiment_dict['neg']:
            # responding well back to user
            await message.channel.send(random.choice(well_response1))
            # need to add more

        elif sentiment_dict['neg'] > sentiment_dict['pos']:
            # The user is not doing well, we must help!
            await message.channel.send(random.choice(light_encouragements))
            # Asking about user's situation
            await message.channel.send(random.choice(bad_response1))
            situation_resp = await chers.wait_for("message", check=check)
            sentiment_dict = sid_obj.polarity_scores(situation_resp.content)

            # debugging
            print("(Neg Feel) Overall sentiment dictionary is : ", sentiment_dict)
            print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
            print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
            print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

            # negative
            if sentiment_dict['compound'] <= 0.5:
                await message.channel.send(random.choice(light_encouragements))
                # Getting nouns
                sitResp_nlp = nlp(situation_resp.content)

                # making sentences
                sentences = list(sitResp_nlp.sents)
                # this will reset after every situational message
                sentCount = 0

                # -after making sentences, getting words from each sentence- #
                for i in range(len(sentences)):
                    sentCount += 1

                word_List = [[] for i in range(0, sentCount)]

                for i in range(sentCount):
                    sent = sentences[i]
                    for words in sent:
                        # special character check
                        if words.text == "," or words.text == ".":
                            continue
                        else:
                            word_List[i].append(words)

                    # debug
                    print(word_List[i])

                # Specific tag List
                objList = [[] for i in range(0, sentCount)]
                adjList = [[] for i in range(0, sentCount)]
                verbList = [[] for i in range(0, sentCount)]
                advList = [[] for i in range(0, sentCount)]

                # putting each word in each appropriate list, knows from WHICH SENTENCE and its POSITION
                for i in range(sentCount):

                    objList[i].append(i)
                    adjList[i].append(i)
                    verbList[i].append(i)
                    advList[i].append(i)

                    for word in word_List[i]:
                        if word.pos_ == "NOUN":
                            if word.text not in objList[i]:
                                objList[i].append(word.text)
                                objList[i].append(word_List[i].index(word))
                            else:
                                continue

                        elif word.pos_ == "ADJ":
                            if word.text not in adjList[i]:
                                adjList[i].append(word.text)
                                adjList[i].append(word_List[i].index(word))
                            else:
                                continue

                        elif word.pos_ == "VERB":
                            if word.text not in verbList[i]:
                                verbList[i].append(word.text)
                                verbList[i].append(word_List[i].index(word))
                            else:
                                continue

                        elif word.pos_ == "ADV":
                            if word.text not in advList[i]:
                                advList[i].append(word.text)
                                advList[i].append(word_List[i].index(word))
                            else:
                                continue

                    print("Obj list:")
                    print(objList[i])

                    print("Adj list:")
                    print(adjList[i])

                    print("Verb list:")
                    print(verbList[i])

                    print("Adv list:")
                    print(advList[i])

                # getting polarity of each noun
                # for nouns in noun_list:

                noun_adjList = {}
                verb_advList = []
                objDict = []
                AdjDict = []

                def Merge(dict1, dict2):
                    res = {**dict1, **dict2}
                    return res

                for i in range(sentCount):
                    if objList[i][i] == adjList[i][i]:
                        # adding a key of objects or adjectives and a value of their indices
                        for j in range(1, len(objList[i]), 2):
                            objDict = dict({objList[i][j]: objList[i][j + 1]})
                        for k in range(1, len(adjList[i]), 2):
                            AdjDict = dict({adjList[i][k]: adjList[i][k + 1]})

                        for key, value in objDict.items():
                            currVal1 = value
                        for key, value in AdjDict.items():
                            currVal2 = value

                        if currVal1 > currVal2:
                            noun_adjList = Merge(AdjDict, objDict)
                            for key, value in AdjDict.items():
                                sentiment_dict = sid_obj.polarity_scores(key)
                                if sentiment_dict['compound'] < 0.5:
                                    for keys, values in objDict.items():
                                        await message.channel.send("Ah, I see. It seems you are concerned about a " + keys + ". Is that correct? **y** or **n**")
                        else:
                            continue

                print(noun_adjList)

                def check(ck):
                    return ck.author == message.author and ck.channel == message.channel and \
                           ck.content.lower() in ["y", "n"]

                sitAns = await chers.wait_for("message", check=check)
                if sitAns.content.lower() == "y":
                    await message.channel.send("Let's talk it out then! Continue to give me some issues!")

                def check(m):
                    return m.author == message.author \
                           and m.channel == message.channel

                issueMsg = await chers.wait_for("message", check=check)


            # neutral
            elif sentiment_dict['neu'] > sentiment_dict['pos'] and sentiment_dict['neu'] > sentiment_dict['neg']:
                await message.channel.send("Ahh, I see...")
            # positive
            else:
                await message.channel.send(random.choice(well_response1))

        # will need a while loop to keep asking and conversing until a specific keyword

        else:
            await message.channel.send(random.choice(neutral_response1))

    # if the user wants to speak to PMA again
    # elif keyWord in msg:
    # await message.channel.send(random.choice(trigger_words))

chers.run('')
