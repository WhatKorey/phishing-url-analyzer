import streamlit as st
from phishing_analyzer import analyze_url

st.title("Phishing URL Analyzer")
st.caption("Check a URL for unencrypted HTTP without opening the link")
url = st.text_input("Enter a URL", placeholder="https://example.com")




if st.button("Analyze", type="primary"):
    if url.strip():
        st.info(analyze_url(url))
    else:
        st.warning("Enter a URL first.")

with st.expander("What does this check?"):
    st.write("The app checks whether a URL starts with htt:// or https://. A phishing site can use HTTPS too.")
    st.write("It also checks for the presence of an @ symbol, which can be used to obscure the real destination.")