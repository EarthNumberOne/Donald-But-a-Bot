import discord
from random import *
import atexit
from discord.utils import get
import re
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')
repeated = ''
repeats = 0
game_randint = None
page = 0
the_max = 100

try:
    @bot.event
    async def on_ready():
        print('Bot is online now')
        print("To access the bot's client, use 'cd discord-bot-client/electron' and 'npm start' to login")
        channel = bot.get_channel(755310786834071643)
        await channel.send("My program is running now!\nUse **!commands** to check out what can I do")
        presences = ["Cyberpunk 2077", "Minecraft", "Counter-Strike Global Offensive", "Grand Theft Auto V",
                     "Call of Duty: Modern Warfare (2019)", "Tom Clancy's Rainbow Six: Siege", "Red Dead Redemption 2",
                     "Need For Speed™", "Forza Horizon 4", "Battlefield V"]
        await bot.change_presence(activity=discord.Game(name=choice(presences)))


    @bot.event
    async def send(message, msg, rand_num):
        msg = msg[6:]
        if rand_num == 1:
            await message.channel.send("???WTF Are you talking about??? {0.author.mention}".format(message))
        if rand_num == 2:
            await message.channel.send("""Emmmmmmm... What is **"{}"**?? Sorry, I'm a idiot, I don't know""".format(msg) + " {0.author.mention}".format(message))
        if rand_num == 3:
            await message.channel.send("**BRUH** {0.author.mention}".format(message))
        if rand_num == 4 or rand_num == 5:
            await message.channel.send("I see... {0.author.mention}".format(message))


    @bot.event
    async def RepeatedOrNot(message, repeated, repeats):
        if str(message.author) != repeated and repeated != "<Donald> But a bot#4766" and repeated != "DDDuoDuo#1782" and "!" not in str(message.content)[0]:
            repeated = str(message.author)
            repeats = 1
        elif repeated != "DDDuoDuo#1782" and repeated != "<Donald> But a bot#4766" and "!" not in str(message.content).split()[0]:
            repeats += 1
        else:
            repeats = 0
            repeated = ''
        if 4 <= repeats < 6:
            await message.channel.send("Stop spamming! If you send more, I will mute you! {0.author.mention}".format(message))
        elif repeats >= 6 and repeats <= 7:
            await message.channel.send("Hey <@!699148103227408397> and <@&751311109885132813>, mute {0.author.mention}!".format(message))
        elif repeats > 7:
            if str(message.author) != "DDDuoDuo#1782":
                try:
                    await tempmute(message, message.author, 10, True)
                    repeated = ''
                    repeats = 0
                except discord.errors.Forbidden:
                    await message.channel.send("Cannot mute {0.author.mention}".format(message) + " because {0.author.mention} is a moderator".format(message))
                    # pass
        return repeated, repeats


    @bot.event
    async def check_message(message, author, check=False):
        messages = open('message.txt', 'r+')
        msg = messages.readline()
        m = msg.split("\t\t")
        t = False
        while msg != '':
            if m[0] == str(author):
                t = True
                with open('message.txt', 'r+') as file:
                    text = file.read()
                    if not check:
                        text = re.sub(msg.strip(), m[0] + "\t\t" + str(int(m[1]) + 1), text)
                    file.seek(0)
                    file.write(text)
                    file.truncate()
                if check:
                    await message.channel.send(
                        f"{message.author.mention}, {author.mention} has sent " + m[1].strip() + " messages since I was online")
                break
            msg = messages.readline()
            m = msg.split("\t\t")
        if not t:
            messages.write(str(author) + "\t\t1\n")

    @bot.event
    async def point_message(message, author, check=False, just_add=0):
        global the_max
        messages = open('points.txt', 'r+')
        msg = messages.readline()
        m = msg.split("\t\t")
        t = False
        while msg != '':
            if m[0] == str(author):
                t = True
                with open('points.txt', 'r+') as file:
                    text = file.read()
                    if not check:
                        if just_add == 0:
                            if the_max:
                                if the_max > 100:
                                    text = re.sub(msg.strip(), m[0] + "\t\t" + str(int(m[1]) + 100), text)
                                else:
                                    text = re.sub(msg.strip(), m[0] + "\t\t" + str(int(m[1]) + (the_max // 10)), text)
                            else:
                                text = re.sub(msg.strip(), m[0] + "\t\t" + str(int(m[1]) + 10), text)
                        else:
                            text = re.sub(msg.strip(), m[0] + "\t\t" + str(int(m[1]) + just_add), text)
                    file.seek(0)
                    file.write(text)
                    file.truncate()
                if check:
                    await message.channel.send(
                        "{0.author.mention} have ".format(message) + '$' + m[1].strip() + "!")
                break
            msg = messages.readline()
            m = msg.split("\t\t")
        if not t:
            messages.write(str(author) + "\t\t0\n")


    @bot.event
    async def on_message(message):
        global repeated, repeats, the_max
        await bot.process_commands(message)
        await check_message(message, message.author)
        # await message.channel.send(" _______
        #                             < hello >
        #                              -------
        #                                         \   ^__^\
        #                                             (oo)
        #                                           \_______(__)\       )\/\||----w |||     ||")
        if message.author == bot.user:
            return
        message.content = message.content.lower()
        message.content = message.content.strip()
        msg = str(message.content)
        memes = [
            "I'm ***GAY*** {0.author.mention} This is the link: https://www.youtube.com/watch?v=ajlkhFnz8eo".format(
                message),
            "NOOOOOOO GOD PLEASEEEEEE NOOOOOOOOOOOO!!! https://www.youtube.com/watch?v=umDr0mPuyQc {0.author.mention}".format(
                message),
            "FBI OPEN UP!!! Link: https://www.youtube.com/watch?v=4wX2xBOuzRg {0.author.mention}".format(message),
            "**I BROKE MY ASS** {0.author.mention}".format(
                message) + " Fun, isn't it? Here's the link: https://www.youtube.com/watch?v=JLREgYXXdB8&list=PLmRdHH1ME75XhlRibFIoxsjL9fHM5JEL5&index=33",
            "At this moment he knew: He **fucked** up {0.author.mention} .".format(message),
            "Hey girllll, wanna ***dance***? (from Kev boi) {0.author.mention}".format(message),
            "Keep Calm and Carry On! {0.author.mention}".format(message),
            "Rainbow **BLOB** {0.author.mention}".format(message),
            "'I'm the Juggernaut, bitch' ---- from old X-Man Cartoon https://www.youtube.com/watch?v=plQIf5fS8xw {0.author.mention}".format(
                message),
            "Trolololololololololololololo!!!!!!! {0.author.mention}!".format(message),
            "Captain: 'Who live in the pineapple under the sea?' Childrens: 'SpongeBob SquarePants!' Haha! This is funny! https://www.youtube.com/watch?v=r9L4AseD-aA {0.author.mention}!".format(
                message),
            "***OBEY***! {0.author.mention}".format(message),
            "**Doge** (Leon's favorite one) {0.author.mention}".format(message),
            "**The Nyan Cat**!!! The YouTube link: https://www.youtube.com/watch?v=QH2-TGUlwu4 {0.author.mention}".format(
                message),
            "LOL (Laughing) {0.author.mention}".format(message),
            "***BRUH*** (Favorite for me and Leon) The sound: https://www.youtube.com/watch?v=D2_r4q2imnQ {0.author.mention}".format(
                message),
            "And his name is **John Cena**! https://www.youtube.com/watch?v=XgUB3lF9IQA&t=2s {0.author.mention}".format(
                message),
            "OOOOOOOOOOOOOF!!! I love to play **ROBLOX**!!! https://www.youtube.com/watch?v=HoBa2SyvtpE",
            "Minion Dance: https://www.youtube.com/watch?v=Uos8weODYtI",
            "Jamal Says 'Every 60 Seconds In Africa, A Minute Passes, Together, we can stop this': https://www.youtube.com/watch?v=7Zm1hPbmzPw"]
        bad = ["fuck", "fuck you", "shit", "piss", "dick", "asshole", "bitch", "bastard", "damn", "hell", "rubbish",
               "bugger", "nigger", "nigga", "ass"]

        #TODO if str(message.author) == "DDDuoDuo#1782":
        #     print(msg)
        if msg == "pls ass" and str(message.author) == "China's best PVPER of all time#4688":
            await message.channel.send(
                "Hey Leon, do you know I wrote a script to prevent you doing this? Stop GHS and FOCUS!!! AND I KNOW YOU WILL DO THIS!!! FUCK YOU!!!")
        repeated, repeats = await RepeatedOrNot(message, repeated, repeats)

        if message.content.startswith("!chat"):
            rand_num = randint(1, 5)

            for w in msg.split():
                if w in bad:
                    if rand_num == 1:
                        await message.channel.send("What's wrong? {0.author.mention}".format(message))
                    if rand_num == 2:
                        await message.channel.send("No swearing is allowed! {0.author.mention}".format(message))
                    if rand_num == 3:
                        await message.channel.send(
                            "{0.author.mention}".format(message) + " Did you just said a bad word?!")
                    if rand_num == 4:
                        await message.channel.send(
                            "{0.author.mention}".format(message) + " Hey! Are you upset or cross?")
                    if rand_num == 5:
                        await message.channel.send("Hey {0.author.mention}!".format(message) + " Wanna talk to me?")
                    break
            else:
                if "hello" in msg or "hi" in msg or "halo" in msg or "hey" in msg or "bello" in msg:
                    if rand_num == 1:
                        await message.channel.send("Hello, {0.author.mention}".format(message) + "!")
                    if rand_num == 2:
                        await message.channel.send(
                            "Hi there, {0.author.mention}".format(message) + "! Nice to meet you")
                    if rand_num == 3:
                        await message.channel.send(
                            "{0.author.mention}".format(message) + " Nice to see you sending messages!")
                    if rand_num == 4:
                        await message.channel.send(
                            "{0.author.mention}".format(message) + " Hey! Good to see you **chatting** with us!")
                    if rand_num == 5:
                        await message.channel.send("Hi {0.author.mention}!".format(message) + " Wanna talk to me?")

                elif "meme" in msg:
                    if "meme" not in msg.split()[-1]:
                        m = msg.split()[-1]
                        for me in memes:
                            if m in me.lower():
                                await message.channel.send(me)
                                if "Rainbow" in me:
                                    await message.channel.send(file=discord.File('blob.gif'))
                                elif "OBEY" in me:
                                    await message.channel.send(file=discord.File('obey.jpg'))
                                elif "moment" in me:
                                    await message.channel.send(file=discord.File('moment.jpg'))
                                elif "Trol" in me:
                                    await message.channel.send(file=discord.File('troll.jpg'))
                                elif "Doge" in me:
                                    await message.channel.send(file=discord.File('doge.jpg'))
                                elif "Calm" in me:
                                    await message.channel.send(file=discord.File('Keep-calm.jpg'))
                                break
                        else:
                            await message.channel.send(
                                "Cannot find '{}'".format(m) + " in my meme list! {0.author.mention}".format(
                                    message))
                    else:
                        meme = choice(memes)
                        await message.channel.send(meme)
                        if "Rainbow" in meme:
                            await message.channel.send(file=discord.File('blob.gif'))
                        elif "OBEY" in meme:
                            await message.channel.send(file=discord.File('obey.jpg'))
                        elif "moment" in meme:
                            await message.channel.send(file=discord.File('moment.jpg'))
                        elif "Trol" in meme:
                            await message.channel.send(file=discord.File('troll.jpg'))
                        elif "Doge" in meme:
                            await message.channel.send(file=discord.File('doge.jpg'))
                        elif "Calm" in meme:
                            await message.channel.send(file=discord.File('Keep-calm.jpg'))

                elif "bruh" in msg or "dude" in msg or "yeet" in msg or "oof" in msg:
                    if rand_num == 1:
                        await message.channel.send(
                            "**Yeet dude!** {0.author.mention} You know **'bruh'** is my favorite word? Ah ha!".format(
                                message))
                    if rand_num == 2:
                        await message.channel.send(
                            "**Ooooof!** {0.author.mention} you like this word too!!!".format(message))
                    if rand_num == 3:
                        await message.channel.send(
                            "Oh, come'on! {0.author.mention} you can do better at bruh-ing!".format(message))
                    if rand_num == 4:
                        await message.channel.send(
                            "{0.author.mention} always like to say this word! Same as me!".format(message))
                    if rand_num == 5:
                        await message.channel.send(
                            "{0.author.mention} ***BRUH***, you are L <:loser:751684371932512298> (Just kidding)".format(
                                message))

                elif "gay" in msg:
                    if "is" in msg:
                        split = msg.split()
                        split = split[split.index('is') + 1]
                        await message.channel.send(
                            "{0.author.mention} Yes, ".format(message) + split.capitalize() + " is a gay!")
                    elif "am" in msg:
                        await message.channel.send("Nope, you're not {0.author.mention}".format(message))
                    else:
                        await message.channel.send("{0.author.mention} Nope, I am not".format(message))

                elif "how are you" in msg or "fine" in msg or "feel" in msg:
                    if rand_num == 1:
                        await message.channel.send("Me? Oh, I'm fine. {0.author.mention}".format(message))
                    if rand_num == 2:
                        await message.channel.send("I am okay... How about you? {0.author.mention}".format(message))
                    if rand_num == 3:
                        await message.channel.send(
                            "Ummmmmm... I feel really bad. {0.author.mention}".format(message))
                    if rand_num == 4:
                        await message.channel.send("I feel bad... Maybe... {0.author.mention}".format(message))
                    if rand_num == 5:
                        await message.channel.send("I'm fine! Don't bother me. {0.author.mention}".format(message))

                elif "sad" in msg or "angry" in msg or "happy" in msg:
                    if rand_num == 1:
                        await message.channel.send("Oh com'on! {0.author.mention}".format(message))
                    if rand_num == 2:
                        await message.channel.send("You can do better than this {0.author.mention}".format(message))
                    if rand_num == 3:
                        await message.channel.send("{0.author.mention} Be positive!".format(message))
                    if rand_num == 4:
                        await message.channel.send("I am **HAPPY**!! {0.author.mention}".format(message))
                    if rand_num == 5:
                        await message.channel.send("**SAD** {0.author.mention}".format(message))

                elif "no" in msg or 'sure' in msg or 'yes' in msg or 'yep' in msg or "ok" in msg or "yeah" in msg:
                    if rand_num == 1:
                        await message.channel.send("Okay... {0.author.mention}".format(message))
                    if rand_num == 2:
                        await message.channel.send("Fine {0.author.mention}".format(message))
                    if rand_num == 3:
                        await message.channel.send("I can't do with that... {0.author.mention}".format(message))
                    if rand_num == 4:
                        await message.channel.send(
                            "...I have nothing can say about {0.author.mention}".format(message))
                    if rand_num == 5:
                        await message.channel.send("BRUH {0.author.mention}".format(message))
                elif "thank" in msg:
                    await message.channel.send("It's okay! {0.author.mention}".format(message))
                elif "how" in msg or "what" in msg or "why" in msg or "why" in msg:
                    if rand_num == 1 or rand_num == 2:
                        await message.channel.send("By some method... {0.author.mention}".format(message))
                    if rand_num == 3:
                        await message.channel.send(
                            "Go to https://www.google.com! {0.author.mention}".format(message))
                    if rand_num == 4 or rand_num == 5:
                        await message.channel.send("Go find out yourself! {0.author.mention} GG".format(message))
                elif "haha" in msg or "lol" in msg or "lmao" in msg or "funny" in msg or "gg" in msg:
                    if rand_num == 1 or rand_num == 2:
                        await message.channel.send("Funny, right? {0.author.mention}".format(message))
                    if rand_num == 3:
                        await message.channel.send(
                            "Haha! I think it's funny too! {0.author.mention}".format(message))
                    if rand_num == 4 or rand_num == 5:
                        await message.channel.send("OOF {0.author.mention} GG".format(message))
                elif "bye" in msg or "cya" in msg or "see" in msg or "ya" in msg:
                    if rand_num == 1 or rand_num == 2:
                        await message.channel.send("Fine {0.author.mention} *GOODBYE AND DON'T BOTHER ME AGAIN*".format(message))
                    if rand_num == 3:
                        await message.channel.send(
                            "Bye! {0.author.mention}".format(message))
                    if rand_num == 4 or rand_num == 5:
                        await message.channel.send("OOF {0.author.mention} cya!".format(message))


                else:
                    await send(message, msg, rand_num)
        if message.content.startswith("!gay_test"):
            if msg == '!gay_test':
                await message.channel.send(
                    "Okay, I will ask you 5 questions and test you how gay you are (from 0% to 100%)! \nAnswer me like this: !gay-test o o o o o (Replace o with 'N' for no, 'Y' for yes)\n\nQuestion 1: Do you know what is **'GAY'**?\nY or N\nQuestion 2: Have you sleep with a male before?\nY or N\nQuestion 3: Have you watched the video called 'I'm GAY' before?\nY or N\nQuestion 4: Do you like to hang out or stay with a male?\nY or N\nQuestion 5: Are you a ***GAY***?\nY or N\n")
            elif 'y' or 'n' in msg:
                tmp = '{0.author.mention}'.format(message)
                await message.channel.send("Calculating how gay is {}".format(tmp))
                if msg.split()[-1] == 'y':
                    await message.channel.send("{} is ".format(tmp) + str(100) + "% of **GAYNESS**")
                elif msg.count('n') == 5:
                    await message.channel.send("{} is ".format(tmp) + str(0) + "% of **GAYNESS**")
                else:
                    await message.channel.send("{} is ".format(tmp) + str(randint(0, 100)) + "% of **GAYNESS**")
        if message.content.startswith("!meme") or message.content.startswith("!memes"):
            if "meme" not in msg.split()[-1]:
                m = msg.split()[1]
                for me in memes:
                    if m in me.lower():
                        await message.channel.send(me)
                        if "Rainbow" in me:
                            await message.channel.send(file=discord.File('blob.gif'))
                        elif "obey" in me:
                            await message.channel.send(file=discord.File('obey.jpg'))
                        elif "moment" in me:
                            await message.channel.send(file=discord.File('moment.jpg'))
                        elif "trol" in me:
                            await message.channel.send(file=discord.File('troll.jpg'))
                        elif "doge" in me:
                            await message.channel.send(file=discord.File('doge.jpg'))
                        elif "calm" in me:
                            await message.channel.send(file=discord.File('Keep-calm.jpg'))
                        break
                else:
                    await message.channel.send(
                        "Cannot find '{}'".format(m) + " in my meme list! {0.author.mention}".format(message))
            else:
                meme = choice(memes)
                await message.channel.send(meme)
                if "Rainbow" in meme:
                    await message.channel.send(file=discord.File('blob.gif'))
                elif "OBEY" in meme:
                    await message.channel.send(file=discord.File('obey.jpg'))
                elif "moment" in meme:
                    await message.channel.send(file=discord.File('moment.jpg'))
                elif "Trol" in meme:
                    await message.channel.send(file=discord.File('troll.jpg'))
                elif "Doge" in meme:
                    await message.channel.send(file=discord.File('doge.jpg'))
                elif "Calm" in meme:
                    await message.channel.send(file=discord.File('Keep-calm.jpg'))
        if str(message.channel) == '📊｜verification':
            if "!verify" in msg:
                role = get(message.author.guild.roles, name='Noobs')
                await message.author.add_roles(role)
                role = get(message.author.guild.roles, name='Unverified')
                await message.author.remove_roles(role)
                await message.channel.send("Successfully verified {0.author.mention}!".format(message))

        if message.content.startswith("!bank"):
            await point_message(message, message.author, True)

        if message.content.startswith("!member"):
            mem = list(message.guild.members)
            mes = "The Member of G6 Discord are: \n"
            for m in mem:
                m = str(m)
                mes += m + "\n"
            await message.channel.send(mes)
        if message.content.startswith("!fuck_you"):
            await message.channel.send("Yeah yeah, I know, Fuck you too ! You are L <:loser:751684371932512298> {0.author.mention}".format(message))


    @bot.command()
    @commands.has_role("Admins")
    async def mute(ctx, member: discord.Member, spam=False, temp=False):
        role = get(member.guild.roles, name='Muted')
        if role in member.roles:
            await ctx.channel.send("{0.mention}".format(member) + " is already muted!")
        else:
            if "Co-owner" in member.roles and "Pro Owner" not in ctx.author.roles:
                await ctx.channel.send(f"You can't mute a Co-owner! {ctx.author.mention}")
            else:
                await member.add_roles(role)
                role = get(member.guild.roles, name='Admins')
                await member.remove_roles(role)
                role = get(member.guild.roles, name='Co-owner')
                await member.remove_roles(role)
                role = get(member.guild.roles, name='Noobs')
                await member.remove_roles(role)
                if spam:
                    await ctx.channel.send("**I AM THE ADMIN!!!** {0.mention}".format(member) + " is temporary **Muted** and returned to ***Noobs*** again because of ***SPAMMING*** in {0.channel}.".format(ctx))
                elif temp:
                    await ctx.channel.send("{0.mention}".format(member) + " is temporary muted and returned to ***Noobs*** again.")
                else:
                    await ctx.channel.send("{0.mention}".format(member) + " is muted and returned to ***Noobs*** again.")

    @bot.command()
    @commands.has_role("Admins")
    async def tempmute(ctx, member: discord.Member, minutes=10, spam=False):
        role = get(member.guild.roles, name='Muted')
        if role in member.roles:
            await ctx.channel.send("{0.mention}".format(member) + " is already muted!")
        else:
            if "Co-owner" in member.roles and "Pro Owner" not in ctx.author.roles:
                await ctx.channel.send(f"You can't mute a Co-owner! {ctx.author.mention}")
            else:
                minutes = int(minutes)
                await mute(ctx, member, spam, True)
                await asyncio.sleep(minutes * 60)
                await unmute(ctx, member)


    @bot.command()
    @commands.has_role('Admins')
    async def unmute(ctx, member: discord.Member):
        role = get(member.guild.roles, name='Muted')
        if role not in member.roles:
            await ctx.channel.send("{0.mention}".format(member) + " is not muted!")
        else:
            role = get(member.guild.roles, name='Noobs')
            await member.add_roles(role)
            role = get(member.guild.roles, name='Muted')
            await member.remove_roles(role)
            await ctx.channel.send("{0.mention}".format(member) + " is unmuted now.")


    @bot.command()
    @commands.has_role("Co-owner")
    async def derole(ctx, member: discord.Member, r):
        role = get(member.guild.roles, name=r)
        if role is None:
            await ctx.channel.send("Cannot find the role **'{}'** ".format(r) + "{0.author.mention}".format(ctx))
        else:
            if role not in member.roles:
                await ctx.channel.send(
                    "{0.mention} is not a ".format(member) + "**{}**!".format(r) + " {0.author.mention}".format(ctx))
            else:
                await member.remove_roles(role)
                await ctx.channel.send("Reomoved the role {}".format(r) + " to {0.mention}".format(member))


    @bot.command()
    @commands.has_role("Co-owner")
    async def role(ctx, member: discord.Member, r):
        role = get(member.guild.roles, name=r)
        if role is None:
            await ctx.channel.send("Cannot find the role **'{}'** ".format(r) + "{0.author.mention}".format(ctx))
        else:
            if role in member.roles:
                await ctx.channel.send(
                    "{0.mention} is already a ".format(member) + "**{}**!".format(r) + " {0.author.mention}".format(
                        ctx))
            else:
                await member.add_roles(role)
                await ctx.channel.send("Added the role {}".format(r) + " to {0.mention}".format(member))


    @bot.command()
    @commands.has_role('Pro Owner')
    async def offline(ctx):
        channel = bot.get_channel(755310786834071643)
        await channel.send("My program is shutting down now!")
        await bot.close()
        exit(1)


    @bot.command()
    async def guess_setup(ctx, minimum=None, maximum=None):
        global game_randint, the_max
        if maximum and minimum:
            minimum, maximum = int(minimum), int(maximum)
            the_max = maximum - minimum
        else:
            the_max = None
        if game_randint:
            await ctx.channel.send(f"{ctx.author.mention} There's already a number chosen!")
        else:
            if minimum and maximum:
                minimum, maximum = int(minimum), int(maximum)
                if maximum - minimum >= 100:
                    game_randint = randint(minimum, maximum)
                    await ctx.channel.send(f"{ctx.author.mention} The number is all set! You may start the game right now! Remember to use " +
                        "**!guess** to guess the number!\n" + "This number is between **{}** to ".format(str(minimum)) + "**{}**!".format(str(maximum)))
                else:
                    await ctx.channel.send(f"{ctx.author.mention} The two numbers' difference are too small, make sure the difference is larger than 100!")
            else:
                game_randint = randint(1, 100)
                await ctx.channel.send(
                    f"{ctx.author.mention} The number is all set! You may start the game right now! Remember to use "
                    "**!guess** to guess the number!\nThis number is from 1 to 100!")
            print("The guessing game number is: " + str(game_randint))


    @bot.command()
    async def guess(ctx, number=None):
        global game_randint, the_max
        if game_randint:
            if the_max:
                the_max = int(the_max)
            else:
                the_max = 100
            if number:
                number = int(number)
                if number == game_randint:
                    if the_max // 10 > 100:
                        await ctx.channel.send(
                            f"Congratulations! {ctx.author.mention} Answered it correctly! $100 is added to your bank!")
                    else:
                        await ctx.channel.send(f"Congratulations! {ctx.author.mention} Answered it correctly! ${the_max // 10} is added to your bank!")
                    game_randint = None
                    await point_message(ctx, ctx.author, False)
                elif number > game_randint:
                    await ctx.channel.send(
                        "Hey {0.author.mention}! The number you guessed is larger than my number!".format(ctx))
                elif number < game_randint:
                    await ctx.channel.send("{0.author.mention} Your number is smaller than my number!".format(ctx))
            else:
                await ctx.channel.send(
                    "{0.author.mention} Please guess a number rather then leave it blank! ".format(ctx))
        else:
            await ctx.channel.send(
                "{0.author.mention} The number is not setup yet! use **!guess_setup** to start the game!".format(ctx))


    @bot.command()
    async def guess_end(ctx):
        global game_randint
        if game_randint:
            game_randint = None
            await ctx.channel.send("{0.author.mention} The game is ended!".format(ctx))
        else:
            await ctx.channel.send("{0.author.mention} The game is not started yet!".format(ctx))


    @bot.command()
    async def rock_paper_scissor(ctx, thing, difficulty="easy"):
        thing = thing.lower()
        difficulty = difficulty.lower()
        if thing != 'r' and thing != 'p' and thing != 's':
            await ctx.channel.send(f"Please enter either R stands for rock, or P stands for paper, or S stands for "
                                   f"scissor! {ctx.author.mention}")
        else:
            if difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "extreme":
                await ctx.channel.send(f"Please enter valid difficulty! {ctx.author.mention}")
            else:
                if difficulty == 'easy':
                    random_thing = choice([1, 2])
                elif difficulty == 'medium':
                    random_thing = choice([1, 2, 3])
                elif difficulty == 'hard':
                    random_thing = choice([1, 2, 3, 4])
                elif difficulty == 'extreme':
                    random_thing = choice([1, 2, 3, 4, 5])
                if random_thing == 1:
                    if thing == 'r':
                        await ctx.channel.send('🤜 vs ✌')
                    elif thing == 'p':
                        await ctx.channel.send('🖐️ vs 🤜')
                    else:
                        await ctx.channel.send('✌ vs 🖐️')
                    if difficulty == 'easy':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You beat me! $1 is added to your bank!")
                        await point_message(ctx, ctx.author, False, 1)
                    elif difficulty == 'medium':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You beat me! $5 is added to your bank!")
                        await point_message(ctx, ctx.author, False, 5)
                    elif difficulty == 'hard':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You beat me! $10 is added to your bank!")
                        await point_message(ctx, ctx.author, False, 10)
                    elif difficulty == 'extreme':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You beat me! $20 is added to your bank!")
                        await point_message(ctx, ctx.author, False, 20)
                elif random_thing == 2:
                    if thing == 'r':
                        await ctx.channel.send('🤜 vs 🤜')
                    elif thing == 'p':
                        await ctx.channel.send('🖐️ vs 🖐️')
                    else:
                        await ctx.channel.send('✌ vs ✌')
                    await ctx.channel.send(f"Ummmmm... {ctx.author.mention} We had a tie!")
                else:
                    if thing == 'r':
                        await ctx.channel.send('🤜 vs 🖐️')
                    elif thing == 'p':
                        await ctx.channel.send('🖐️ vs ✌')
                    else:
                        await ctx.channel.send('✌ vs 🤜')
                    if difficulty == 'easy':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You lost! $2 is removed to your bank!")
                        await point_message(ctx, ctx.author, False, -2)
                    elif difficulty == 'medium':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You lost! $10 is removed to your bank!")
                        await point_message(ctx, ctx.author, False, -10)
                    elif difficulty == 'hard':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You lost! $20 is removed to your bank!")
                        await point_message(ctx, ctx.author, False, -20)
                    elif difficulty == 'extreme':
                        await ctx.channel.send(f"Hey {ctx.author.mention}! You lost! $40 is removed to your bank!")
                        await point_message(ctx, ctx.author, False, -40)


    @bot.command()
    async def messages(ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        try:
            await check_message(ctx, member, True)
        except:
            await ctx.channel.send(f"Can't find the user {str(member)}! {ctx.author.mention}")


    @bot.command()
    async def commands(ctx):
        global page
        if page == 0:
            page = 1
            contents = [
                "\n\t**!commands**\n\t**!chat** (Chat with it)\n\t**!gay_test** (Test how gay you are)\n\t**!meme** (You can "
                "enter a meme you want to see or just leave it blank to get a random one)\n\t**!offline** (To shut down the "
                "bot, only works for me)",
                "\n\t**!messages** (Check the messages you sent and others sent)\n\t**!member** (Check all members)\n\t**!fuck_you** (Say fuck "
                "to it)\n\t**!mute** (To mute someone, only work for Admins and me)\n\t**!unmute** (To unmute someone, only work for Admins and me)\n\t",
                "\n\t**!tempmute** (Temporary mute someone, you may enter the time in minutes, only work for Admins and me)\n\t**!role** (To give someone a role, only work for Co-owners and me)\n\t**!derole** (To remove someone's role, only work for Co-owners and me)\n**!bank** (To see how much money you have)\n"]
            pages = 3
            cur_page = 1
            command = discord.Embed(title=f"Commands Page {cur_page}/{pages}", description="Please wait for more features ;-;", color=0xd3fdac)
            command.add_field(name="Commands", value=contents[cur_page - 1], inline=False)
            command.add_field(name="Games", value="**--------------------**\n**Guessing game:**\n\t**!guess_setup** (To setup a guessing "
                                                          "game, you can enter the range for your number if you "
                                                          "want)\n\t**!guess** (Guess a number of the guessing "
                                                          "game)\n\t**!guess_end** (End a guessing game)\n**!bank** (To see how much money you have)\n**--------------------**\n**Rock-Paper-Scissor game:**\n**!rock_paper_scissor** (Enter R stands for rock, P stands for paper, S stands for scissor)\nYou can add difficulties at the end! (Easy, Medium, Hard, Extreme)\n\nMore games "
                                                          "coming ;-;")
            message = await ctx.channel.send(embed=command)

            await message.add_reaction("◀️")
            await message.add_reaction("▶️")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

            while True:
                try:
                    reaction, user = await bot.wait_for("reaction_add", timeout=90, check=check)

                    if str(reaction.emoji) == "▶️" and cur_page != pages:
                        cur_page += 1
                        new = discord.Embed(title=f"Commands Page {cur_page}/{pages}", description="Please wait for more features ;-;", color=0xd3fdac)
                        new.add_field(name="Commands", value=contents[cur_page - 1], inline=False)
                        new.add_field(name="Games", value="**--------------------**\n**Guessing game:**\n\t**!guess_setup** (To setup a guessing "
                                                          "game, you can enter the range for your number if you "
                                                          "want)\n\t**!guess** (Guess a number of the guessing "
                                                          "game)\n\t**!guess_end** (End a guessing game)\n**!bank** (To see how much money you have)\n**--------------------**\n**Rock-Paper-Scissor game:**\n**!rock_paper_scissor** (Enter R stands for rock, P stands for paper, S stands for scissor)\nYou can add difficulties at the end! (Easy, Medium, Hard, Extreme)\n\nMore games "
                                                          "coming ;-;")
                        await message.edit(embed=new)
                        await message.remove_reaction(reaction, user)

                    elif str(reaction.emoji) == "◀️" and cur_page > 1:
                        cur_page -= 1
                        new = discord.Embed(title=f"Commands Page {cur_page}/{pages}", description="Please wait for more features ;-;", color=0xd3fdac)
                        new.add_field(name="Commands", value=contents[cur_page - 1], inline=False)
                        new.add_field(name="Games", value="**--------------------**\n**Guessing game:**\n\t**!guess_setup** (To setup a guessing "
                                                          "game, you can enter the range for your number if you "
                                                          "want)\n\t**!guess** (Guess a number of the guessing "
                                                          "game)\n\t**!guess_end** (End a guessing game)\n**!bank** (To see how much money you have)\n**--------------------**\n**Rock-Paper-Scissor game:**\n**!rock_paper_scissor** (Enter R stands for rock, P stands for paper, S stands for scissor)\nYou can add difficulties at the end! (Easy, Medium, Hard, Extreme)\n\nMore games "
                                                          "coming ;-;")
                        await message.edit(embed=new)
                        await message.remove_reaction(reaction, user)

                    else:
                        await message.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    await message.delete()
                    await ctx.channel.send("Timed out! The command embed is deleted")
                    page = 0
                    break
        else:
            await ctx.channel.send("There's already a commands page shown!")
except Exception as e:
    error = str(e)
    print(f"There's an error occurred: {error}")

TOKEN = "NzUyMDI2NDYxNzM2NjY1MTUy.X1RpOA.VctojLEaJke7H51SNWjsT22z0iI"

bot.run(TOKEN)


def exit_handler():
    print('Bot is offline now')


atexit.register(exit_handler)
