from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun

arama_motoru = DuckDuckGoSearchRun()

beyin = OllamaLLM(model="llama3.2")

def ajani_calistir():
    print("--- AI AJANI HAZIR (Çıkmak için 'kapat' yaz) ---")
    
    while True:
        soru = input("\nSiz: ")
        
        if soru.lower() == "kapat":
            break
            
        print("Ajan: İnternette araştırıyorum, lütfen bekle...")
        
        arama_sonucu = arama_motoru.run(soru)
        
        talimat = f"""
        Sen yardımcı bir asistansın. Aşağıdaki güncel bilgileri kullanarak soruyu cevapla.
        
        İnternetten Gelen Bilgi: {arama_sonucu}
        
        Kullanıcı Sorusu: {soru}
        """
        
        cevap = beyin.invoke(talimat)
        print(f"\nAjan: {cevap}")

if __name__ == "__main__":
    ajani_calistir()
