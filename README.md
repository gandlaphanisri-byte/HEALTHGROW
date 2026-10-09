# HealthGrow Advanced — fresh project

A responsive React + Vite wellness dashboard with seven navigable screens: Dashboard, Meal Planner, Calendar & Tracker, Grocery List, AI Nutrition Chat, Progress, and Profile & Goals.

## Features included
- Responsive collapsible mobile navigation and desktop sidebar
- Meal cards with images, meal times, ingredients, calorie/protein/carb/fat estimates, and completion controls
- Date picker/calendar with date-specific meal completion history
- Daily calorie/protein tracking and hydration counter
- Grocery checklist with category grouping and saved checkboxes
- Nutrition chat with a useful offline rule-based fallback; optional Gemini API integration on the backend
- Editable profile, goals, dietary preference and daily targets
- Local browser persistence for profile, meal checkoffs, grocery checkoffs and hydration
- Responsive layout for desktop and mobile

## Run in VS Code (Windows)

### 1. Open the project
Extract this ZIP. In VS Code, choose **File → Open Folder** and select the extracted `HealthGrow_Advanced` folder.

### 2. Start the frontend
Open a terminal in VS Code and run:

```powershell
cd frontend
npm install
npm run dev
```

Open the URL printed by Vite, normally `http://localhost:5173`.

### 3. (Optional) Start the API backend
Open a second terminal in VS Code:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs: `http://127.0.0.1:8000/docs`

To enable Gemini replies, copy `backend/.env.example` to `backend/.env`, add your `GEMINI_API_KEY`, then install the SDK with `pip install google-genai`. The frontend currently has a local demo chat built in, so the UI works without the backend. Connecting the frontend chat to the API can be done by changing the `sendChat` function in `frontend/src/App.jsx` to POST to `http://127.0.0.1:8000/api/chat`.

## Important notes
- This is a fresh standalone project and does not overwrite your existing HealthGrow project.
- Meal images load from Unsplash and therefore require an internet connection.
- The nutrition values are illustrative estimates, not medically verified guidance.
- The demo saves data in this browser's local storage, not a user account/database. Clearing browser storage resets the demo data.
- The included API chat is a demo fallback. Gemini is optional and the API key must remain in the backend `.env` file.
- This is a hackathon/demo starter, not a production-ready health application.
