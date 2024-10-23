import os
import telebot
import speech_recognition
from pydub import AudioSegment
from PIL import Image, ImageEnhance, ImageFilter
from telebot.apihelper import send_message

# ↓↓↓ Ниже нужно вставить токен, который дал BotFather при регистрации
# Пример: token = '2007628239:AAEF4ZVqLiRKG7j49EC4vaRwXjJ6DN6xng8'
token = '7921587804:AAF0_qyr0YyEqZKUw6SzHFtOWLbuxuRIHWw'  # <<< Ваш токен

bot = telebot.TeleBot(token)


def transform_image(filename, brightness):
    # Функция обработки изображения
    source_image = Image.open(filename)
    enhancer = ImageEnhance.Brightness(source_image)
    # to reduce brightness by 50%, use factor 0.5
    source_image = enhancer.enhance(brightness / 100)
    source_image.save(filename)
    return filename

@bot.message_handler(content_types=['photo'])
def resend_photo(message):
    bot.send_message(message.from_user.id, "Brightness")
    # Функция отправки обработанного изображения
    file_id = message.photo[-1].file_id
    filename = download_file(bot, file_id)
    transform_image(filename, 50)
    # Трансформируем изображение



    image = open(filename, 'rb')
    bot.send_photo(message.chat.id, image)
    image.close()

    # Не забываем удалять ненужные изображения
    if os.path.exists(filename):
        os.remove(filename)


def oga2wav(filename):
    # Конвертация формата файлов
    new_filename = filename.replace('.oga', '.wav')
    audio = AudioSegment.from_file(filename)
    audio.export(new_filename, format='wav')
    return new_filename


def recognize_speech(oga_filename):
    # Перевод голоса в текст + удаление использованных файлов
    wav_filename = oga2wav(oga_filename)
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.WavFile(wav_filename) as source:
        wav_audio = recognizer.record(source)

    text = recognizer.recognize_google(wav_audio, language='ru')

    if os.path.exists(oga_filename):
        os.remove(oga_filename)

    if os.path.exists(wav_filename):
        os.remove(wav_filename)

    return text


def download_file(bot, file_id):
    # Скачивание файла, который прислал пользователь
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = file_id + file_info.file_path
    filename = filename.replace('/', '_')
    with open(filename, 'wb') as f:
        f.write(downloaded_file)
    return filename


@bot.message_handler(commands=['start'])
def say_hi(message):
    # Функция, отправляющая "Привет" в ответ на команду /start
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['voice'])
def transcript(message):
    # Функция, отправляющая текст в ответ на голосовое
    filename = download_file(bot, message.voice.file_id)
    text = recognize_speech(filename)
    bot.send_message(message.chat.id, text)


# Запускаем бота. Он будет работать до тех пор, пока работает ячейка (крутится значок слева).
# Остановим ячейку - остановится бот
bot.polling()
