import random
import string

def generate_random_filename(length=8, extension=''):
    # Generate a random string of uppercase letters, lowercase letters, and digits
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
    
    # Combine the random string with the given extension (if any)
    filename = random_string + extension
    
    return filename
