import telebot  # https://pypi.org/project/pyTelegramBotAPI/
from telebot import types

bot = telebot.TeleBot('6198377914:AAEZ0MAf__3sdqqm8B-hujwaTH7QaNZi3AE')

print("hi")
def generate_start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    directions = types.KeyboardButton('О направлениях 📚')
    sign_up_for_classes = types.KeyboardButton('Записаться на занятие 📝')
    website = types.KeyboardButton('Наш сайт 🌐')
    markup.add(directions, sign_up_for_classes, website)
    return markup


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Классное фото, давай еще!')


@bot.message_handler(commands=['start'])
def start(message):
    markup = generate_start_markup()
    mess = f'Привет, <b>{message.from_user.first_name}</b>! Я твой йога-помощник, и я с радостью помогу тебе ' \
           f'подобрать подходящую именно для тебя практику и быстро записаться на нее.'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def messages(message):
    """"""
    get_message_bot = message.text

    if get_message_bot == 'О направлениях 📚':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton('Йога 🧘️'),
            types.KeyboardButton('Пилатес 🤸‍♀️'),
            types.KeyboardButton('Родительские практики 🤱'),
            types.KeyboardButton('Кинезитерапия ⛑'),
            types.KeyboardButton('Бодиролинг 💆‍♀️'),
            types.KeyboardButton('В начало 🔙')
        )
        final_message = "Выберите интересующее направление"
    elif get_message_bot == 'Йога 🧘️':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton('Хатха-Йога', callback_data='hatha_yoga'),
            types.InlineKeyboardButton('Йога Айенгара', callback_data='yoga_aengara'),
            types.InlineKeyboardButton('Универсальная Йога', callback_data='universal_yoga'),
            types.InlineKeyboardButton('Аштана-Йога', callback_data='ashtana_yoga'),
            types.InlineKeyboardButton('Йога-Нидра', callback_data='yoga_nidra'),
            types.InlineKeyboardButton('Виньяса-Йога', callback_data='viniysa_yoga'),
            types.InlineKeyboardButton('Йога в гамаках', callback_data='yoga_in_hammock'),
            types.InlineKeyboardButton('Йога для начинающих', callback_data='yoga_beginer'),
            types.InlineKeyboardButton('Йога в воздухе', callback_data='yoga_in_air')
        )
        final_message = "Выберите интересующее направление в разделе 'Йога'"
    elif get_message_bot == 'Родительские практики 🤱':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton('Йога для беременных', callback_data='yoga_pregnant'),
            types.InlineKeyboardButton('Бейби Йога', callback_data='baby_yoga'),
            types.InlineKeyboardButton('Йога для детей', callback_data='yoga_children'),
            types.InlineKeyboardButton('Коррекция осанки', callback_data='posture_correction'),
            types.InlineKeyboardButton('Snag-гольф', callback_data='snag_golf')
        )
        final_message = "Выберите интересующее направление в разделе 'Родительские практики'"
    elif get_message_bot in ['Бодиролинг 💆‍♀️', 'Пилатес 🤸‍♀️', 'Кинезитерапия ⛑']:
        final_message = f"{get_message_bot} - это ..."
        bot.send_message(message.chat.id, final_message, parse_mode='html')
        return
    elif get_message_bot == 'В начало 🔙':
        start(message)
        return
    elif get_message_bot == 'Наш сайт 🌐':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url='https://yogavtule.ru/'))
        final_message = 'Для перехода на наш сайт нажмите на кнопку ниже'
    elif get_message_bot == 'Записаться на занятие 📝':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Записаться",
                                              url='https://mobifitness.ru/schedule-widget/?vk&code=100931&type'
                                                  '=schedule&host=mobifitness.ru&version=v6&club=&language=#/schedule'))
        final_message = 'Для записи нажмите на кнопку ниже'
    else:
        final_message = '⬇️Пожалуйста, выберите из предложенных вариантов⬇️'
        bot.send_message(message.chat.id, final_message, parse_mode='html')
        return
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    responses = {
        'hatha_yoga': 'Хатха-Йога - это ...',
        'yoga_aengara': 'Йога Аенгара- это ...',
        'universal_yoga': 'Универсальная Йога - это ...',
        'ashtana_yoga': 'Аштана Йога - это ...',
        'yoga_nidra': 'Йога нидра- это ...',
        'viniysa_yoga': 'Виньяса Йога - это ...',
        'yoga_in_hammock': 'Йога в гамаках - это ...',
        'yoga_beginer': 'Йога для начинающих - это ...',
        'yoga_in_air': 'Йога в воздухе - это ...',
        'yoga_pregnant': 'Йога для беременных - это ...',
        'baby_yoga': 'Бейби Йога - это ...',
        'yoga_children': 'Йога для детей - это ...',
        'posture_correction': 'Коррекция осанки - это ...',
        'snag_golf': 'Snag-гольф - это ...',
    }
    response = responses.get(call.data)
    if response:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=response)

print("hi2")
bot.polling(none_stop=True)