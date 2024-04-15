from src.get_letters import *
letters = get_letters("data\\teste.png")
for i in range(len(letters)):
    letters[i] = resize_image(letters[i])
save_images(letters, "data\letters")