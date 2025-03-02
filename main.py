import random
import math
import time

global health 
global dice_roll
global user_input
global roll_value
global enemy_initiative
global enemy_health 
global battle_order
global initiative
global spell_slots

def player_fight_command(action, enemy_health, spell_slots, health):
    global reason_count
    action = action.lower()
    if action == "fight":
       print("You raise your dagger and rush at the enemy! Roll for success! (D20)")
       main_menu("roll d20")
       if roll_value + dexterity_mod >= 20:
          print("With a loud war cry, you jump into the air and stab the enemy in the chest! Roll for damage! (D8)")
          main_menu("roll d8")
          damage = roll_value + strength_mod + dexterity_mod
          enemy_health -= damage
          print("You deal", damage, "damage!")
       elif roll_value + dexterity_mod >= 10:
          print("You lunge forward and stab the enemy in the torso! Roll for damage! (D8)")
          main_menu("roll d8")
          damage = roll_value + strength_mod + 2
          enemy_health -= damage
          print("You deal", damage, "damage!")
       else:
          print("The enemy deftly dodges your attack before dropping onto the floor and breaking it down. They than get back up and the battle recommences.\n")
       return enemy_health, spell_slots
          
    elif action == "act":
       print("Acts | cast spell | reason | exit")
       act = input("Act >")
       act = act.lower()            
       if act == "cast spell" and spell_slots > 0:
        print(f"Spell slots: {spell_slots} \nSpells: \n|Thunder - Low success rate with 3d6 damage!|\n\n|Firebolt - High success rate with 1d4 damage|\n\n|Darkblast - Medium success rate with 1d6 damage. 1/2 chance for double damage|\n\n||\n")
        spell = input("Cast >") 
        spell = spell.lower() 
           
        if spell == "thunder":
           spell_slots -=1
           print("You mutter something indistinct and wave your hands. Roll for success! (D20)\n") 
           main_menu("roll d20")
           if roll_value + wisdom_mod >= 15:
            print("Success! Roll 3 d6 for damage!")
            damage = 0
            for i in range (3):
               main_menu("roll d6")
               damage += roll_value
               if damage <= 0:
                  damage = 1
            enemy_health -= damage + intelligence_mod
            print(f"Dark clouds encircle the enemy and a huge bolt of thunder strikes them dealing {damage} damage!\n")
           else:
                print("The enemy flinches as your hands glow with magic power. Unfortunately, it seems to be a dud and nothing happens.\n")
           return enemy_health, spell_slots
               
        elif spell == "firebolt":
           spell_slots -=1
           print("You throw a dash of gunpowder before saying something, causing the powder to glow. You thrust your hands forward, willing a flame to appear. Roll for success! (D20)\n")
           main_menu("roll d20")
           if roll_value + wisdom_mod >= 7:
              print("Success! Roll 1d4 for damage!")
              main_menu("roll d4")
              damage = roll_value + intelligence_mod
              if damage <= 0:
                 damage = 1
              enemy_health -= damage
              print(f"The gunpowder gathers in front of your hands and a bolt of fire shoots out. The enemy takes {damage} damage!\n") 
              
           else:
               print("As you cast the spell, you decide to shout 'FALCON RANGED PAWNCH'! Unfortunately, nothing happens and you look like an IDIOT!\n")
           return enemy_health, spell_slots
               
        elif spell == "darkblast":
            spell_slots -=1
            print("You start whispering under your breath and a candle manifests before being snuffed out. Roll for success! (D20)\n")
            main_menu("roll d20")
            if roll_value + wisdom_mod >= 10:
                damage = 0
                print("Success! Roll 1d6 for damage!")
                main_menu("roll d6")
                damage += roll_value + intelligence_mod
                if damage <= 0:
                   damage = 1
                if random.randint(1,2) == 1:
                    damage *= 2
                    print(f"A cloud of dark miasma flies towards the enemy before doubling in size! Your enemy finds themselves overwhelmed by the sheer darkness of the dark miasma produced by Darkblast.\nThe enemy takes {damage} damage!\n")
                else:   
                    print(f"A cloud of dark miasma flies towards the enemy who finds themselves overwhelmed by the sheer darkness of the dark miasma produced by Darkblast.\nThe enemy takes {damage} damage!\n")
                enemy_health -= damage
            
                
            else: 
                print("You FAILLLL because you aren't dark enough (What?) anyways\n")
            return enemy_health, spell_slots
            
        elif spell == "iceblast":
            spell_slots -=1
            print("You pull out a small ice cube and shout 'ICEBLAST', throwing it onto the ground. Roll for success! (D20)\n")
            main_menu("roll d20")
            if roll_value + wisdom_mod >= 10:
               disadvantage = True
               print("Success! The ice cube glows with heat before exploding, shards landing all over the floor, covering it with a thin sheet of ice.\nThe enemy is now disadvantaged against attack rolls!\n")
               return enemy_health, spell_slots, disadvantage
            else:         
                print("The ice cube sits there pathetically and nothing happens.\n")
            return enemy_health, spell_slots
           
        elif spell_slots <= 1: 
           print("You have 0 spell slots left. You can't cast anymore spells.\n")
           print("Choose another action: attack | act | items |")
           new_action = input(">")
           return player_fight_command(new_action, enemy_health, spell_slots, disadvantage, health)
 
        else:
           print("Somethings not right!\n")
           print("Choose another action: attack | act | items |")
           new_action = input("Action >")
           return player_fight_command(new_action, enemy_health, spell_slots, disadvantage, health)
           
       elif act == "reason":
          print("You try to reason with the enemy. Roll for success! (D20)\n")
          main_menu("roll d20")
          if roll_value + charisma_mod >= 10:
            if reason_count == 0:
               print("The enemy seems contemplative, but continues to attack you.\n")
            elif reason_count == 1:
               print("The enemy looks at you, clearly swayed by whatever convincing things you said, but continues to attack you.\n")
            elif reason_count == 2:   
               print("The enemy starts nodding along, visibly liking your words.\n")
            else:
               print("The enemy sits down, unwilling to fight after the potent words you just preached.\n")
            reason_count += 1 
          else:
             reason_count -= 1
             print("The enemy looks at you strangely and laughs as you flounder under the scrutiny.\n")
          print("\n")
          return reason_count
          
       elif act == exit:
          print("\n")
          print("Choose another action: attack | act | items |")
          new_action = input(">")
          return player_fight_command(new_action, enemy_health, spell_slots, disadvantage, health)
          
          

    elif action == "items":
         print("\n")
         print(f"Items: {items}\n Which item would you like to use?\n")
         item = input("Item >")
         item = item.lower()
         if item == "health potion":
            items.remove("Health potion")
            print("You drink a health potion, restoring your health by 1D6 (Roll D6)!\n")
            main_menu("roll d6")
            health_gained = roll_value + constitution_mod
            print(f"You gain {health_gained} health!")
            health += health_gained
            print(f"Health: {health}\n")
            return enemy_health, spell_slots, health
         else:
            print("That's not a item!\n")
            return player_fight_command("items", enemy_health, spell_slots, disadvantage, health)
    else:
       print("Uhh thats not a valid action. Please choose an ACTUAL action.\n")
       print("Choose another action: attack | act | items |")
       new_action = input("Action >")
       return player_fight_command(new_action, enemy_health, spell_slots, disadvantage, health)
          
