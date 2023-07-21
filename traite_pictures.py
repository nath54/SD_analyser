import shutil
import os
import json
from PIL import Image
from tqdm import tqdm

model = "DreamShaper"
test = "animals"

for model in ["DreamShaper", "AnalogMadness", "GhostMix", "FreedomRedmond"]:
    for test in ["animals", "people", "landscapes"]:

        print("Model : ", model, " test : ", test, "...")

        PROMPT_FILE = f"C:/Users/Cerisara Nathan/Documents/GitHub/SD_analyser/prompts/{test}.txt"
        DOSSIER_INITIAL = f"D:/StableDiffusion/MYSUPERSTABLEDIFFUSIONV2/stable-diffusion-webui/outputs/txt2img-images/SDAN_{model}_{test}/"
        DOSSIER_FINAL = f"C:/Users/Cerisara Nathan/Documents/GitHub/SD_analyser/res/pictures/{model}/{test}/"


        # Format :
        #   - "titre": {"url": url, "note": note/10}

        # Notes : 
        #  (5) - Parfait
        #  (4) - Bien avec quelques petits défauts
        #  (3) - Correct, avec des défauts
        #  (2) - Pas bon, bcp de défauts
        #  (1) - Hors-sujet, mais jolie image
        #  (0) - trop de défauts, moche, hors-sujet

        data = {

        }


        #

        fi = open(PROMPT_FILE, "r")
        lst_data_elts = [e.strip().lower() for e in fi.readlines()]
        fi.close()

        lst_data_elts.sort(key = lambda x : len(x), reverse=True)

        #

        tmp_data = []

        lstdir = os.listdir(DOSSIER_INITIAL)

        print("First check...")

        for f in tqdm(lstdir):
            if f.endswith(".txt") and f[:-4]+".png" in lstdir:
                fi = open(DOSSIER_INITIAL+f, "r")
                prompt = fi.readline()
                fi.close()
                #
                tmp_data.append([prompt, DOSSIER_INITIAL+f[:-4]+".png"])

        #

        for elt in lst_data_elts:
            for dt in tmp_data:
                if elt in dt[0].lower():
                    data[elt] = {"url": dt[1], "note": -1}
                    tmp_data.remove(dt)
                    break
            #

        print("Copying", len(data), "elts...")

        final_data = {

        }

        dt_keys = list(data.keys())
        dt_keys.sort()

        for e in tqdm(dt_keys):
            shutil.copy(data[e]["url"], f"C:/Users/Cerisara Nathan/Documents/GitHub/SD_analyser/res/pictures/{model}/{test}/{e}.png")
            #
            img = Image.open(f"C:/Users/Cerisara Nathan/Documents/GitHub/SD_analyser/res/pictures/{model}/{test}/{e}.png", "r")
            im2 = img.resize((128, 128))
            im2.save(f"res/pictures/{model}/{test}/{e}_small.png")
            #
            final_data[e] = {"url": f"res/pictures/{model}/{test}/{e}.png", "url_small":f"res/pictures/{model}/{test}/{e}_small.png", "note": -1}

        fi = open(f"js/{model}_{test}.js", "w")
        fi.write("const data="+json.dumps(final_data)+"; \n add_imgs();")
        fi.close()

