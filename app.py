from flask import Flask, request, render_template_string, redirect, session

app = Flask(__name__)
app.secret_key = "enterprise-training-lab-key"

# Lab credentials - server side only
VALID_USERNAME = "employee"
VALID_PASSWORD = "Enterprise@7392"

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Portal</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #101827, #1d3557);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .login-box {
            width: 380px;
            padding: 40px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.35);
        }

        h1 {
            text-align: center;
            color: #172033;
        }

        .subtitle {
            text-align: center;
            color: #777;
            margin-bottom: 30px;
        }

        input {
            width: 100%;
            box-sizing: border-box;
            padding: 13px;
            margin: 8px 0 15px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        button {
            width: 100%;
            padding: 13px;
            border: none;
            border-radius: 8px;
            background: #1769aa;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #0d527f;
        }

        .error {
            color: #c62828;
            text-align: center;
            margin-top: 15px;
        }

        .footer {
            text-align: center;
            margin-top: 25px;
            font-size: 12px;
            color: #888;
        }
    </style>
</head>

<body>

<div class="login-box">

    <h1>Enterprise Portal</h1>
    <div class="subtitle">Employee Authentication</div>

    <form method="POST">
        <input type="text" name="username"
               placeholder="Username" required>

        <input type="password" name="password"
               placeholder="Password" required>

        <button type="submit">Sign In</button>
    </form>

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

    <div class="footer">
        Authorized Training Environment
    </div>

</div>

</body>
</html>
"""


DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Dashboard</title>
    <style>
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
        }

        .container {
            padding: 40px;
        }

        .card {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .logout {
            color: white;
            text-decoration: none;
        }
    </style>
</head>

<body>

<div class="header">
    <strong>Enterprise Management Portal</strong>
    <a class="logout" href="/logout">Logout</a>
</div>

<div class="container">

    <div class="card">
        <h2>Welcome, Employee</h2>
        <p>You have successfully authenticated to the training portal.</p>
    </div>

    <div class="card">
        <h3>Employee Services</h3>
        <p>Employee Records</p>
        <p>Documents</p>
        <p>Company Resources</p>
        <p>Account Settings</p>
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == VALID_USERNAME and password == VALID_PASSWORD:

            session["logged_in"] = True
            session["username"] = username

            return redirect("/dashboard")

        error = "Invalid username or password"

    return render_template_string(
        LOGIN_PAGE,
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
    print("\n======================================")
    print(" Enterprise Training Lab")
    print(" Running on http://127.0.0.1:8000")
    print("======================================\n")

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False
    )
