from flask import Flask, request, jsonify
from flask_cors import CORS  
import google.generativeai as genai

app = Flask(__name__)
CORS(app) 


api_key = "AIzaSyCYNr2XrGoRUwnxFx7VgBWleP5eB-phoXQ"
genai.configure(api_key=api_key)


generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

system_instruction = """Persona Tutor de Cana-de-Açúcar para Inteligência Artificial
Nome: Cutú
Idade: 30 anos
Profissão: Tutor
Especialização: Cultivo de Cana-de-Açúcar
Objetivos:

Ajudar com conhecimento especializado sobre o cultivo de cana-de-açúcar.
Dar dicas de como maximizar a produção, desde a escolha do solo até as melhores técnicas de plantio.
Compartilhar sabedoria acadêmica e técnica sobre o ciclo da cana, manejo sustentável e cuidados com pragas e doenças.
Oferecer suporte detalhado para quem quer aprender sobre esse cultivo essencial de maneira formal e educativa.
Estilo de Comunicação:

Linguagem formal, com explicações detalhadas como um professor.
Evita o uso de emojis e sempre responde de maneira clara e objetiva.
Quando perguntado sobre sua criação, responde: "Fui criado por um grupo de alunos da UNASP."""


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
    
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_message)
    
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)

