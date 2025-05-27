# Langflow Customer Service Chatbot

An intelligent customer service chatbot built with Langflow and Streamlit that provides automated support for customer inquiries.

## Features

- 🤖 AI-powered responses to customer inquiries
- 📊 Order tracking and status information
- 📋 Product details and catalog information
- ❓ FAQ support for common questions
- 💬 Interactive chat interface with Streamlit

## Dataset

The project includes sample data:
- `sample_orders.csv` - Order information with customer details
- `sample_products.csv` - Product catalog with descriptions and pricing
- `Company_FAQ.pdf` - Frequently asked questions documentation

## Setup

1. Clone the repository
2. Create a `.env` file with your Langflow API token:
   ```
   APP_TOKEN=your_token_here
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Update the configuration in `app/CustBot.py`:
   - Set your `LANGFLOW_ID`
   - Set your `FLOW_ID`

## Usage

Run the application:

```bash
streamlit run app/CustBot.py
```

## Requirements

- Python 3.8+
- Streamlit
- Requests
- python-dotenv
- Langflow API access

## License

MIT 