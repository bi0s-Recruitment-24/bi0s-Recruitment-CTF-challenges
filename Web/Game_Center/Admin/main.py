from flask import Flask, request,render_template
import random
import os
app = Flask(__name__)
flag=os.getenv('flag') or "bi0s{'congo'}"
print(flag)
names = [
    "Amanda", "Aarav", "Liam", "Saanvi", "Arjun", "Leila", "Umesh", "Priya", "Rohan", "Zara",
    "Ayaan", "Sofia", "Adhira", "Maya", "Dhruv", "Noor", "Kiran", "Anika", "Aria", "Kavya",
    "Rishi", "Meera", "Omkar", "Veer", "Advika", "Karan", "Diya", "Samar", "Tanya", "Aadhya",
    "Kunal", "Nisha", "Nikhil", "Ayesha", "Ansh", "Ramesh", "Dev", "Naina", "Kabir", "Anjali",
    "Sahil", "Ira", "Aditya", "Ishita", "Raghav", "Simran", "Aarohi", "Anaya", "Siddharth", "Jiya",
    "Ayush", "Reyansh", "Aditi", "Rahul", "Tara", "Harsh", "Mira", "Avi", "Radhika", "Krish",
    "Anvi", "Laksh", "Aravindakshan", "Aryan", "Shreya", "Mihir", "Akira", "Nirvaan", "Aarushi", "Ishaanvi",
    "Sudheesh", "Rhea", "Rudra", "Avni", "Kiaan", "Shanaya", "Trisha", "Sara", "Ahan", "Ratheesh",
    "Ritvik", "Vanya", "Aarush", "Shivani", "Yash", "Anushka", "Madhav", "Gauri", "Manav", "Yuvika",
    "Arnav", "Jhanvi", "Siddhi", "Aarya", "Krishna", "Ritika", "Ethan", "Amaya", "Leo", "Nia",
    "Mason", "Riya", "Elena", "Rehaan", "Zoe", "Sumesh", "Ishaan", "Lily", "Vivaan", "Ram"
]

games = [
    "The Legend of Zelda: Breath of the Wild",
    "Super Mario Odyssey",
    "Red Dead Redemption 2",
    "The Witcher 3: Wild Hunt",
    "Minecraft",
    "Grand Theft Auto V",
    "The Last of Us Part II",
    "Horizon Zero Dawn",
    "God of War",
    "Fortnite",
    "Call of Duty: Warzone",
    "Apex Legends",
    "Cyberpunk 2077",
    "Assassin's Creed Valhalla",
    "FIFA 23",
    "NBA 2K23",
    "Overwatch",
    "Valorant",
    "League of Legends",
    "Dota 2",
    "Counter-Strike: Global Offensive",
    "Among Us",
    "Fall Guys",
    "Animal Crossing: New Horizons",
    "Persona 5",
    "Sekiro: Shadows Die Twice",
    "Dark Souls III",
    "Bloodborne",
    "Resident Evil Village",
    "Resident Evil 2 Remake",
    "Monster Hunter: World",
    "Super Smash Bros. Ultimate",
    "Mario Kart 8 Deluxe",
    "Splatoon 2",
    "Pokémon Sword and Shield",
    "The Elder Scrolls V: Skyrim",
    "DOOM Eternal",
    "Halo Infinite",
    "Gears 5",
    "Forza Horizon 4",
    "Destiny 2",
    "No Man's Sky",
    "Rainbow Six Siege",
    "Battlefield V",
    "Final Fantasy VII Remake",
    "Ghost of Tsushima",
    "Death Stranding",
    "Control",
    "Nier: Automata",
    "Yakuza: Like a Dragon",
    "The Division 2",
    "Far Cry 5",
    "Far Cry 6",
    "Watch Dogs Legion",
    "Hitman 3",
    "Mortal Kombat 11",
    "Street Fighter V",
    "Tekken 7",
    "Rocket League",
    "Dead by Daylight",
    "PUBG",
    "Hades",
    "Hollow Knight",
    "Celeste",
    "Cuphead",
    "Stardew Valley",
    "Terraria",
    "Subnautica",
    "The Sims 4",
    "Cities: Skylines",
    "XCOM 2",
    "Civilization VI",
    "Star Wars Jedi: Fallen Order",
    "Star Wars Battlefront II",
    "Mass Effect: Legendary Edition",
    "Dragon Age: Inquisition",
    "Titanfall 2",
    "A Plague Tale: Innocence",
    "Little Nightmares II",
    "Outer Wilds",
    "Journey",
    "The Witness",
    "Ori and the Will of the Wisps",
    "Horizon Forbidden West",
    "Returnal",
    "Demon's Souls (PS5)",
    "Ratchet & Clank: Rift Apart",
    "It Takes Two",
    "Sackboy: A Big Adventure",
    "Marvel's Spider-Man: Miles Morales",
    "Marvel's Spider-Man",
    "Batman: Arkham Knight",
    "Metal Gear Solid V: The Phantom Pain",
    "Bloodstained: Ritual of the Night",
    "Control",
    "Outer Worlds",
    "Disco Elysium",
    "Divinity: Original Sin 2",
    "Pillars of Eternity II: Deadfire"
]

rand_name=names[random.randint(51,90)]
print(rand_name)

d={}
for name in names:
    if rand_name==name:
        d[name]=[flag]
        continue
    d[name]=random.sample(games, random.randint(1, 5))

print(d)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/profile')
def profile():
    user_id = request.args.get('user_id')
    name=list(d)[int(user_id)]
    print(name)
    games=d[name]
    print(games)

    return render_template('user.html',games=games,name=name)

@app.route('/about')
def about():
   return render_template("about.html")


@app.route('/game')
def game():
    name= request.args.get('name')
    return render_template('game.html',name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000, debug=False)

