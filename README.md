# PaddleOCR Windows 11 Setup

Quick setup for testing PaddleOCR with table images on Windows 11, optimized for Railway deployment.

## 🚀 One-Command Setup

```bash
pip install -r requirements.txt && python test_custom_file.py
```

## 📋 Prerequisites

- **Windows 11** (tested)
- **Python 3.9+** 
- **pip** (comes with Python)

## 📁 Project Structure

```
PaddleOCR/
├── requirements.txt          # Python dependencies
├── test_custom_file.py      # Main test script
├── tables/                  # Your image files
│   └── table1.png          # Add your table image here
└── output/                 # Results (auto-created)
    ├── table1_results.json # OCR text data
    └── table1_visual.jpg   # Annotated image
```

## 🔧 Step-by-Step Setup

### 1. Clone/Download This Project
```bash
# If using git
git clone <your-repo-url>
cd PaddleOCR

# Or download and extract the files
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your Table Image
- Put your table image as `tables/table1.png`
- Supports: PNG, JPG, JPEG formats

### 4. Run the Test
```bash
python test_custom_file.py
```

## 📊 What This Does

1. **Downloads mobile models** (~8-17MB total, Railway-optimized)
2. **Processes your table image** with OCR
3. **Extracts text** with confidence scores and positions
4. **Saves results** to the `output/` folder:
   - JSON file with structured data
   - Visual image with bounding boxes

## 🛠️ Troubleshooting

### Common Issues:

**"No module named 'paddleocr'"**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**"File not found: tables/table1.png"**
- Make sure your image is named exactly `table1.png`
- Place it in the `tables/` folder

**Installation takes a long time**
- PaddleOCR downloads models on first run (~200MB total)
- This is normal and only happens once

**CUDA/GPU warnings (can ignore)**
- The warnings about MKL-DNN/CUDA are normal
- PaddleOCR will use CPU mode automatically

## 🚀 Railway Deployment Ready

This setup uses:
- ✅ **Mobile models** (small size)
- ✅ **Latest PP-OCRv5** API
- ✅ **Optimized settings** for cloud deployment
- ✅ **BOS download source** (faster in production)

## 📝 Model Information

**Downloaded Models:**
- `PP-LCNet_x1_0_textline_ori` (~2MB) - Text orientation
- `PP-OCRv5_mobile_det` (~4MB) - Text detection  
- `PP-OCRv5_mobile_rec` (~4MB) - Text recognition
- **Total: ~10MB** (vs 100MB+ for server models)

**Storage Location:**
- Windows: `C:\\Users\\<username>\\.paddlex\\official_models`

## 🔍 Example Output

```
🧪 Testing PaddleOCR with: tables/table1.png
📱 Initializing PaddleOCR with Railway-optimized settings...
✅ PaddleOCR initialized successfully with PP-OCRv5

📄 OCR Results for tables/table1.png
==================================================
📝 Processing result...
Text: "Invoice Number" | Confidence: 0.987
Text: "Date: 2024-01-15" | Confidence: 0.923
Text: "Total: $1,234.56" | Confidence: 0.956
✅ Results saved to output/table1*

🎉 Success! PaddleOCR is working on Windows!
📁 Check the 'output' folder for results
🚀 Ready for Railway deployment!
```

## 🌐 Next Steps

1. **Test locally** with this setup
2. **Copy files** to your main project repo
3. **Deploy to Railway** using the same requirements.txt
4. **Use as API** by wrapping in FastAPI/Flask

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure Python 3.9+ is installed
3. Try running with `python -m pip install -r requirements.txt`