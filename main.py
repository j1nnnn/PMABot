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


chers.run('')
