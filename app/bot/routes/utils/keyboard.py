from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.navigation import NavMain


def close_notification_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text=_("💥 Close"),
            callback_data=NavMain.CLOSE_NOTIFICATION,
        )
    )

    return builder.as_markup()


def back_button(callback: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=_("◀️ Back"), callback_data=callback)


def back_keyboard(callback: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[back_button(callback)]])


def back_to_main_menu_button() -> InlineKeyboardButton:
    return InlineKeyboardButton(text=_("◀️ Back to main menu"), callback_data=NavMain.MAIN_MENU)


def back_to_main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[back_to_main_menu_button()]])


def cancel_button(callback: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=_("◀️ Cancel"), callback_data=callback)


def cancel_keyboard(callback: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[cancel_button(callback)]])
