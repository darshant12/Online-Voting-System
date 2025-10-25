# Online Voting System

A small Flask-based online voting demo that lets users vote for candidates and view results. This repository contains a minimal web app used for learning and demonstration purposes.

## Features

- Simple voting form
- View current results
- Persists vote counts to a CSV file (`votes.csv`)

## Prerequisites

- Python 3.8 or newer
- pip

## Setup (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the app

From the project root run:

```powershell
python app.py
```

Open your browser at http://127.0.0.1:5000/ to access the app.

## Project structure

```
.
├─ app.py           # Main Flask application
├─ models.py        # (present but currently unused in this project)
├─ votes.csv        # CSV file used to persist vote counts
└─ templates/       # HTML templates
   ├─ index.html
   ├─ results.html
   └─ success.html
```

## Data storage

Votes are stored in `votes.csv` as simple rows of `candidate,votes`. The app writes the whole candidates dictionary back to the CSV on each vote.

If you want to reset the counts, you can either edit `votes.csv` directly or delete it and the app will recreate it on the next vote (initial counts are defined in `app.py`).

## Notes

- This is a demo application and is not production-ready. It does not include authentication, input validation against tampering, or concurrency-safe writes for multiple simultaneous users.
- For production use consider a proper database and user/session management.

## Contributing

Feel free to open issues or pull requests. Small improvements that help with documentation, packaging, or tests are welcome.

## License

This project is provided as-is for learning purposes. Add a license file if you plan to publish it publicly.
