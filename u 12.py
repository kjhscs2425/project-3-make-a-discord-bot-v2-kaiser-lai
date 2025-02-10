import random
def russian():
    while True:
        game = input("Let's play, shall we... casual or extreme? ")

        if game == "extreme":
            input("2 bullets loaded enter to start")
            cylinder = ["click"] * 4 + ["boom"] *2
            random.shuffle(cylinder)
            
            while True:
                input("Press Enter to pull the trigger.")
                trigger = cylinder.pop()
                print(trigger)
                
                if trigger == "boom":
                    print("game over")
                    break
                if not cylinder:
                    random.shuffle(cylinder)
                    cylinder = ["click"] * 4 + ["boom"] *2
                    print("reloading")
        if game == "casual":
            input("1 bullets loaded enter to start")
            cylinder = ["click"] * 5 + ["boom"] *1
            random.shuffle(cylinder)
            
            while True:
                input("Press Enter to pull the trigger.")
                trigger = cylinder.pop()
                print(trigger)
                
                if trigger == "boom":
                    print("game over")
                    break
                if not cylinder:
                    random.shuffle(cylinder)
                    cylinder = ["click"] * 5 + ["boom"] *1
                    print("reloading")
       
            
        

russian()
            
             
       
        



async def russian(ctx, mode: str = None):
    if mode not in ["casual", "deathwish"]:
        await ctx.send("Select your game mode... `deathwish` or `casual`.")
        return

    if mode == "casual":
        await ctx.send("1 bullet loaded, enter to fire and type `c` to pass to bot.")
        cylinder = ["click"] * 5 + ["boom"]

    elif mode == "deathwish":
        await ctx.send("2 bullets loaded, enter to fire and type `c` to pass to bot.")
        cylinder = ["click"] * 4 + ["boom"] * 2

    random.shuffle(cylinder)

    def check(m):
        return m.channel == ctx.channel and m.content.lower() in ["fire", "c"]

    while cylinder:
        msg = await ctx.bot.wait_for("message", check=check)
        user = msg.author
        user_choice = msg.content.lower()

        if user_choice == "fire":
            trigger = cylinder.pop()
            await ctx.send(f"{user.mention} pulled the trigger... {trigger.upper()}!")

            if trigger == "boom":
                await ctx.send(f"{user.mention} is dead! Game Over.")
                return

        elif user_choice == "c":
            await ctx.send("Bot's turn...")
            trigger = cylinder.pop()
            await ctx.send(f"{trigger.upper()}!")

            if trigger == "boom":
              await ctx.send("bot ded u win")
            return
        if not cylinder:
                  await ctx.send(" Reloading...")
                  cylinder = ["click"] * 5 + ["boom"]
                  random.shuffle(cylinder)