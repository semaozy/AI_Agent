import os
import datetime
from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Araçlarımızı ve hafıza dosyamızı tanımlayalım
beyin = OllamaLLM(model="llama3.2")
arama_motoru = DuckDuckGoSearchRun()
hafiza_dosyasi = "hafiza.txt"

def not_kaydet(metin):
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(hafiza_dosyasi, "a", encoding="utf-8") as f:
        f.write(f"[{zaman}] {metin}\n")
    return "Bilgiyi hafızama kaydettim."

def hafizayi_oku():
    if os.path.exists(hafiza_dosyasi):
        with open(hafiza_dosyasi, "r", encoding="utf-8") as f:
            return f.read()
    return "Henüz bir not alınmamış."

def ajani_baslat():
    print("\n--- AKILLI HAFIZALI ASİSTAN BAŞLATILDI ---")
    print("İpuçları:")
    print("- 'Not et: ...' derseniz bilgiyi saklarım.")
    print("- Normal sorularınızda önce hafızama, sonra internete bakarım.")
    print("- 'kapat' yazarak çıkabilirsiniz.")

    while True:
        soru = input("\nSiz: ")
        
        if soru.lower() == "kapat":
            break

        # DURUM 1: Not Kaydetme
        if soru.lower().startswith("not et:"):
            kayit_icerigi = soru[7:].strip()
            sonuc = not_kaydet(kayit_icerigi)
            print(f"Ajan: {sonuc}")
            continue

        # DURUM 2: Soru Cevaplama (Hafıza + İnternet)
        print("Ajan: Düşünüyorum...")
        mevcut_hafiza = hafizayi_oku()
        
        # Ajana hafızasını ve soruyu veriyoruz
        karar_propt = f"""
        Senin hafızanda şunlar yazılı:
        {mevcut_hafiza}
        
        Kullanıcı sana şunu sordu: "{soru}"
        
        Talimatlar:
        1. Eğer cevap hafızanda varsa doğrudan cevap ver.
        2. Eğer cevap hafızanda yoksa ve güncel bir bilgi gerekiyorsa sadece 'ARA' yaz.
        3. Eğer hafızanda yoksa ve genel bir bilgiyse kendi bilginle cevap ver.
        """
        
        karar = beyin.invoke(karar_propt).strip()

        if "ARA" in karar.upper():
            print("Ajan: Hafızamda bulamadım, internete bakıyorum...")
            arama_sonucu = arama_motoru.run(soru)
            final_cevap = beyin.invoke(f"Soru: {soru}\nİnternet Bilgisi: {arama_sonucu}\nCevabı Türkçe ver:")
            print(f"\nAjan: {final_cevap}")
        else:
            print(f"\nAjan: {karar}")

if __name__ == "__main__":
    ajani_baslat()