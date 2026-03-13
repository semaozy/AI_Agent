# 🤖 Local AI Agent with Persistent Memory & Web Search
## Yerel Hafızalı ve İnternet Erişimli Yapay Zeka Ajanı

This is a privacy-focused, 100% free AI agent that runs locally on your machine. It features *Persistent Memory* (storing information in a local file) and *Real-time Web Search* capabilities.

Bu proje, tamamen yerel çalışan, gizlilik odaklı ve %100 ücretsiz bir yapay zeka ajanıdır. *Kalıcı Hafıza* (bilgileri yerel dosyada saklama) ve *Gerçek Zamanlı Web Araması* özelliklerine sahiptir.

---

## 🌟 Key Features | Temel Özellikler

- *🧠 Persistent Local Memory:* Save important information with the "Not et:" (Note down) command. The agent checks its local memory before searching the web.
- *🌐 Web Search:* Uses DuckDuckGo to provide up-to-date information without any API keys.
- *🛡️ 100% Private & Local:* All processing happens on your hardware via Ollama. No data leaves your machine.
- *⚡ Optimized for Intel Ultra:* High-performance execution on the new Intel Core Ultra (Lunar Lake) architecture.

---

## 🛠️ How it Works | Nasıl Çalışır?

The agent follows a decision-making logic:
1. *Input:* Receives user query.
2. *Memory Check:* Reads hafiza.txt to see if the information is already known.
3. *Reasoning:* Decides whether it needs to search the web or answer from its own memory/knowledge.
4. *Output:* Provides a contextualized Turkish response.



---

## 📦 Installation | Kurulum

1. *Clone the repository:*

   git clone 
   cd Local-AI-Memory-Agent
Install dependencies:

pip install langchain langchain-ollama langchain-community duckduckgo-search
Required Software:

Install Ollama

Pull the model: ollama pull llama3.2

## 🎮 Usage | Kullanım
Run the agent:

python ajan.py
Commands:

To Save Info: Not et: Benim adım Ahmet, yazılım mühendisliği okuyorum.

To Ask Memory: Benim adım ne? or Nerede okuyorum?

To Search Web: Bugün teknoloji dünyasında neler oldu?

## 💻 Hardware Specs | Donanım Bilgileri
Developed and tested on:

Device: ASUS ExpertBook P5

CPU: Intel Core Ultra 7 258V

RAM: 32GB LPDDR5X

GPU: Intel Arc Graphics 140V
