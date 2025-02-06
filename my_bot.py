import random
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  return True

async def russian(ctx, mode: str = None):
  if mode not in ["casual", "deathwish"]:
    await ctx.send ("select your game mode... deathwish or casual")
    return
  if mode == "casual":
    await ctx.send("1 bullet loaded, enter too fire and type c to pass to bot")
    cylinder = ["click"]*5 + ["boom"]
    
  elif mode == "deathwish":
      await ctx.send("2 bullet loaded, enter too fire and type c to pass to bot")
      cylinder = ["click"]*4 + 2["boom"]
    
  random.shuffle
      
  def check(m):o
        return m.user == ctx.user and ctx.content.lower() in ["fire", "c"]
      
  while cylinder:
        msg = await ctx.bot.wait_for("message", check=check)
        if msg.content.lower() == "fire":
          trigger = cylinder.pop()
          await ctx.send("{trigger.upper}!")
          if trigger == "boom":
            await ctx.send("lol u ded")
            return
          
          elif msg.content.lower() == "c":
            await ctx.send ("bot's turn ...")
            if trigger == "boom":
              await ctx.send("bot ded u win")
            return
          if not cylinder:
                  await ctx.send("🔄 Reloading...")
                  cylinder = ["click"] * 5 + ["boom"]
                  random.shuffle(cylinder)


        

      




  

    
        
    
        




        
        

  




#**Do NOT change the name of this function.**

#"This function will be called every time the `should_i_respond` function returns `True`.

#* This function returns a string.
#* The bot will post the returned string on the channel where the original message was sent.
#* You can have the bot respond differently to different messages and users

def respond(user_message, user_name):
  if "do you speak mandarin":
    return f""" no... ingles por favor
  {user_message.replace("robot", user_name)}"""
  elif "cats" in user_message:
    return "I eat them"
  if "russian"in user_message:
    return russian()
  if "i like dogs"in user_message:
    return "i eat them"
  if "potato"in user_message:
    return "potato"
  if "who is your daddy"in user_message:
    return "my creator is kaiser my father"
  if "favorite color"in user_message:
    return "what is a color... no comprendo ingles"
  if "what is winnie the pooh's real life counter part?":
    return "who is that.. idk"
  if "english or spanish"in user_message:
    return "no hablo inglese y espanol"
  if"what is your favorite music?"in user_message:
    return "listen to break it out by rock summer"



  

  









            
             
       
        



