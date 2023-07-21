
# WICH_PROMPT = "realistic" # "Realistic" "Anime" "Modern Art"
# TYPE = "animal" # "Animal", "Object", "People", "Style"


for WICH_PROMPT in ["realistic", "anime", "modern_art"]:
    for TYPE in ["animals", "objects", "people", "landscapes"]:
        f = open(f"prompts/{TYPE}.txt", "r")
        elts = f.readlines()
        f.close()

        lst = []

        for a in elts:
            aa = a.strip().lower()
            if aa[0] in ["h", "a", "e", "i", "o", "u", "y"]:
                aa = "an "+aa
            else:
                aa = "a "+aa
            if TYPE == "animals":
                if WICH_PROMPT == "realistic":
                    prompt = f"Picture of {aa} in its natural environment, {aa} animal, realistic, professional photography, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "anime":
                    prompt = f"Picture of {aa} in its natural environment, {aa} animal, anime style, professional art, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "modern_art":
                    prompt = f"Art of {aa} in its natural environment, {aa} animal, modern art style, professional modern art, perfect composition, 8k, beautiful, intricate, details, original, intense, masterpiece"
            elif TYPE == "objects":
                if WICH_PROMPT == "realistic":
                    prompt = f"Picture of {aa}, {aa}, realistic, professional photography, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "anime":
                    prompt = f"Picture of {aa}, {aa}, anime style, professional art, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "modern_art":
                    prompt = f"Art of {aa}, {aa}, modern art style, professional modern art, perfect composition, 8k, beautiful, intricate, details, original, intense, masterpiece"
            elif TYPE == "people":
                if WICH_PROMPT == "realistic":
                    prompt = f"Portrait photo of {aa}, {aa}, realistic, professional photography, studio shot, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "anime":
                    prompt = f"Portrait picture of {aa}, {aa}, anime style, professional art, studio digital art, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "modern_art":
                    prompt = f"Portrait Art of {aa}, {aa}, modern art style, professional modern art, studio digital art, perfect composition, 8k, beautiful, intricate, details, original, intense, masterpiece"
            elif TYPE == "landscapes":
                if WICH_PROMPT == "realistic":
                    prompt = f"Picture of {aa} landscape, {aa} landscape environment, realistic, professional photography, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "anime":
                    prompt = f"Picture of {aa} landscape, {aa} landscape environment, anime style, professional art, perfect composition, 8k, beautiful, intricate, details"
                elif WICH_PROMPT == "modern_art":
                    prompt = f"Art of {aa} landscape, {aa} landscape environment, modern art style, professional modern art, perfect composition, 8k, beautiful, intricate, details, original, intense, masterpiece"
            #
            lst.append(prompt)

        txt = "\n".join(lst)

        f = open(f"prompts/prompts_{TYPE}_{WICH_PROMPT}.txt", "w")
        f.write(txt)
        f.close()


###########################################################################################################

base_prompts_style_test = [
    "a beautiful young woman, 1girl, beautiful girl",
    "a beautiful young man, 1man, beautiful man",
    "a cat, cute cat animal",
    "a cube shape, cube geometry, cubic",
    "a forest landscape, landscape, forest, trees"
]

f = open(f"prompts/styles_expressions.txt", "r")
stls = f.readlines()
f.close()

stls = [s.strip().lower() for s in stls]

lsts = {}
for b in base_prompts_style_test:
    lsts[b] = []

for s in stls:
    for bp in base_prompts_style_test:
        prompt = bp+", "+s
        lst.append(prompt)


for s1 in stls:
    for s2 in stls:
        if s1 != s2:
            for bp in base_prompts_style_test:
                prompt = bp+", "+s1+", "+s2
                lsts[bp].append(prompt)
                

for k in lsts.keys():

    txt = "\n".join(lsts[k])

    f = open(f"prompts/prompts_styles_test_{k}.txt", "w")
    f.write(txt)
    f.close()