def handle_command(command):
    print("\n")
    global roll_value
    roll_value = 0
    command = command.lower()
    if "roll" in command:
        if command == "roll d20":
           roll_value = rolldice(20)  
        elif command == "roll d12":
           roll_value = rolldice(12) 
        elif command == "roll d10":
           roll_value = rolldice(10) 
        elif command == "roll d8":
           roll_value = rolldice(8) 
        elif command == "roll d6":
           roll_value = rolldice(6) 
        elif command == "roll d4":
           roll_value = rolldice(4) 
        else:
           return "Thats not right! Please reroll.\n" 
        print (f"You rolled a {roll_value}!\n")
        return False 
    elif command == "help":
        print("Available commands:")
        print("roll d20 - Roll a 20 sided die\nroll d12 - Roll a 12 sided die\nroll d10 - Roll a 10 sided die\nroll d8 - Roll a 8 sided die\nroll d6 - Roll a 6 sided die\nroll d4 - Roll a 4 sided die\ncheck sheet - check your stats\n")
        return True

    elif command == "check sheet":
        print(f"\nYour stats are:\nStrength: {strength} |{strength_mod}|\nDexterity: {dexterity} |{dexterity_mod}|\nConstitution: {constitution} |{constitution_mod}|\nIntelligence: {intelligence} |{intelligence_mod}|\nWisdom: {wisdom} |{wisdom_mod}|\nCharisma: {charisma} |{charisma_mod}|\nHealth:{health}\nSpell slots: |{spell_slots}|\n")
        return False

    else: 
        print(f"That's not the right command. Please enter the {command} command.\n")
        return True

