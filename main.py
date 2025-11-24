
import ollama_conf as oc
import open_file as of
import pyttsx3
import threading
import os 


# Warna pakai ANSI escape code
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


tts_enabled = False
# Fungsi untuk membacakan teks dengan suara
def speak(text):
     def run():
          engine = pyttsx3.init()
          engine.setProperty('rate', 175)
          engine.setProperty('volume', 1.0)
          engine.say(text)
          engine.runAndWait()
          engine.stop()

     # Membuat thread baru untuk menjalankan fungsi speak
     threading.Thread(target=run, daemon=True).start()

#memastikan nama file adalah main.py
if __name__ == "__main__":
     text = r"""
     _________ __            .___.__   _____          __          
     /   _____//  |_ __ __  __| _/|__| /     \ _____ _/  |_  ____  
     \_____  \\   __\  |  \/ __ | |  |/  \ /  \\__  \\   __\/ __ \ 
     /        \|  | |  |  / /_/ | |  /    Y    \/ __ \|  | \  ___/ 
    /_______  /|__| |____/\____ | |__\____|__  (____  /__|  \___ >
          \/                 \/            \/     \/          \/ 
     """
     print(BLUE + text + RESET)
     print("[1] Chat AI", "[2] AI File Reader", "[3] Exit", sep=" " * 10)
     

     while True:
          user_input = input("Pilih opsi (1/2/3): " + RESET).strip()
     
          if user_input == "1":
               print( RED +"\n [ Catatan: Jawaban AI bisa saja kurang akurat‼️ ] \n" + RESET)
               tts_choice = input("Aktifkan suara asisten? (y/n): ").strip().lower()
               if tts_choice == "y":
                    tts_enabled = True
                    print(GREEN + "\n 🔊 Suara asisten diaktifkan!\n" + RESET)
               else:
                    print(BLUE + "\n 🔇 Suara asisten dimatikan.\n" + RESET)

               while True:
                    message = input("You 😏: ").strip()
                    if message.lower() == "exit":
                         print(GREEN + "Kembali ke menu utama...\n" + RESET)
                         tts_enabled = False
                         break

                    indent = " " * 3
                    ai_reply = oc.get_ai_response(message, tts_enabled)
                    print(indent, "Hayabusa 🤖: ", end="")
                    oc.type_effect(ai_reply, delay=0.015)
                    
                    if tts_enabled is True:
                         speak(ai_reply)
               

     
          elif user_input == "2":
               tts_choice = input("Aktifkan suara asisten? (y/n): ").strip().lower()
               if tts_choice == "y":
                    tts_enabled = True
                    print(GREEN + "\n 🔊 Suara asisten diaktifkan!\n" + RESET)
               else:
                    print(BLUE + "\n 🔇 Suara asisten dimatikan.\n" + RESET)

               print(BLUE + "\nMODE BACA FILE + KESIMPULAN AI\n" + RESET)

               filename = input("Nama file di folder ./read-file/: ").strip()
               full_path = os.path.join("./read-file", filename)

               if not os.path.exists(full_path):
                    print(RED + "File tidak ditemukan!\n" + RESET)
                    continue

               try:
                    file_content = of.load_file(filename)
                    print(GREEN + "File berhasil dibaca!\n" + RESET)
               except Exception as e:
                    print(RED + f"Gagal membaca file: {e}\n" + RESET)
                    continue

               print("Mengirim isi file ke AI...\n")

               read_prompt =  "Isi file:\n" + file_content
          
               ai_reply = oc.get_ai_response(read_prompt, tts_enabled)

               print(BLUE + "\n=== Hasil Analisis AI ===\n" + RESET)
               oc.type_effect(ai_reply, delay=0.015)

               if tts_enabled is True:
                    speak(ai_reply)

               print("\n" + GREEN + "Selesai! Kembali ke menu utama.\n" + RESET)
               tts_enabled = False

          #keluar program
          elif user_input == "3":
               print(GREEN + "\n Terima kasih telah menggunakan program ini. Sampai jumpa! \n" + RESET)
               break
          else:
               print(RED + "\n Opsi tidak valid. Silakan pilih 1, 2, atau 3. \n" + RESET)