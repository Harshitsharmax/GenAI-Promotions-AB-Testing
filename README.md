# 📧 A/B Email Testing App

Welcome to the **A/B Email Testing App**, a streamlined and interactive application that helps marketers, product teams, and email campaign designers test multiple promotional email variants for effectiveness. This app utilizes **Modern LLMs API** to generate high-quality, personalized emails based on user inputs like location, interests, and communication style.

Built with **Streamlit**, this app offers a seamless way to generate, preview, and compare email versions side-by-side, and capture feedback with one click.

Try the [🚀WebApp](https://promotional-emails-genai.streamlit.app/)
---

## 🚀 Features

✅ **Input Personalization**  
- Accepts recipient’s name, location, interests (comma-separated), and preferred communication style (e.g., Inspirational, Funny, Critical).

✅ **Dual Email Generation (A/B Testing)**  
- Automatically generates two distinct promotional emails (A & B) using Gemini API prompts based on the provided inputs.

✅ **Side-by-Side Comparison**  
- Emails are rendered side-by-side using styled markdown for easy visual comparison.

✅ **Preview Popup for Each Email**  
- Click the **“📬 Preview”** button to view the full email in a beautifully styled modal popup (mimicking a real email client).

✅ **Feedback Collection**  
- Choose between Email A, Email B, or "It's a tie" after reviewing both options.

✅ **History Tracking**  
- All feedback is stored in `results.json` and the 5 most recent results are displayed in the sidebar for easy reference.

✅ **Clean Markdown UI**  
- Uses markdown formatting and semantic styling to emphasize subject lines and key email elements.

---

## 🧠 Powered by

- [Streamlit](https://streamlit.io/) for the interactive web interface  
- [Gemini Pro API (Google Generative AI)](https://ai.google.dev/gemini-api/docs/get-started) for content generation  

---

## 📁 Folder Structure

```
ab-email-tester/
│
├── main.py                # Main Streamlit app logic
├── email_generator.py     # Handles Gemini API requests
├── utils.py               # Contains prompt builder logic
├── results.json           # Stores previous A/B test feedback
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ab-email-tester.git
cd ab-email-tester
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate      # macOS/Linux
myenv\Scripts\activate         # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, manually install:
```bash
pip install streamlit google-generativeai
```

### 4. Configure the Gemini API

**Option A: Set environment variable**

```bash
export GOOGLE_API_KEY="your_gemini_api_key"    # Linux/macOS
set GOOGLE_API_KEY=your_gemini_api_key         # Windows CMD
$env:GOOGLE_API_KEY="your_gemini_api_key"      # PowerShell
```

**Option B: Directly in `email_generator.py`**

```python
genai.configure(api_key="your_gemini_api_key")
```

### 5. Run the App

```bash
streamlit run main.py
```

---

## 📸 Screenshots

![mainform](https://github.com/user-attachments/assets/eaa79b7d-f4f3-4c78-b76f-b0e8467a50e3)
![compareoutput](https://github.com/user-attachments/assets/3a7ed767-ed43-4d47-8f78-3444a1dcff2e)
![appwithsidebar](https://github.com/user-attachments/assets/e510da17-7df0-48cf-ae44-3468b4a1e846)

---

## 🛠 Future Improvements

- Add email click-rate prediction using ML.
- Export results to CSV or Google Sheets.
- Enable theme customization.
- Add user login & authentication.

---

## 🤝 Contributing

Have suggestions or want to contribute? Feel free to fork the repo and open a pull request!

---

## 📄 License

MIT License
