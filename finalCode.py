import torch
from diffusers import FluxPipeline
import os 
from transformers import pipeline
import gradio as gr
from datetime import datetime
import PIL
import deepl

flux1 = FluxPipeline.from_pretrained("C:\\codes\\flux1schnell",torch_dtype=torch.bfloat16) #Accessing Flux.1 schnell model, change the according to your model path 
flux1.enable_sequential_cpu_offload()  #offloading the weights performance to the cpu then loading them to the GPU to save memory 
tranlator = deepl.Translator("c80d959f-7a64-4253-86d3-f049ac07dc32:fx") #accessing DeepL API

def img_gen(prompt):
      
    image = flux1( #defining the pipe
        prompt,
        height=512, #height of the image, adjust if needed
        width=1024, #width of the image
        guidance_scale=1.3,
        output_type="pil", #pillow
        num_inference_steps=4, #how many steps the model should take, rasing it will make the performance time slower
        max_sequence_length=256,
        #generator=torch.Generator("cpu").manual_seed(0) #seed(0) means everytime you will get the same image, if I increase the seed I will get random images with each prompt
        generator=torch.Generator("cuda").manual_seed(0) #This means gpu will run :)
    ).images[0] #access the first image

    image_path = "C:\\codes\\flux1schnell\\gallery" #the folder which the images will be saved to
    if not os.path.exists(image_path):
        os.mkdir(image_path) #if the folder is not found then create the dictionary

    curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #the current time to make each image name unique
    image_save_path =f"{image_path}\\{curr_datetime}.jpeg"
    image.save(image_save_path) #saving the image to the specified folder

    return image_save_path #return the image path to pass to gradio

def arabic_to_english(prompt):
    prompt = str(tranlator.translate_text(prompt, target_lang="EN-US")) #converting the output to string so the model could accept it, the initial data type was a class 
    to_english = img_gen(prompt) #calling flux.1 function and passing the translating prompt then returing the image path
    return to_english


example1= ["A dark blue ocean, the sun is orange, the sky filled with clouds, birds, a small boat sailing."]
example2= ["حديقة مليئة بالزهور الملونة، السماء زرقاء والشمس منيرة، فراشات ملونة حول الزهور"]
            

english_interface = gr.Interface(
    fn=img_gen,
    inputs=gr.Textbox(label= "Enter the image prompt"),
    outputs=gr.Image(label="The Image", type='filepath'),
    title = "An Image generator interface Using Flux1Sschnell",
    examples= example1 #the english example
)

Arabic_interface = gr.Interface(
    fn = arabic_to_english,
    inputs = gr.Textbox("أدخل وصف الصورة"),
    outputs=gr.Image(label="الصورة", type='filepath'),
    title = "flux1scnell توليد الصور باستخدام ",
    examples= example2 #the arabic example
    
)

gr.TabbedInterface(
    [english_interface, Arabic_interface],["English","Arabic"]
).launch() #Putting each interface in a seperate tap to access each needed function

