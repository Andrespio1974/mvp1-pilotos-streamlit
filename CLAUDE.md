# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MVP for a pilot training AI coach built with Streamlit. The application provides a chat interface where pilots can interact with a fine-tuned OpenAI model specifically trained for CBTA/EBT (Competency-Based Training & Assessment / Evidence-Based Training) scenarios.

## Architecture

- **Single-file application**: `streamlit_app.py` contains the entire application
- **Streamlit-based**: Web interface using Streamlit framework
- **OpenAI integration**: Uses fine-tuned GPT-4o-mini model for pilot coaching
- **Session-based chat**: Conversation history maintained in Streamlit session state
- **Cloud deployment ready**: Configured for Streamlit Community Cloud deployment

## Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application locally (Windows PowerShell)
$env:OPENAI_API_KEY="sk-..." ; $env:OPENAI_MODEL="ft:gpt-4o-mini-2024-07-18:alphapio::By30iumK"
streamlit run streamlit_app.py

# Run the application locally (Unix/Linux/MacOS)
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="ft:gpt-4o-mini-2024-07-18:alphapio::By30iumK"
streamlit run streamlit_app.py
```

### Environment Configuration
- Requires `OPENAI_API_KEY` environment variable or Streamlit secret
- Uses specific fine-tuned model: `ft:gpt-4o-mini-2024-07-18:alphapio::By30iumK`
- Temperature is configurable via sidebar (default: 0.3)

## Key Components

### Chat System
- Messages stored in `st.session_state.messages`
- System prompt defines the AI as a CBTA/EBT training coach
- Custom CSS styling for chat bubbles and layout
- Avatar system: 🧑‍✈️ for users, 🤖 for assistant

### UI Features
- Sidebar configuration panel with temperature control
- Clear chat functionality
- Sticky input container at bottom
- Responsive layout with max-width constraint
- Custom styling for professional aviation training appearance

## Deployment

This application is designed for Streamlit Community Cloud deployment:
1. Push to GitHub repository
2. Connect via https://share.streamlit.io/
3. Configure secrets for `OPENAI_API_KEY` and `OPENAI_MODEL`
4. Application will be available at public URL