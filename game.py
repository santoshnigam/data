import streamlit as st

st.set_page_config(
    page_title="🔥 Free Fire Gaming Store",
    page_icon="🎮",
    layout="wide"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

.title{
    text-align:center;
    font-size:48px;
    color:#ffb000;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#d1d5db;
    font-size:20px;
}

.card{
    background:#1f2937;
    border-radius:18px;
    padding:20px;
    border:2px solid #ff9900;
    margin-bottom:20px;
    box-shadow:0px 0px 15px rgba(255,165,0,0.3);
}

.price{
    color:#00ff95;
    font-size:28px;
    font-weight:bold;
}

.buyButton{
    background:#ff5500;
    color:white;
    padding:10px;
    border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ---------------- #

st.markdown('<p class="title">🔥 FREE FIRE GAMING STORE 🔥</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Top-Up Diamonds • Membership • Elite Pass</p>', unsafe_allow_html=True)

st.divider()

# ---------------- Sidebar ---------------- #

st.sidebar.title("🎮 Store Menu")

menu = st.sidebar.radio(
    "Choose",
    ["Home", "Diamond Shop", "Membership", "Weapons", "About"]
)

# ---------------- Home ---------------- #

if menu == "Home":

    st.header("Welcome Gamer 👑")

    st.image(
        "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200",
        use_container_width=True,
    )

    st.success("Best Free Fire Gaming Store")

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("Customers","12,500+")

    with c2:
        st.metric("Orders","50,000+")

    with c3:
        st.metric("Rating","4.9 ⭐")

# ---------------- Diamond Shop ---------------- #

elif menu=="Diamond Shop":

    st.header("💎 Diamond Top Up")

    col1,col2,col3=st.columns(3)

    packages=[
        ("💎 100 Diamonds","$0.99"),
        ("💎 310 Diamonds","$2.99"),
        ("💎 520 Diamonds","$4.99"),
        ("💎 1060 Diamonds","$9.99"),
        ("💎 2180 Diamonds","$19.99"),
        ("💎 5600 Diamonds","$49.99"),
    ]

    cols=[col1,col2,col3]

    for i,(name,price) in enumerate(packages):
        with cols[i%3]:
            st.markdown(f"""
            <div class="card">
            <h2>{name}</h2>
            <p class="price">{price}</p>
            </div>
            """,unsafe_allow_html=True)

            if st.button(f"Buy {name}",key=i):
                st.success(f"{name} added successfully!")

# ---------------- Membership ---------------- #

elif menu=="Membership":

    st.header("👑 Membership")

    col1,col2=st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h2>Weekly Membership</h2>
        <h1 style="color:#00ff99;">$1.99</h1>
        </div>
        """,unsafe_allow_html=True)

        st.button("Buy Weekly")

    with col2:
        st.markdown("""
        <div class="card">
        <h2>Monthly Membership</h2>
        <h1 style="color:#00ff99;">$7.99</h1>
        </div>
        """,unsafe_allow_html=True)

        st.button("Buy Monthly")

# ---------------- Weapons ---------------- #

elif menu=="Weapons":

    st.header("🔫 Popular Weapons")

    weapons=[
        "AWM Sniper",
        "MP40",
        "M1887",
        "AK47",
        "Desert Eagle",
        "SCAR"
    ]

    for gun in weapons:
        st.markdown(f"""
        <div class="card">
        <h2>{gun}</h2>
        <p>Power ⭐⭐⭐⭐⭐</p>
        </div>
        """,unsafe_allow_html=True)

# ---------------- About ---------------- #

elif menu=="About":

    st.header("ℹ About Store")

    st.write("""
This is a modern gaming store UI built using **Streamlit**.

### Features
- 🔥 Dark Gaming Theme
- 💎 Diamond Shop
- 👑 Membership
- 🔫 Weapon Showcase
- 🎮 Responsive Layout

Made with ❤️ using Python + Streamlit.
""")

st.divider()

st.markdown(
    "<center>© 2026 Free Fire Gaming Store | Python + Streamlit</center>",
    unsafe_allow_html=True,
)