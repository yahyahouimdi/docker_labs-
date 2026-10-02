from flask import Flask, request
from datetime import datetime
from babel.dates import format_date

app = Flask(__name__)

@app.route("/date")
def get_date():
    lang = request.args.get("lang", "fr")
    now = datetime.now()

    return format_date(now, format="full", locale=lang)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
