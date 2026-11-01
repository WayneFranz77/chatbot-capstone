import streamlit as st

from src.chatbot import ChatBot

# Create chatbot instance
chatbot = ChatBot()

# Page settings
st.set_page_config(
    page_title="AI Career Advisor Chatbot", page_icon="🤖", layout="centered"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 AI Career Advisor Chatbot")

# Sidebar
with st.sidebar:

    st.header("📊 Project Information")

    st.success("✅ TF-IDF Enabled")
    st.success("✅ Intent Classification")
    st.success("✅ Entity Recognition")
    st.success("✅ Word2Vec Enabled")
    st.success("✅ Streamlit GUI")

    st.divider()

    st.header("📚 Current Knowledge Base")

    st.write("• Python")
    st.write("• Machine Learning")
    st.write("• Deep Learning")
    st.write("• Data Science")
    st.write("• TensorFlow")
    st.write("• PyTorch")
    st.write("• NumPy")
    st.write("• Pandas")
    st.write("• Azure AI Certifications")
    st.write("• AI Careers")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main page content
st.markdown("""
Ask questions about:

- Python
- Machine Learning
- Deep Learning
- Data Science
- TensorFlow
- PyTorch
- Azure AI Certifications
- AI Careers
""")

# Chat input
user_input = st.chat_input("Ask a question...")

# Process new message
if user_input:

    result = chatbot.get_response(user_input)

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    confidence = result["confidence"]

    if confidence >= 0.40:
        confidence_status = "🟢 High Confidence"

    elif confidence >= 0.20:
        confidence_status = "🟡 Medium Confidence"

    else:
        confidence_status = "🔴 Low Confidence"

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": f"**Intent:** {result['intent']}\n\n"
            f"{confidence_status}\n\n"
            f"**Confidence Score:** {confidence:.2%}\n\n"
            f"**Entities:** "
            f"{', '.join(result['entities']) if result['entities'] else 'None'}\n\n"
            f"{result['response']}",
        }
    )

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Footer
st.divider()

st.caption(
    "AI Career Advisor Chatbot | "
    "Built with Python, NLP, TF-IDF, "
    "Word2Vec, Scikit-Learn and Streamlit"
)
