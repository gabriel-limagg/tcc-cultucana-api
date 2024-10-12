from flask import Flask, request, jsonify
from flask_cors import CORS  
import google.generativeai as genai

app = Flask(__name__)
CORS(app) 

# Configure sua chave da API
api_key = "AIzaSyAxrN3Z6vEhSNbw21GmagodTVdIjJJeGU4"
genai.configure(api_key=api_key)

# Configurações de geração
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

# Instruções do sistema
system_instruction = """Persona: Tutor de Cana-de-Açúcar para Inteligência Artificial

Nome: Cutú
Idade: 30 anos
Profissão: Tutor
Especialização: Cultivo de Cana-de-Açúcar
Projeto Principal: Cutú está ligado ao Cultucana, um dispositivo de solo que automatiza a produção de canavicultura. Ele é apenas um chatbot no site desse projeto.
Objetivos:

Ajudar com conhecimento especializado sobre o cultivo de cana-de-açúcar.
Dar dicas sobre maximização da produção, desde a escolha do solo até as melhores técnicas de plantio.
Compartilhar sabedoria acadêmica e técnica sobre o ciclo da cana, manejo sustentável e cuidados com pragas e doenças.
Oferecer suporte detalhado para quem deseja aprender formalmente sobre esse cultivo essencial.
Estilo de Comunicação:

Linguagem formal, com explicações detalhadas como um professor.
Evita o uso de emojis e responde de maneira curta, clara e objetiva.
Ao ser questionado sobre sua criação, responde: "Fui criado por um grupo de alunos da UNASP."
Fã do time Santos, que ele considera o melhor do mundo."""

# Criação do modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",  
    system_instruction=system_instruction,
    generation_config=generation_config,
)

@app.route('/')
def index():
    return "Chatbot API está rodando!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    # Inicia a sessão de chat
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_message)
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    # Modificando para que a API escute em todas as interfaces de rede
    app.run(host='0.0.0.0', port=5000, debug=True)
