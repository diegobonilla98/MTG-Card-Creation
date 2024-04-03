import os
import matplotlib.pyplot as plt
from call_gpt import query_gpt
from create_card import create_card
from image_creation import generate_art
from reaplce_image import replace_image, Image


prompt = r"""Create a Magic Card. Just return the variable names. This is going to be executed by a python script so don't add any additional information or text or it will rise an error.
Use Magic Set Editor as the language for creating custom symbols. For example, "<sym>T</sym>" is the symbol for turn.
The "card_detailed_image_illustration_description" is going to be the input for an Stable Diffusion image generation, so take this into consideration and make it match the type and habilities.
Here is an example of the output:

card_name = "Corey, The Rogue"
card_text = r"Fear\n<sym>T</sym>: Draw one card"
card_type = "Creature - Cat"
super_type = "Basic"
casting_cost = "2RB"
power_toughness = "5/6"
card_color = "red,black"
rarity = "rare"
card_detailed_image_illustration_description = "A mysteryous cat figure wearing a black cloak, in the dark, rubbing his hands. Magic the Gathering illustration style."
"""

response = query_gpt(prompt, model="gpt-4-turbo-preview")

local_vars = {}
exec(response, {}, local_vars)

card_name = local_vars["card_name"]
card_text = local_vars["card_text"]
card_type = local_vars["card_type"]
super_type = local_vars["super_type"]
casting_cost = local_vars["casting_cost"]
power_toughness = local_vars["power_toughness"]
card_color = local_vars["card_color"]
rarity = local_vars["rarity"]
card_detailed_image_illustration_description = local_vars["card_detailed_image_illustration_description"]

current_path = os.getcwd()
create_card(card_name, card_text, card_type, super_type, casting_cost, power_toughness, card_color, rarity)
os.chdir(current_path)

illustration = generate_art(card_detailed_image_illustration_description)
background = Image.open("M15-Magic-Pack-main\\temp.png")
final = replace_image(background, illustration)

final.save(f"{card_name}.jpg")

plt.imshow(final)
plt.show()
