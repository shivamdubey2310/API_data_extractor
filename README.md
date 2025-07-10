# API Data Extractor 🔍

A simple and professional web app built with Streamlit that allows users to extract and download JSON data from any free public API endpoint.

---

## 🎓 Features

* Easy-to-use web interface
* Extracts and saves API responses in JSON format
* Optional timestamped file downloads
* Data preview option before downloading
* Error handling and clean user feedback

---

## 💪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shivamdubey2310/api-data-extractor.git
cd api-data-extractor
```

### 2. Install Dependencies

I recommend using a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📚 Project Structure

```
api-data-extractor/
├── app.py                  # Main Streamlit app
├── BackEnd.py              # Custom backend logic for data extraction
├── raw_json/               # Folder to store downloaded JSON files
├── requirements.txt        # Python dependencies
├── Environment             # Python virtual environment
└── README.md               # Project documentation
```

---

## 🔧 Backend Function Requirements

The `BackEnd.py` file should include the following functions:

```python
def extract_domain_name(api_url: str) -> str:
    # Extract domain name from URL
    pass

def Extracting_data(api_url: str, domain: str):
    # Fetch and save JSON data to raw_json/{domain}_raw.json
    pass
```

---

## 🚀 To-Do / Future Features

* API key/auth token support
* Response format customization (CSV, XLSX)
* Better error reporting (status codes, response time)

---

## 👨‍💼 Author

**Shivam Dubey**
*Data Engineering Enthusiast*

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
