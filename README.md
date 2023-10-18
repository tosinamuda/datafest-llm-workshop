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
  <li>OpenAI Account and API Key: https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key OR Cloudflare AI API key: https://developers.cloudflare.com/workers-ai/get-started/rest-api/</li>
  <li>Clone this repo and follow the ReadME instruction for setup: https://github.com/tosinamuda/datafest-llm-workshop</li>
  <li>Working Internet to connect to internet to be able to access OpenAI API</li>
</ul>

## Development Setup

- React Frontend Dependencies are managed through yarn (not NPM) as we rely on yarn workspace for managing the entire monorepo
- Python Backend Dependencies is managed through pipenv
- Entire Monorepo is managed through yarn workspace

### Step by Step Instruction

1. clone this repo by running `git clone https://github.com/tosinamuda/datafest-llm-workshop.git`
2. Change your directory to datafest-llm-workshop by running: `cd datafest-llm-workshop`
3. Run `yarn` to install all the dependencies
4. Copy the `.env.sample` to `.env` and replace the `OPENAI_API_KEY` or `CF_API_KEY` (Cloudflare API Key, include your CF Account ID if using cloudflare ) in .env with your own API Key
5. Run ``yarn dev` to start a development environment
6. If everything runs well, visit localhost:8000/docs for the apis and localhost:5173 for the frontend
7. Run ``yarn start` to start a production-ready environment
