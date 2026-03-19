# MiroFish Project Context

**MiroFish** is a next-generation AI prediction and social simulation engine powered by multi-agent technology. It enables users to upload "seed materials" (e.g., news reports, policy drafts, novels), which are then transformed into a high-fidelity digital world where thousands of intelligent agents interact and evolve to predict future outcomes.

## 🏗️ Architecture Overview

The project is structured as a full-stack application with a Python backend and a Vue.js frontend.

### Backend (`MiroFish/backend`)
- **Framework:** Flask (Python 3.11+)
- **Dependency Management:** `uv` (recommended)
- **Key Technologies:**
  - **OASIS (Open Agent Social Interaction Simulations):** The core simulation engine for Twitter/Reddit-like environments.
  - **GraphRAG:** Knowledge extraction and entity relationship mapping from documents.
  - **Zep Cloud:** Long-term memory management for agents.
  - **OpenAI SDK:** Interface for various LLMs (OpenAI, Qwen, etc.).
  - **PyMuPDF:** Document parsing (PDF, TXT, MD).

### Frontend (`MiroFish/frontend` & `MiroFish/frontend-english`)
- **Framework:** Vue 3 + Vite
- **Visualization:** D3.js for graph relationship visualization.
- **API Client:** Axios (communicates with backend at `:5001`).

## 🔄 Core Workflow

1.  **Graph Building:** Extracts entities and relationships from uploaded materials to build a collective memory/knowledge graph.
2.  **Environment Setup:** Generates agent personas and platform configurations (Twitter or Reddit).
3.  **Simulation:** Runs parallel simulations where agents interact based on their personas and the injected context.
4.  **Report Generation:** A specialized `ReportAgent` analyzes simulation data to produce detailed prediction reports.
5.  **Interaction:** Users can "interview" agents within the simulated world or chat with the Report Agent for deeper insights.

## 🚀 Building and Running

### Prerequisites
- Node.js 18+
- Python 3.11 or 3.12
- `uv` (Python package manager)
- API Keys: LLM (OpenAI compatible) and Zep Cloud.

### Setup
1.  **Environment:** Copy `.env.example` to `.env` in the `MiroFish/` root and fill in `LLM_API_KEY`, `LLM_BASE_URL`, and `ZEP_API_KEY`.
2.  **Dependencies:**
    ```bash
    npm run setup:all  # Installs root, frontend, and backend dependencies
    ```

### Development
```bash
npm run dev        # Starts both frontend (port 3000) and backend (port 5001)
npm run backend    # Starts only the backend
npm run frontend   # Starts only the frontend
```

### Docker
```bash
docker compose up -d
```

## 📂 Project Structure

- `MiroFish/backend/app/api/`: REST API endpoints (graph, simulation, report).
- `MiroFish/backend/app/services/`: Core logic for simulation management, IPC, and graph building.
- `MiroFish/backend/scripts/`: Standalone simulation runners and utility scripts.
- `MiroFish/frontend/src/`: Vue components, API services, and D3 visualizations.
- `MiroFish/uploads/`: Storage for uploaded documents and simulation databases.

## 🛠️ Development Conventions

- **Environment Variables:** Always loaded from the root `.env` file.
- **API Communication:** Frontend talks to `/api/*` on the backend.
- **Simulation IPC:** The backend manages simulation processes via JSON-based Inter-Process Communication (IPC) located in simulation directories.
- **Encoding:** The project prioritizes UTF-8 to handle Chinese characters correctly, especially in Windows environments.
