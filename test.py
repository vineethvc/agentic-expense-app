# # Initialize PaddleOCR instance
from paddleocr import PaddleOCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

# Run OCR inference on a sample image
result = ocr.predict(
    input=r"C:\Users\vinee\Downloads\20250803_214914.jpg")

# Visualize the results and save the JSON results
for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")

# import easyocr
# import pprint
#
# reader = easyocr.Reader(['de','en'])
#
# result = reader.readtext(r"C:\Users\vinee\Downloads\gmail_images20250717_225203.png", detail = 0)
#
# pprint.pp(result)