# 📊 CSV Visualizer & Analyzer

A **Streamlit-based data analysis and visualization web application** for uploading, analyzing, cleaning, visualizing, and exploring CSV datasets.

The application provides dataset statistics, data cleaning tools, an interactive dashboard, and multiple Plotly-based visualizations.

---

## ✨ Features

### 📂 CSV Upload

- Upload CSV files directly through the web interface
- Automatically detect dataset size
- Display number of rows and columns
- Preview uploaded data
- Store the uploaded dataset using Streamlit Session State

### 🔍 Analyze & Clean CSV

Analyze the structure and quality of your dataset.

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Column data types
- Missing-value handling
  - Mean for numeric columns
  - Median for numeric columns
  - `Unknown` for categorical/text columns
- Dataset preview
- Download cleaned CSV

### 📊 Dashboard

A dedicated dashboard provides a quick overview of the uploaded dataset.

#### Dataset Overview

Displays KPI cards for:

- Rows
- Columns
- Missing Values
- Duplicates

#### Dashboard Visualizations

- 📊 Sales by Category — Bar Chart
- 📈 Sales by Year — Line Chart
- 🥧 Category Distribution — Pie Chart
- 🔥 Correlation — Heatmap
- 📋 Recent Dataset Preview

The dashboard combines important dataset information and visualizations into a single view.

### 📈 Visualizations

Create interactive charts using Plotly:

- Bar Chart
- Line Chart
- Pie Chart
- Histogram
- Scatter Plot
- Box Plot
- Area Chart
- Correlation Heatmap

### 💾 Export

- Download cleaned CSV files
- Download generated Plotly charts as PNG images

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **Streamlit** | Web application and UI |
| **Plotly** | Interactive data visualization |
| **Kaleido** | Export Plotly charts as PNG |

---

## 📁 Project Structure

```text
CSV-Visualizer/
│
├── main.py
├── analyzer.py
├── charts.py
├── dashboard.py
├── sample_data.csv
├── requirements.txt
└── README.md
```

> If your dashboard is implemented inside `main.py` instead of a separate `dashboard.py`, remove `dashboard.py` from this structure.

### File Description

| File | Description |
|---|---|
| `main.py` | Main Streamlit application and navigation |
| `analyzer.py` | Dataset analysis, cleaning, preview, and CSV export |
| `charts.py` | Plotly chart generation and chart export |
| `dashboard.py` | Dashboard layout and overview visualizations |
| `sample_data.csv` | Example dataset for testing |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🖥️ Application Structure

The application is organized into different sections:

```text
📊 CSV Visualizer & Analyzer
│
├── 📂 Upload CSV
│   ├── Upload dataset
│   ├── Dataset metrics
│   └── Dataset preview
│
├── 🔍 Analyze & Clean CSV
│   ├── Dataset information
│   ├── Missing values
│   ├── Duplicate detection
│   ├── Data cleaning
│   └── CSV export
│
├── 📊 Dashboard
│   ├── Dataset overview
│   ├── KPI cards
│   ├── Bar chart
│   ├── Line chart
│   ├── Pie chart
│   ├── Correlation heatmap
│   └── Dataset preview
│
└── 📈 Visualize CSV
    ├── Bar Chart
    ├── Line Chart
    ├── Pie Chart
    ├── Histogram
    ├── Scatter Plot
    ├── Box Plot
    └── Area Chart
```

---

## ⚙️ Requirements

- Python 3.8+
- pip
- Modern web browser

Python dependencies are listed in `requirements.txt`.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd CSV-Visualizer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

Streamlit will display a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser.

---

## 📊 How to Use

### Step 1 — Upload a Dataset

Go to **Upload CSV** and select a `.csv` file.

The application will display:

- Number of rows
- Number of columns
- Dataset preview

### Step 2 — Analyze & Clean

Open **Analyze & Clean CSV** to inspect:

- Dataset structure
- Data types
- Missing values
- Duplicate rows

You can also clean missing values and download the cleaned dataset.

### Step 3 — View Dashboard

Open **Dashboard** to get a quick visual summary of the dataset.

The dashboard displays important metrics and charts in one place.

### Step 4 — Create Custom Visualizations

Open **Visualize CSV** and select a chart type.

Choose the appropriate dataset columns and generate an interactive Plotly chart.

### Step 5 — Export

Generated charts can be downloaded as PNG files, and cleaned datasets can be downloaded as CSV files.

---

## 📌 Current Status

### Implemented

- [x] CSV upload
- [x] Dataset preview
- [x] Row and column statistics
- [x] Missing-value detection
- [x] Duplicate detection
- [x] Data type information
- [x] Mean-based missing-value replacement
- [x] Median-based missing-value replacement
- [x] Categorical missing-value replacement
- [x] Cleaned CSV download
- [x] Dashboard
- [x] KPI metrics
- [x] Bar chart
- [x] Line chart
- [x] Pie chart
- [x] Histogram
- [x] Scatter plot
- [x] Box plot
- [x] Area chart
- [x] Correlation heatmap
- [x] Interactive Plotly charts
- [x] PNG chart export

---

## 🖼️ Screenshots

Screenshots can be added to showcase the application.

Structure:

```text
screenshots/
│
├── upload.png
├── analyze.png
├── dashboard.png
└── visualize.png
```

File Location:

```markdown
![Upload](screenshots\Upload.png)
![Analyze_&_clean](screenshots\Analyze_&_clean.png)
![Visualize](screenshots\Visualize.png)
![Dashboard](screenshots\Dashboard.png)
```

---

## 🔧 Troubleshooting

### Streamlit does not start

Make sure the virtual environment is activated:

```bash
.venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run main.py
```

### Plotly chart image export fails

The application uses **Kaleido** for PNG export.

Install or update Kaleido:

```bash
pip install -U kaleido
```

Make sure Kaleido is installed in the same Python environment where Streamlit is running.

### CSV upload fails

Check that:

- The file has a `.csv` extension
- The CSV is not corrupted
- The file uses a supported encoding
- The dataset has a valid tabular structure

---

## 🔮 Future Improvements

Possible future improvements include:

- 📋 Advanced statistical analysis
- 📊 More automatic dashboard generation
- 🧹 More advanced data-cleaning options
- 🔎 Column-level filtering
- 🎛️ Interactive dashboard filters
- 📈 Additional visualization types
- 🎨 Improved UI/UX
- 🧪 Automated testing
- ☁️ Cloud deployment

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python programming
- Pandas DataFrame manipulation
- Data cleaning
- Exploratory data analysis
- Data visualization
- Plotly
- Streamlit
- Session State
- File uploading and downloading
- Interactive web applications
- Basic data analytics

---

## 👨‍💻 Author

**Rudra Pratap Nayak**

Built as a Python-based **CSV Data Analysis and Visualization** project using Streamlit, Pandas, and Plotly.

---

## 📄 License

This project is available for educational and personal use.