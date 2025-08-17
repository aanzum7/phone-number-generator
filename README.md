```markdown
# Bangladesh Mobile Number Generator

## Overview
The **Bangladesh Mobile Number Generator** is a Streamlit-based web application designed to generate Bangladesh mobile numbers quickly and efficiently. Users can select a mobile operator, choose a prefix, specify the number of phone numbers to generate, preview a sample, and download the dataset in either `xlsx` or `csv` format. Each operator comes with its unique theming for a professional and visually appealing interface.

---

## 🎨 Key Features

- **Operator-Themed UI:** Unique color schemes for background, headers, buttons, inputs, and tables per operator.  
- **Interactive Sidebar:** Displays project and author information.  
- **Dynamic Prefix Handling:** Automatically selects prefix or provides a dropdown for multiple options.  
- **Real-Time Preview:** Preview generated numbers before downloading.  
- **Customizable Output:** Download datasets in `xlsx` or `csv` formats.  
- **Modular Codebase:** Reusable and maintainable code structure for future enhancements.  
- **Optimized Layout:** Wide layout for desktop screens.

---

## Project Structure

```

bd-mobile-number-generator/
│
├── app.py                 # Main Streamlit application
├── config.py              # Operator prefixes and UI themes
├── generator.py           # Mobile number generation module
├── exporter.py            # Export to Excel or CSV module
├── ui.py                  # UI theming and sidebar utilities
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules

````

---

## Modules Overview

### **config.py**
- Stores **operator prefixes**:
```python
PREFIXES = {
    "Airtel": ["016"],
    "Grameenphone": ["017", "013"],
    "Robi": ["018"],
    "Banglalink": ["019", "014"]
}
````

* Contains **UI theme configurations** per operator.

### **generator.py**

* Generates unique mobile numbers using `random.SystemRandom`.
* Returns a **pandas DataFrame**.
* Function: `generate_numbers(operator, prefix, count)`

### **exporter.py**

* Exports the generated numbers to `xlsx` or `csv`.
* Function: `export_data(df, file_format="xlsx")`

### **ui.py**

* Applies operator-specific themes and styling across the app.
* Functions:

  * `apply_full_theme(operator)` – applies full screen operator theme.
  * `sidebar_info()` – displays project and author info in sidebar.
  * `get_theme_color()` – retrieves main color for buttons and headers.

### **app.py**

* Main Streamlit workflow:

  1. Displays sidebar information.
  2. Allows operator and prefix selection.
  3. Accepts number count and output format input.
  4. Generates numbers and previews the first 10 results.
  5. Provides a download option via a themed button.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aanzum7/phone-number-generator.git
cd phone-number-generator
```

2. Create and activate a Conda environment with Python 3.13:

```bash
conda create -n bdnumbergen python=3.13 -y
conda activate bdnumbergen
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run app.py
```

* The app will open in a browser window.
* Select **operator**, **prefix**, **number count**, and **output format**.
* Click **Generate Numbers** to preview.
* Click **Download** to save the dataset.

---

## Dependencies

```
streamlit>=1.48.0
pandas>=2.0.0
openpyxl>=3.1.0
```

---

## 👨‍💻 About the Author

**Tanvir Anzum**
Analytics Scientist & Strategist
Passionate about AI, data, and building interactive tools.

[LinkedIn](https://www.linkedin.com/in/aanzum) | [GitHub](https://github.com/aanzum7)

---

## 🔗 Live Demo

Check out the live demo here:
[https://bdnumbergen.streamlit.app/](https://bdnumbergen.streamlit.app/)

```
```
