import random
import discord
from textblob import TextBlob

chers = discord.Client()

greetings_list = ["Hello", "Hi", "Hey", "hello", "hi", "hey",
                  "how are you?", "How are you?", "What's up?", "what's up?"]
in_greetings_list = ["how r u?", "how are u?", "how are u", "how r u", "whats up?", "whats up"]

greetings_reply = ["Hello! How are you!", "How are __you__ doing today?",
"Hi! I'm doing well!","What's up, fam?", "I'm good! You?"]

name_reply = ["What is your name?", "May I ask for your name?", "So, what's ya name?"]

nick_ques = ["Do you have a nickname?", "Have a nickname?", "Do you have another name?"]

nick_reply1 = ["Nice to meet you, ", "Hiya, " "What's going on, ", "What's good, " "Nice name, "]

nick_reply2 = ["Then I'll call ya, ", "Alrighty, ", "Well, ", "Then you'll be called, "]

feel_respondQuestion = ["How are you?", "How are you feeling today?", "So, how ya doin'?", "So, what's up?"]

well_response1 = ["Awesome! That's good to hear!", "Nice, nice, nice! So glad to hear that.", "If you're doing well, then I'm happy!"
"Wow! Someone's doing well!", "Dope! Man, am I happy to hear that.", "Oh, really? Super duper! That's amazing!"]

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
        await message.channel.send(random.choice(greetings_reply))
        # asking for name
        await message.channel.send(random.choice(name_reply))
        user_name = input()
        # asking for nickname
        await message.channel.send(random.choice(nick_ques))
        nick_name = input()
        # adding nickname to your name
        if 'y' in nick_name.lower():
            nickname = input("Then what's your nickname? ")
            await message.channel.send(random.choice(nick_reply + nickname))
        else:
            nickname = user_name + user_name[-1] + 'y'
            await message.channel.send(random.choice(nick_reply2 + nickname))
        
        # == Asking user how they are == #
        await message.channel.send(random.choice(feel_respondQuestion))
        feelAns = input()
        blob = TextBlob(feelAns)

        if blob.polarity > 0:
            # responding well back to user
            await message.channel.send(random.choice(well_response1))
        
        else:
            # The user is not doing well, we must help!
            await message.channel.send(random.choice(light_encouragement))




chers.run('ODU5OTc2OTU0NDg0NDkwMjQx.YN0h8w.ip5Jbnk9qhg-AZq8QaSo-9UTayU')

