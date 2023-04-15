from telebot import types

from config import TEXT


def return_found(session, search, found):
    message_text = 'Нашлись следующие ребята:\n'
    for i in found:
        message_text += TEXT.format(
            name=i.name,
            available=i.available,
            worktime=i.worktime,
            education=i.education,
            city=i.city,
            wants=i.wants,
            can_do=i.can_do,
            tg_nickname=i.tg_nickname,
        ) + '\n'

    session.delete(search)
    session.commit()

    return message_text


def add_to_btns(buttons, entity):
    for i in entity:
        buttons.append(types.KeyboardButton(i))
