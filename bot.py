from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8978724330:AAEZz4sq4woyrbdFB7bN04aluWgU9QV0DpU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "សួស្តី! 🤖 ខ្ញុំជា Bot គណនាបំណុល\n\n"
        "សូមផ្ញើទិន្នន័យតាមរូបមន្ត៖\n"
        "ប្រាក់ដើមនៅសល់, រយៈពេលនៅសល់\n\n"
        "ឧទាហរណ៍៖\n"
        "1000000, 24"
    )


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = update.message.text.split(",")

        principal = float(data[0].strip())  # ប្រាក់ដើមនៅសល់
        months = float(data[1].strip())     # រយៈពេលនៅសល់

        short_debt = (principal / months) * 12
        long_debt = principal - short_debt

        result = (
            "📊 លទ្ធផលគណនា\n\n"
            f"💰 ប្រាក់ដើមនៅសល់: {principal:,.0f}\n"
            f"⏳ រយៈពេលនៅសល់: {months:.0f} ខែ\n\n"
            f"🔹 បំណុលខ្លី: {short_debt:,.0f}\n"
            f"🔹 បំណុលវែង: {long_debt:,.0f}"
        )

        await update.message.reply_text(result)

    except:
        await update.message.reply_text(
            "❌ ទម្រង់មិនត្រឹមត្រូវ!\n\n"
            "សូមផ្ញើជា៖ ប្រាក់ដើមនៅសល់, រយៈពេលនៅសល់\n"
            "ឧ. 1000000,24"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

print("Bot Running...")
app.run_polling()
