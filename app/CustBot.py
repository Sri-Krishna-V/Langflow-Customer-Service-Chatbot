import requests
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "<your_langflow_id>"
FLOW_ID = "<your_flow_id>"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "customer"


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " +
               APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def main():
    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .stChatMessage {
        font-size: 16px !important;
    }
    .feature-card {
        background-color: #1c1c1c;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .feature-card h4, .feature-card p {
        color: #f0f4f8;
    }
    .feature-card:hover {
        transform: scale(1.02);
        background-color: #262626;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .feature-icon {
        font-size: 24px;
        margin-right: 10px;
        color: #f0f4f8;
    }
    .quick-action-button {
        width: 100%;
        text-align: left;
        margin-bottom: 10px;
        padding: 10px;
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        background-color: #f9f9f9;
        transition: background-color 0.3s ease;
    }
    .quick-action-button:hover {
        background-color: #f0f0f0;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🚀 Advanced Customer Support")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Sidebar with feature showcase and quick actions
    st.sidebar.header("🔍 Quick Actions")

    faqs = {
        "What are your shipment times?": "We typically process and ship orders within 1-3 business days. Delivery times vary by location and shipping method selected during checkout.",
        "How can I track my order?": "Once your order is shipped, you'll receive a tracking number via email. You can track your package using our website or the carrier's tracking system.",
        "What is your return policy?": "We offer a 30-day hassle-free return policy. Items must be unused, in original packaging, and accompanied by the original receipt.",
        "What payment methods do you accept?": "We accept major credit cards (Visa, MasterCard, American Express), PayPal, Apple Pay, and Google Pay for your convenience."
    }

    # Sidebar for FAQ buttons
    st.sidebar.header("Quick Questions")
    for question in faqs.keys():
        if st.sidebar.button(question, key=question):
            # Simulate sending FAQ question to chat
            st.session_state.chat_history.append({
                'role': 'user',
                'content': question
            })

            # Get AI response for the FAQ
            try:
                response = run_flow(question)
                bot_response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                st.session_state.chat_history.append({
                    'role': 'assistant',
                    'content': bot_response
                })
            except Exception as e:
                st.session_state.chat_history.append({
                    'role': 'assistant',
                    'content': f"Error processing your question: {str(e)}"
                })

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # Customer Support Information
    st.sidebar.header("Contact Support")
    st.sidebar.markdown("""
    📧 Email: support@yourcompany.com
    📞 Phone: 1-800-123-4567
    
    Available: Monday to Friday
    9 AM to 5 PM (local time)
    """)

    # Feature Explanation Section
    st.markdown("## 🌟 What Can I Help You With?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 Order Tracking</h4>
            <p>Easily track your order status by providing your order number.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <h4>📋 Product Details</h4>
            <p>Get comprehensive information about any product in our catalog.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>❓ FAQ Support</h4>
            <p>Instant answers to common questions about shipping, returns, and more.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <h4>🌐 Comprehensive Assistance</h4>
            <p>Our AI can help you with a wide range of customer support queries.</p>
        </div>
        """, unsafe_allow_html=True)

    # Chat History and Input
    for message in st.session_state.chat_history:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # Chat input
    prompt = st.chat_input(
        "Ask me anything about your order, products, or support...")

    if prompt:
        # Add user message to chat history
        st.session_state.chat_history.append({
            'role': 'user',
            'content': prompt
        })

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Show loading spinner and get response
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                try:
                    response = run_flow(prompt)
                    bot_response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                    st.markdown(bot_response)

                    # Add bot response to chat history
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': bot_response
                    })
                except Exception as e:
                    st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
