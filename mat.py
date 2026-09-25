from flask import Flask, request, redirect, url_for, session, render_template_string, jsonify
import sqlite3
import os
import secrets
import html
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import quote

app = Flask(__name__)

# Барои Render
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(32))

DB = "carparking.db"
WHATSAPP = "992104143449"


# =========================================================
# 🚗 ФАҚАТ СУРАТҲОИ НАВ
# =========================================================

CARS = [
    {
        "name": "CAMRY 7",
        "slug": "camry7-1",
        "price": 15,
        "bonus": 50,
        "image": "camry7_1.jpg"
    },
    {
        "name": "BMW M5",
        "slug": "bmw-m5",
        "price": 15,
        "bonus": 50,
        "image": "bmw_m5.jpg"
    },
    {
        "name": "GELIK",
        "slug": "gelik",
        "price": 15,
        "bonus": 50,
        "image": "gelik.jpg"
    },
    {
        "name": "BMW M2",
        "slug": "bmw-m2",
        "price": 15,
        "bonus": 50,
        "image": "bmw_m2.jpg"
    },
    {
        "name": "FORMULA 1",
        "slug": "formula1",
        "price": 10,
        "bonus": 50,
        "image": "formula1.jpg"
    },
    {
        "name": "BMW M4",
        "slug": "bmw-m4",
        "price": 15,
        "bonus": 50,
        "image": "bmw_m4.jpg"
    },
    {
        "name": "FORD",
        "slug": "ford",
        "price": 15,
        "bonus": 50,
        "image": "ford.jpg"
    },
    {
        "name": "CAMRY 7",
        "slug": "camry7-2",
        "price": 15,
        "bonus": 50,
        "image": "camry7_2.jpg"
    }
]


# =========================================================
# 👤 АКАУНТҲО
# =========================================================

ACCOUNTS = [
    {
        "name": "FULL ACCOUNT",
        "price": 180,
        "bonus": 60,
        "info": "212 мошин • 500K танга • 50 млн сум"
    },
    {
        "name": "ACCOUNT 150",
        "price": 150,
        "bonus": 60,
        "info": "190 мошин • 500K танга • 50 млн сум"
    },
    {
        "name": "ACCOUNT 100",
        "price": 100,
        "bonus": 60,
        "info": "150 мошин • 500K танга • 50 млн сум"
    },
    {
        "name": "ACCOUNT 80",
        "price": 80,
        "bonus": 60,
        "info": "100 мошин • 500K танга • 50 млн сум"
    },
    {
        "name": "KING ACCOUNT",
        "price": 50,
        "bonus": 60,
        "info": "80 мошин • 500K танга • 50 млн сум"
    }
]


# =========================================================
# 🖼️ СУРАТҲОИ ИҶОЗАТДОДАШУДА
# СУРАТҲОИ КӮҲНА АЗ static/images НЕСТ КАРДА МЕШАВАНД
# =========================================================

ALLOWED_IMAGES = {x["image"] for x in CARS}


def clean_old_images():
    folder = os.path.join(
        os.path.dirname(__file__),
        "static",
        "images"
    )

    if not os.path.isdir(folder):
        return

    for filename in os.listdir(folder):
        if filename.lower().endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        ):
            if filename not in ALLOWED_IMAGES:
                try:
                    os.remove(
                        os.path.join(folder, filename)
                    )
                except OSError:
                    pass


# =========================================================
# DATABASE
# =========================================================

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def init_db():
    c = db()

    c.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        bonus INTEGER NOT NULL DEFAULT 0,
        referral_code TEXT UNIQUE NOT NULL,
        referred_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product_type TEXT NOT NULL,
        product_name TEXT NOT NULL,
        price INTEGER NOT NULL,
        bonus_reward INTEGER NOT NULL DEFAULT 0,
        payment_type TEXT NOT NULL DEFAULT 'whatsapp',
        status TEXT NOT NULL DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        username TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    c.commit()
    c.close()


def current_user():
    if not session.get("user_id"):
        return None

    c = db()

    u = c.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    c.close()

    return u


