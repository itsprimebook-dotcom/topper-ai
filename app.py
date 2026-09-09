
import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(
    page_title="Topper Classes | AI Study Portal",
    page_icon="🎓",
    layout="wide"
)

# ध्यान दें: नीचे अपनी स्टेप 1 वाली API Key पेस्ट करें
import os

API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

col_logo, col_text = st.columns([1, 4])

with col_logo:
    try:
        st.image("logo.jpg", width=170)
    except:
        st.title("🎓")

with col_text:
    st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0px;'>TOPPER CLASSES</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top: 0px; color: #E0E0E0;'>By : Vikash Verman</h3>", unsafe_allow_html=True)
    st.caption("Better Education • Brighter Future | WBBSE Class X AI Portal")
    st.markdown("🎯 *Concepts Made Simple | Regular Practice | Personal Guidance | Exam Success*")

st.divider()

tab1, tab2, tab3 = st.tabs([
    "🔍 WBBSE डाउट समाधान (प्रमाण सहित)", 
    "✍️ आंसर-शीट चेकर (मात्रा व अंक)",
    "⏳ इतिहास टाइमलाइन व साक्ष्य"
])

with tab1:
    st.subheader("📚 WBBSE कक्षा 10 डाउट क्लीयरेंस")
    subject = st.selectbox(
        "विषय चुनें:",
        ["इतिहास", "भूगोल", "भौतिक विज्ञान", "जीवन विज्ञान", "गणित", "हिंदी/प्रथम भाषा", "अंग्रेजी"]
    )
    user_question = st.text_area("अपना प्रश्न या डाउट लिखें:")
    if st.button("समाधान और प्रमाण देखें"):
        if user_question:
            prompt = f"आप Topper Classes के WBBSE कक्षा 10 के शिक्षक हैं। विषय: {subject}, प्रश्न: {user_question}। कृपया विस्तृत उत्तर दें और अंत में WBBSE पुस्तक के अध्याय का प्रमाण जोड़ें।"
            res = model.generate_content(prompt)
            st.write(res.text)

with tab2:
    st.subheader("📝 आंसर शीट चेकर व वर्तनी जांच")
    uploaded_image = st.file_uploader("कॉपी की फ़ोटो अपलोड करें", type=["jpg", "jpeg", "png"])
    max_score = st.number_input("कुल अंक (Total Marks):", min_value=1, max_value=20, value=5)
    if uploaded_image and st.button("कॉपी जांचें"):
        img = Image.open(uploaded_image)
        st.image(img, caption="अपलोड की गई कॉपी", width=300)
        eval_prompt = f"आप WBBSE बोर्ड के परीक्षक हैं। इस कॉपी को {max_score} में से अंक दें, मात्रा/वर्तनी की गलतियाँ बताएं और पूरे अंक लाने के उपाय लिखें।"
        eval_res = model.generate_content([eval_prompt, img])
        st.write(eval_res.text)

with tab3:
    st.subheader("⏳ इतिहास टाइमलाइन व साक्ष्य")
    event_query = st.text_input("घटना का नाम दर्ज करें:")
    if st.button("तारीख देखें"):
        if event_query:
            hist_prompt = f"WBBSE क्लास 10 इतिहास के अनुसार इस घटना की सही तारीख और प्रमाण बताएं: {event_query}"
            hist_res = model.generate_content(hist_prompt)
            st.write(hist_res.text)
