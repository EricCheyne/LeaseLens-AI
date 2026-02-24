# LeaseLensAI
**AI Lease Financial Workflow Automation SaaS**

LeaseLensAI is a multi-tenant platform designed to automate the painful process of lease abstraction and financial reconciliation for property managers and asset managers. By leveraging AI-driven extraction and structured financial modeling, it transforms manual PDF-based workflows into automated, error-free accounting operations.

---

## 🏗 Architecture

LeaseLensAI follows a modern, scalable multi-tenant architecture:

- **Frontend:** Next.js + Tailwind CSS (Responsive Dashboard)
- **Backend:** FastAPI (Python) - High-performance asynchronous API
- **Database:** PostgreSQL + `pgvector` (Structured data + Semantic Search)
- **Storage:** AWS S3 (Secure document storage)
- **AI/ML:** LLM-based extraction (NLP) and chunking pipelines
- **Workers:** Background processing for PDF parsing and forecasting
- **Auth:** Multi-tenant isolation with Row-Level Security (RLS)

---

## ⚙️ Services

- **API Service:** Handles authentication, multi-tenant logic, and CRUD operations.
- **Extraction Engine:** Asynchronous worker that processes PDF uploads, extracts key terms, and generates embeddings.
- **Financial Engine:** Generates amortized payment schedules, escalation projections, and reconciliation reports.
- **Search Service:** Vector-based semantic search across lease documents.

---

## 🛠 Local Development

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL with `pgvector` extension
- Docker (optional, for local services)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/LeaseLens-AI.git
   cd LeaseLens-AI
   ```

2. **Backend Setup:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

3. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

---

## 🔑 Environment Variables

Create a `.env` file in both `backend/` and `frontend/` directories.

**Backend (.env):**
- `DATABASE_URL`: PostgreSQL connection string
- `AWS_S3_BUCKET`: Storage bucket name
- `OPENAI_API_KEY`: For AI extraction and embeddings
- `SECRET_KEY`: JWT signing key

**Frontend (.env):**
- `NEXT_PUBLIC_API_URL`: Backend API endpoint

---

## 🚀 Roadmap

### Phase 1: MVP (Core Extraction)
- [ ] Multi-tenant Auth & Organization management
- [ ] Secure PDF upload to S3
- [ ] AI-powered extraction (Base Rent, Term, Escalations)
- [ ] Structured Lease Dashboard

### Phase 2: Financial Automation
- [ ] Amortized Payment Schedule Engine
- [ ] Rent Roll Reconciliation Tool
- [ ] Basic 12-month Revenue Forecasting

### Phase 3: Enterprise & Scaling
- [ ] Advanced Monte Carlo Risk Simulation
- [ ] Full Audit Trails & SOC2 Logging
- [ ] Export to Excel/ERP (Yardi, MRI integration)
- [ ] Semantic search across portfolio documents

