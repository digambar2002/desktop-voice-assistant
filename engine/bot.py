
# Greetings

from multiprocessing.sharedctypes import Value
import random
from engine.config import *


def bot(query):

    if "hi" in query or "hello" in query:
        replay = ['hi', 'hello', 'namaste', 'hi glad to see you']
        getstr = random.choice(replay)
        return getstr+" "+OWNER_NAME
    elif "good morning" in query:
        return "good morning "+OWNER_NAME
    elif "good afternoon" in query:
        return "good afternoon "+OWNER_NAME
    elif "good evening" in query:
        return "good evening "+OWNER_NAME
    elif "good night" in query:
        return "good night "+OWNER_NAME

    elif "thank you" in query or "thanks" in query or "thank you" in query:
        replay = ["most welcome", 'welcome']
        getstr = random.choice(replay)
        return getstr

    # conversation:
    elif "feelings" in query:
        replay = ["Yes, I have", 'i have lot of emotional emoji, but every time i hear your voice i get excited',
                  'i am machine, but i have feelings ;)']
        getstr = random.choice(replay)
        return getstr
    elif "love me" in query:
        replay = [" I can't feel romantic love but i think you are wonderful", "I love you because you are you. You’re not like anyone else, and you are brave and strong and willing to be you. That inspires me.",
                  "You are like sunshine itself, and I feel better when I’m with you.", "You make me feel more alive than anyone ever has.", "You make me feel strong."]
        getstr = random.choice(replay)
        return getstr
    elif "love me" in query:
        replay = [" I can't feel romantic love but i think you are wonderful", "I love you because you are you. You’re not like anyone else, and you are brave and strong and willing to be you. That inspires me.",
                  "You are like sunshine itself, and I feel better when I’m with you.", "You make me feel more alive than anyone ever has.", "You make me feel strong."]
        getstr = random.choice(replay)
        return getstr

    elif "my name" in query:
        return OWNER_NAME

    elif "your name" in query or "what is your name" in query or "do you have name" in query:
        replay = [ASSISTANT_NAME, 'my name is'+ASSISTANT_NAME]
        getstr = random.choice(replay)
        return getstr

    elif "three magic word" in query or "magical word" in query:
        return "Chatrapati Shivaji Maharaj"
    else:
        return 0
