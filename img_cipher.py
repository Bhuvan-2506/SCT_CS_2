from PIL import Image
import os

def encrypt_decrypt_image(input_image_path, key):
   
    try:
        # 1. Open the image
        img = Image.open(input_image_path)
    except FileNotFoundError:
        print(f"Error: File not found at {input_image_path}")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    pixel_data = list(img.getdata())
    
    new_pixel_data = []

    for pixel_value in pixel_data:
        
        new_pixel = tuple(channel_value ^ key for channel_value in pixel_value)
        new_pixel_data.append(new_pixel)

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixel_data)

   
    file_name, file_ext = os.path.splitext(input_image_path)
    
    if "_encrypted" in file_name:
       
        output_image_path = f"{file_name.replace('_encrypted', '_decrypted')}{file_ext}"
        operation = "Decryption"
    else:
        output_image_path = f"{file_name}_encrypted{file_ext}"
        operation = "Encryption"
        
    new_img.save(output_image_path)

    print("-" * 50)
    print(f"{operation} Complete!")
    print(f"Input: {os.path.basename(input_image_path)}")
    print(f"Output saved to: {os.path.basename(output_image_path)}")
    print(f"Key used: {key}")
    print("-" * 50)


def main():

    print("--- Simple Image Encryption Tool (XOR Cipher) ---")
    
    
    image_path = input("Enter the path to the image file (e.g., photo.png): ")

    
    while True:
        try:
            key = int(input("Enter an integer key (0-255) for encryption/decryption: "))
           
            if 0 <= key <= 255:
                break
            else:
                print("Key should ideally be between 0 and 255 for standard 8-bit color channels.")
        except ValueError:
            print("Invalid input. Please enter an integer for the key.")

   
    encrypt_decrypt_image(image_path, key)


if __name__ == "__main__":
    main()
