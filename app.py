from flask import Flask, render_template, request

app = Flask(__name__)

pin = None
balance = 0

@app.route("/", methods=["GET", "POST"])   # ✅ FIXED HERE
def home():
    global pin, balance
    message = ""

    if request.method == "POST":
        action = request.form["action"]

        if action == "create":
            pin = request.form["pin"]
            message = "PIN created successfully!"

        elif action == "show":
            if pin:
                message = f"Your PIN is: {pin}"
            else:
                message = "No PIN created yet!"

        elif action == "balance":
            entered_pin = request.form["pin"]
            if pin and entered_pin == pin:
                message = f"Current Balance: ₹{balance}"
            else:
                message = "Incorrect PIN!"

        elif action == "deposit":
            entered_pin = request.form["pin"]
            if pin and entered_pin == pin:
                try:
                    amount = int(request.form["amount"])
                    balance += amount
                    message = f"Deposit Successful! New Balance: ₹{balance}"
                except:
                    message = "Enter valid amount!"
            else:
                message = "Incorrect PIN!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)