# handlers/callback_handlers.py

import csv
import io
from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext
from parser.iec_parser import parse_iec_page
from config import URLS, ELEMENTS

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    element = query.data

    output = io.StringIO()
    csv_writer = csv.writer(output)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if element == "parse_all":
        headers = ["URL"] + list(ELEMENTS.keys()) + ["Timestamp"]
        csv_writer.writerow(headers)
        for url in URLS:
            row = [url] + [parse_iec_page(url, elem) for elem in ELEMENTS.values()] + [timestamp]
            csv_writer.writerow(row)
        filename = 'parsed_all_elements.csv'
    else:
        csv_writer.writerow(["URL", element, "Timestamp"])
        for url in URLS:
            data = parse_iec_page(url, element)
            csv_writer.writerow([url, data, timestamp])
        filename = f'parsed_{element}.csv'

    output.seek(0)
    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=io.BytesIO(output.getvalue().encode('utf-8')),
        filename=filename
    )
    await query.edit_message_text(f"Парсинг элемента '{element}' завершен. CSV файл отправлен.")
