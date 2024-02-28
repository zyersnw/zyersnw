from flask import Flask, render_template, request
import random

app = Flask(__name__)


def computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_selection = computer_choice()

        if player_choice == computer_selection:
            result = "무승부"
        elif (
            (player_choice == "가위" and computer_selection == "보") or
            (player_choice == "바위" and computer_selection == "가위") or
            (player_choice == "보" and computer_selection == "바위")
        ):
            result = "승리"
        else:
            result = "패배"

    return render_template("index.html", result=result, player_choice = player_choice, computer_selection = computer_selection)

if __name__ == "__main__":
    app.run(debug=True)
