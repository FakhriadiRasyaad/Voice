import speech_recognition as sr
from pygame import mixer
import serial
import serial.tools.list_ports
import os
import re
import time
import winsound 

# Inisialisasi mixer
mixer.init()

# Path folder suara
FOLDER_SUARA = "rekaman/"

# Inisialisasi Serial Arduino
def init_arduino():
    """Mencari dan menginisialisasi koneksi Arduino"""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Arduino biasanya terdeteksi sebagai USB Serial
        if 'USB' in port.description or 'Arduino' in port.description:
            try:
                ser = serial.Serial(port.device, 9600, timeout=1)
                time.sleep(2)  # Tunggu Arduino reset
                print(f"Arduino terhubung di {port.device}")
                return ser
            except:
                continue
    
    # Jika tidak otomatis terdeteksi, coba manual
    try:
        # Ganti COM3 sesuai port Arduino Anda
        ser = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)
        print("Arduino terhubung di COM3")
        return ser
    except:
        print("PERINGATAN: Arduino tidak terdeteksi. Mode audio only.")
        return None

def send_to_arduino(arduino, command):
    """Mengirim perintah ke Arduino"""
    if arduino and arduino.is_open:
        try:
            arduino.write(command.encode())
            # Baca response dari Arduino
            time.sleep(0.1)
            if arduino.in_waiting > 0:
                response = arduino.readline().decode().strip()
                print(f"Arduino: {response}")
            return True
        except Exception as e:
            print(f"Error mengirim ke Arduino: {e}")
            return False
    return False

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

    # Inisialisasi Arduino
    arduino = init_arduino()

    # Inisialisasi Recognizer
    rec = sr.Recognizer()
    rec.energy_threshold = 400 
    rec.dynamic_energy_threshold = True
    rec.pause_threshold = 0.5

    print("=== AI JONAS PHOTO: CONTINUOUS MONITORING + ARDUINO CONTROL ===")
    print("Perintah suara:")
    print("- 'Hai/Halo' = Sapaan")
    print("- 'Jonas 1-10' / 'Preset 1-10' / 'Angka 1-10' = Aktifkan posisi servo")
    print("- 'Bye' = Penutup")

    with sr.Microphone() as source:
        print("Menyesuaikan noise latar belakang... silakan diam sebentar.")
        rec.adjust_for_ambient_noise(source, duration=1.5)
        print("Sistem Standby. Silakan sebutkan perintah.")

        while True:
            try:
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

                # 3. Logika Preset dengan Trigger Arduino
                else:
                    # Regex mencari angka 1-10 (sesuai preset Arduino)
                    match = re.search(r'\b([1-9]|10)\b', text)
                    if match:
                        angka = match.group(1)
                        # Memastikan kata kunci relevan atau hanya angka murni
                        if any(k in text for k in ["jonas", "preset", "angka", "reset"]) or text.strip() == angka:
                            # Putar audio
                            play_audio(f"{angka}.mp3")
                            
                            # Kirim ke Arduino
                            if angka == "10":
                                arduino_cmd = '0'  # Posisi 10 = karakter '0'
                            else:
                                arduino_cmd = angka  # Posisi 1-9 = karakter '1'-'9'
                            
                            if send_to_arduino(arduino, arduino_cmd):
                                print(f"✓ Servo digerakkan ke Posisi {angka}")
                            else:
                                print(f"✗ Gagal mengirim ke Arduino")
                
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("Koneksi internet bermasalah.")
                time.sleep(2)
            except KeyboardInterrupt:
                print("\nProgram dihentikan.")
                if arduino:
                    arduino.close()
                break
            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    main()