from aiogram.utils.keyboard import InlineKeyboardBuilder
import parser

def menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Информация о специальностях ℹ️", callback_data="info")
    keyboard_builder.button(text="Часто задаваемые вопросы ❔", callback_data="faq")
    keyboard_builder.button(text="Консультация с ИИ ассистентом 🤖", callback_data="ai")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
def klass():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="9 классов", callback_data="9kl")
    keyboard_builder.button(text="11 классов", callback_data="11kl")
    keyboard_builder.button(text="Назад 🔙", callback_data="menu")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
def nineklass():
    keyboard_builder = InlineKeyboardBuilder()
    for i in range(len(parser.nkl)):
        if i != 6:
            keyboard_builder.button(text=(str(parser.nkl[i]).split(". "))[0], callback_data=f"n{i}")
    keyboard_builder.button(text="Назад 🔙", callback_data="info")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
def elevenklass():
    keyboard_builder = InlineKeyboardBuilder()
    for i in range(len(parser.ekl)):
        keyboard_builder.button(text=(str(parser.ekl[i]).split(". "))[0], callback_data=f"e{i}")
    keyboard_builder.button(text="Назад 🔙", callback_data="info")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
def faq():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Какие документы нужны для поступления?", callback_data="a1")
    keyboard_builder.button(text="Какие есть способы подачи документов для поступления?", callback_data="a2")
    keyboard_builder.button(text="По какому адресу находится приёмная комиссия?", callback_data="a3")
    keyboard_builder.button(text="Когда будут известны результаты зачисления?", callback_data="a4")
    keyboard_builder.button(text="Предоставляет ли Колледж общежитие? ", callback_data="a5")
    keyboard_builder.button(text="Какой минимальный проходной балл для поступления?", callback_data="a6")
    keyboard_builder.button(text="На какой площадке я буду обучаться? / По какому адресу проходит обучение?", callback_data="a7")
    keyboard_builder.button(text="Можно ли поступить в ВУЗ после Колледжа на льготных условиях? / Можно ли поступить в ВУЗ на бюджет после Вашего Колледжа?", callback_data="a8")
    keyboard_builder.button(text="Нужна ли для поступления временная регистрация?", callback_data="a9")
    keyboard_builder.button(text="Нужно ли сдавать вступительные испытания? Нужны ли результаты ЕГЭ/ОГЭ?", callback_data="a10")
    keyboard_builder.button(text="Имеет ли значение, когда подал документы?", callback_data="a11")
    keyboard_builder.button(text="Нужно ли заверять копии документов у нотариуса?", callback_data="a12")
    keyboard_builder.button(text="Последний день предоставления оригинала документа об образовании?", callback_data="a13")
    keyboard_builder.button(text="Предоставляется ли отсрочка от армии?", callback_data="a14")
    keyboard_builder.button(text="Возможен ли перевод из других колледжей?", callback_data="a15")
    keyboard_builder.button(text="Есть ли у вас льготные условия для поступления?", callback_data="a16")
    keyboard_builder.button(text="Назад 🔙", callback_data="menu")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
def tomenu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Назад 🔙", callback_data="menu")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

