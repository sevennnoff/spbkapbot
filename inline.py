from aiogram.utils.keyboard import InlineKeyboardBuilder

def menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Информация о специальностях ℹ️", callback_data="info")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
def klass():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="9 класс", callback_data="9kl")
    keyboard_builder.button(text="11 класс", callback_data="11kl")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()