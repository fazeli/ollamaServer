# Ollama Server

## Overview

Ollama Server is a project designed to provide a robust and scalable server environment for various applications. This project uses Python 3.12 and a virtual environment to manage dependencies.

Using Ollama you can run your LLM models locally so you don't have to pay to use the models for developement. Supported local LLMs are here:
https://github.com/ollama/ollama/blob/main/README.md#quickstart

## Setup

To set up the project, follow these steps:

1. Donwload and install Ollama locally from here: https://ollama.com/download
2. Create a virtual python environment by following these steps:
   - Create a new folder and in your terminal with the folder path then type:
     - on Windows: python -m venv openai-api
     - on Mac: source openai-env/bin/activate
   -
3. Activate the virtaul environment by following these steps while you are at your terminal:

   - on Windows: openai-env\Scripts\activate.bat
   - on Mac: source openai-env/bin/activate

4. Install the required dependencies by running this command while still at your terminal and on same path:
   pip install -r requirements.txt

## Usage

1. To run Ollama, while at your terminal on the same path run:
   ollama serve
2. Open another termianl and then run: For reuirements of your phisycal machine requirements check Ollama's page before choosing a model
   ollama run <The model that you intend to use> e.g. ollama run llama3.2:1b
3. To run the server, in another termianl then type command:
   python server.py

4. Testing if everything is OK! Once the above steps are done successfully, you can test to make sure the endpints are working:

   - on Windows: Either use postman or run the this command in Git Bash
     curl -X POST http://localhost:3000/api/chat \
      -H "Content-Type: application/json" \
      -d '{"prompt": "Give me an exercise plan for today. Keep it short in 50 words."}'
   - on Mac: ust run the above command!

5. Now that your endpoint is running you can have your client app to use the api endpoint to use your model locally.

## Project strusture

Your project strusture after installing dpendencies should look like this:

--Project
-openai-api
-openai-env
-.env
-requirements
-server.py

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
