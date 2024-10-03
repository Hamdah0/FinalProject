# Image Generating using the Flux.1 schnell model Final Project
This is the final project for Tuwaiq Data Science and Machine Learning bootcamp.
It's a simple project that runs Flux.1 schnell locally with only the program you are using to code and python,
to generate good looking images with both english and arabic prompts.

## Expected outputs
You must see two tapped gradio interfaces at the end, one to enter your Enlgish prompts on and the other for arabic.
The output should be the generated image.
![Screenshot 2024-10-03 123340](https://github.com/user-attachments/assets/4d760bdd-5768-4b51-9711-a8a84c50f8d4)

## Model Choices
# Flux.1 Scnell
I used this model becuase it's the corrent prefer one with the AI comunnity.
Firstly it's an open source model, -not the DEV version- that you can easily use in your own machine.
It produces amazing results from its high image quality, to its advanced human anatomy, to its textures and speed time.

## Flux1.Schnell explanation
To use the code you need to download the model files from https://huggingface.co/black-forest-labs/FLUX.1-schnell
you can refer to the guide included in the slides for more information on how to do that.

### Dependencies
torch
diffusers
huggingface_hub
transformers
os
datetime
deepl
torchvision
torchaudio
accelerate
sentencepiece
protobuf

## Special measures to support Arabic
Since the model does not support Arabic, I used a function that traslate arabic prompts to english then pass it to the model.
This was done by accessing DeepL Translator API, which is a translator that translate text using AI.
https://www.deepl.com/en/translator

### Video recording
