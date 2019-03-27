import time
import vk_methods

connect = vk_methods.connect_to_server()
r3 = vk_methods.get_updates(connect[0], connect[1], connect[2])

while 1:
    sender = vk_methods.get_sender_id(r3.text)
    if sender:
        vk_methods.get_attachments(r3.text)
        name = vk_methods.get_sender_info(sender)['first_name']
        if name == 'Андрей':
            vk_methods.send_messages(sender, 'Привет, Андрей. Ну где ты был, ну обними меня скорей')
        else:
            vk_methods.send_messages(sender, "Привет, " + name, image='photo-179378864_456239017')

    ts = r3.json()['ts']
    time.sleep(10)
    r3 = vk_methods.get_updates(connect[0], ts, connect[2])


