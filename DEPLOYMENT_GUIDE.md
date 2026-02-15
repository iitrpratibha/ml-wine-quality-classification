# Deployment Guide - ML Assignment 2

## ✅ Completed Tasks

1. ✅ Dataset prepared (Wine Quality - 6,497 instances, 12 features)
2. ✅ All 6 ML models implemented and trained
3. ✅ Comprehensive evaluation metrics calculated
4. ✅ Interactive Streamlit web application created
5. ✅ README.md with detailed documentation
6. ✅ requirements.txt created
7. ✅ GitHub repository created and code pushed

## 📦 GitHub Repository

**URL**: https://github.com/iitrpratibha/ml-wine-quality-classification

Repository contains:
- Complete source code
- All trained model files (.pkl)
- Dataset files
- requirements.txt
- Comprehensive README.md
- Streamlit web application (app.py)

---

## 🚀 Next Steps

### Step 1: Deploy on Streamlit Community Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Sign in with your GitHub account (iitrpratibha)

2. **Create New App**
   - Click "New app" button
   - Select repository: `iitrpratibha/ml-wine-quality-classification`
   - Branch: `master` (or `main` if you renamed it)
   - Main file path: `app.py`
   - Click "Deploy"

3. **Wait for Deployment**
   - Deployment takes 2-5 minutes
   - Streamlit will automatically install dependencies from requirements.txt
   - You'll get a live URL like: `https://iitrpratibha-ml-wine-quality-classification.streamlit.app`

4. **Test the App**
   - Open the live URL
   - Test all features:
     - ✅ Model comparison page
     - ✅ Predictions page with CSV upload
     - ✅ Evaluation metrics display
     - ✅ Confusion matrix visualization

**Note**: If deployment fails, check the logs and ensure:
- All files are committed to GitHub
- requirements.txt is correct
- File paths in app.py are relative (not absolute)

---

### Step 2: Execute on BITS Virtual Lab

**IMPORTANT**: Assignment must be performed on BITS Virtual Lab for 1 mark

#### Instructions:

1. **Login to BITS Virtual Lab**
   - Access your BITS Virtual Lab environment

2. **Clone the Repository**
   ```bash
   git clone https://github.com/iitrpratibha/ml-wine-quality-classification.git
   cd ml-wine-quality-classification
   ```

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Model Training (to verify)**
   ```bash
   python model/train_models.py
   ```

6. **Run Streamlit App Locally**
   ```bash
   streamlit run app.py
   ```

7. **Take Screenshot**
   - Take a screenshot showing:
     - BITS Lab terminal/environment
     - The command you ran
     - The output/results
     - Streamlit app running (if visible)
   - Save as: `bits_lab_execution_screenshot.png`

---

### Step 3: Prepare Final Submission PDF

Create a **single PDF file** containing (in this order):

#### Page 1: Cover Page
```
BITS Pilani - WILP
M.Tech (AIML/DSE)
Machine Learning - Assignment 2

Student Name: [Your Name]
Student ID: [Your ID]
Date: 15-Feb-2026
```

#### Page 2: Submission Links
```
1. GitHub Repository Link:
   https://github.com/iitrpratibha/ml-wine-quality-classification

2. Live Streamlit App Link:
   [Your deployed Streamlit URL - add after deployment]

3. Repository Contents:
   ✓ Complete source code
   ✓ requirements.txt
   ✓ README.md with all required sections
   ✓ All 6 trained models
   ✓ Dataset files
```

#### Page 3: BITS Lab Screenshot
- Insert the screenshot taken on BITS Virtual Lab

#### Page 4-N: README Content
- Copy the entire README.md content (formatted)
- Include:
  - Problem statement
  - Dataset description
  - Model comparison table
  - Model performance observations
  - All other sections

---

## 📋 Final Checklist (Before Submission)

Use this checklist to verify everything:

### Code & Repository
- [ ] All code pushed to GitHub
- [ ] Repository is public
- [ ] README.md is complete with all sections
- [ ] requirements.txt includes all dependencies
- [ ] All 6 models are trained and saved

