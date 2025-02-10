import random
state = "not russian"
def should_i_respond(user_message, user_name):
    return True




#**Do NOT change the name of this function.**

#"This function will be called every time the `should_i_respond` function returns `True`.

#* This function returns a string.
#* The bot will post the returned string on the channel where the original message was sent.
#* You can have the bot respond differently to different messages and users

def respond(user_message, user_name):
  global state, cylinder
  if "do you speak mandarin" in user_message:
    return f""" no... ingles por favor
  {user_message.replace("robot", user_name)}"""
  elif "cats" in user_message:
    return "I eat them"
  if "russian"in user_message:
    state = "start"
    return "Let's play, shall we... casual or deathwish? "
  
  
  if "russian" in user_message:
        state = "start"
        return "Let's play, shall we... casual or deathwish? "

  if state == "start":
        if user_message == "deathwish":
            state = "deathwish"
            cylinder = ["click"] * 4 + ["boom"] * 2
            random.shuffle(cylinder)
            return "2 bullets loaded, press e to start"

  if state == "deathwish":
        if user_message == "e":
            if not cylinder:
                cylinder = ["click"] * 4 + ["boom"] * 2
                random.shuffle(cylinder)
                return "Reloading... press e to continue"

            trigger = cylinder.pop()
            if trigger == "boom":
                state = "not russian"
                return "game over"
            else:
                return "Click! You're still alive. Press enter to pull the trigger again."
            
        if "i like dogs" in user_message:
          return "I eat them"

        if "potato" in user_message:
          return "potato"
  if "who is your daddy"in user_message:
    return "my creator is kaiser my father"
  if "favorite color"in user_message:
    return "what is a color... no comprendo ingles"
  if "what is winnie the pooh's real life counter part?":
    return "who is that.. idk"
  if "english or spanish"in user_message:
    return "no hablo inglese y espanol"
  if "what is your favorite music?"in user_message:
    return "listen to break it out by rock summer"



  

  









            
             
       
        



