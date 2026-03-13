from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Adım: İnternette arama yapacak aracı tanımlıyoruz
arama_motoru = DuckDuckGoSearchRun()

# 2. Adım: Ollama üzerinden Llama 3.2 modelimizi çağırıyoruz
beyin = OllamaLLM(model="llama3.2")

def ajani_calistir():
    print("--- AI AJANI HAZIR (Çıkmak için 'kapat' yaz) ---")
    
    while True:
        soru = input("\nSiz: ")
        
        if soru.lower() == "kapat":
            break
            
        print("Ajan: İnternette araştırıyorum, lütfen bekle...")
        
        # Ajan önce internete gidip bilgi topluyor
        arama_sonucu = arama_motoru.run(soru)
        
        # Topladığı bilgiyi kendi zekasıyla birleştirip sana sunuyor
        talimat = f"""
        Sen yardımcı bir asistansın. Aşağıdaki güncel bilgileri kullanarak soruyu cevapla.
        
        İnternetten Gelen Bilgi: {arama_sonucu}
        
        Kullanıcı Sorusu: {soru}
        """
        
        cevap = beyin.invoke(talimat)
        print(f"\nAjan: {cevap}")

# Programı başlat
if __name__ == "__main__":
    ajani_calistir()