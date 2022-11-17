import telebot
import datetime
from datetime import timedelta
from datetime import datetime

token = '5685006727:AAFEvW-0TfJcVAtOuccEYu7Ny_wmgEbQdv8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start_dict_bot'])
def start(message):
    user_id = str(message.from_user.id)
    username = '@' + message.from_user.username
    users_dict = {}
    f = open("database.txt", 'r+')
    for line in f.readlines():
        data = line.split(' ')
        users_dict[data[0]] = data[1]
    if username not in users_dict:
        f.write(username + ' ' + user_id + '\n')
    f.close()


@bot.message_handler(commands=['help'])
def help(message):
    help_message = "Привет! Я бот-диктатор и наведу порядок в этом чате!" + '\n' + " 1) dictator make_admin @username - сделать пользователя админом" + '\n' + "2) dictator ban @username - забанить пользователя" + '\n' + "3) dictator stats - увидеть статистику по чату" +'\n'+ "4) dictator leave - бот выйдет из чата"
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
    new_member_message = "Приветствую, " + str(message.json['new_chat_participant']['username']) + ' !' + '\n' + ' Вот тебе приветственный вопрос: кого ты больше любишь, маму или папу?'
    bot.reply_to(message, new_member_message)


@bot.message_handler(content_types=['text'])
def main(message):
    text = message.text.split(' ')
    print(text)
    if len(text) == 0:
        return
    if text[0] == 'dictator':
        if len(text) <= 1:
            bot.send_message(message.chat.id, "Ты не сказал что от меня хочешь...")
        elif text[1] == 'make_admin':
            make_admin(message)
        elif text[1] == 'ban':
            ban(message)
        elif text[1] == 'unban':
            unban(message)
        elif text[1] == 'stats':
            statistics(message)
        elif text[1] == 'leave':
            leave_chat(message)
        else:
            bot.send_message(message.chat.id, "Я такого не умею...")


def make_admin(message):
    text = message.text.split(' ')
    if len(text) < 2:
        bot.send_message(message.chat.id, "Ты не написал кого ты хочешь сделать админом...")
    else:
        users_dict = {}
        f = open("database.txt", 'r')
        for line in f.readlines():
            data = line.split(' ')
            users_dict[data[0]] = data[1].rstrip()
        name = text[2]
        if name not in users_dict:
            bot.send_message(message.chat.id, "Такого юзера нет в чате или он не пользуется ботом....")
        else:
            admins = bot.get_chat_administrators(chat_id=message.chat.id)
            flag = True
            for admin in admins:
                if name == '@' + admin.user.username:
                    bot.send_message(message.chat.id, "Этот пользователь и так админ!")
                    flag = False
                    break
            if flag:
                bot.promote_chat_member(chat_id=message.chat.id, user_id=int(users_dict[name]), can_delete_messages=True,
                                    can_restrict_members=True, can_invite_users=True, can_pin_messages=True,
                                    can_manage_video_chats=True, can_promote_members=True)
                bot.send_message(message.chat.id, "Поприветствуем нового админа " + name)


def ban(message):
    text = message.text.split(' ')
    if len(text) < 2:
        bot.send_message(message.chat.id, "Ты не написал кого ты хочешь заблокировать...")
    else:
        users_dict = {}
        f = open("database.txt", 'r')
        for line in f.readlines():
            data = line.split(' ')
            users_dict[data[0]] = data[1].rstrip()
        name = text[2]
        if name not in users_dict:
            bot.send_message(message.chat.id, "Такого юзера нет в чате или он не пользуется ботом....")
        else:
            admins = bot.get_chat_administrators(chat_id=message.chat.id)
            flag = True
            for admin in admins:
                if name == '@' + admin.user.username:
                    bot.send_message(message.chat.id, "Этот пользователь админ, его нельзя банить!")
                    flag = False
                    break
            if flag:
                bot.restrict_chat_member(chat_id=message.chat.id, user_id=int(users_dict[name]), until_date=datetime.now() + timedelta(minutes=2))
                bot.send_message(message.chat.id, "Кто о чем, а " + message.from_user.username + " о банах")


def unban(message):
    text = message.text.split(' ')
    if len(text) < 2:
        bot.send_message(message.chat.id, "Ты не написал кого ты хочешь разблокировать...")
    else:
        users_dict = {}
        f = open("database.txt", 'r')
        for line in f.readlines():
            data = line.split(' ')
            users_dict[data[0]] = data[1].rstrip()
        name = text[2]
        if name not in users_dict:
            bot.send_message(message.chat.id, "Такого юзера нет в чате или он не пользуется ботом....")
        else:
            admins = bot.get_chat_administrators(chat_id=message.chat.id)
            flag = True
            for admin in admins:
                if name == '@' + admin.user.username:
                    bot.send_message(message.chat.id, "Этот пользователь админ, тут ты беспомощен")
                    flag = False
                    break
            if flag:
                bot.unban_chat_member(chat_id=message.chat.id, user_id=int(users_dict[name]))
                bot.send_message(message.chat.id, "Разбанен")


def statistics(message):
    admins = bot.get_chat_administrators(chat_id=message.chat.id)
    for admin in admins:
        print(admin.user.username)
    users_num = bot.get_chat_member_count(chat_id=message.chat.id)
    bot.send_message(message.chat.id, "В этом чате " + str(users_num) + " участников и " + str(len(admins)) + " админа")


def leave_chat(message):
    bot.send_message(message.chat.id, "Ну раз вы меня не любите...")
    bot.leave_chat(chat_id=message.chat.id)


bot.polling(non_stop=True)
