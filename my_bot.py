"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

def should_i_respond(user_message, user_name):
  # standardize user message by removing commas and making everything lowercase
  # then check if user message == "rock paper"
  if "robot" in user_message:
    return True
  elif "sports score" in user_message:
    return True
  elif "joke" in user_message:
    return True
  elif "birthday" in user_message:
    return True
  elif "rock paper scissors" in user_message:
    return True
  elif "lyrics" in user_message:
    return True
  elif "fun fact" in user_message:
    return True
  elif "day" in user_message:
    return True
  elif "todays date" or "date" in user_message:
    return True
  elif "time" in user_message:
    return True
  elif "math" in user_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
import random
import datetime

def respond(user_message, user_name):
  jokes = ["What's the best thing about Switzerland? The flag is a big plus", "I had a joke about paper today, but it was tearable.", "Why did the crab cross the road? It didnt—it used the sidewalk."]
  rps = ["rock", "paper", "scissors"]
  fun_fact = ["Australia is wider than the moon: Australia is almost 4,000 km wide from east to west, while the moon is 3,400 km in diameter.", "Avocados are fruits: Avocados are biologically fruits, even though they are often prepared and eaten like vegetables.", "Flamingos aren't born pink: Flamingos are not born pink." , "Ketchup was once medicine", "The heart of a blue whale is huge: A blue whale's heart weighs about 400 pounds and can be heard beating from two miles away.", "Trees can communicate: Trees can communicate with each other.","Dolphins have names for each other: Dolphins have names for each other.", "Bamboo is the fastest growing plant: Bamboo is the world's fastest growing plant.", "Sharks don't have bones: Sharks don't have any bones."]
  lyrics = [ 
    "I get a feeling that I never never never never had before, no no",
    "I get a good feeling, yeah",
    "Oh oh, sometimes I get a good feeling, yeah",
    "I get a feeling that I never never never never had before, no no",
    "I get a good feeling, yeah",
    "Yes I can, doubt better leave, I'm running with this plan",
    "Pull me, grab me, crabs in the bucket can't have me",
    "I'll be the president one day",
    "January first, oh, you like that gossip",
    "Like you the one drinking what God sip dot com",
    "Now I gotta work with your tongue",
    "How many rolling stones you want",
    "Yeah I got a brand new spirit,",
    "Speak it and it's done",
    "Rolled up on the side of the bed like I won",
    "Talk like a winner, my chest to that sun",
    "G5 dealer, US to Taiwan",
    "Now who can say that I wanna play back",
    "Mama knew I was a needle in a haystack",
    "A Bugatti boy, plus Maybach",
    "I got a feeling it's a wrap, ASAP",
    "Oh, oh, sometimes I get a good feeling, yeah",
    "I get a feeling that I never never never never had before, no no",
    "I get a good feeling, yeah",
    "The mountain top, walk on water",
    "I got power, feel so royal",
    "One second, I'mma strike oil",
    "Diamond, platinum, no more for you",
    "Gotta drill it in, never giving in",
    "Giving up's not an option, gotta get it in",
    "Witness I got the heart of twenty men",
    "No fear, go to sleep in the lion's den",
    "That flow, that spark, that crown",
    "You looking at the king of the jungle now",
    "Stronger than ever, can't hold me down",
    "A hundred miles feelin' from the picture smile",
    "Straight game face, it's game day",
    "See me running through the crowd full of melee",
    "No trick plays, I'm Bill Gates,",
    "Take a genius to understand me",
    "Oh, oh, sometimes I get a good feeling, yeah",
    "I get a feeling that I never never never never had before, no no",
    "I get a good feeling, yeah",
    "Good feelin', good feelin'",
    "I know you got the good feelin'",
    "Let's get it, let's get it",
    "Gotta love the life that we livin'",
    "Let's get it, let's get it",
    "I know you got the good feelin'",
    "Let's get it, let's get it",
    "Gotta love the life that we livin'",
    "Oh, oh, sometimes I get a good feeling, yeah",
    "I get a feeling that I never never never never had before, no no",
    "I get a good feeling, yeah"
]
  
  if "robot" in user_message:
    return f"""you said my name!!
      {user_message.replace("robot", user_name)}"""
  elif "sports score" in user_message:
    return "To find sports scores look at https://www.espn.com"
  elif "birthday" in user_message:
    return f"""Happy birthday {user_message.replace("birthday", user_name)}!!"""
  elif "joke" in user_message:
    return random.choice(jokes)
  elif "lyrics" in user_message:
    return random.choice(lyrics)
  elif "fun fact" in user_message:
    return random.choice(fun_fact)
  elif "day" in user_message:
    x = datetime.datetime.now()
    print(x.strftime("%A"))
    return f"""Today is
    {x.strftime("%A")}"""
  elif "todays date" or "date" in user_message:
    x = datetime.datetime.now()
    print(x.strftime("%x"))
    return f"""Todays date is 
    {x.strftime("%x")}"""
  elif "math" in user_message:
        problem = user_message.replace("math")
        answer = eval(problem)
        return f"The answer to {problem} is {answer}."
  elif "time" in user_message:
    x = datetime.datetime.now()
    print(x.strftime("%X"))
    return f"""It is
    {x.strftime("%X")}"""
  elif "rock paper scissors" in user_message:
    user_choice = user_message.replace("rock paper scissors")
    bot_choice = random.choice(rps)
    if user_choice == bot_choice:
      result = "It's a tie!" 
    elif (user_choice == "rock" and bot_choice == "scissors") or \
            (user_choice == "paper" and bot_choice == "rock") or \
             (user_choice == "scissors" and bot_choice == "paper"):
      result = "You win!"
    else:
      result = "I win!"
    return f"You chose {user_choice}. I chose {bot_choice}. {result}"
   


  
  


