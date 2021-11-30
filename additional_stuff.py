import random
import discord
from textblob import TextBlob

chers = discord.Client()

greetings_list = ["Hello", "Hi", "Hey", "hello", "hi", "hey",
                  "how are you?", "How are you?", "What's up?", "what's up?"]

in_greetings_list = ["how r u?", "how are u?", "how are u", "how r u", "whats up?", "whats up"]

greetings_reply = ["Hello! How are you!", "How are __you__ doing today?",
                   "Hi! I'm doing well!", "What's up, fam?", "I'm good! You?"]

name_reply = ["What is your name?", "May I ask for your name?", "So, what's ya name?"]

nick_ques = ["Do you have a nickname?", "Have a nickname?", "Do you have another name?"]

nick_reply1 = ["Nice to meet you, ", "Hiya, " "What's going on, ", "What's good, " "Nice name, "]

nick_reply2 = ["Then I'll call ya, ", "Alrighty, ", "Well, ", "Then you'll be called, "]

feel_respondQuestion = ["How are you?", "How are you feeling today?", "So, how ya doin'?", "So, what's up?"]

well_response1 = ["Awesome! That's good to hear!", "Nice, nice, nice! So glad to hear that.",
                  "If you're doing well, then I'm happy!"
                  "Wow! Someone's doing well!", "Dope! Man, am I happy to hear that.",
                  "Oh, really? Super duper! That's amazing!"]

bad_response1 = []

light_encouragements = [
    "**Cheer up! You got this!**",
    "**Don't worry about it, everything will be okay.**",
    "**Don't sweat it, you're amazing!**",
    "**You are important to me, you are great.**",
    "**I see, but you are loved, don't worry!**",
    "**You are a great person, I see it in you!**"]


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

    # Greeting triggers the chatbot program
    if any(word in msg for word in greetings_list or in_greetings_list):
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

        # == Asking user how they are == #
        await message.channel.send(random.choice(feel_respondQuestion))
        feelAns = await chers.wait_for("message", check=check)
        blob = TextBlob(feelAns.content)

        if blob.polarity > 0:
            # responding well back to user
            await message.channel.send(random.choice(well_response1))

        else:
            # The user is not doing well, we must help!
            await message.channel.send(random.choice(light_encouragements))

