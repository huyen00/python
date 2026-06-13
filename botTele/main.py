# main.py
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import shutil
import requests
# Bật logging để theo dõi lỗi
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)



# Hàm xử lý lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Chào bạn! Tôi là một bot được tạo bởi Hoàng Huyền xinh gái. Hãy nói tôi xinh, tôi sẽ trả lời các câu hỏi của bạn ><!")

# Hàm xử lý tin nhắn văn bản và phản hồi lại
async def echo(update, context):
    user_text = update.message.text
    try:
        result = eval(user_text)
        await context.bot.send_message(chat_id= update.effective_chat.id, text=f"Kết quả của {user_text} = {result}")
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=user_text)
# kiểm tra lệnh check_disk trên telegram, trả về thông tin dung lượng ổ đĩa
async def check_disk(update, context):
    path = 'C:\\'  # Thay đổi đường dẫn nếu bạn muốn kiểm tra ổ đĩa khác
    usage = shutil.disk_usage(path)
    total = usage.total /(1024**3)
    used = usage.used / (1024**3)
    remain = usage.free /(1024**3)
    message = (f"Thông tin dung lượng ổ đĩa:\n"
               f"Tổng dung lượng: {total:.2f} GB \n"
               f"Đã sử dụng: {used:.2f} GB\n"
               f"Còn lại: {remain:.2f} GB")
    await context.bot.send_message(chat_id = update.effective_chat.id, text=message)

# hàm kiểm tra ip của máy
import socket
async def check_ip(update, context):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    message = f"Địa chỉ IP của máy: {ip_address}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text = message)

# kiểm tra trang web có hoạt động không khi nhập /check_url URL-name

async def check_url(update, context):
    try:
        url = context.args[0] # lấy url từ đối số của lệnh context do người dùng nhập vào
        response = requests.get(url)
        if response.status_code ==200:
            message = f"Trang web {url} hoạt động bình thường với mã trạng thái {response.status_code}"
        else:
            message = f"Trang web {url} có vấn đề với mã trạng thái {response.status_code}"
    except:
        message = "Vui lòng nhập URL hợp lệ sau lệnh /check_url"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
def main():
    # Tạo đối tượng Application
    application = Application.builder().token(TOKEN).build()

    # Tạo các trình xử lý (handler) cho lệnh và tin nhắn
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    # tạo trình xử lý cho lệnh check_disk và tin nhắn
    check_disk_handler = CommandHandler('check_disk', check_disk)
    # tạo trình xử lý cho lệnh check_ip và tin nhắn
    check_ip_handler = CommandHandler('check_ip', check_ip)
    # tạo trình xử lý cho lệnh check_url và tin nhắn
    check_url_handler = CommandHandler('check_url', check_url)

    # Đăng ký các handler với application
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(check_disk_handler)
    application.add_handler(check_ip_handler)
    application.add_handler(check_url_handler)

    # Chạy bot cho đến khi bạn nhấn Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()