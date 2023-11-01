import discord
from discord.ext import commands
from gtts import gTTS
from random import choice
from bot_token import bot_token
from emoji_utils import text_to_speech

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
language = 'ru'


def random_language(language):
    if language == 'ru':
        from service_russian import random_list
    else:
        from service_english import random_list
    return random_list


def transport_language(language):
    if language == 'ru':
        from service_russian import transport_list
    else:
        from service_english import transport_list
    return transport_list


def environment_language(language):
    if language == 'ru':
        from service_russian import environment_list
    else:
        from service_english import environment_list
    return environment_list


def ecology_language(language):
    if language == 'ru':
        from service_russian import ecology_list
    else:
        from service_english import ecology_list
    return ecology_list


def common_language(language):
    if language == 'ru':
        from service_russian import common_tips
    else:
        from service_english import common_tips
    return common_tips


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1168923155126038631)  # 1165238682467434528
    await channel.send(f'```Привет, {member}! Список доступных команд на сервере:\n$random - отправляет случайный совет\n$change_language - позволяет сменить язык (по умолчанию русский)\n$category - советы по категориям\n$record - запись произвольного текста\n\nHello {member}! List of available commands on the server:\n$random - sends a random tip\n$change_language - allows you to change the language (Russian by default)\n$category - tips by category\n$record - record arbitrary text```')


@bot.command()
async def random(ctx):
    global language
    if language == 'ru':
        await ctx.send('''```В каком формате Вы хотите получить сообщение(1 - voice/2 - text)?```''')
    else:
        await ctx.send('''```In what format would you like to receive the message (1 - voice/2 - text)?```''')

    format_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    random_list = random_language(language)
    if format_value.content.lower() == '1':
        tts = text_to_speech(choice(random_list), language=language)
        tts.save('voices/voice.mp3')

        await ctx.send(file=discord.File('voices/voice.mp3'))
    elif format_value.content.lower() == '2':
        await ctx.send(f'```{choice(random_list)}```')
    else:
        if language == 'ru':
            await ctx.send('''```Такого формата не существует, напишите voice/text```''')
        else:
            await ctx.send('''```This format does not exist, send voice/text```''')
            return


@bot.command()
async def change_language(ctx):
    global language
    if language == 'ru':
        await ctx.send('''```Введите язык, который будет использован(ru/eng)```''')
    else:
        await ctx.send('''```Enter the language that will be used(ru/eng)```''')
    language_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if language_value.content.lower() == 'ru':
        language = 'ru'
        await ctx.send('''```Язык был успешно изменен на русский```''')
    elif language_value.content.lower() == 'eng':
        language = 'en'
        await ctx.send('''```The language has been successfully changed to English```''')
    else:
        if language == 'ru':
            await ctx.send('''```Извините, но этот язык не поддерживается```''')
        else:
            await ctx.send('''```Sorry, but this language is not supported```''')
        return


