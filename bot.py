
import discord

client = discord.Client()

rokuji = 32, 42, 57, 12, 19, 27

sitiji = 12, 19, 27, 37, 47, 2, 17, 32

hatiji = 2, 17, 32, 44, 47, 7, 27, 47

kuji = 7, 27, 47, 7, 27, 47
# juuji

juuitiji = 7, 27, 47, 7, 19, 27

juuniji = 7, 19, 27, 47, 7, 27, 47

juusanji = 7, 27, 47, 2, 17, 32

juuyoji = 2, 17, 32, 47, 57, 12, 27, 42

juugoji = 12, 27, 42, 57, 12, 19, 27

juurokuji = 12, 19, 27, 42, 57, 12, 19, 27

jusitiji = 12, 19, 42, 57, 12, 19, 32

juhatiji = 12, 19, 32, 47, 17, 47, 17

jukuji = 17, 47, 17, 47, 17

nijuuji = 17, 47, 17, 32, 42

nijuuitiji = 17, 32, 42, 57

jikann = ('6:', '7:', '8:', '9:', '10:', '11:', '12:', '13:', '14:', '15:', '16:', '17:', '18:', '19:', '20:', '21:')

# ! /usr/bin/env python
# coding: UTF-8

import datetime

now = datetime.datetime.now()

