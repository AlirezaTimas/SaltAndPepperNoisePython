import numpy as np
import cv2

#baraye taghir dar % noisy shodan khorooji mizan noise ro taghir bedid:
#(meghdare noise 0.1 = 10%)
#(meghdare noise 0.50 = 50%)
#(meghdare noise 0.25 = 25%)

def add_salt_and_pepper_noise(image_path, meghdare_noise=0.50): 
   
   #load kardan image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    #Mohasebe tedad pixel hayi ke bayad noisy beshan
    num_noise_pixels = int(meghdare_noise * image.size)
    
    #Tolid shakhes random baraye noise salt (White pixels)
    salt = [np.random.randint(0, i - 1, num_noise_pixels) for i in image.shape]
    image[salt[0], salt[1]] = 255
    
    #Tolid shakhes random baraye noise pepper (Black pixels)
    pepper = [np.random.randint(0, i - 1, num_noise_pixels) for i in image.shape]
    image[pepper[0], pepper[1]] = 0
    
    return image


#Estefade az function:
noisy_image = add_salt_and_pepper_noise('Original_Image_Path')
cv2.imshow('Salt and Pepper Noise', noisy_image)

#Masire_save_image
output_path = 'output_image_path(the path to where you want to save the noisy image in)'
cv2.imwrite(output_path, noisy_image)
print(f"Noisy image saved as {output_path}")


cv2.waitKey(0)
cv2.destroyAllWindows()


#AlirezaTimas

