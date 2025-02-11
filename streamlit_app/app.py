import streamlit as st
import os
import pandas as pd

# Compute absolute path for favicon
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "Image carmila", "Logo-Carmila-CMJN.jpg")

# Set page configuration for professional dashboard appearance
st.set_page_config(page_title="Carmila Dashboard", page_icon=logo_path, layout="wide")

# Custom CSS for modern, intuitive UI/UX
st.markdown(
    """
    <style>
    /* Professional background and text styling */
    .stApp {
        background-color: #F4F5F7;
    }
    .main {
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Carmila Dashboard")

st.markdown("""
<link href='https://fonts.googleapis.com/css?family=Roboto:300,400,700' rel='stylesheet'>
<style>
body { font-family: 'Roboto', sans-serif; background: linear-gradient(135deg, #f8f9fa, #e9ecef); }
.header-container { text-align: center; padding: 2rem; background: rgba(255,255,255,0.8); border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 2rem; }
.header-text { font-size: 3rem; font-weight: 700; margin: 0; color: #2C3E50; }
.subheader-text { font-size: 1.5rem; margin-top: 0.5rem; color: #34495E; }
.hr-divider { border: 0; height: 1px; background: #BDC3C7; margin: 40px 0; }
.btn { background-color: #3498DB; color: white; padding: 0.5rem 1.5rem; border: none; border-radius: 5px; font-size: 1rem; cursor: pointer; }
.btn:hover { background-color: #2980B9; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='header-container'>
  <h1 class='header-text'>Carmila Dashboard</h1>
  <p class='subheader-text'>Empowering your business with data-driven insights.</p>
</div>
""", unsafe_allow_html=True)

# Lottie Animation for dynamic effects (requires streamlit-lottie package)
try:
    from streamlit_lottie import st_lottie
    import requests
    lottie_url = "https://assets10.lottiefiles.com/packages/lf20_yr6zz3wv.json"
    r = requests.get(lottie_url)
    if r.status_code == 200:
        lottie_json = r.json()
        st_lottie(lottie_json, height=200)
except ImportError:
    st.info("Install streamlit-lottie via pip to enable animations!")

# Interactive metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Sales", value="$1.2M", delta="5%")
with col2:
    st.metric(label="Visitors", value="8.1K", delta="-2%")
with col3:
    st.metric(label="Conversion Rate", value="3.4%", delta="+1.5%")

st.markdown('<hr class="hr-divider">', unsafe_allow_html=True)

# Interactive chart using Plotly
import plotly.express as px
chart_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 300, 250, 400, 350, 450]
}
df = pd.DataFrame(chart_data)
fig = px.area(df, x="Month", y="Sales", markers=True, title="Monthly Sales Trend",
              template="seaborn", color_discrete_sequence=["#3498DB"])
st.plotly_chart(fig, use_container_width=True)

# Future Sales Simulation slider
st.subheader("Simulate Future Sales")
future_sales = st.slider("Forecast Sales Increase (%)", 0, 100, 10)
projected = 450 * (1 + future_sales / 100)
st.write(f"With a {future_sales}% increase, projected sales for next month: ${projected:.0f}K")

# Additional info button
if st.button("Learn More About Carmila"):
    st.info("Carmila is at the forefront of innovation. Our advanced dashboard uses cutting-edge analytics and deep insights to drive business growth. Stay tuned for continuous enhancements and detailed reports!")

st.sidebar.title("Navigation")
st.sidebar.markdown("- [Home](#)")
st.sidebar.markdown("- Analysis Page 1")
st.sidebar.markdown("- Analysis Page 2")
st.sidebar.markdown("- Analysis Page 3")
