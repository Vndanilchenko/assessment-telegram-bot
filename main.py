import telebot
import logging
import os

# импортируем токены
try:
    token = os.environ['TOKEN-HomeCreditAssessmentBot']
except:
    from private.token import token

# импортируем id админа
try:
    token = os.environ['TG_ADMIN_ID']
except:
    from private.token import admin_id

bot = telebot.TeleBot(token=token)

# добавим логирование
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

############################################ тексты для логики ############################################

REPLY_START = 'Привет, рад приветствовать тебя и готов помочь в поиске ответа на вопросы по оценочной процедуре \n' \
              '/startfaq - получить консультацию \n' \
              '/whatyoucando - узнать о функционале бота \n' \
              '/stop - завершить работу с ботом \n'


REPLY_WHOIS = 'я могу выполнить ответить по заранее подготовленным вопросам, если согласен принять участие, жми /startfaq'

REPLY_POLL = 'тут будет опрос'

REPLY_TEXT = 'пока могу отвечать только на выбранные из списка варианты или введи /start'
REPLY_DOC = 'пока не могу обрабатывать документы, выбери вариант из списка'
REPLY_AUDIO = 'пока не могу обрабатывать аудио, выбери вариант из списка'
REPLY_STOP = 'надеюсь вы получили получили ответ на свой вопрос, если нет, то обратитесь в <ОТДЕЛ>. '

############################################ тексты ответов на вопросы ############################################

REPLY1 = 'Сотрудники категорий M, D, N, RN, DR, SM, MV, GR, S, SR, AH, PA, TP, TD, NV, EC, UD, NC, SB, ST, NS, NZ, IP, BR, NB, SF, RB, RP, MB, HA, MO, HK, OD, DI, MK, NP, RD, принятые до 1 октября 2021 года, участвуют в годовой оценке деятельности.'
REPLY2 = 'Ты можешь проверить свою категорию в <Личном кабинете> на Портале обучения.'
REPLY3 = 'Сотрудники категорий M, D, N, RN, DR, SM, MV, GR проходят оценку в системе Aspire.\nСотрудники категорий S, SR, AH, PA, TP, TD, NV, EC, UD, NC, SB, ST, NS, NZ, IP, BR, NB, SF, RB, RP, MB, HA, MO, HK, OD, DI, MK, NP, RD, проходят оценку на Портале обучения.'
REPLY4 = 'Проверь, пожалуйста, какой браузер ты используешь. Мы рекомендуем использовать Google Chrome. И убедись, что верно выбрал кнопку для входа - Login for Russia.'
REPLY5 = 'Оценка проходит в двух системах: Aspire и на Портале обучения. В зависимости от категорий сотрудников в твоей команде они будут отражены в одной из систем.'
REPLY6 = 'Подобная ошибка часто появляется, если в браузере выбрана функция автоматического перевода с английского языка. Отключи данную функцию и попробуй внести комментарии еще раз.'
REPLY7 = 'Да, необходимо заполнить. В функциональных компетенциям мы фиксируем профессиональные знания и навыки, которые на данный момент нужно освоить/усилить для решения поставленных целей.'
REPLY8 = 'Необходимо описать конкретные ситуации за оцениваемый период, в которых проявились поведенческие проявления компетенций сотрудника. Рекомендуем использовать гид по компетенциям, который доступен для скачивания по <ссылке>.'
REPLY9 = 'Чтобы завершить оценку необходимо нажать кнопку «Отправить на калибровку». После этого бланк недоступен для корректировок, но сотруднику результаты еще не видны.'
REPLY10 = 'Результаты оценки будут доступны сотрудникам после их централизованной публикации.'

############################################ ЛОГИКА ############################################

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('узнать функционал', 'получить консультацию')

# приветственное сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, REPLY_START, reply_markup=keyboard1)

# приветственное сообщение
@bot.message_handler(commands=['stop'])
def stop_message(message):
    bot.send_message(message.chat.id, REPLY_STOP)
    # bot.stop_polling()