def battle_loop(enemy_health, enemy_initiative, initiative, health, armour_class, enemy):
   global spell_slots 
   global turn
   turn = 0
   if enemy_initiative > initiative:
        player_first = False
   else:
        player_first = True
        
   while enemy_health > 0 and health > 0:
        turn += 1
        if player_first:
           print(f"Options\nfight - attack the {enemy} with your dagger\nact - misc actions including spells\nitems - use items\n")
           action = input("Action >")
           
           updated_values = player_fight_command(action, enemy_health, spell_slots, health, disadvantage)
           if updated_values:
              if isinstance(updated_values, tuple):
                 if len(updated_values) == 2:
                    enemy_health, spell_slots = updated_values
                 elif len(updated_values) == 3:
                    enemy_health, spell_slots, health = updated_values 
           
           if enemy_health <= 0:
              break
                      
           player_first = False
           continue
           
        else: 
          if enemy == "guard": 
           print("The guard takes his sword and takes a swing at you!")
          elif enemy == "robot":
           print("The robot beeps incessantly and rushes at you, arms swinging wildly!")
          else:
           print("The giant casually steps forward, unaware that you are right under him!!")
          if rolldice(20) >= armour_class:
                if enemy == "guard":
                  damage = rolldice(6)  
                  print("You try to dodge the sword, but you move into the attack instead!")
                elif enemy == "robot":  
                   damage = rolldice(8)
                   print("You casually sidestep the robot's arms but you get hit anyways when it shoots a laser at you!")
                else:
                   damage = rolldice(6) + rolldice(6)   
                   print("You try to think of someway to avoid it, but you can do nothing but look at the giant's foot and pray you survive!")
                print(f"The {enemy} deals {damage} damage!")
                health -= damage
                print(f"Health: {health}\n")
          else:
                print(f"Your {enemy}'s attack misses you by an inch and you breath a sigh of relief!\n")
          
          player_first = True
           
   if health <= 0:
       print("As you stagger from the hit, your vision starts to fade. You feel your life slipping away as you realize that you have died. (LMAO)\n") 
       exit() 
   elif enemy_health <= 0:
       print("You have defeated your enemy! You are victorious!\n")
       return True
   elif reason_count >= 3:
       print("You're enemy no longer wants to fight you. You have won!\n")
       return True

def check_options(location, health, spell_slots):
 print("Type a, b, c, etc to choose an option\n")
 if location == "p1":
    choice = input(">")
    if choice == "a":
       print("You try to force the door open, straining against the bars with all your might. Roll a strength check (D20)\n")
       main_menu("roll d20") 
       if roll_value + strength_mod >= 16:
          print("You manage to force the door open, and you walk out into a hallway. You see a guard standing in front of you, holding a sword. Roll initiative! (D20)\n")
          enemy = "guard"
          battle_setup(enemy)
          print("Good job! You defeated the guard! Unfortunately this is as far as You can go on this route! Expansions coming Never!") 
          exit()
       else: 
           if roll_value > 1:
              print("You slam yourself against the door, but to no avail.\nThe door won't budge, so you should probably find another way.\n")
              check_options("p1", health, spell_slots)
           else:
               print("You rush at the door, but you slip on a conveniently placed banana peel and hit a wall, taking 1d4 damage.\n")
               health -= rolldice(4)
               print(f"Health: {health}\n")
               check_options("p1", health, spell_slots)
           
    if choice == "b":
       print("You take your dagger out of your pocket and put it into the lock. Roll a intelligence check (D20)\n")
       main_menu("roll d20") 
       if roll_value + intelligence_mod >= 12:
          print("You manage to open the door and you walk out into a dungeon. Fire crackles in the distance and you find yourself in a... Volcano?!\n")
          print("As you blink in shock, you hear a surprised shout behind you. You turn around and you see a trembling dwarf with a wrench in his name.He screams unintelligibly and runs away as fast as he can.\nBefore you can chase after him, a you hear a loud thud and a clank from behind you. You turn around and see a giant robot with lava flowing through its veins. It looks like it's about to attack! Roll initiative! (D20)\n")
          enemy = "robot" 
          battle_setup(enemy)
          print("The robot takes a step towards you, eyes alight with rage before it stops. Stutters. Finally, it slumps down onto the ground and explodes into ash. You win!\nGood job, but I don't want to do anything else so yeahh. Expansions coming Never!")
       else:
           if roll_value > 1:
              print("You try to twist your dagger, but something jams and you can't turn it.")
              check_options("p1", health, spell_slots)
           else:
               print("You try to picklock the door, and find yourself succesful!\n\nUnfortunately, you walk out into a room full of guards. They look straight at you and don't hesitate before STABBING YOU.\nYou die lmao! Game Over\n")
               exit()
              
    if choice == "c":
       print("You look around the room and you notice a poster on the wall. Of course, you find a secret passageway behind it. You walk down the passageway and find yourself outside! As you stare at the forest around you, you hear a groan. You turn around, but you see nothing but a mountain. As you ponder on on what caused the sound, the mountain shifts before standing up! It's actually a giant!")
       if name == "david": 
        print("\nYou feel yourself surrounded by a golden glow as you stare at the giant. You feel a sense of power as you stare the giant down and realize that you have recieved a buff from the heavens!")
       print("Roll initiative! (D20)\n")  
       enemy = "giant"
       battle_setup(enemy)
       print("The giant howls in pain, pinpricks of blood dotting its feet, the only damage you were able to inflict. With tears in its eyes, it turns around and runs into the distance. You win!\nAlso game ends now. Yay good work!")
       exit()

