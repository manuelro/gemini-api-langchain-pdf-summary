## About
This project demonstrates how to summarize PDF documents using artificial intelligence. Both examples use Google Gemini AI, but one uses [LangChain](https://python.langchain.com/docs/get_started/introduction) and the other one accesses [Gemini AI API](https://deepmind.google/technologies/gemini/#introduction) directly.

### `geminiai-api-example.py` - Google Gemini AI API Implementation
This example implements Google Gemini AI API directly (using the PDF loader from LangChain for simplicity).

### `langchain-example.py` - LangChain Implementation
This example (the default one) implements LangChain abstraction.

## Installation:

### Step 1: Setup Your Environment (assuming you are using MacOS)
1. `python -m venv/venv` - Creates a new virtual environment, we will use this to store temporary API keys in a secure way.
2. `source venv/bin/activate` - Activate the virtual environment.

See [this guide](https://docs.python.org/3/library/venv.html) if you are using other operating systems.

### Step 2: Istall Dependencies and Configure Your API Key
Run the following commands in order to install the required dependencies and configure your `GOOGLE_API_KEY`:

1. `pip install -r requirements.txt` - Install the required packages.
2. `export GOOGLE_API_KEY="your_google_api_key"` - You can obtain your API key by going to [Google AI Studio](https://makersuite.google.com/app/apikey) and following the instructions.

### Step 3: Run the Project
Run one of the following commands in order to run either one of the examples:
1. `python geminiai-api-example.py` - Optional, this uses Gemini AI API.
2. `python langchain-example.py` - Optional, this uses LangChain.
___

### How to Tweak It
Either is you are running the `langchain-example.py` (LangChain) or the `geminiai-api-example.py` (Gemini AI API), you simply need to modify lines `5` or `10` of each of the files if you would like to see different results in your output.

___
### Example Output for a 5 Pages PDF File
The output for the current PDF (which contains five pages) is as follows:
>Climate change poses risks to businesses, including physical risks like floods and droughts, price risks due to resource scarcity, product risks from shifting preferences, ratings risks from investors, regulation risks from government action, and reputation risks from public perception. Companies can adapt by forecasting scenarios, investing in resilience, and embracing sustainability.

![Demo Output](https://raw.githubusercontent.com/manuelro/gemini-api-langchain-pdf-summary/master/screenshots/output.png)

