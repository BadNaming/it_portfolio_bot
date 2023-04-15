from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import telebot
from telebot import types

from config import (
    ABORT_TEXT,
    EXPERIENCE,
    NOT_FOUND,
    SEARCH_TEXT,
    SPECIALITIES,
    STEP1_TEXT,
    STEP2_TEXT,
    TOKEN,
    WELCOME_TEXT,
)
from models import Base, Participant, Search
from services import add_to_btns, return_found

TRIGGERS = SPECIALITIES + EXPERIENCE + [SEARCH_TEXT]

bot = telebot.TeleBot(TOKEN)

# engine = create_engine(
#     'postgresql+psycopg2://postgres:9415892mb)@db',
#     echo=False
# )
engine = create_engine('sqlite:///sqlite.db', echo=False)
Base.metadata.create_all(bind=engine)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(SEARCH_TEXT)
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        text=WELCOME_TEXT,
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def flow(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    if message.text in TRIGGERS:
        with Session(engine) as session:
            search = session.query(Search).filter_by(
                user=str(message.chat.id)
            ).first()
            if search:
                if search.spec is None:
                    message_text = STEP1_TEXT
                    if message.text in SPECIALITIES:
                        search.spec = message.text
                        session.add(search)
                        session.commit()
                        add_to_btns(buttons, EXPERIENCE)
                        message_text = STEP2_TEXT
                    else:
                        add_to_btns(buttons, SPECIALITIES)
                elif search.exp is None:
                    message_text = STEP2_TEXT
                    if message.text in EXPERIENCE:
                        search.exp = message.text
                        session.add(search)
                        session.commit()
                        found = session.query(Participant).filter_by(
                            spec=search.spec,
                            exp=search.exp,
                        ).all()
                        if found:
                            message_text = return_found(session, search, found)
                        else:
                            message_text = NOT_FOUND
                    else:
                        add_to_btns(buttons, EXPERIENCE)
                else:
                    found = session.query(Participant).filter_by(
                        spec=search.spec,
                        exp=search.exp,
                    ).all()
                    if found:
                        message_text = return_found(session, search, found)
                    else:
                        message_text = NOT_FOUND
            else:
                with Session(engine) as session:
                    user = Search(user=str(message.chat.id))
                    session.add(user)
                    session.commit()
                for spec in SPECIALITIES:
                    buttons.append(types.KeyboardButton(spec))
                message_text = STEP1_TEXT
        buttons.append(types.KeyboardButton(ABORT_TEXT))
        markup.add(*buttons)
        bot.send_message(
            message.chat.id,
            text=message_text,
            reply_markup=markup,
            parse_mode='HTML'
        )

    elif message.text == ABORT_TEXT:
        with Session(engine) as session:
            search = session.query(Search).filter_by(
                user=str(message.chat.id)
            ).first()
            if search:
                session.delete(search)
                session.commit()

        btn = types.KeyboardButton(SEARCH_TEXT)
        markup.add(btn)
        bot.send_message(
            message.chat.id,
            text=WELCOME_TEXT,
            reply_markup=markup
        )

    else:
        bot.send_message(message.chat.id, 'ЯННП, воспользуйтесь кнопками меню')


bot.polling(none_stop=True, interval=0)