def main_menu(expected_command):
    running = True 
    while running:
      user_input = input("> ")
      user_input = user_input.lower()
      
      if expected_command and expected_command != "no":
          if user_input == expected_command:
              running = handle_command(expected_command)
              if not running: 
                  return 
          elif user_input in ["help", "check sheet", "quit"]:
              running = handle_command(user_input)        
          else:
              print(f"Please type '{expected_command}'")
      else:
          running = handle_command(user_input)
  
def battle_setup(enemy):
    if enemy == "robot":
       enemy_initiative = rolldice(20) + 4
       enemy_health = (rolldice(6) + rolldice(6) + 16)
    elif enemy == "guard":
        enemy_initiative = rolldice(20) + 4
        enemy_health = (rolldice(8) + rolldice(8) + 10)
    else:
        enemy_initiative = rolldice(8) 
        enemy_health = (rolldice(10) + rolldice(10) + 24)
       
    main_menu("roll d20")
    initiative = roll_value
    battle_loop(enemy_health, enemy_initiative, initiative, health, armour_class, enemy,) 
    

def rolldice(sides):
    return random.randint(1, sides)

print("Welcome to the DND simulator!\nWe will begin with your character!")
name = input("What do you wish to name your character?\n")
print(f"{name}? Great choice! Now we shall roll for your stats, starting with Strength! Type 'help' to see what commands are available and choose the one which rolls a d20!\n")
name = name.lower()
roll_value = 0
main_menu("roll d20")
strength = roll_value
if name == "david":
 strength += 10
strength_mod = math. floor((strength - 10) / 2)

print(f"Okay, so your strength is {strength} and your modifier is {strength_mod}, so next is Dexterity! Type roll d20 to roll the dice!")
roll_value = 0
main_menu("roll d20")
dexterity = roll_value
if name == "david":
 dexterity += 10
dexterity_mod = math.floor((dexterity - 10) / 2)

print(f"Your dexterity is {dexterity} and your modifier is {dexterity_mod}! Now that you know the ropes, we'll roll for the rest of your stats and we will begin the adventure!")
dice_roll = "roll d20"
roll_value = 0
constitution = rolldice(20) 
intelligence = rolldice(20) 
wisdom = rolldice(20) 
charisma = rolldice(20) 
if name == "david":
 constitution += 10
 intelligence +=10
 wisdom += 10
 charisma += 10  

constitution_mod = math.floor((constitution - 10) / 2)
intelligence_mod = math.floor((intelligence - 10) / 2)
wisdom_mod = math.floor((wisdom - 10) / 2)
charisma_mod = math.floor((charisma - 10) / 2)
armour_class = (10 + dexterity_mod)
spell_slots = 12
reason_count = 0
items = ["Health potion", "Health potion", "Health potion"]

health = (12 + rolldice(8) + constitution_mod)
print("rolling...")

time.sleep(4)

print("Done!\nUse the command check sheet to see your stats!")
dice_roll = "no"
main_menu(dice_roll)

print("Now that you've rolled your stats, we will begin the adventure!\nYou woozily wake up, and you find yourself in a dark room. You try to recall something, but you can't remember a thing. You look around and you find a prison door, iron bars and a bed with paper thin sheets on it. You search your pockets but can only find a small dagger, sharp enough to fit inside a keyhole.\nYou look around and notice 3 things you could do. a: you could try and force the door open. b: you could try and pick the lock on the door. c: you could try to search the room for more information. \nWhat do you do?")
check_options("p1", health, spell_slots)

            
           
             
            
         