def product(pt, slug):
    if pt == "car":
        return next(
            (x for x in CARS if x["slug"] == slug),
            None
        )

    if pt == "account":
        return next(
            (x for x in ACCOUNTS if x["name"] == slug),
            None
        )

    return None


# =========================================================
# 🏠 HOME
# =========================================================

@app.route("/")
def home():

    u = current_user()

    c = db()

    news = c.execute(
        "SELECT * FROM notifications ORDER BY id DESC LIMIT 10"
    ).fetchall()

    c.close()

    return render_template_string(
        TEMPLATE,
        user=u,
        cars=CARS,
        accounts=ACCOUNTS,
        news=news,
        wa=WHATSAPP,
        q=request.args.get("q", "")
    )


# =========================================================
# 👤 REGISTRATION
# =========================================================

@app.route("/register", methods=["POST"])
def register():

    username = request.form.get(
        "username", ""
    ).strip()

    email = request.form.get(
        "email", ""
    ).strip().lower()

    password = request.form.get(
        "password", ""
    )

    ref = request.form.get(
        "ref", ""
    ).strip()

    if (
        len(username) < 3
        or "@" not in email
        or len(password) < 6
    ):
        return redirect(
            url_for(
                "home",
                error="Маълумоти регистрация нодуруст аст."
            )
        )

    c = db()

    exists = c.execute(
        """
        SELECT 1
        FROM users
        WHERE username=? OR email=?
        """,
        (username, email)
    ).fetchone()

    if exists:
        c.close()

        return redirect(
            url_for(
                "home",
                error="Username ё Email аллакай истифода шудааст."
            )
        )

    inviter = None

    if ref:
        inviter = c.execute(
            """
            SELECT id
            FROM users
            WHERE referral_code=?
            """,
            (ref,)
        ).fetchone()

    code = secrets.token_hex(4).upper()

    while c.execute(
        "SELECT 1 FROM users WHERE referral_code=?",
        (code,)
    ).fetchone():
        code = secrets.token_hex(4).upper()

    cur = c.execute(
        """
        INSERT INTO users
        (
            username,
            email,
            password,
            bonus,
            referral_code,
            referred_by
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            username,
            email,
            generate_password_hash(password),
            100,
            code,
            inviter["id"] if inviter else None
        )
    )

    uid = cur.lastrowid
 # +50 барои дӯсти даъватшуда
    if inviter:
        c.execute(
            """
            UPDATE users
            SET bonus=bonus+50
            WHERE id=?
            """,
            (inviter["id"],)
        )

    c.commit()
    c.close()

    session["user_id"] = uid

    return redirect(url_for("home"))


# =========================================================
# 🔐 LOGIN
# =========================================================

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get(
        "email", ""
    ).strip().lower()

    password = request.form.get(
        "password", ""
    )

    c = db()

    u = c.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    ).fetchone()

    c.close()

    if not u or not check_password_hash(
        u["password"],
        password
    ):
        return redirect(
            url_for(
                "home",
                error="Email ё парол нодуруст аст."
            )
        )

    session["user_id"] = u["id"]

    return redirect(url_for("home"))


# =========================================================
# 🚪 LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =========================================================
# 🎁 ХАРИД БО БОНУС
# =========================================================

@app.route("/buy/<pt>/<path:slug>")
def buy(pt, slug):

    if not session.get("user_id"):
        return redirect(
            url_for(
                "home",
                error="Аввал ба аккаунт даро."
            )
        )

    p = product(pt, slug)

    if not p:
        return redirect(
            url_for(
                "home",
                error="Маҳсулот ёфт нашуд."
            )
        )

    c = db()

    u = c.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    if u["bonus"] < p["price"]:

        c.close()

        return redirect(
            url_for(
                "home",
                error=(
                    f"Бонус кофӣ нест. "
                    f"Барои {p['name']} "
                    f"{p['price']} бонус лозим."
                )
            )
        )

    c.execute(
        """
        UPDATE users
        SET bonus=bonus-?
        WHERE id=?
        """,
        (
            p["price"],
            u["id"]
        )
    )

    c.execute(
        """
        INSERT INTO orders
        (
            user_id,
            product_type,
            product_name,
            price,
            bonus_reward,
            payment_type,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            u["id"],
            pt,
            p["name"],
            p["price"],
            0,
            "bonus",
            "paid"
        )
    )

    c.commit()
    c.close()

    return redirect(
        url_for(
            "home",
            ok=f"{p['name']} бо бонус гирифта шуд."
        )
    )


