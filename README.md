# TourAG2 - Agentic RAG System for Tours

TourAG2 is an intelligent chat application that provides information about concerts and music tours using advanced AI capabilities.

## Overview

This application uses a conversational interface powered by Gradio to help users find information about concerts, music tours, and related events. The agent specifically searches platforms like Songkick and Festivaly.eu to provide accurate and up-to-date information.

## Features

- Interactive chat interface for querying about concerts and music tours
- Integration with DuckDuckGo search for retrieving real-time information
- Domain-specific search focusing on music events databases
- Multi-language support (responds in the same language as the question)
- Powered by Google's Gemini 2.0 Flash model

## Requirements

- Python 3.10 or higher
- Required packages (managed via dependencies):
  - gradio (5.34.0+)
  - python-dotenv (1.1.0+)
  - smolagents (1.18.0+)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tourag2
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Create a `.env` file in the project root and add your API key:
   ```
   GEMINI_API=your_gemini_api_key_here
   ```

## Usage

To start the application, run:

```bash
python app.py
```

This will launch a Gradio web interface where you can interact with the agent by asking questions about concerts and music tours.

## Project Structure

- `app.py`: Main application file that sets up the Gradio interface
- `agent.py`: Contains the AI agent implementation using smolagents
- `tools/`: Directory for any additional custom tools
- `pyproject.toml`: Project configuration and dependencies

## How It Works

The application uses an agent-based approach where:

1. User queries are processed through a Gradio chat interface
2. The agent processes the query using the Gemini 2.0 Flash model
3. If needed, the agent performs searches on music event websites via DuckDuckGo
4. The agent formulates and returns a concise response to the user

## Environment Variables

- `GEMINI_API`: Your Google Gemini API key

## License

See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
# TourAG2 - Agentic RAG System for Tours

TourAG2 is an intelligent chat application that provides information about concerts and music tours using advanced AI capabilities.

## Overview

This application uses a conversational interface powered by Gradio to help users find information about concerts, music tours, and related events. The agent specifically searches platforms like Songkick and Festivaly.eu to provide accurate and up-to-date information.

## Features

- Interactive chat interface for querying about concerts and music tours
- Integration with DuckDuckGo search for retrieving real-time information
- Domain-specific search focusing on music events databases
- Multi-language support (responds in the same language as the question)
- Powered by Google's Gemini 2.0 Flash model

## Requirements

- Python 3.10 or higher
- Required packages (managed via dependencies):
  - gradio (5.34.0+)
  - python-dotenv (1.1.0+)
  - smolagents (1.18.0+)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tourag2
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install uv:
   ```bash
   pip install uv
   ```

4. Install dependencies using uv:
   ```bash
   uv pip install -e .
   ```

5. Create a `.env` file in the project root and add your API key:
   ```
   GEMINI_API=your_gemini_api_key_here
   ```


## Usage

To start the application, run:

```bash
python app.py
```

This will launch a Gradio web interface where you can interact with the agent by asking questions about concerts and music tours.
