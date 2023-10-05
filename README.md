# FastReact: REACT + FASTAPI Monorepo
This project is a mono-repo template for boostraping a react frontend app and a python fastapi backend app all orchestrated using yarn workspace

# Requirements
- Python 3.7 +
- Pip 3
- Node JS 16+

## Local Development Setup
- React Frontend Dependencies are managed through yarn (not NPM) as we rely on yarn workspace for managing the entire monorepo
- Python Backend Dependencies is managed through pipenv
- Entire Monorepo is managed through yarn workspace

### Frontend Setup
1. Change your directory to frontend by running ```cd frontend```
2. Run ```yarn``` to install all the dependencies


### Backend Setup
1. Change your directory to backend by running ```cd backend```
2. Run ```yarn preinstall``` to install all the dependencies


### Monorepo root
1. Ensure you are in the root folder
2. Run ```yarn``` to install dependencies in the root folder to allow the scripts in the workspace run.
3. You can run ```yarn dev``` to start both the frontend and the backend

