from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Deep link ativo! Acesse /yt para redirecionar para o canal."

@app.route("/yt")
def youtube_deep_link():
    user_agent = request.headers.get('User-Agent', '').lower()

    # Link com sub_confirmation=1
    youtube_link = "https://www.youtube.com/@otto.professor?sub_confirmation=1"

    # Podemos usar lógica de sistema se quiser no futuro, mas aqui sempre direciona pro link de inscrição
    return redirect(youtube_link)

# Necessário para o Render funcionar corretamente
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
