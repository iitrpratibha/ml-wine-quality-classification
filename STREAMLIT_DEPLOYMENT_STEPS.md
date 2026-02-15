# Streamlit Cloud Deployment - Step-by-Step Guide

## 🚀 Complete Deployment Instructions

### Prerequisites
- ✅ GitHub account: **iitrpratibha**
- ✅ GitHub repository: **ml-wine-quality-classification** (already created)
- ✅ All code pushed to GitHub (already done)

---

## Step 1: Sign In to Streamlit Cloud

1. **Open Streamlit Cloud**
   - Go to: https://streamlit.io/cloud
   - OR: https://share.streamlit.io/

2. **Sign In with GitHub**
   - Click "Sign in" button
   - Select "Continue with GitHub"
   - Authorize Streamlit to access your GitHub account (**iitrpratibha**)
   - You may need to grant permissions to access repositories

---

## Step 2: Create New App

1. **Click "New app" Button**
   - You'll see a button "New app" in the top right
   - Click it to start the deployment process

2. **Fill in the Deployment Form**

   **Repository:**
   ```
   iitrpratibha/ml-wine-quality-classification
   ```

   **Branch:**
   ```
   master
   ```
   (or `main` if you renamed the branch)

   **Main file path:**
   ```
   app.py
   ```

   **App URL (optional - or leave default):**
   - Streamlit will auto-generate: `iitrpratibha-ml-wine-quality-classification`
   - You can customize if you want

3. **Advanced Settings (Optional - usually not needed)**
   - Python version: 3.9+ (auto-detected)
   - Leave other settings as default

4. **Click "Deploy" Button**

---

## Step 3: Wait for Deployment

1. **Deployment Process** (takes 2-5 minutes)
   - Installing dependencies from `requirements.txt`
   - Building the application
   - Starting the Streamlit server

2. **Monitor Progress**
   - You'll see a progress screen with logs
   - Watch for any errors (red text)
   - Green checkmarks indicate successful steps

3. **Expected Log Output:**
   ```
   ✓ Cloning repository
   ✓ Installing Python 3.x
   ✓ Installing dependencies
   ✓ Starting app
   ✓ App is live!
   ```

---

## Step 4: Verify Deployment

Once deployed, you'll get a URL like:
```
https://iitrpratibha-ml-wine-quality-classification.streamlit.app
```

**Test All Features:**

1. **Home Page** ✅
   - Check that it loads properly
   - Verify all text and formatting

2. **Model Comparison Page** ✅
   - View the comparison table
   - Check bar charts and heatmap load correctly
   - Verify all 6 models are shown

3. **Make Predictions Page** ✅
   - Select a model from dropdown
   - Upload the sample CSV file (`sample_test_data.csv`)
   - Click "Predict Quality"
   - Verify metrics and confusion matrix appear

4. **About Dataset Page** ✅
   - Check dataset information loads
   - Verify feature statistics table
   - Check correlation heatmap

---

## Step 5: Copy the Live URL

Once everything works:

1. **Copy the full URL** from your browser
2. **Format**:
   ```
   https://iitrpratibha-ml-wine-quality-classification.streamlit.app
   ```

3. **Save this URL** - you need it for:
   - Your PDF submission
   - Testing and verification

---

## 🛠️ Troubleshooting Common Issues

### Issue 1: "ModuleNotFoundError"

**Problem**: Missing Python package

**Solution**:
1. Check `requirements.txt` has all packages
2. Add missing package to requirements.txt
3. Commit and push changes
4. Streamlit will auto-redeploy

**Fix:**
```bash
# In your local project
source venv/bin/activate
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements.txt"
git push
```

### Issue 2: "File not found" Error

**Problem**: App can't find model files or data files

**Solution**:
1. Ensure all `.pkl` files are committed to GitHub
2. Check file paths in `app.py` are relative, not absolute
3. Verify files exist in repository

**Check:**
```bash
git ls-files | grep .pkl  # Should show all 6 model files
git ls-files | grep data  # Should show dataset files
```

