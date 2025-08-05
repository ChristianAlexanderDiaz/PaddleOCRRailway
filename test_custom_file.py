#!/usr/bin/env python3
"""
PaddleOCR Test Script - Windows 11 & Railway Optimized
Tests your custom table image with mobile models
"""
from paddleocr import PaddleOCR
import os
from pathlib import Path

def setup_environment():
    """Setup for Windows and Railway optimization"""
    os.environ['PADDLE_PDX_MODEL_SOURCE'] = 'BOS'  # Faster downloads
    Path("output").mkdir(exist_ok=True)

def test_custom_file(image_path):
    """Test PaddleOCR with custom image file using latest PP-OCRv5 API"""
    print(f"🧪 Testing PaddleOCR with: {image_path}")
    
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        print("💡 Make sure to add your table1.png to the tables/ folder")
        return False
    
    try:
        print("📱 Initializing PaddleOCR with Railway-optimized settings...")
        # Initialize PaddleOCR with mobile models (Railway-friendly)
        ocr = PaddleOCR(
            use_doc_orientation_classify=False,  # Saves space
            use_doc_unwarping=False,            # Saves space
            use_textline_orientation=True,      # Good for tables
            lang='en'  # English language
        )
        print("✅ PaddleOCR initialized successfully with PP-OCRv5")
        
        # Perform OCR using the new predict method
        result = ocr.predict(input=image_path)
        
        print(f"\n📄 OCR Results for {image_path}")
        print("=" * 50)
        
        # Handle the new result format
        for res in result:
            print("📝 Processing result...")
            res.print()  # Use built-in print method
            
            # Save results
            output_name = Path(image_path).stem
            res.save_to_img(f"output/{output_name}")
            res.save_to_json(f"output/{output_name}")
            print(f"✅ Results saved to output/{output_name}*")
        
        return True
        
    except Exception as e:
        print(f"❌ Error with new API: {e}")
        print("🔄 Trying fallback method...")
        return test_fallback_method(image_path)

def test_fallback_method(image_path):
    """Fallback method using older API if needed"""
    try:
        ocr = PaddleOCR(
            use_textline_orientation=True,
            lang='en'
        )
        
        # Try the older ocr method
        result = ocr.ocr(image_path)
        
        print(f"\n--- Fallback OCR Results for {image_path} ---")
        if result and result[0] is not None:
            for line in result[0]:
                text = line[1][0]
                confidence = line[1][1]
                bbox = line[0]
                print(f"Text: '{text}' | Confidence: {confidence:.3f}")
                print(f"  Position: {bbox}")
        else:
            print("No text detected")
        
        return True
        
    except Exception as e:
        print(f"✗ Fallback method also failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 PaddleOCR Custom File Test - Windows 11 Ready")
    print("=" * 50)
    
    # Setup environment
    setup_environment()
    
    # Test with your custom table image
    image_path = "tables/table1.png"
    
    if os.path.exists(image_path):
        success = test_custom_file(image_path)
        if success:
            print("\n🎉 Success! PaddleOCR is working on Windows!")
            print("📁 Check the 'output' folder for results")
            print("🚀 Ready for Railway deployment!")
        else:
            print("\n❌ Test failed. Check the error messages above.")
    else:
        print(f"📁 Waiting for you to add: {image_path}")
        print("💡 Add your table image and run: python test_custom_file.py")