# =========================================================
# 📱 ЗАКАЗ → WHATSAPP
# =========================================================

@app.route("/order/<pt>/<path:slug>")
def order(pt, slug):

    if not session.get("user_id"):
        return redirect(
            url_for(
                "home",
                error="Аввал ба аккаунт даро."
            )
        )

    p = product(pt, slug)

    if not p:
        return redirect(
            url_for(
                "home",
                error="Маҳсулот ёфт нашуд."
            )
        )

    u = current_user()

    c = db()

    c.execute(
        """
        INSERT INTO orders
        (
            user_id,
            product_type,
product_name,
            price,
            bonus_reward,
            payment_type,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            u["id"],
            pt,
            p["name"],
            p["price"],
            p["bonus"],
            "whatsapp",
            "pending"
        )
    )

    c.commit()
    c.close()

    text = (
        f"Салом! Ман мехоҳам {p['name']} харам. "
        f"Нарх: {p['price']} сомонӣ. "
        f"Username: {u['username']}"
    )

    return redirect(
        "https://wa.me/"
        + WHATSAPP
        + "?text="
        + quote(text)
    )


# =========================================================
# 🔎 SEARCH
# =========================================================

@app.route("/search")
def search():

    q = request.args.get(
        "q",
        ""
    ).strip().lower()

    return redirect(
        url_for(
            "home",
            q=q
        )
    )


# =========================================================
# 💬 CHAT
# =========================================================

@app.route("/chat/messages")
def chat_messages():

    c = db()

    rows = c.execute(
        """
        SELECT username,message,created_at
        FROM chat
        ORDER BY id DESC
        LIMIT 50
        """
    ).fetchall()

    c.close()

    return jsonify(
        [
            dict(r)
            for r in reversed(rows)
        ]
    )


@app.route("/chat/send", methods=["POST"])
def chat_send():

    u = current_user()

    if not u:
        return jsonify(
            ok=False,
            error="login"
        ), 401

    msg = html.escape(
        request.form.get(
            "message",
            ""
        ).strip()
    )

    if not msg or len(msg) > 500:
        return jsonify(
            ok=False,
            error="message"
        )

    c = db()

    c.execute(
        """
        INSERT INTO chat
        (
            user_id,
            username,
            message
        )
        VALUES (?, ?, ?)
        """,
        (
            u["id"],
            u["username"],
            msg
        )
    )

    c.commit()
    c.close()

    return jsonify(ok=True)


# =========================================================
# 🎨 DESIGN
# =========================================================

TEMPLATE = r"""
<!doctype html>
<html lang="tg">

<head>

<meta charset="utf-8">

<meta name="viewport"
content="width=device-width,initial-scale=1">

<title>carparking.xxm</title>

<style>

*{
box-sizing:border-box
}

body{
margin:0;
background:#050a18;
color:#fff;
font-family:Arial,sans-serif
}

a{
text-decoration:none;
color:inherit
}

header{
position:sticky;
top:0;
z-index:20;
background:#070b18ee;
backdrop-filter:blur(10px);
border-bottom:1px solid #18336f;
padding:12px 4%
}

.nav{
max-width:1200px;
margin:auto;
display:flex;
gap:8px;
align-items:center;
flex-wrap:wrap
}

.logo{
font-size:25px;
font-weight:900;
color:#39a9ff;
margin-right:auto
}

.btn{
display:inline-block;
padding:11px 15px;
border-radius:11px;
background:#12265b;
border:1px solid #3977df;
color:#fff;
font-weight:800;
cursor:pointer
}

.wa{
background:#1d9b45;
border-color:#37d56b
}

.danger{
background:#6e1d2d
}

main{
max-width:1200px;
margin:auto;
padding:18px 4%
}

.hero{
min-height:300px;
border:1px solid #2e5ca8;
border-radius:25px;
padding:35px;
text-align:center;
background:
linear-gradient(
120deg,
#07132e,
#102f75
);
display:flex;
flex-direction:column;
justify-content:center
}

.hero h1{
font-size:52px;
margin:0 0 15px
}

.hero p{
font-size:18px;
color:#b8d7ff
}

.menu{
display:grid;
grid-template-columns:
repeat(6,1fr);
gap:12px;
margin:22px 0
}

.menu .btn{
height:75px;
display:flex;
align-items:center;
justify-content:center;
text-align:center
}

.section{
margin:28px 0
}

.section h2{
color:#8dd8ff
}

.grid{
display:grid;
grid-template-columns:
repeat(4,1fr);
gap:16px
}

.card{
background:#0b1734;
border:1px solid #28549c;
border-radius:18px;
overflow:hidden;
box-shadow:0 8px 30px #0006
}
.card img{
width:100%;
height:190px;
object-fit:cover;
display:block
}

.cardbody{
padding:14px
}

.name{
font-size:20px;
font-weight:900
}

.price{
font-size:18px;
color:#66d6ff;
font-weight:900;
margin:8px 0
}

.bonus{
color:#ffd34e;
font-weight:800;
margin-bottom:10px
}

.actions{
display:flex;
gap:8px;
flex-wrap:wrap
}

.small{
font-size:13px;
color:#a9c5ec
}

.search{
display:flex;
gap:8px;
margin:18px 0
}

.search input,
.modal input,
.chat input{
width:100%;
padding:13px;
border-radius:10px;
border:1px solid #3168bd;
background:#061026;
color:#fff
}

.panel{
background:#091632;
border:1px solid #28549c;
border-radius:18px;
padding:18px
}

.news{
border-left:4px solid #40bfff;
padding:10px 14px;
margin:10px 0;
background:#0b1c3b;
border-radius:8px
}

.overlay{
display:none;
position:fixed;
inset:0;
background:#000a;
z-index:100;
align-items:center;
justify-content:center;
padding:15px
}

.modal{
width:min(560px,100%);
max-height:90vh;
overflow:auto;
background:#07132b;
border:1px solid #3977df;
border-radius:20px;
padding:22px
}

.modal:target{
display:flex;
flex-direction:column
}

.close{
float:right
}

.modal form{
display:grid;
gap:10px
}

.modal button{
border:0
}

.chatbox{
height:320px;
overflow:auto;
background:#040b19;
border-radius:12px;
padding:10px;
margin-bottom:10px
}

.msg{
padding:8px;
border-bottom:1px solid #172b50
}

.ref{
word-break:break-all;
background:#051027;
padding:10px;
border-radius:10px
}

footer{
text-align:center;
color:#7f9bc7;
padding:40px 10px
}

.err{
background:#6e1d2d;
padding:12px;
border-radius:10px
}

.ok{
background:#145e38;
padding:12px;
border-radius:10px
}

@media(max-width:900px){

.grid{
grid-template-columns:
repeat(2,1fr)
}

.menu{
grid-template-columns:
repeat(3,1fr)
}

.hero h1{
font-size:38px
}

}

@media(max-width:560px){

.nav{
gap:5px
}

.logo{
width:100%;
font-size:22px
}

.nav .btn{
padding:9px 10px;
font-size:12px
}

.grid{
grid-template-columns:1fr
}

.menu{
grid-template-columns:
repeat(2,1fr)
}

.hero{
min-height:220px;
padding:22px
}

.hero h1{
font-size:30px
}

.card img{
height:220px
}

}

</style>

</head>

<body>

<header>

<div class="nav">

<div class="logo">
🚗 carparking.xxm
</div>

<a class="btn" href="#search">
🔎 Ҷустуҷӯ
</a>

<a class="btn" href="#news">
🔔 Нав
</a>

<a class="btn" href="#chat">
💬 Чат
</a>

<a class="btn" href="#profile">
👤 Профил
</a>

<a class="btn wa"
href="https://wa.me/{{wa}}">
💬 WhatsApp
</a>

</div>

</header>


<main>

{% if request.args.get('error') %}

<div class="err">
{{request.args.get('error')}}
</div>

{% endif %}


{% if request.args.get('ok') %}

<div class="ok">
{{request.args.get('ok')}}
</div>

{% endif %}


<section class="hero">

<h1>
carparking.xxm
</h1>

<p>
🚗 Мошинҳо • 👤 Аккаунтҳо • 🎁 Бонусҳо
</p>

</section>


<div class="menu">

<a class="btn"
href="#cars">
💰 НАРХНОМА
</a>

<a class="btn"
href="#accounts">
👤 НАРХИ АКАУНТҲО
</a>

<a class="btn"
href="#cars">
🖼 СУРАТҲО
</a>

<a class="btn"
href="#profile">
👤 ПРОФИЛ
</a>

<a class="btn"
href="#bonus">
🎁 БОНУС
</a>

<a class="btn"
href="#contact">
📞 ТАМОС БО АДМИН
</a>

</div>


<section id="search"
class="section">

<h2>
🔎 Ҷустуҷӯ
</h2>

<form class="search"
action="/search">

<input
name="q"
value="{{q}}"
placeholder="Номи мошин ё аккаунт..."
>

<button class="btn">
Ҷустуҷӯ
</button>

</form>

</section>


<section id="cars"
class="section">

<h2>
🚗 МОШИНҲО
</h2>

<div class="grid">

{% for p in cars %}

{% if not q or q.lower() in p.name.lower() %}

<article class="card">

<img
src="{{url_for('static',filename='images/'+p.image)}}"
alt="{{p.name}}"
>

<div class="cardbody">

<div class="name">
{{p.name}}
</div>

<div class="price">
{{p.price}} сомонӣ
</div>

<div class="bonus">
🎁 +{{p.bonus}} бонус
</div>

<div class="actions">

<a class="btn"
href="{{url_for('order',pt='car',slug=p.slug)}}">
Заказ
</a>

<a class="btn"
href="{{url_for('buy',pt='car',slug=p.slug)}}">
Бо бонус
</a>

</div>

</div>

</article>

{% endif %}

{% endfor %}

</div>

</section>


<section id="accounts"
class="section">

<h2>
👤 АКАУНТҲО
</h2>
<div class="grid">

{% for p in accounts %}

{% if not q or q.lower() in p.name.lower() %}

<article class="card">

<div class="cardbody">

<div class="name">
{{p.name}}
</div>

<div class="price">
{{p.price}} сомонӣ
</div>

<div class="bonus">
🎁 +{{p.bonus}} бонус
</div>

<div class="small">
{{p.info}}
</div>

<br>

<div class="actions">

<a class="btn"
href="{{url_for('order',pt='account',slug=p.name)}}">
Заказ
</a>

<a class="btn"
href="{{url_for('buy',pt='account',slug=p.name)}}">
Бо бонус
</a>

</div>

</div>

</article>

{% endif %}

{% endfor %}

</div>

</section>


<section id="bonus"
class="section">

<h2>
🎁 БОНУСҲО
</h2>

<div class="panel">

<p>
Регистрация:
<b>+100</b>
</p>

<p>
Дӯстро даъват кун:
<b>+50</b>
</p>

<p>
Хариди мошин:
<b>+50</b>
</p>

<p>
Хариди аккаунт:
<b>+60</b>
</p>

{% if user %}

<p>
Бонуси ҳозира:
<b>{{user.bonus}} 🎁</b>
</p>

{% endif %}

</div>

</section>


<section id="news"
class="section">

<h2>
🔔 НАВИГАРИҲО
</h2>

{% for n in news %}

<div class="news">

<b>
{{n.title}}
</b>

<br>

{{n.text}}

</div>

{% else %}

<div class="panel">
Ҳоло маҳсулоти нав нест.
</div>

{% endfor %}

</section>


<section id="profile"
class="section">

<h2>
👤 ПРОФИЛ
</h2>

{% if user %}

<div class="panel">

<p>
Username:
<b>{{user.username}}</b>
</p>

<p>
Email:
<b>{{user.email}}</b>
</p>

<p>
Бонус:
<b>{{user.bonus}} 🎁</b>
</p>

<p>
Коди referral:
</p>

<div class="ref">
{{user.referral_code}}
</div>

<p>
Линки referral:
</p>

<div class="ref">
{{request.host_url}}?ref={{user.referral_code}}
</div>

<br>

<a class="btn danger"
href="/logout">
Баромадан
</a>

</div>

{% else %}

<div class="panel">

<p>
Барои истифодаи бонус аввал аккаунт соз.
</p>

<a class="btn"
href="#account">
Регистрация / Вход
</a>

</div>

{% endif %}

</section>


<section id="chat"
class="section">

<h2>
💬 ЧАТ
</h2>

<div class="panel">

<div id="chatbox"
class="chatbox">
Загрузка...
</div>

{% if user %}

<form id="chatForm"
class="chat">

<div style="display:flex;gap:8px">

<input
id="chatInput"
name="message"
maxlength="500"
placeholder="Паёми худро навис..."
required
>

<button class="btn">
Фиристодан
</button>

</div>

</form>

{% else %}

<p>
Барои чат аввал ворид шавед.
</p>

{% endif %}

</div>

</section>


<section id="contact"
class="section">

<h2>
📞 ТАМОС БО АДМИН
</h2>

<div class="panel">

<p>
WhatsApp / Telegram:
<b>104143449</b>
</p>

<p>

<a class="btn"
href="https://www.instagram.com/carparking.xxm?igsh=MXNyeTM5ZHFrODNzNg==">
Instagram
</a>

</p>

<p>

<a class="btn"
href="https://t.me/+IhmFDF-ER6kyZDUy">
💬 Чати Telegram
</a>

</p>

</div>

</section>

</main>


<footer>
carparking.xxm © 2026
</footer>


<div id="account"
class="overlay">

<div class="modal">

<a class="btn close"
href="#">
✕
</a>

<h2>
👤 Аккаунт
</h2>

<h3>
Регистрация — +100 бонус 🎁
</h3>

<form
method="post"
action="/register">

<input
name="username"
placeholder="Username"
required
>

<input
type="email"
name="email"
placeholder="Email"
required
>

<input
type="password"
name="password"
minlength="6"
placeholder="Парол (6+)"
required
>

<input
name="ref"
placeholder="Коди даъват (ихтиёрӣ)"
value="{{request.args.get('ref','')}}"
>

<button class="btn">
ҚУШОДАНИ АККАУНТ +100 🎁
</button>

</form>

<hr>

<h3>
Воридшавӣ
</h3>

<form
method="post"
action="/login">

<input
type="email"
name="email"
placeholder="Email"
required
>

<input
type="password"
name="password"
placeholder="Парол"
required
>

<button class="btn">
Ворид шудан
</button>

</form>

</div>

</div>


<script>

async function loadChat(){

try{

let r = await fetch(
"/chat/messages"
);

let a = await r.json();

document.getElementById(
"chatbox"
).innerHTML =
a.map(
x =>
<div class="msg">
<b>${x.username}</b>:
${x.message}
<div class="small">
${x.created_at}
</div>
</div>
).join("")
||
"Чат ҳоло холӣ аст.";

}catch(e){}

}

loadChat();

setInterval(
loadChat,
3000
);


const f =
document.getElementById(
"chatForm"
);

if(f){

f.addEventListener(
"submit",
async e => {

e.preventDefault();

let fd =
new FormData(f);
let r =
await fetch(
"/chat/send",
{
method:"POST",
body:fd
}
);

if(r.ok){

f.reset();

loadChat();

}

}
);

}

</script>

</body>
</html>
"""


# =========================================================
# 🚀 START
# =========================================================

init_db()
clean_old_images()

if __name__ == "main":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
    iuehdhc _hedheib"jebkmnash "
    yeoglksg