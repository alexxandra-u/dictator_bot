# dictator_bot

# !КОД ЛЕЖИТ В ВЕТКЕ MASTER #

Телеграм бот, предназначенный для использования в чате, который умеет
1) Делать пользователя админом
2) Блокировать (на 1 минуту) и разблокировать пользователя
3) Публиковать статистику по чату (сколько в чате пользователей и сколько админов)
4) Покидать чат

Также при входе в чат новых пользователей, он задает им приветственный вопрос.

Чтобы выполнить команду, нужно написать в чат
dictator имя_комманды [аргументы]

Для каждой из 4 комманд выше:
1) dictator make_admin @username
2) dictator ban @username    или dictator unban @username
3) dictator stats
4) dictator leave

Чтобы начать пользоваться ботам пользователю нужно прожать команду /start_dict_bot
Чтобы получить информацию о работе бота нужно нажать /help

database.txt - пустой файл, но в него будут добаляться ники и id-шники пользователей по мере того, как они будут нажимать /start_dict_bot