### Issue 3: "Memory Limit Exceeded"

**Problem**: App uses too much memory (Streamlit free tier has limits)

**Solutions**:
1. The app uses `@st.cache_data` and `@st.cache_resource` - already optimized
2. Dataset size is reasonable (6,497 rows)
3. Should not exceed free tier limits

If it happens:
- Reduce dataset size in uploaded files
- Use test data only (already documented)

### Issue 4: App is Slow

**Expected Behavior**:
- First load: 5-10 seconds (models loading)
- Subsequent loads: 1-2 seconds (cached)
- Predictions: 1-3 seconds

**Normal for free tier** - not an error

### Issue 5: "Repository Not Found"

**Problem**: Streamlit can't access your repository

**Solution**:
1. Make sure repository is **public** (not private)
2. Re-authenticate Streamlit with GitHub
3. Grant necessary permissions

**Check Repository Visibility:**
```bash
gh repo view iitrpratibha/ml-wine-quality-classification
# Should show "Visibility: public"
```

---

## 📝 Post-Deployment Checklist

After successful deployment:

- [ ] App URL is accessible from any browser
- [ ] All 4 pages load without errors
- [ ] Model comparison table shows all 6 models
- [ ] CSV upload works correctly
- [ ] Predictions generate successfully
- [ ] Confusion matrix displays properly
- [ ] No error messages in the app
- [ ] URL copied and saved for submission

---

## 🔄 Updating Your Deployed App

If you need to make changes:

1. **Make changes locally**
   ```bash
   # Edit files as needed
   git add .
   git commit -m "Description of changes"
   git push
   ```

2. **Auto-Redeploy**
   - Streamlit Cloud automatically detects changes
   - Redeploys within 1-2 minutes
   - No manual action needed

3. **Manual Redeploy (if needed)**
   - Go to Streamlit Cloud dashboard
   - Click "Reboot app" or "Redeploy"

---

## 📱 Sharing Your App

Once deployed, you can:

1. **Share the URL** with anyone
   - No login required for viewers
   - Works on desktop and mobile
   - Publicly accessible

2. **Embed in Documentation**
   - Add to your README
   - Include in PDF submission
   - Share with evaluators

3. **Social Sharing** (optional)
   - Streamlit provides sharing buttons
   - Can share on LinkedIn, Twitter, etc.

---

## 🎯 Expected Final Result

Your app should look like this:

**Home Page:**
- Title: "🍷 Wine Quality Classification"
- Navigation sidebar with 4 pages
- Welcome message and features list

**Model Comparison:**
- Table with 6 models and 6 metrics
- Bar charts showing performance
- Heatmap of all metrics

**Predictions:**
- Model dropdown (6 options)
- CSV upload button
- Results table with predictions
- Confusion matrix visualization

**About Dataset:**
- Dataset description
- Feature statistics
- Correlation heatmap

---

## ⏱️ Estimated Time

- **Sign in**: 1-2 minutes
- **Fill deployment form**: 1 minute
- **Deployment process**: 2-5 minutes
- **Testing**: 3-5 minutes
- **Total**: ~10-15 minutes

---

## 🆘 Need Help?

1. **Streamlit Documentation**
   - https://docs.streamlit.io/streamlit-community-cloud

2. **Streamlit Community Forum**
   - https://discuss.streamlit.io/

3. **GitHub Issues**
   - Check your repository issues tab

4. **Status Check**
   ```bash
   # Check if your app is running
   curl -I https://iitrpratibha-ml-wine-quality-classification.streamlit.app
   # Should return "HTTP/2 200" if working
   ```

---

## ✅ Deployment Complete!

Once you see "App is live!" and can access your URL, you're done!

**Next Steps:**
1. ✅ Copy the live URL
2. ✅ Test all features
3. ✅ Add URL to your PDF submission
4. ✅ Execute on BITS Lab
5. ✅ Submit your assignment

---

Good luck with your deployment! 🚀
