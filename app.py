from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Deep link ativo! Use /yt para redirecionar."

@app.route("/yt")
def youtube_deep_link():
    user_agent = request.headers.get('User-Agent', '').lower()

    if "android" in user_agent:
        return redirect("vnd.youtube://user/otto.professor")  # Android
    elif "iphone" in user_agent or "ipad" in user_agent:
        return redirect("youtube://www.youtube.com/@otto.professor")  # iOS
    else:
        return redirect("https://www.youtube.com/@otto.professor")  # fallback
