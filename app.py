import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,jsonify
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from tempfile import mkdtemp  # Creates a unique temporary directory
from flask import abort

# configure application
app = Flask(__name__)

# To reload templates automatically
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use the filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure library to use SQLite database
db = SQL("sqlite:///commerce.db")

# set API key
os.environ.setdefault("API_KEY", "sk_f87a03e71d384183b25d9e0d2f21e849")
API_KEY = os.environ["API_KEY"]
if not API_KEY:
    raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    # Ensure responses are not cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# index page route
@app.route("/")
@login_required
def index():
    return render_template("index.html")

#login route
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("name"):
            return "Username required!!"
        elif not request.form.get("password"):
            return "Password required"

        print(f"Username: {request.form.get('name')}")
        print(f"Password: {request.form.get('password')}")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("name")
        )

        print(f"Rows: {rows}")

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            print(
                f"Hash Check: {check_password_hash(rows[0]['hash'], request.form.get('password'))}"
            )
            return "Invalid username or password"

        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")



@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return ("Username required")
        elif not password or not confirmation:
            return ("Password required twice")
        elif password != confirmation:
            return ("Passwords do not match")

        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return ("Username exists")

        hashed_password = generate_password_hash(password)

        # Insert the new user into the users table with the hashed password
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            hashed_password,
        )

        # Redirect user to login page after successful registration
        flash("Registration successful!")
        return redirect("/login")
    else:
        return render_template("register.html")

#logout route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# This route handles requests for the "tops" category.
@app.route("/tops")
@login_required
def tops():
    # Fetch data from the database for products in the "tops" category.
    tops_data = db.execute("SELECT id, name, price, image_path, description FROM products WHERE type = 'tops' ORDER BY order_number")
    # Render the template "tops.html" and pass the fetched data to the template.
    return render_template("tops.html", tops_data=tops_data)

# This route handles requests for the "dresses" category.
@app.route("/dresses")
@login_required
def dresses():
    # Fetch data from the database for products in the "dresses" category.
    dresses_data = db.execute("SELECT id, name, price, image_path, description FROM products WHERE type = 'dresses' ORDER BY order_number")
    # Print the information of the first product in the console (for debugging purposes).
    print("First product:", dresses_data[0])
    # Render the template "dresses.html" and pass the fetched data to the template.
    return render_template("dresses.html", dresses_data=dresses_data)

# This route handles requests for the "jeans" category.
@app.route("/jeans")
@login_required
def jeans():
    # Fetch data from the database for products in the "jeans" category.
    jeans_data = db.execute("SELECT id, name, price, image_path, description FROM products WHERE type = 'jeans' ORDER BY order_number")
    # Render the template "jeans.html" and pass the fetched data to the template.
    return render_template("jeans.html", jeans_data=jeans_data)

# This route handles requests for the "shoes" category.
@app.route("/shoes")
@login_required
def shoes():
    # Fetch data from the database for products in the "shoes" category.
    shoes_data = db.execute("SELECT id, name, price, image_path, description FROM products WHERE type = 'shoes' ORDER BY order_number")
    # Render the template "shoes.html" and pass the fetched data to the template.
    return render_template("shoes.html", shoes_data=shoes_data)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    user_id = session["user_id"]
    quantity = int(request.form.get("quantity", 1))

    # Check if the product is already in the cart
    existing_item = db.execute(
        "SELECT * FROM cart WHERE user_id = ? AND product_id = ?", user_id, product_id
    )

    if existing_item:
        # If the product is already in the cart, update the quantity
        db.execute(
            "UPDATE cart SET quantity = quantity + ? WHERE id = ?", quantity, existing_item[0]["id"]
        )
    else:
        # If the product is not in the cart, insert a new cart item
        db.execute(
            "INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)",
            user_id,
            product_id,
            quantity,
        )

    return redirect(request.referrer)



@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    return redirect("/view_cart")

@app.route("/remove_from_cart/<int:cart_id>", methods=["POST"])
@login_required
def remove_from_cart(cart_id):
    # Get the current quantity of the item in the cart
    result = db.execute("SELECT quantity FROM cart WHERE id = ?", cart_id)

    # Check if the result is not empty
    if result:
        current_quantity = result[0]["quantity"]

        # If the current quantity is greater than 0, decrement the quantity
        if current_quantity > 1:
            db.execute("UPDATE cart SET quantity = ? WHERE id = ?", current_quantity - 1, cart_id)
        else:
            # If the current quantity is <1, remove the item from the cart
            db.execute("DELETE FROM cart WHERE id = ?", cart_id)

        return jsonify(success=True)
    else:
        return jsonify(success=False, error="Cart item not found"), 404




@app.route("/update_quantity/<int:cart_id>", methods=["POST"])
@login_required
def update_quantity(cart_id):

    new_quantity = int(request.form.get("new_quantity", 1))

    # If the new quantity is less than or equal to 0, remove the item from the cart
    if new_quantity <= 0:
        db.execute("DELETE FROM cart WHERE id = ?", cart_id)
    else:
        # Update the quantity of the cart item
        db.execute("UPDATE cart SET quantity = ? WHERE id = ?", new_quantity, cart_id)

    return jsonify(success=True)

@app.route("/view_cart")
@login_required
def view_cart():
    # Fetch cart items for the current user
    cart_items = db.execute(
        "SELECT c.id, p.name, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?",
        session["user_id"],
    )

   # Calculate total price
    total_price = sum(item["price"] * item["quantity"] for item in cart_items)

    return render_template("cart.html", cart_items=cart_items, total_price=total_price)

@app.route("/checkout")
@login_required
def checkout():
    # Fetch cart items for the current user
    cart_items = db.execute(
        "SELECT c.id, p.name, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?",
        session["user_id"],
    )

    # Calculate total price
    total_price = sum(item["price"] * item["quantity"] for item in cart_items)

    return render_template("checkout.html", cart_items=cart_items, total_price=total_price)
