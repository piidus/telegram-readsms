from config import client
from telethon import events

# for reply sms
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

# client.start()
# client.run_until_disconnected()
async def send_sms(id):
    await client.send_message(id, 'This is for Testing Purpose! Please Ignore')
# with client:
#     client.loop.run_until_complete(send_sms())

@client.on(events.NewMessage)
async def handler(event):
    # Good
    # chat = await event.get_chat()
    # sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    text = event.raw_text
    # print('chat', chat, '\n', 
        #   'sender', sender, '\n',
    # print(sender)
    print('chat id', chat_id, '\n', 'sender_id', sender_id,'\n',
          'text ::', text)
client.start()
client.run_until_disconnected()



