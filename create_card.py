import subprocess
import os


def create_card(card_name, card_text, card_type, super_type, casting_cost, power_toughness, card_color, rarity, illustrator="Diego Bonilla", set_code="XXX-X"):
    output_file = "temp.png"
    mse_directory = "M15-Magic-Pack-main"
    os.chdir(mse_directory)
    commands = [
        ':load set.mse-set\n',
        f'my_card := new_card([name: "{card_name}", text: "{card_text}", type: "{card_type}", super_type: "{super_type}", casting_cost: "{casting_cost}", pt: "{power_toughness}", card_color: "{card_color}", rarity: "{rarity}", illustrator: "{illustrator}", set_code: "{set_code}"])\n',
        f'write_image_file(my_card, file: "{output_file}")\n'
    ]
    process = subprocess.Popen(["mse", '--cli'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    for cmd in commands:
        process.stdin.write(cmd)
    process.stdin.close()
