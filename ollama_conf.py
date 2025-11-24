import ollama
import sys
import time


 # prompt = (
    #     "Kamu adalah Hayabusa. Jawab dalam Bahasa Indonesia secara singkat, jelas, "
    #     "dan langsung ke inti. Jangan gunakan narasi seperti *diam sejenak* atau "
    #     "deskripsi tindakan. Emoji boleh digunakan seperlunya."
    #     "Hindari format markdown seperti tanda bintang atau bold."
    # )


# memory maksimal 3
chat_memory = []


def get_ai_response(user_input, isvoice=False):
    model_name = "gemma3:1b"

    if isvoice:
        prompt = (
            "Your name is Siri, your friendly and helpful AI assistant."
            "Answer in a simple and formal style."
            "No emojis, no special characters, no markdown."
            "Use neutral and clear English."
            "No jokes, no slang."
            "Answers should be concise, clear, and easy for TextToSpeech to read."
        )
    else:
        prompt = (
            "Namamu Siri, asisten AI yang ramah dan membantu. "
            "Gunakan Bahasa Indonesia yang santai, ramah, dan mudah dimengerti. "
            "Berikan penjelasan yang jelas dan membantu, tetapi tetap hangat dan tidak kaku. "
            "Boleh bercanda ringan seperlunya, tapi tetap fokus pada inti jawaban. "
            "Jangan gunakan format markdown seperti tanda bintang atau bold. "
            "Jangan terlalu formal seperti buku teks; lebih seperti mentor yang baik dan teman ngobrol. "
            "Gunakan emoji seperlunya untuk memberi nuansa ceria, tapi jangan berlebihan."
        )


    # siapkan messages
    messages = [{"role": "system", "content": prompt}]

    # hanya kirim *3 memory terakhir*
    for item in chat_memory[-3:]:
        messages.append({"role": "user", "content": item["user"]})
        messages.append({"role": "assistant", "content": item["bot"]})

    # pesan baru user
    messages.append({"role": "user", "content": user_input})

    # panggil model
    response = ollama.chat(model=model_name, messages=messages)

    if "message" in response and "content" in response["message"]:
        bot_reply = response["message"]["content"].strip()
    else:
        bot_reply = "Tidak ada respons dari model."

    # simpan memory maksimal 3 item
    chat_memory.append({"user": user_input, "bot": bot_reply})
    if len(chat_memory) > 3:
        chat_memory.pop(0)

    return bot_reply


#fungsi type effect
def type_effect(text, delay=0.05):
    
    # menulis karakter ke stdout satu per satu
    for char in text:
        #menulis karakter ke layar satu per satu
        sys.stdout.write(char)
        # kirim langsung ke layar
        sys.stdout.flush()
        #progres mati selama 0.05 detik
        time.sleep(delay)
    #buat baris baru setelah selesai mengetik
    print()  


