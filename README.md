# AgriGene-AI: AI-Based Crop Recommendation System

An AI-powered agricultural decision-support application designed to assist users with crop selection, soil-related insights, and agricultural recommendations.

## Overview

**AgriGene-AI** is a Python-based project that aims to support data-driven agricultural decisions through crop recommendation and soil analysis. The application brings together agricultural information and machine-learning-oriented functionality in an accessible software interface.

The project focuses on helping users explore suitable crop options, understand soil-related conditions, and access relevant agricultural guidance.

## Objectives

- Provide crop recommendations using available agricultural input data.
- Support soil diagnosis and soil-related decision-making.
- Present fertilizer guidance where supported by the application.
- Integrate weather information where API configuration and connectivity are available.
- Maintain an accessible interface for agricultural decision support.
- Apply software testing practices to evaluate application components.

## Features

- **Crop Recommendation:** Supports crop-selection recommendations based on the inputs and prediction logic implemented in the application.
- **Soil Diagnosis:** Provides soil-related analysis through the implemented soil module.
- **Fertilizer Guidance:** Offers fertilizer-related information where supported by the application.
- **Weather Integration:** Designed to use weather information when the required API configuration is available.
- **Data Insights:** Provides agricultural data-related insights through the implemented functionality.
- **Application History:** Supports history-related functionality using a local database where enabled.
- **Testing:** Includes automated tests for the soil module.

> Feature availability depends on the current implementation, required datasets, configuration, and external service availability.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| User interface | Streamlit, if enabled in the current application |
| Data storage | SQLite |
| Testing framework | pytest |
| Version control | Git and GitHub |
| Development environment | Visual Studio Code |

## Project Structure

The following is a representative structure. Update it to match the actual files in the repository.

```text
AI-Based-Crop-Recommendation-System/
├── tests/
│   └── test_soil.py
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── history.db
└── ...
```

- `app.py` — application entry point, if this is the file used to launch the application.
- `tests/test_soil.py` — automated tests for soil-related functionality.
- `requirements.txt` — Python dependencies required to run the application.
- `history.db` — local application database, if used by the implementation.

## Prerequisites

Before running the project, ensure that you have:

- Python installed.
- Git installed.
- A code editor such as Visual Studio Code.
- The project source code and required datasets.
- API credentials in environment variables or an appropriate local secrets configuration if external services require them.

## Installation and Setup

### 1. Clone the repository

Replace the URL below with the actual URL of your GitHub repository.

```bash
git clone https://github.com/aryan-mukherjee-cs/AgriGene-AI.git
cd AgriGene-AI
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

If a complete and up-to-date `requirements.txt` is available, run:

```bash
python -m pip install -r requirements.txt
```

If the dependency file is missing or incomplete, install the dependencies specified by the actual project source code rather than assuming a package list.

### 5. Configure environment variables

If the application uses external APIs, configure the required credentials locally.

Do not commit API keys, passwords, tokens, or private configuration files to GitHub.

### 6. Run the application

If `app.py` is the actual Streamlit entry point, run:

```bash
streamlit run app.py
```

If the application uses a different entry point, replace `app.py` with the correct filename.

## Testing

The project includes automated tests for soil-related functionality using `pytest`.

Run the soil test suite from the project root:

```bash
python -m pytest tests/test_soil.py -v
```

**Previously recorded test result:** 18 passed, 0 failed.

This result refers to the reported execution of the soil test suite and should not be interpreted as proof that every application module has been tested.

Additional testing can cover:

- Valid and invalid user inputs.
- Crop recommendation logic.
- Soil diagnosis.
- Error handling and missing data.
- Database operations.
- External API failures.
- User interface behaviour.

Only report additional test results after executing the corresponding tests.

## Security and Data Handling

- Keep API keys and credentials outside version control.
- Exclude virtual environments, caches, and generated files from Git.
- Avoid publishing databases containing personal or sensitive information.
- Review datasets and model artifacts before making the repository public.
- Use `.gitignore` to exclude local files that do not belong in the public source repository.

## Limitations

- Recommendation quality depends on the accuracy, coverage, and suitability of the available data.
- External weather services may require API credentials and internet connectivity.
- Model performance should be evaluated using documented experiments before making claims about accuracy.
- Agricultural recommendations should be interpreted in the context of local climate, soil conditions, irrigation, season, and expert guidance.
- The presence of a testing module does not establish that every feature has been independently validated.

## Future Enhancements

Potential extensions include:

- Integration of additional verified agricultural datasets.
- Improved model evaluation and validation.
- More comprehensive soil and fertilizer decision support.
- Regional and seasonal crop recommendations.
- Improved uncertainty reporting and explainability.
- A more comprehensive automated testing suite.
- Deployment through a suitable cloud hosting platform.
- Mobile-friendly interface improvements.

These are proposed enhancements and are not necessarily implemented in the current version.

## Contributing

Contributions are welcome where permitted by the project owner.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Submit a pull request describing the changes and test results.

## License

No license has been specified in this repository. Unless a license is added, the source code should not be assumed to be available for unrestricted reuse. Add an appropriate license only after confirming that you have the right to distribute the project under its terms.

## Author

**Aryan Mukherjee**  
GitHub: [@aryan-mukherjee-cs](https://github.com/aryan-mukherjee-cs)

## Acknowledgements

This project is developed as an agricultural decision-support and software engineering initiative focused on applying data-driven methods to crop recommendation and soil-related analysis.
