from flask import Flask, request, render_template, render_template_string, redirect, session
import os

app = Flask(__name__)

# Session secret
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "enterprise-training-lab-key"
)

# Training-lab credentials
# Later, Render par inhe Environment Variables me move kar sakte ho.
VALID_USERNAME = os.environ.get("LAB_USERNAME", "employee")
VALID_PASSWORD = os.environ.get("LAB_PASSWORD", "Enterprise@7392")


DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Dashboard</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
        }

        .header {
            background: #172033;
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header strong {
            font-size: 20px;
        }

        .logout {
            color: white;
            text-decoration: none;
            background: #c62828;
            padding: 9px 16px;
            border-radius: 7px;
        }

        .container {
            padding: 40px;
            max-width: 1100px;
            margin: auto;
        }

        .welcome {
            background: #1769aa;
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 25px;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .card h3 {
            color: #172033;
        }

        .card p {
            color: #666;
        }
    </style>
</head>

<body>

<div class="header">
    <strong>Enterprise Management Portal</strong>
    <a class="logout" href="/logout">Logout</a>
</div>

<div class="container">

    <div class="welcome">
        <h2>Welcome, Employee</h2>
        <p>
            You have successfully authenticated to the training portal.
        </p>
    </div>

    <div class="services">

        <div class="card">
            <h3>Employee Records</h3>
            <p>View employee information and records.</p>
        </div>

        <div class="card">
            <h3>Documents</h3>
            <p>Access company documents and resources.</p>
        </div>

        <div class="card">
            <h3>Company Resources</h3>
            <p>Access internal training resources.</p>
        </div>

        <div class="card">
            <h3>Account Settings</h3>
            <p>Manage account-related settings.</p>
        </div>

    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == VALID_USERNAME and password == VALID_PASSWORD:

            session["logged_in"] = True
            session["username"] = username

            return redirect("/dashboard")

        error = "Invalid username or password"

    return render_template(
        "login.html",
        error=error
    )


@app.route("/dashboard")
def dashboard():

    if not session.get("logged_in"):
        return redirect("/")

    return render_template_string(DASHBOARD)


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    print("\n======================================")
    print(" Enterprise Training Lab")
    print("======================================")
    print(f" Running on port: {port}")
    print("======================================\n")

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
