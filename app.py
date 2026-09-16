import streamlit as st
import anthropic

st.title("Aerchain — API Test")
st.caption("Proving a real Claude API call works before we build features.")

# Read the API key from Streamlit's secure secrets store (not hardcoded)
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

# A text box for the user to type into
user_text = st.text_area("Type something and click Send:", "Say hello in one sentence.")

if st.button("Send to Claude"):
    with st.spinner("Calling Claude..."):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=500,
            messages=[{"role": "user", "content": user_text}],
        )
        st.success("Claude replied:")
        st.write(message.content[0].text)