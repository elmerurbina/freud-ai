from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/support", methods=["GET", "POST"])
def redApoyo():
    if request.method == "POST":
        # Get form data
        contact_one = request.form.get("contact-one")
        contact_two = request.form.get("contact-two")
        psychologist_email = request.form.get("psychologist-email")

        # Code to process form data goes here

        # Return success response
        return jsonify({"message": "Support contacts saved successfully!"})

    # Render the redApoyo.html template for GET requests
    return render_template("redApoyo.html")

if __name__ == "__main__":
    app.run(debug=True)
