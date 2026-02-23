import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я помогу тебе понять самые сильные экологические проблемы нашего мира!")

@bot.message_handler(commands=['ecology'])
def send_welcome(message):  
        bot.reply_to(message, "Вот топ самых ужасных проблем: 1.Глобальное потепление 2.Загрязнение воздуха 3.Загрязнение Мирового океана 4.Истощение природных ресурсов")

@bot.message_handler(commands=['ecology1'])
def send_welcome(message):  
        bot.reply_to(message, "Последствия глобального потепления:таяние ледников, повышение уровня моря, что приводит к затоплению прибрежных территорий и городов;егативные последствия для сельского хозяйства, особенно в тропических и субтропических регионах.")

@bot.message_handler(commands=['ecology2'])
def send_welcome(message):
        bot.reply_to(message, "Источники загрязнения воздуха:промышленные выбросы (фабрики и электростанции выделяют диоксид серы, оксиды азота и мелкие частицы);сжигание ископаемого топлива (при сжигании угля, нефти и природного газа образуются углекислый газ и диоксид серы).")

@bot.message_handler(commands=['ecology3'])
def send_welcome(message):
        bot.reply_to(message, "Виды загрязнения мирового океана:Пластиковое;Нефтяное;Тепловое")

@bot.message_handler(commands=['ecology4'])
def send_welcome(message):
        bot.reply_to(message, "Примеры истощения природных ресурсов:Истощение исчерпаемых невозобновляемых ресурсов — полезных ископаемых;Истощение биологических ресурсов — растительности и животного мира;Истощение почв — в районах интенсивного сельского хозяйства плодородие снижается быстро, почвы истощаются;Истощение рыбных запасов — возникает, когда количество выловленной рыбы превышает возможности её естественного восстановления и размножения.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)


bot.polling()
