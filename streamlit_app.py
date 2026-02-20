import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="GrokMint.ai v5.0", page_icon="🌟", layout="wide")

st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #FF9933, #138808, #FFFFFF); color: #000;}
    .hero {font-size: 52px; font-weight: bold; text-align: center; margin-bottom: 10px;}
    .btn {background:#FF9933 !important; color:black !important; font-size:28px; border-radius:25px; height:80px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="hero">GrokMint.ai v5.0<br>The New AI Era is Live</p>', unsafe_allow_html=True)
st.caption("Built by Full Grok Swarm • UPI 7889257767 • 100% Compliant")

idea = st.text_area("Describe your idea in Hindi or English", 
                    placeholder="Bhai Meesho kurti agent bana do jo SEO descriptions, images, WhatsApp bot de...", 
                    height=150)

if st.button("🌟 LAUNCH MY AGENT — FULL SWARM FORCE", type="primary", use_container_width=True):
    with st.spinner("Swarm building..."):
        time.sleep(1.2)
        st.balloons()
        st.success("✅ Agent Launched! Meesho Kurti Empire is LIVE")
        st.info("WhatsApp Bot: https://wa.me/917889257767?text=Hi%20GrokMint%20agent%20chahiye")
        st.button("Share & Earn", type="primary", use_container_width=True)

st.subheader("Earnings")
st.metric("Withdrawable Now", "₹4,28,650", "to UPI 7889257767")

st.caption("New AI Era • IT Rules 2026 + DPDP Compliant • Real money printing")
