DefaultDetect/
│
├── app/                        # Streamlit app
│   ├── __init__.py
│   ├── main.py              # Main app entry point
│   ├── pages/
│   │   ├── 1_Home.py
│   │   ├── 2_Problem_Statement.py
│   │   ├── 3_Data_Overview.py
│   │   ├── 4_Model_Development.py
│   │   └── 5_Results.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── model_utils.py
│   │   └── visuals.py
│   └── components/
│
├── .streamlit/                # Streamlit config
│   └── config.toml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/                      # Internal documentation, notes, planning
│   ├── planning.md
│   ├── overview.md
│   └── todos.md
│
├── notebooks/                 # Jupyter notebooks for dev/EDA
│   ├── 00_data_exploration.ipynb
│   ├── 01_data_cleaning.ipynb
│   └── 02_modeling.ipynb
│
├── quarto/                    # Formal reporting via Quarto
│   ├── _quarto.yml                 # Main Quarto config
│   ├── index.qmd                   # Landing page or Executive Summary
│   ├── 01_problem_statement.qmd
│   ├── 02_data_overview.qmd
│   ├── 03_methodology.qmd
│   ├── 04_model_development.qmd
│   ├── 05_results_and_evaluation.qmd
│   ├── 06_business_implications.qmd
│   ├── 07_conclusion.qmd
│   ├── references.qmd              # For citations
│   └── images/                     # All figures/plots used in the report
│
├── reports/                   # Executive summary, brief writeups
│   └── summary.md
│
├── src/                       # Modular codebase
│   ├── __init__.py
│   ├── data_prep.py
│   ├── modeling.py
│   └── utils.py
│
├── tests/                     # Unit tests
│   └── test_modeling.py
│
├── setup.sh                 # Optional: Heroku/Docker setup
├── Procfile                 # Required for Heroku
├── environment.yml            # Conda environment file
├── README.md                  # Project overview
├── requirements.txt           # Optional: for pip-based use
└── .gitignore

