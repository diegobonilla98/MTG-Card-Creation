# MTG-Card-Creation
MTG Card Creator: A Fusion of GPT and Stable Diffusion


Welcome to Magic: The Generation, a fun weekend project that melds the creativity of Magic: The Gathering (MTG) card game with the power of AI, specifically ChatGPT and Stable Diffusion. As a solo developer, I've created a Python script that automates the generation of unique MTG cards, complete with custom illustrations.


## What does this do

The script prompts ChatGPT to come up with the card details—name, type, abilities, and more—following the conventions of MTG card creation. It then uses these details as input for Stable Diffusion to generate a fitting artwork. Finally, leveraging Magic Set Editor, the script compiles these elements into a visually appealing and game-ready MTG card.


## Results

![](./Examples/Ethereal%20Librarian.jpg)
![](./Examples/Elena,%20The%20Enchantress.jpg)
![](./Examples/Corey,%20The%20Rogue.jpg)

I think because the desired aspect ratio, the used Stable Diffusion tends to duplicate stuff...

I've tried EVERYTHING but I could not change the image in the MTG Card using the cli... So I made it using Pillow.


## Behind the Scenes

Here's a brief rundown of how it works:

- Card Creation: Using a predefined prompt, ChatGPT designs the card's details.
- Art Generation: Stable Diffusion takes the card description and creates a unique piece of artwork.
- Card Assembly: With Magic Set Editor, the script combines the details and artwork into the final card design.

Check out [Magic Set Editor](https://magicseteditor.boards.net/) to explore how you can further customize your cards.