### Streamlit App
- [ ] App deployed on Streamlit Community Cloud
- [ ] Live link is accessible
- [ ] Dataset upload feature works
- [ ] Model selection dropdown works
- [ ] Evaluation metrics are displayed
- [ ] Confusion matrix is shown
- [ ] No errors when loading

### Documentation
- [ ] README.md has problem statement
- [ ] Dataset description is complete (1 mark)
- [ ] Model comparison table with all 6 metrics (6 marks)
- [ ] Observations for all 6 models (3 marks)
- [ ] All sections properly formatted

### BITS Lab Execution
- [ ] Code executed on BITS Virtual Lab
- [ ] Screenshot taken showing execution
- [ ] Screenshot clearly shows BITS Lab environment

### PDF Submission
- [ ] Single PDF file created
- [ ] GitHub link included
- [ ] Streamlit app link included
- [ ] BITS Lab screenshot included
- [ ] Complete README content included
- [ ] All items in correct order
- [ ] File size is reasonable (< 10 MB)

---

## 🎯 Expected Marks Breakdown (15 Total)

### Model Implementation & GitHub (10 marks)
- Dataset description: 1 mark ✅
- Models comparison table (6 models × all 6 metrics): 6 marks ✅
- Model performance observations: 3 marks ✅

### Streamlit App (4 marks)
- Dataset upload option: 1 mark ✅
- Model selection dropdown: 1 mark ✅
- Display evaluation metrics: 1 mark ✅
- Confusion matrix/classification report: 1 mark ✅

### BITS Lab Execution (1 mark)
- Screenshot proof: 1 mark ⏳ (pending)

---

## 🆘 Troubleshooting

### Streamlit Deployment Issues

**Error: "ModuleNotFoundError"**
- Solution: Ensure all packages are in requirements.txt
- Run: `pip freeze > requirements.txt` and commit

**Error: "File not found"**
- Solution: Use relative paths in code, not absolute
- Check: All file paths in app.py are relative

**Error: "Memory limit exceeded"**
- Solution: Reduce model file sizes or use smaller dataset
- Consider: Uploading only essential files

### BITS Lab Issues

**Cannot access BITS Lab**
- Email: neha.vinayak@pilani.bits-pilani.ac.in
- Subject: "ML Assignment 2: BITS Lab issue"

**Python/pip not working**
- Use: `python3` instead of `python`
- Use: `pip3` instead of `pip`

---

## 📞 Support

If you face any issues:

1. **GitHub/Git issues**: Check GitHub documentation or Stack Overflow
2. **Streamlit issues**: Check Streamlit docs at https://docs.streamlit.io
3. **BITS Lab access**: Email neha.vinayak@pilani.bits-pilani.ac.in
4. **Assignment clarifications**: Ask your course instructor

---

## ⏰ Important Dates

- **Deadline**: 15-Feb-2026, 23:59 PM
- **No extensions** will be provided
- **Only ONE submission** allowed (no resubmissions)
- **No DRAFT submissions** - Must click SUBMIT

---

## ✅ What's Already Done

You have successfully completed:

1. ✅ Dataset selection and preparation
2. ✅ Implementation of all 6 ML models
3. ✅ Calculation of all 6 evaluation metrics
4. ✅ Model comparison table created
5. ✅ Detailed performance observations written
6. ✅ Interactive Streamlit app developed
7. ✅ GitHub repository created and code pushed
8. ✅ Comprehensive README.md documentation
9. ✅ requirements.txt with all dependencies

**Remaining tasks:**

1. ⏳ Deploy Streamlit app to Cloud (5-10 minutes)
2. ⏳ Execute on BITS Lab and take screenshot (10-15 minutes)
3. ⏳ Create final PDF submission (15-20 minutes)

**Total remaining time**: ~40 minutes

You're almost done! 🎉

---

Good luck with your submission! 🚀
