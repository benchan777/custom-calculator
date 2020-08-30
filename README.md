# Tera plate crafting calculator
A simple calculator written in python to calculate the number of talents and kits needed to craft siglos or plates in the MMORPG Tera. Also calculates the total price of all materials needed.

## Explanation
In the mmo, Tera, silver plates are materials needed to upgrade and/or craft many different items and gear. In order to craft silver plates, the player needs an item called a silver siglo which also needs to be crafted. In order to craft silver siglos, the player needs a base item called a silver talent. 5 silver talents along with 60 refining kits are needed to craft 3 silver siglos, and 5 silver siglos along with 240 refining kits are needed to craft 3 silver plates.

Since only the final item, silver plates, are needed for most item upgrades, a player has to calculate backwards to try to figure out how many of the base silver talents are needed. This can be a tedious and annoying process. This calculator aims to simplify the calculatin process.

The calculator is not limited to only calculating the number of silver talents and refining kits needed to craft a silver plate, but can also calculate the number of silver talents and refining kits needed to craft a silver siglo.

## Usage
* Input whether you'd like to calculate number of materials needed to craft silver siglos or silver plates. Accepted inputs are "siglo" or "plate."
* Input the price of each silver talent

The calculator will then provide you with the number of talents needed (rounded down), the number of refining kits needed, and the total cost of all materials needed.