@bot.command()
async def category(ctx):
    if language == 'ru':
        await ctx.send('''```По какой категории Вы хотите получить информацию\n(1 - транспорт/2 - окружающая среда/3 - экология/4 - общее)?```''')
    else:
        await ctx.send('''```Which category do you want to receive information\n(1 - transport/2 - environment/3 - ecology/4 - general)?```''')
    category_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if category_value.content == '1':
        if language == 'ru':
            await ctx.send('''```Вы выбрали категорию `транспорт`\nВ каком формате Вы хотите получить сообщение(1 - voice/2 - text)?```''')
        else:
            await ctx.send('''```You have selected the `transport` category\nIn what format would you like to receive the message (1 - voice/2- text)?```''')
        format_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        transport_list = transport_language(language)
        if format_value.content.lower() == '1':
            tts = text_to_speech(choice(transport_list), language=language)
            tts.save('voices/voice-transport.mp3')

            await ctx.send(file=discord.File('voices/voice-transport.mp3'))
        elif format_value.content.lower() == '2':
            await ctx.send(f'```{choice(transport_list)}```')
        else:
            if language == 'ru':
                await ctx.send('''```Такого формата не существует, напишите voice/text```''')
            else:
                await ctx.send('''```This format does not exist, send voice/text```''')
            return
    elif category_value.content == '2':
        if language == 'ru':
            await ctx.send('''```Вы выбрали категорию `окружающая среда`\nВ каком формате Вы хотите получить сообщение(1 - voice/2 - text)?```''')
        else:
            await ctx.send('''```You have selected the `environment` category\nIn what format would you like to receive the message (1 - voice/2 - text)?```''')
        format_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        environment_list = environment_language(language)
        if format_value.content.lower() == '1':
            tts = text_to_speech(choice(environment_list), language=language)
            tts.save('voices/voice-environment.mp3')

            await ctx.send(file=discord.File('voices/voice-environment.mp3'))
        elif format_value.content.lower() == '2':
            await ctx.send(f'```{choice(environment_list)}```')
        else:
            await ctx.send('''```Такого формата не существует, напишите voice/text```''')
            return
    elif category_value.content == '3':
        if language == 'ru':
            await ctx.send('''```Вы выбрали категорию `экология`\nВ каком формате Вы хотите получить сообщение(1 - voice/2 - text)?```''')
        else:
            await ctx.send('''```You have selected the `ecology` category\nIn what format would you like to receive the message (1- voice/2 - text)?```''')
        format_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        ecology_list = ecology_language(language)
        if format_value.content.lower() == '1':
            tts = text_to_speech(choice(ecology_list), language=language)
            tts.save('voices/voice-ecology.mp3')

            await ctx.send(file=discord.File('voices/voice-ecology.mp3'))
        elif format_value.content.lower() == '2':
            await ctx.send(f'```{choice(ecology_list)}```')
        else:
            if language == 'ru':
                await ctx.send('''```Такого формата не существует, напишите voice/text```''')
            else:
                await ctx.send('''```This format does not exist, send voice/text```''')
            return
    elif category_value.content == '4':
        if language == 'ru':
            await ctx.send('''```Вы выбрали категорию `общее`\nВ каком формате Вы хотите получить сообщение(1 - voice/2 - text)?```''')
        else:
            await ctx.send('''```You have selected the `general` category\nIn what format would you like to receive the message (1 - voice/2 - text)?```''')
        format_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        common_tips = common_language(language)
        if format_value.content.lower() == '1':
            tts = text_to_speech(choice(common_tips), language=language)
            tts.save('voices/voice-common.mp3')

            await ctx.send(file=discord.File('voices/voice-common.mp3'))
        elif format_value.content.lower() == '2':
            await ctx.send(f'```{choice(common_tips)}```')
        else:
            if language == 'ru':
                await ctx.send('''```Такого формата не существует, напишите voice/text```''')
            else:
                await ctx.send('''```This format does not exist, send voice/text```''')
            return
    else:
        if language == 'ru':
            await ctx.send('''```Такой категории не существует```''')
        else:
            await ctx.send('''```No such category exists```''')
        return


@bot.command()
async def record(ctx, *text):
    global language
    if not text:
        if language == 'ru':
            await ctx.send('''```Напишите команду $record и через пробел укажите текст, который потребуется для преобразования в голосовое сообщение```''')
        else:
            await ctx.send('''```Send the command $record and, separated by a space, specify the text that will be needed to convert it into a voice message```''')
        return
    if language == 'ru':
        await ctx.send('''```В каком формате Вы хотите получить сообщение(1 - voice/2 - text)?```''')
    else:
        await ctx.send('''```In what format would you like to receive the message (1 - voice/2 - text)?```''')
    format_value = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if format_value.content.lower() == '1':
        text_to_speech = ' '.join(text)
        tts = gTTS(text_to_speech, lang=language)
        tts.save('voices/voice.mp3')

        await ctx.send(file=discord.File('voices/voice.mp3'))
    elif format_value.content.lower() == '2':
        string = ' '.join(text)
        await ctx.send(f'```diff\n- {string}```')
    else:
        if language == 'ru':
            await ctx.send('''```Такого формата не существует, напишите voice/text```''')
        else:
            await ctx.send('''```This format does not exist, send voice/text```''')
        return


bot.run(bot_token)
