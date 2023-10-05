# DataFest Full Stack LLM App Workshop
This project is a mono-repo template for boostraping a react frontend app and a python fastapi backend for building a full stack LLM app.

# Requirements
<ul>
  <li>CLI Terminal</li>
  <li>Setup <code>Python 3.8+ & Pip 3</code>: I recommend using Pyenv to install python and pip:
    <ul>
      <li>Windows Installation Guide: https://github.com/pyenv-win/pyenv-win</li>
      <li>Mac Installation Guide: https://medium.com/geekculture/setting-up-python-environment-in-macos-using-pyenv-and-pipenv-116293da8e72</li>
      <li>Linux Installation Guide: https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875</li>
    </ul>
  </li>
  <li>NodeJS 16+: https://nodejs.org/en/download</li>
  <li>OpenAI Account and API Key: https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key</li>
  <li>Clone this repo and follow the ReadME instruction for setup: https://github.com/tosinamuda/datafest-llm-workshop</li>
  <li>Working Internet to connect to internet to be able to access OpenAI API</li>
</ul>

## Development Setup
- React Frontend Dependencies are managed through yarn (not NPM) as we rely on yarn workspace for managing the entire monorepo
- Python Backend Dependencies is managed through pipenv
- Entire Monorepo is managed through yarn workspace

### Step by Step Instruction
1. clone this repo by running ```git clone https://github.com/tosinamuda/datafest-llm-workshop.git```
2. Change your directory to datafest-llm-workshop by running: ```cd datafest-llm-workshop```
3. Run ```yarn``` to install all the dependencies
4. Run ```yarn dev`` to start a development environment
5. Run ```yarn start`` to start a production-ready environment


### Monorepo root
1. Ensure you are in the root folder
2. Run ```yarn``` to install dependencies in the root folder to allow the scripts in the workspace run.
3. You can run ```yarn dev``` to start both the frontend and the backend