a = 0



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    if message.content.startswith("//バス"):
        if client.user != message.author:
            # メッセージを書きます
            m = now
            if now.hour == 6 and rokuji[a] > now.minute:
                me = (rokuji[a], rokuji[a + 1], rokuji[a + 2])

            elif now.hour == 6 and rokuji[a] < now.minute < rokuji[a + 1]:
                me = (rokuji[a + 1], rokuji[a + 2], rokuji[a + 3])

            elif now.hour == 6 and rokuji[a + 1] < now.minute < rokuji[a + 2]:
                me = (rokuji[a + 2], rokuji[a + 3], rokuji[a + 4])

            elif now.hour == 6 and rokuji[a + 2] < now.minute < rokuji[a + 3]:
                me = (rokuji[a + 3], rokuji[a + 4], rokuji[a + 5])

            elif now.hour == 6 and rokuji[a + 3] < now.minute < rokuji[a + 4]:
                me = (rokuji[a + 4], rokuji[a + 5], rokuji[a + 6])

            elif now.hour == 7 and sitiji[a] > now.minute:
                me = (sitiji[a], sitiji[a + 1], sitiji[a + 2])

            elif now.hour == 7 and sitiji[a] < now.minute < sitiji[a + 1]:
                me = (sitiji[a + 1], sitiji[a + 2], sitiji[a + 3])

            elif now.hour == 7 and sitiji[a + 1] < now.minute < sitiji[a + 2]:
                me = (sitiji[a + 2], sitiji[a + 3], sitiji[a + 4])

            elif now.hour == 7 and sitiji[a + 2] < now.minute < sitiji[a + 3]:
                me = (sitiji[a + 3], sitiji[a + 4], sitiji[a + 5])

            elif now.hour == 7 and sitiji[a + 3] < now.minute < sitiji[a + 4]:
                me = (sitiji[a + 4], sitiji[a + 5], sitiji[a + 6])

            elif now.hour == 7 and sitiji[a + 4] < now.minute < sitiji[a + 5]:
                me = (sitiji[a + 5], sitiji[a + 6], sitiji[a + 7])

            elif now.hour == 8 and hatiji[a] > now.minute:
                me = (hatiji[a], hatiji[a + 1], hatiji[a + 2])

            elif now.hour == 8 and hatiji[a] < now.minute < hatiji[a + 1]:
                me = (hatiji[a + 1], hatiji[a + 2], hatiji[a + 3])

            elif now.hour == 8 and hatiji[a + 1] < now.minute < hatiji[a + 2]:
                me = (hatiji[a + 2], hatiji[a + 3], hatiji[a + 4])

            elif now.hour == 8 and hatiji[a + 2] < now.minute < hatiji[a + 3]:
                me = (hatiji[a + 3], hatiji[a + 4], hatiji[a + 5])

            elif now.hour == 8 and hatiji[a + 3] < now.minute < hatiji[a + 4]:
                me = (hatiji[a + 4], hatiji[a + 5], hatiji[a + 6])

            elif now.hour == 8 and hatiji[a + 4] < now.minute < hatiji[a + 5]:
                me = (hatiji[a + 5], hatiji[a + 6], hatiji[a + 7])

            elif now.hour == 9 and kuji[a] > now.minute:
                me = (kuji[a], kuji[a + 1], kuji[a + 2])

            elif now.hour == 9 and kuji[a] < now.minute < kuji[a + 1]:
                me = (kuji[a + 1], kuji[a + 2], kuji[a + 3])

            elif now.hour == 9 and kuji[a + 1] < now.minute < kuji[a + 2]:
                me = (kuji[a + 2], kuji[a + 3], kuji[a + 4])

            elif now.hour == 9 and kuji[a + 2] < now.minute < kuji[a + 3]:
                me = (kuji[a + 3], kuji[a + 4], kuji[a + 5])

            elif now.hour == 9 and kuji[a + 3] < now.minute < kuji[a + 4]:
                me = (kuji[a + 4], kuji[a + 5], kuji[a + 6])

            elif now.hour == 10 and kuji[a] > now.minute:
                me = (kuji[a], kuji[a + 1], kuji[a + 2])

            elif now.hour == 10 and kuji[a] < now.minute < kuji[a + 1]:
                me = (kuji[a + 1], kuji[a + 2], kuji[a + 3])

            elif now.hour == 10 and kuji[a + 1] < now.minute < kuji[a + 2]:
                me = (kuji[a + 2], kuji[a + 3], kuji[a + 4])

            elif now.hour == 10 and kuji[a + 2] < now.minute < kuji[a + 3]:
                me = (kuji[a + 3], kuji[a + 4], kuji[a + 5])

            elif now.hour == 10 and kuji[a + 3] < now.minute < kuji[a + 4]:
                me = (kuji[a + 4], kuji[a + 5], kuji[a + 6])

            elif now.hour == 11 and juuitiji[a] > now.minute:
                me = (juuitiji[a], juuitiji[a + 1], juuitiji[a + 2])

            elif now.hour == 11 and juuitiji[a] < now.minute < juuitiji[a + 1]:
                me = (juuitiji[a + 1], juuitiji[a + 2], juuitiji[a + 3])

            elif now.hour == 11 and juuitiji[a + 1] < now.minute < juuitiji[a + 2]:
                me = (juuitiji[a + 2], juuitiji[a + 3], juuitiji[a + 4])

            elif now.hour == 11 and juuitiji[a + 2] < now.minute < juuitiji[a + 3]:
                me = (juuitiji[a + 3], juuitiji[a + 4], juuitiji[a + 5])

            elif now.hour == 11 and juuitiji[a + 3] < now.minute < juuitiji[a + 4]:
                me = (juuitiji[a + 4], juuitiji[a + 5], juuitiji[a + 6])

            elif now.hour == 11 and juuitiji[a + 4] < now.minute < juuitiji[a + 5]:
                me = (juuitiji[a + 5], juuitiji[a + 6], juuitiji[a + 7])

            elif now.hour == 12 and juuniji[a] > now.minute:
                me = (juuniji[a], juuniji[a + 1], juuniji[a + 2])

            elif now.hour == 12 and juuniji[a] < now.minute < juuniji[a + 1]:
                me = (juuniji[a + 1], juuniji[a + 2], juuniji[a + 3])

            elif now.hour == 12 and juuniji[a + 1] < now.minute < juuniji[a + 2]:
                me = (juuniji[a + 2], juuniji[a + 3], juuniji[a + 4])

            elif now.hour == 12 and juuniji[a + 2] < now.minute < juuniji[a + 3]:
                me = (juuniji[a + 3], juuniji[a + 4], juuniji[a + 5])

            elif now.hour == 12 and juuniji[a + 3] < now.minute < juuniji[a + 4]:
                me = (juuniji[a + 4], juuniji[a + 5], juuniji[a + 6])

            elif now.hour == 12 and juuniji[a + 4] < now.minute < juuniji[a + 5]:
                me = (juuniji[a + 5], juuniji[a + 6], juuniji[a + 7])

            elif now.hour == 13 and juusanji[a] > now.minute:
                me = (juusanji[a], juusanji[a + 1], juusanji[a + 2])

            elif now.hour == 13 and juusanji[a] < now.minute < juusanji[a + 1]:
                me = (juusanji[a + 1], juusanji[a + 2], juusanji[a + 3])

            elif now.hour == 13 and juusanji[a + 1] < now.minute < juusanji[a + 2]:
                me = (juusanji[a + 2], juusanji[a + 3], juusanji[a + 4])

            elif now.hour == 13 and juusanji[a + 2] < now.minute < juusanji[a + 3]:
                me = (juusanji[a + 3], juusanji[a + 4], juusanji[a + 5])

            elif now.hour == 13 and juusanji[a + 3] < now.minute < juusanji[a + 4]:
                me = (juusanji[a + 4], juusanji[a + 5], juusanji[a + 6])

            elif now.hour == 14 and juuyoji[a] > now.minute:
                me = (juuyoji[a], juuyoji[a + 1], juuyoji[a + 2])

            elif now.hour == 14 and juuyoji[a] < now.minute < juuyoji[a + 1]:
                me = (juuyoji[a + 1], juuyoji[a + 2], juuyoji[a + 3])

            elif now.hour == 14 and juuyoji[a + 1] < now.minute < juuyoji[a + 2]:
                me = (juuyoji[a + 2], juuyoji[a + 3], juuyoji[a + 4])

            elif now.hour == 14 and juuyoji[a + 2] < now.minute < juuyoji[a + 3]:
                me = (juuyoji[a + 3], juuyoji[a + 4], juuyoji[a + 5])

            elif now.hour == 14 and juuyoji[a + 3] < now.minute < juuyoji[a + 4]:
                me = (juuyoji[a + 4], juuyoji[a + 5], juuyoji[a + 6])

            elif now.hour == 14 and juuyoji[a + 4] < now.minute < juuyoji[a + 5]:
                me = (juuyoji[a + 5], juuyoji[a + 6], juuyoji[a + 7])

            elif now.hour == 15 and juugoji[a] > now.minute:
                me = (juugoji[a], juugoji[a + 1], juugoji[a + 2])

            elif now.hour == 15 and juugoji[a] < now.minute < juugoji[a + 1]:
                me = (juugoji[a + 1], juugoji[a + 2], juugoji[a + 3])

            elif now.hour == 15 and juugoji[a + 1] < now.minute < juugoji[a + 2]:
                me = (juugoji[a + 2], juugoji[a + 3], juugoji[a + 4])

            elif now.hour == 15 and juugoji[a + 2] < now.minute < juugoji[a + 3]:
                me = (juugoji[a + 3], juugoji[a + 4], juugoji[a + 5])

            elif now.hour == 15 and juugoji[a + 3] < now.minute < juugoji[a + 4]:
                me = (juugoji[a + 4], juugoji[a + 5], juugoji[a + 6])

            elif now.hour == 16 and juurokuji[a] > now.minute:
                me = (juurokuji[a], juurokuji[a + 1], juurokuji[a + 2])

            elif now.hour == 16 and juurokuji[a] < now.minute < juurokuji[a + 1]:
                me = (juurokuji[a + 1], juurokuji[a + 2], juurokuji[a + 3])

            elif now.hour == 16 and juurokuji[a + 1] < now.minute < juurokuji[a + 2]:
                me = (juurokuji[a + 2], juurokuji[a + 3], juurokuji[a + 4])

            elif now.hour == 16 and juurokuji[a + 2] < now.minute < juurokuji[a + 3]:
                me = (sitiji[a + 3], sitiji[a + 4], sitiji[a + 5])

            elif now.hour == 16 and juurokuji[a + 3] < now.minute < juurokuji[a + 4]:
                me = (juurokuji[a + 4], juurokuji[a + 5], juurokuji[a + 6])

            elif now.hour == 16 and juurokuji[a + 4] < now.minute < juurokuji[a + 5]:
                me = (juurokuji[a + 5], juurokuji[a + 6], juurokuji[a + 7])

            elif now.hour == 17 and jusitiji[a] > now.minute:
                me = (jusitiji[a], jusitiji[a + 1], jusitiji[a + 2])

            elif now.hour == 17 and jusitiji[a] < now.minute < jusitiji[a + 1]:
                me = (jusitiji[a + 1], jusitiji[a + 2], jusitiji[a + 3])

            elif now.hour == 17 and jusitiji[a + 1] < now.minute < jusitiji[a + 2]:
                me = (jusitiji[a + 2], jusitiji[a + 3], jusitiji[a + 4])

            elif now.hour == 17 and jusitiji[a + 2] < now.minute < jusitiji[a + 3]:
                me = (jusitiji[a + 3], jusitiji[a + 4], jusitiji[a + 5])

            elif now.hour == 17 and jusitiji[a + 3] < now.minute < jusitiji[a + 4]:
                me = (jusitiji[a + 4], jusitiji[a + 5], jusitiji[a + 6])

            elif now.hour == 18 and juhatiji[a] > now.minute:
                me = (juhatiji[a], juhatiji[a + 1], juhatiji[a + 2])

            elif now.hour == 18 and juhatiji[a] < now.minute < juhatiji[a + 1]:
                me = (juhatiji[a + 1], juhatiji[a + 2], juhatiji[a + 3])

            elif now.hour == 18 and juhatiji[a + 1] < now.minute < juhatiji[a + 2]:
                me = (juhatiji[a + 2], juhatiji[a + 3], juhatiji[a + 4])

            elif now.hour == 18 and juhatiji[a + 2] < now.minute < juhatiji[a + 3]:
                me = (juhatiji[a + 3], juhatiji[a + 4], juhatiji[a + 5])

            elif now.hour == 18 and juhatiji[a + 3] < now.minute < juhatiji[a + 4]:
                me = (juhatiji[a + 4], juhatiji[a + 5], juhatiji[a + 6])

            elif now.hour == 19 and jukuji[a] > now.minute:
                me = (jukuji[a], jukuji[a + 1], jukuji[a + 2])

            elif now.hour == 19 and jukuji[a] < now.minute < jukuji[a + 1]:
                me = (jukuji[a + 1], jukuji[a + 2], jukuji[a + 3])

            elif now.hour == 19 and jukuji[a + 1] < now.minute < jukuji[a + 2]:
                me = (jukuji[a + 2], jukuji[a + 3], jukuji[a + 4])

            elif now.hour == 20 and nijuuji[a] > now.minute:
                me = (nijuuji[a], nijuuji[a + 1], nijuuji[a + 2])

            elif now.hour == 20 and nijuuji[a] < now.minute < nijuuji[a + 1]:
                me = (nijuuji[a + 1], nijuuji[a + 2], nijuuji[a + 3])

            elif now.hour == 20 and nijuuji[a + 1] < now.minute < nijuuji[a + 2]:
                me = (nijuuji[a + 2], nijuuji[a + 3], nijuuji[a + 4])

            elif now.hour == 21 and nijuuitiji[a] > now.minute:
                me = (nijuuitiji[a], nijuuitiji[a + 1], nijuuitiji[a + 2])

            elif now.hour == 21 and nijuuitiji[a] < now.minute < nijuuitiji[a + 1]:
                me = (nijuuitiji[a + 1], nijuuitiji[a + 2], nijuuitiji[a + 3])
            else:
                me = (nijuuitiji[a + 1], nijuuitiji[a + 2], nijuuitiji[a + 3])
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
            aw  message.channel.send(me)

    if message.content.startswith("//kosen"):
        await message.channel.send('http://www.nagaoka-ct.ac.jp/')
    if message.content.startswith("sirabas000"):
        await message.channel.send('https://syllabus.kosen-k.go.jp/Pages/PublicDepartments?school_id=16&year=2018')
    if message.content.startswith("810"):
        await message.channel.send('https://ja.wikipedia.org/wiki/810')
    if message.content.startswith("//1145141919810"):
        await message.channel.send('https://web.archive.org/web/20011007070049/www.gay.co.jp/VJ/label/bln/main/25.html')
    if message.content.startswith("//脱糞"):
        await message.channel.send('https://www.nicovideo.jp/watch/sm25579199')
    if message.content.startswith("//help"):
        await message.channel.send('【//バス】で最速で乗れるバスがわかります。19分、４４分と表示された場合、高専前発になり、その他は片貝入り口から乗ることができます。')
    if message.content.startswith("//porn.hub"):
        await message.channel.send('https://jp.pornhub.com/')

client.run('NjM0NzkxNjI4MzE3NjU1MDUw.XanrUw.-YiouXxcEUCDTcUP8k8esqcvW3M')
