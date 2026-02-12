import speech_recognition as sr
from pygame import mixer
import os
import re
import time
import winsound 

# Inisialisasi mixer
mixer.init()

# Path folder suara
FOLDER_SUARA = "rekaman/"

def play_audio(file_name):
    """Memutar audio dan memberikan feedback beep setelah selesai"""
    path_lengkap = os.path.join(FOLDER_SUARA, file_name)
    if os.path.exists(path_lengkap):
        print(f"Menjalankan Perintah: {file_name}")
        mixer.music.load(path_lengkap)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        
        # Jeda nafas agar tidak langsung feedback
        time.sleep(0.5)
        
        # BEEP HANYA BUNYI SETELAH PERINTAH SELESAI
        print("[Selesai - Memberikan feedback Beep]")
        winsound.Beep(1000, 500) 
    else:
        print(f"File {file_name} tidak ditemukan di folder {FOLDER_SUARA}")

def main():
    if not os.path.exists(FOLDER_SUARA):
        print(f"Error: Folder '{FOLDER_SUARA}' tidak ditemukan!")
        return

    # Inisialisasi Recognizer
    rec = sr.Recognizer()
    rec.energy_threshold = 400 # Sedikit tinggi agar tidak trigger suara nafas
    rec.dynamic_energy_threshold = True
    rec.pause_threshold = 0.5

    print("=== AI JONAS PHOTO: CONTINUOUS MONITORING (HENING) ===")

    # Menggunakan Microphone sebagai context manager agar tetap terbuka
    with sr.Microphone() as source:
        # Kalibrasi noise di awal sekali saja
        print("Menyesuaikan noise latar belakang... silakan diam sebentar.")
        rec.adjust_for_ambient_noise(source, duration=1.5)
        print("Sistem Standby. Silakan sebutkan perintah (Hai/Preset/Angka/Bye).")

        while True:
            try:
                # Mendengarkan tanpa timeout agar tidak error jika sepi
                # phrase_time_limit pendek agar respon cepat saat kata terdeteksi
                audio = rec.listen(source, phrase_time_limit=3)
                text = rec.recognize_google(audio, language='id-ID').lower()
                print(f"Terdeteksi suara: {text}")

                # 1. Logika Sapaan
                sapaan = ["halo", "hallo", "hai", "hi"]
                if any(word == text.strip() or word in text.split() for word in sapaan):
                    play_audio("hai.mp3")

                # 2. Logika Penutup
                elif any(word in text for word in ["bye", "goodbye", "dadah", "sampai jumpa"]):
                    play_audio("bye.mp3")

                # 3. Logika Preset (Jonas 1-20, Preset 1-20, Angka 1-20, atau 1-20 saja)
                else:
                    # Regex mencari angka 1-20
                    match = re.search(r'\b([1-9]|1[0-9]|20)\b', text)
                    if match:
                        angka = match.group(1)
                        # Memastikan kata kunci relevan atau hanya angka murni saja yang disebut
                        if any(k in text for k in ["jonas", "preset", "angka", "reset"]) or text.strip() == angka:
                            play_audio(f"{angka}.mp3")
                
            except sr.UnknownValueError:
                # Jika suara tidak jelas, abaikan saja (jangan beep, jangan respon)
                continue
            except sr.RequestError:
                print("Koneksi internet bermasalah.")
                time.sleep(2)
            except Exception as e:
                # Mengabaikan error lain agar sistem tidak mati
                continue

if __name__ == "__main__":
    main()