# узнать о функционале бота
@bot.message_handler(commands=['whatyoucando'])
def whatyoucando(message):
    bot.send_message(message.chat.id, REPLY_WHOIS, reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in ['узнать функционал', 'функционал', 'whatyoucando', '/whatyoucando']:
        bot.send_message(message.chat.id, REPLY_WHOIS, reply_markup=keyboard1)
    elif message.text in ['получить консультацию', 'консультация', 'startfaq', '/startfaq']:
        startfaq(message)
    elif message.text in ['остановить бота', 'stop', '/stop']:
        bot.send_message(message.chat.id, REPLY_STOP)
    elif message.text in ['старт', 'start', '/start']:
        bot.send_message(message.chat.id, REPLY_START, reply_markup=keyboard1)
    elif message.text == 'Участвую ли я в оценке деятельности?':
        bot.send_message(message.chat.id, f'{REPLY1}');
    elif message.text == 'Какая у меня категория?':
        bot.send_message(message.chat.id, f'{REPLY2}');
    elif message.text == 'Где я прохожу оценку?':
        bot.send_message(message.chat.id, f'{REPLY3}');
    elif message.text == 'При переходе по ссылке Aspire не могу зайти в личный кабинет, появляется ошибка.':
        bot.send_message(message.chat.id, f'{REPLY4}');
    elif message.text == 'Почему в системе я вижу не всю свою команду?':
        bot.send_message(message.chat.id, f'{REPLY5}');
    elif message.text == 'Нет возможности внести комментарии по Целям и/или Компетенциям в Aspire.':
        bot.send_message(message.chat.id, f'{REPLY6}');
    elif message.text == 'Нужно ли заполнять функциональные компетенции? Что в них писать?':
        bot.send_message(message.chat.id, f'{REPLY7}');
    elif message.text == 'Что писать в комментариях к компетенциям?':
        bot.send_message(message.chat.id, f'{REPLY8}');
    elif message.text == 'Раньше нельзя было нажимать кнопку «Публиковать» в Aspire, а сейчас что делать?':
        bot.send_message(message.chat.id, f'{REPLY9}');
    elif message.text == 'Руководитель завершил мою оценку, но комментарии не доступны для просмотра.':
        bot.send_message(message.chat.id, f'{REPLY10}');
    else:
        bot.send_message(message.chat.id, REPLY_TEXT)


@bot.message_handler(content_types=['document'])
def get_text_messages(message):
    bot.send_message(message.chat.id, REPLY_DOC)

@bot.message_handler(content_types=['audio'])
def get_text_messages(message):
    bot.send_message(message.chat.id, REPLY_AUDIO)



def check_user_data(message):
    # global username, first_name, last_name

    username = message.from_user['username']
    first_name = message.from_user['first_name']
    last_name = message.from_user['last_name']
    return username, first_name, last_name

# вопросы
@bot.message_handler(commands=['startfaq'])
def startfaq(message):
    # bot.send_message(message.chat.id, REPLY_WHOIS)
    # username, first_name, last_name = check_user_data(message)

    question = 'выберите вопрос из списка:';

    ########################################### INLINE KEYBOARD ###########################################
    # keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
    # key_1 = telebot.types.InlineKeyboardButton(text='Участвую ли я в оценке деятельности?', callback_data='1');
    # keyboard.add(key_1);  # добавляем кнопку в клавиатуру
    # key_2 = telebot.types.InlineKeyboardButton(text='Какая у меня категория?', callback_data='2');
    # keyboard.add(key_2);
    # key_3 = telebot.types.InlineKeyboardButton(text='Где я прохожу оценку?', callback_data='3');
    # keyboard.add(key_3);
    # key_4 = telebot.types.KeyboardButton(text='При переходе по ссылке Aspire не могу зайти\n в личный кабинет, появляется ошибка.', );
    # # key_4 = telebot.types.InlineKeyboardButton(text='При переходе по ссылке Aspire не могу зайти\n в личный кабинет, появляется ошибка.', callback_data='4');
    # keyboard.add(key_4);
    # # # несколько кнопок в одну строку
    # # key_4_1 = telebot.types.InlineKeyboardButton(text='При переходе по ссылке Aspire не могу зайти', callback_data='4');
    # # key_4_2 = telebot.types.InlineKeyboardButton(text='в личный кабинет, появляется ошибка.', callback_data='4');
    # # keyboard.add(key_4_1, key_4_2);
    # key_5 = telebot.types.InlineKeyboardButton(text='Почему в системе я вижу не всю свою команду?', callback_data='5');
    # keyboard.add(key_5);
    # key_6 = telebot.types.InlineKeyboardButton(text='Нет возможности внести комментарии по Целям \nи/или Компетенциям в Aspire.', callback_data='6');
    # keyboard.add(key_6);
    # key_7 = telebot.types.InlineKeyboardButton(text='Нужно ли заполнять функциональные компетенции?\n Что в них писать?', callback_data='7');
    # keyboard.add(key_7);
    # key_8 = telebot.types.InlineKeyboardButton(text='Что писать в комментариях к компетенциям?', callback_data='8');
    # keyboard.add(key_8);
    # key_9 = telebot.types.InlineKeyboardButton(text='Раньше нельзя было нажимать кнопку «Публиковать»\n в Aspire, а сейчас что делать?', callback_data='9');
    # keyboard.add(key_9);
    # key_10 = telebot.types.InlineKeyboardButton(text='Руководитель завершил мою оценку, но комментарии\n не доступны для просмотра.', callback_data='10');
    # keyboard.add(key_10);

    ########################################### END ###########################################

    ########################################### REPLY KEYBOARD ###########################################
    keyboard = telebot.types.ReplyKeyboardMarkup()
    key_1 = telebot.types.KeyboardButton(text='Участвую ли я в оценке деятельности?');
    keyboard.add(key_1);  # добавляем кнопку в клавиатуру
    key_2 = telebot.types.KeyboardButton(text='Какая у меня категория?');
    keyboard.add(key_2);
    key_3 = telebot.types.KeyboardButton(text='Где я прохожу оценку?');
    keyboard.add(key_3);
    key_4 = telebot.types.KeyboardButton(text='При переходе по ссылке Aspire не могу зайти в личный кабинет, появляется ошибка.');
    keyboard.add(key_4);
    key_5 = telebot.types.KeyboardButton(text='Почему в системе я вижу не всю свою команду?');
    keyboard.add(key_5);
    key_6 = telebot.types.KeyboardButton(text='Нет возможности внести комментарии по Целям и/или Компетенциям в Aspire.');
    keyboard.add(key_6);
    key_7 = telebot.types.KeyboardButton(text='Нужно ли заполнять функциональные компетенции? Что в них писать?');
    keyboard.add(key_7);
    key_8 = telebot.types.KeyboardButton(text='Что писать в комментариях к компетенциям?');
    keyboard.add(key_8);
    key_9 = telebot.types.KeyboardButton(text='Раньше нельзя было нажимать кнопку «Публиковать» в Aspire, а сейчас что делать?');
    keyboard.add(key_9);
    key_10 = telebot.types.KeyboardButton(text='Руководитель завершил мою оценку, но комментарии не доступны для просмотра.');
    keyboard.add(key_10);

    ########################################### END ###########################################


    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # bot.register_next_step_handler(message, second_question)

# обработка ответов
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # сделаем отдельную обработку на каждый блок вопросов
    # call.data это callback_data, которую мы указали при объявлении кнопки
    print(call.data)
    if call.data[0]=='1':
        response_1 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_1}\n'+REPLY1);
    elif call.data[0]=='2':
        response_2 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_2}\n'+REPLY2);
    elif call.data[0] == '3':
        response_3 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_3}\n'+REPLY3);
    elif call.data[0]=='4':
        response_4 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_4}\n'+REPLY4);
    elif call.data[0]=='5':
        response_5 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_5}\n'+REPLY5);
    elif call.data[0]=='6':
        response_6 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_6}\n'+REPLY6);
    elif call.data[0]=='7':
        response_7 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_7}\n'+REPLY7);
    elif call.data[0]=='8':
        response_8 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_8}\n'+REPLY8);
    elif call.data[0]=='9':
        response_9 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_9}\n'+REPLY9);
    elif call.data[0]=='10':
        response_10 = call.data
        bot.send_message(call.message.chat.id, f'Вы выбрали: {response_10}\n'+REPLY10);



############################################ запуск бота ############################################
bot.polling(none_stop=True, interval=0)
