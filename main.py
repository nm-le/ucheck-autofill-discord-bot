"""
Discord Bot
"""

import discord
import autofill


client = discord.Client()


@client.event
async def on_ready() -> None:
    """
    Signal that bot is running.
    :return: None
    """
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message) -> None:
    """
    Message sent event.
    :param message: the message sent in the channel
    :return: None
    """
    if message.content.startswith('ucheck'):
        channel = message.channel

        await channel.send('Please enter your UTORID')

        def check(m) -> bool:
            """
            Check if channel is the same and author is not the bot itself.
            :param m: the message sent in the channel
            :return: boolean
            """
            return m.author != client.user and m.channel == channel

        msg_id = await client.wait_for('message', check=check, timeout=10000)
        utorid = msg_id.content

        await channel.send('Please enter your password')

        msg_pw = await client.wait_for('message', check=check, timeout=10000)
        pwd = msg_pw.content

        autofill.automate_ucheck(utorid, pwd)


        await channel.send(file=discord.File('screenshots/' + autofill.date + utorid + '.png'))


client.run('OTI3MDIzODQ4MTU3NzU3NTAy.YdEMPA.pYVVG66VDdzQAJjnc_2 - G0AtBBw')
