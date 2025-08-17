# FastAPI Data Analysis Service

An AI-powered data analysis service that accepts file uploads and generates Python code to answer questions about the data.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your OpenAI API key
4. Run: `python app.py`

## Usage

Send POST requests to `/api/` with:
- `questions.txt` file containing your question
- Data files (CSV, images, archives)

## License

MIT License - see LICENSE file for details.
