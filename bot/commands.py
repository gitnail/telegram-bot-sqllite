def proceess_db_result(res):
    res = res.strip()
    if not res:
        res = "<empty_reply>"


def do_safe(func, message):
    try:
        func(message)
    except Exception as ex:
        bot.send_message(message.chat.id, "Error: '{}'".format(ex))


def execute(message):
    def action(message):
        client = SQLighter(DB_PATH)
        res = client.execute(message.text)
        proceess_db_result(res)
        bot.send_message(message.chat.id, res)

    do_safe(action, message)


def get_by_date(message):
    def action(message):
        date = datetime.datetime.strptime(message.text, "%Y-%M-%d")
        bot.send_message(message.chat.id, "Date format is correct")
    
    do_safe(action, message)
