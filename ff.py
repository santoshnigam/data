import streamlit as st
import sqlite3
import re

st.set_page_config(page_title="🔥 Free Fire Gaming Store", layout="wide")

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("store.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
uid TEXT,
nickname TEXT,
package TEXT,
price TEXT,
payment TEXT,
status TEXT
)
""")

conn.commit()

# ---------------- SESSION ---------------- #

if "login" not in st.session_state:
    st.session_state.login=False

if "user" not in st.session_state:
    st.session_state.user=""

# ---------------- SIDEBAR ---------------- #

menu=["Home"]

if st.session_state.login:
    menu+=["Diamond Shop","Orders","Logout"]
else:
    menu+=["Login","Signup"]

choice=st.sidebar.selectbox("Menu",menu)

# ---------------- HOME ---------------- #

if choice=="Home":

    st.title("🔥 FREE FIRE GAMING STORE")

    st.image("https://wallpapercave.com/wp/wp5128415.jpg")

    st.success("Buy Diamonds Safely")

# ---------------- SIGNUP ---------------- #
elif choice=="Signup":

    st.title("Create Account")

    user = st.text_input("Email or Phone Number")

    pwd = st.text_input("Password", type="password")

    if st.button("Register"):

        if user.strip()=="" or pwd.strip()=="":
            st.error("❌ Please fill all fields.")

        else:

            # Email or 10-digit phone validation
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            phone_pattern = r'^\d{10}$'

            if not (re.match(email_pattern, user) or re.match(phone_pattern, user)):
                st.error("❌ Enter a valid Email or 10-digit Phone Number.")

            elif len(pwd) < 6:
                st.error("❌ Password must be at least 6 characters.")

            else:

                c.execute("SELECT * FROM users WHERE username=?", (user,))
                if c.fetchone():
                    st.warning("⚠️ Account already exists.")

                else:
                    c.execute(
                        "INSERT INTO users(username,password) VALUES(?,?)",
                        (user, pwd)
                    )
                    conn.commit()
                    st.success("✅ Account Created Successfully")

    # st.title("Create Account")

    # user=st.text_input("Email or Phone number")

    # pwd=st.text_input("Password",type="password")

    # if st.button("Register"):

    #     c.execute("INSERT INTO users(username,password) VALUES(?,?)",(user,pwd))
    #     conn.commit()

    #     st.success("Account Created Successfully")

# ---------------- LOGIN ---------------- #

elif choice=="Login":

    st.title("Login")

    user=st.text_input("Email or phone number")

    pwd=st.text_input("Password",type="password")

    if st.button("Login"):

        c.execute("SELECT * FROM users WHERE username=? AND password=?",(user,pwd))

        data=c.fetchone()

        if data:

            st.session_state.login=True

            st.session_state.user=user

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Wrong Username or Password")

# ---------------- LOGOUT ---------------- #

elif choice=="Logout":

    st.session_state.login=False

    st.session_state.user=""

    st.rerun()

# ---------------- ORDERS ---------------- #

elif choice=="Orders":


    st.title("📦 My Orders")

    c.execute("""
    SELECT uid,nickname,package,price,payment,status
    FROM orders
    WHERE username=?
    """,
    (st.session_state.user,)
    )

    rows = c.fetchall()

    for row in rows:

        st.info(f"""
UID : {row[0]}

Nickname : {row[1]}

Package : {row[2]}

Price : {row[3]}

Payment : {row[4]}

Status : {row[5]}
""")
    

# ---------------- DIAMOND SHOP ---------------- #

elif choice=="Diamond Shop":

    st.header("💎 Diamond Shop")

    uid=st.text_input("Free Fire UID")

    nickname=st.text_input("Nickname")

    payment=st.selectbox("Payment Method",
    ["eSewa"])

    packages=[
    ("100 Diamonds","Rs.110"),
    ("240 Diamonds","Rs.230"),
    ("355 Diamonds","Rs.330"),
    ("480 Diamonds","Rs.450"),
    ("610 Diamonds","Rs.590"),
    ("725 Diamonds","Rs.695"),
    ("850 Diamonds","Rs.795"),
    ("965 Diamonds","Rs.899"),
    ("1090 Diamonds","Rs.999"),
    ("1240 Diamonds","Rs.1185"),
    ("1480 Diamonds","Rs.1350"),
    ("1720 Diamonds","Rs.1550"),
    ("2530 Diamonds","Rs.2300"),
    ("5060 Diamonds","Rs.4800"),
    ("10120 Diamonds","Rs.9800"),
    (" ELITE WEEKLY","Rs.80"),
    ("WEEKLY","Rs.250"),
    ("MONTHLY","Rs.1200")
    ]

    col1,col2,col3=st.columns(3)

    cols=[col1,col2,col3]

    for i,(name,price) in enumerate(packages):

        with cols[i%3]:

            st.info(name)

            st.write(price)

            if st.button("Buy",key=i):

                if uid=="":

                    st.error("Enter UID")

                else:

                    c.execute("""
                    INSERT INTO orders(username,uid,nickname,package,price,payment,status)
                    VALUES(?,?,?,?,?,?,?)
                    """,(st.session_state.user,
                    uid,
                    nickname,
                    name,
                    price,
                    payment,
                    "Pending"))

                    conn.commit()

                    st.success("Order Created")

                    st.write("### Order Details")

                    st.write("UID :",uid)

                    st.write("Nickname :",nickname)

                    st.write("Package :",name)

                    st.write("Price :",price)

                    st.write("Payment :",payment)

                    st.image("pay.jpg",width=220)

                    receipt = st.file_uploader(
                            "Upload Payment Screenshot",
                    type=["png","jpg","jpeg"],
                    key=i
                    )

                    if receipt:

                        c.execute("""
                        UPDATE orders
                        SET status=?
                        WHERE username=? AND uid=? AND package=?
                                                                 """,
                        (
                            "Delivered",
                            st.session_state.user,
                            uid,
                            name
                        ))

                        conn.commit()

                        st.success("✅ Payment Screenshot Uploaded Successfully")

                        st.balloons()

                        st.success("🎉 Order Delivered Successfully!")

                    # receipt=st.file_uploader(
                    # "Upload Payment Screenshot",
                    # type=["png","jpg","jpeg"],
                    # key=i
                    # )

                    # if receipt:

                    #     st.success("Screenshot Uploaded")
