from PIL import Image

def convert_to_grayscale(input_path, output_path):
   
    try:
        
        img = Image.open(input_path)
        
        
        gray_img = img.convert("L")
        
        
        gray_img.save(output_path)
        print(f"Grayscale image saved as {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")
        
convert_to_grayscale("f:/bongodev-class-content/python-practice-problems/advanced-level/Problem-09/color_image.jpg", "f:/bongodev-class-content/python-practice-problems/advanced-level/Problem-09/grayscale_image.jpg")
