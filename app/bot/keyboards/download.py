from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.keyboards.back import back_button
from app.bot.navigation import NavDownload, NavSupport


def platforms_keyboard() -> InlineKeyboardMarkup:
    """
    Generates a keyboard for selecting the platform to download the app.

    Returns:
        InlineKeyboardMarkup: Keyboard with platform selection options.
    """
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="🍏 IOS", callback_data=NavDownload.PLATFORM_IOS),
        InlineKeyboardButton(text="🤖 Android", callback_data=NavDownload.PLATFORM_ANDROID),
        InlineKeyboardButton(text="💻 Windows", callback_data=NavDownload.PLATFORM_WINDOWS),
    )

    builder.row(back_button(NavSupport.HOW_TO_CONNECT))
    return builder.as_markup()


def download_keyboard(platform: NavDownload, key: str) -> InlineKeyboardMarkup:
    """
    Generates a keyboard with download and connection options based on the selected platform.

    Arguments:
        platform (NavDownload): The selected platform for download.
        key (str): Unique identifier used in the connection URL.

    Returns:
        InlineKeyboardMarkup: Keyboard with download and connection buttons.
    """
    builder = InlineKeyboardBuilder()

    # v2raytun://import/ | hiddify://import/ #TODO: TinyUrl not work in Russia "https://tinyurl.com/bbpy5bx7/{key}" "https://tinyurl.com/5cea6ra4/{key}"
    if platform == NavDownload.PLATFORM_IOS:
        download = "https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532"
        connect = f"hiddify://import/{key}"
    elif platform == NavDownload.PLATFORM_ANDROID:
        download = "https://play.google.com/store/apps/details?id=app.hiddify.com"
        connect = f"hiddify://import/{key}"
    else:
        download = (
            "https://github.com/hiddify/hiddify-next/releases/download/"
            + "v2.5.7/Hiddify-Windows-Setup-x64.exe"
        )
        connect = f"hiddify://import/{key}"

    builder.row(
        InlineKeyboardButton(text=_("📥 Download"), url=download),
        InlineKeyboardButton(text=_("🔌 Connect"), url=connect),
    )

    builder.row(back_button(NavDownload.MAIN))
    return builder.as_markup()
