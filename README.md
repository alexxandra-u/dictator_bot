# dictator_bot

## you can see the code in master branch ##

Telegram bot, dedicated to control communication in telegram chats. It can
1) Make user an admin
2) Block and unblock users
3) Ask new chat members a welcome question
4) Publish chat statistics (number of users, admins etc)
5) Leave the chat



To execute the command, use such a notation:
dictator command_name [args]

Examples for the commands listed above:
1) dictator make_admin @username
2) dictator ban @username    or    dictator unban @username
3) - (automatically)
4) dictator stats
5) dictator leave

To start usage press /start_dict_bot
For additional info about the bot press /help

database.txt - empty file, but new users and their ids will be added during bot work
