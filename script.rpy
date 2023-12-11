
# The script of the game goes in this file.
transform big_size:
    zoom 1.5
transform half_size:
    zoom 0.75
# Declare characters used by this game. The color argument colorizes the
# name of the character.


define VO = Character("Vault Overseer", image = "")

define VS1 = Character("Vault Security", image = "VaultSecurity")

define VSC1 = Character("Vault Scientist", image = "VaultScientist")

define BB = Character("Bunker Guy")

define MH = Character("Mr. Handy")

define DM = Character("Dogmeat")

define DW = Character("Distressed Women")
# The game starts here.

label start:
    $ caps = 0
    $ items = []
    $ weapons = []
    $ clothes = []
    $ special = []
    $ companion = []
    $ queststatus = []
    #play music #Fallout intro music

    scene bg room #fallout

    show eileen happy #VAULT OVERSEER


    VO "Holy crap! the bombs just dropped!"

    VO "Hurry up and make your way into the vault its our only safety! Thank Goodness for Vault-Tec."

label safetyordeath:

    menu:
        "Should I trust my life with Vaul-Tec or should I hop into this conviently placed Pulowski Preservation Shelter."

        "Enter the vault.":

            jump vaultEntrance

        "Ill be better off in the Pulowski Chamber.":

            jump pulowskiDeath

label pulowskiDeath:

    #play sound #Pulowski chamber ad

    scene #Picture of interior of chamber

    "Seems like this was the safe option."

    scene #picture of skeleton in chamber

    "{b}YOU ARE DEAD{/b}"

    jump safetyordeath

label vaultEntrance:

    #play sound #vault door closing sound

    scene vaultentrance at big_size

    show vaultsecurity at half_size, left

    show vaultscientist at big_size, center

    VS1 "Welcome to the Vault, here's your jumpsuit."
    $ clothes = ["vault jumpsuit"]
    VSC1 "Follow me this way towards our decontamination chambers."

    scene insidecryopod

    VSC1 "You're just going to feel a little blast of cold air."

    scene black

    "{b}SOME TIME PASSES{/b}"

    scene openpod

    "What the hell happened? I feel like I have been sleeping for days."
    "Where is everyone? It seems like all the staff are gone and all the dwellers are frozen in these weird pods."
    
    menu:
        "Maybe I should try to leave, or maybe I should look around."
    
        "Leave the Vault.":

            jump outsidevault
        
        "Search the Vault before leaving.":

            jump vaultStorageRoom

label vaultStorageRoom:

    scene vaultstorageroom

    show deadsecurity

    "It seems like something must have happened theres a dead security guard and everyone else seems to be gone."


label choiceloot:

    scene vaultstorageroom

    show deadsecurity

    menu:
        "Should I check the terminal, try to pick the locked armory, or leave the vault?"

        "Check the Terminal.":

            jump terminalscreen
        
        "Try to pick the armory lock.":
                                
            jump armoryclose

        "Leave the Vault.":

            jump outsidevault

label armoryclose:

    scene armorycloseup

    "I doubt im going to be able to pick this lock but ill try."

    $ lockpick = renpy.random.randint(1,10)

    if lockpick > 3:
        "Wow, I did it, looks like I found a 10mm pistol."
        $ weapons = ["Pistol"]
    else:
        "No surprise, I failed, but I was able to grab a combat knife through the gaps."
        $ weapons = ["Melee"]

    jump choiceloot

label terminalscreen:

    scene terminalscreen

    "Shit, the terminal is saying that its the year 2100, which would mean that I have been asleep for 23 years."

    "The terminal also says that all staff left over 10 years ago and just decided to leave everyone frozen. It says the decision was made by the overseer."

    jump choiceloot

label outsidevault:

    scene outsidevault

    "Looks like the whole Common Wealth has been destroyed my neighborhood is in ruins and it looks like half of Boston's skyscrapers have collapsed."

    "I should try to find out answers to why the vault staff isnt in the vault anymore"

label explorechoice:

    menu:

        "Should I head towards Boston to investigate Vault-Tec headquarters or go check out my neighborhood?"

        "Head to Boston.":

            jump pathtoboston

        "Check out my Neighborhood":

            jump neighborhood
        
label neighborhood:

    scene neighborhood

    "Wow this place is destroyed my house is in shambles."

    "I wonder what happen to my neighbors who didnt end up frozen in the vault."

label neighborhoodchoice:

    scene neighborhood

    menu:

        "Should I check out my house, my neighbors houses, or head to Boston."

        "Head to Boston.":

            jump pathtoboston

        "Check out my house.":

            jump myhouse
        
        "Check out my neighbors houses.":

            jump neighborhouses

label myhouse:

    scene myhouse

    "There's not much left here, but I might have some clothes I could wear instead of this jumpsuit."

label myhousechoice:

    scene myhouse

    menu:

        "What should I loot or should I go back to the neighborhood?"

        "Check the bedroom.":

            scene bedroom

            $ clothesfound = renpy.random.choice(["Pajamas","Military Fatigues","Black Suit"])

            if clothesfound == "Pajamas":
                
                menu: 

                    "I found Pajamas should I wear them instead of my jumpsuit?"

                    "Yes.":

                        $ clothes = ["Pajamas"]
                    
                    "No.":

                        $ clothes = ["Vault Jumpsuit"]

            elif clothesfound == "Military Fatigues":
                            
                    menu: 

                        "I found my old Military Fatigues should I wear them instead of my jumpsuit?"

                        "Yes.":

                            $ clothes = ["Military Fatigues"]
                                
                        "No.":

                            $ clothes = ["Vault Jumpsuit"]

            elif clothesfound == "Black Suit":
                                        
                    menu: 

                        "I found my old Military Fatigues should I wear them instead of my jumpsuit?"

                        "Yes.":

                            $ clothes = ["Military Fatigues"]
                                            
                        "No.":

                            $ clothes = ["Vault Jumpsuit"]

            jump myhousechoice 
        
        "Check Garage":

            scene garage

            $ gunfound = renpy.random.randint(1,10)

            if gunfound > 8:

                $ weapons = ["Shotgun"]

                "I found my old hunting shotgun, this has to be better then what i've found already."
            
            else:

                "I found nothing someone must have robbed my house."

            jump myhousechoice

        "Check the kitchen":
            
            scene kitchen

            "There's nothing left in here except some very old Nuka Cola and Salisbury Steaks."

            "I probably shouldn't eat those."

            jump myhousechoice

        "Head back to the neighborhood.":

            jump neighborhoodchoice

label neighborhouses:
    
    scene neighborhood

    "It looks like my neighbors houses are in better condition then mine maybe ill find something in them."

    "My one neighbor still seems to have a working Mr. Handy maybe ill talk to it."

label neighborhouseschoice:

    menu:

        "Should I talk to the Mr. Handy, loot the houses, or head back to my house."

        "Talk to Mr. Handy.":

            label misterhandychoice1:

                scene lonewanderhouse

                show mrhandy

                MH "MASTER YOUR HOME!"

                MH "Wait your not master."

                "Mr. Handy have you seen any other people?"

                MH "Sorry, im programmed to only talk to master and his family."

                menu:

                    "Mr. Handy wont talk to me what should I do?"

                    "Convince Mr. Handy im master : Charisma":

                        "I am your master, do you not remember me?"
                        
                        if "Charisma" in special:

                            MH "Sorry, Master my hardware must have been mistaken."

                            MH "What would you like to know?"

                            label mrhandychoices:

                                menu:

                                    "What should I ask Mr. Handy?"

                                    "What year is it?":

                                        MH "The year is 2100."

                                        jump mrhandychoices
                                    
                                    "What are you still doing here?":

                                        MH "I am programmed to do my job no matter the conditions."

                                        jump mrhandychoices
                                    
                                    "Have you seen anybody recently?":

                                        MH "Sir, Most of your neighbors are gone but the one who lives in the yellow house is in a bunker in his backyard."

                                        "Have you seen anyone else?"

                                        MH "There was a vault dweller who was asking for direction to Vault-TEC HQ but I couldn't help since he wasnt my programmed master."

                                        "Thank you Mr. Handy."

                                        jump mrhandychoices
                                    
                                    "Go Back.":

                                        jump neighborhouseschoice

                        else: 
                            
                            MH "No your not."

                            jump misterhandychoice

                    "Lie and Tell Mr. Handy I am his family : 50%% ":

                        $ lie = renpy.random.randint(1,10)

                        if lie > 5:

                            MH "Oh sorry I was mistaken, sorry for the inconvenience"

                            MH "What would you like to know?"

                            label mrhandychoices2:

                                menu:

                                    "What should I ask Mr. Handy?"

                                    "What year is it?":

                                        MH "The year is 2100."

                                        jump mrhandychoices2
                                    
                                    "What are you still doing here?":

                                        MH "I am programmed to do my job no matter the conditions."

                                        jump mrhandychoices2
                                    
                                    "Have you seen anybody recently?":

                                        MH "Sir, Most of your neighbors are gone but the one who lives in the yellow house is in a bunker in his backyard."

                                        "Have you seen anyone else?"

                                        MH "There was a vault dweller who was asking for direction to Vault-TEC HQ but I couldn't help since he wasnt my programmed master."

                                        "Thank you Mr. Handy."

                                        jump mrhandychoices2
                                    
                                    "Go Back.":

                                        jump neighborhouseschoice
                            
                        else: 

                            MH "You're not part of masters family."

                            jump misterhandychoice1

                    "Reprogram Mr. Handy and set myself as master : Intelligence":
                        
                        if "Intelligence" in special:

                            MH "NEW MASTER DETECTED"

                            MH "Hello, new master."

                            MH "What would you like to know?"

                            label mrhandychoices3:

                                menu:

                                    "What should I ask Mr. Handy?"

                                    "What year is it?":

                                        MH "The year is 2100."

                                        jump mrhandychoices3
                                    
                                    "What are you still doing here?":

                                        MH "I am programmed to do my job no matter the conditions."

                                        jump mrhandychoices3
                                    
                                    "Have you seen anybody recently?":

                                        MH "Sir, Most of your neighbors are gone but the one who lives in the yellow house is in a bunker in his backyard."

                                        "Have you seen anyone else?"

                                        MH "There was a vault dweller who was asking for direction to Vault-TEC HQ but I couldn't help since he wasnt my programmed master."

                                        "Thank you Mr. Handy."

                                        jump mrhandychoices3
                                    
                                    "Go Back.":

                                        jump neighborhouseschoice

                        else: 
                            
                            MH "Your not intelligent enough."

                            jump misterhandychoice1

                    "Go Back.":

                        jump neighborhouseschoice

        "Loot the Houses.":

            label loothouseneighchoice:

                scene loothouse

                menu:

                    "should I loot the yellow house, the blue house, or should I go back?"

                    "Loot the yellow house.":

                        label yellowhouselooting:

                            scene yellowhouse

                            menu:

                                "You found a bunker in the backyard of the yellow house. It looks homemade should I check it out or move on?"

                                "Try to lockpick the bunker.":

                                    scene bunkerdoor

                                    $ lockpick = renpy.random.randint(1,10)

                                    if lockpick > 4:

                                        label bunkerchoice:

                                            scene bunkerdoor

                                            menu:

                                                "I unlocked the bunker, should I enter the bunker?"
                                                
                                                "Yes enter the bunker.":

                                                    scene insidebunker

                                                    show bunkerguy

                                                    BB "HEY, WHAT ARE YOU DOING IN HERE?"

                                                    if "Military Fatigues" in clothes:

                                                        BB "Wait, your in the military I've been waiting for you guys to come."

                                                        BB "Are you here restore order and rebuild America?"

                                                        label bunkerguychoice:

                                                            scene insidebunker

                                                            menu:

                                                                "This guy is wondering if im in the military what should I say?"

                                                                "Yes, im here to save you but I need your Service Rifle that you have over there":

                                                                    $ conversationchance = renpy.random.randint (1,10)

                                                                    if conversationchance > 8:

                                                                        $ weapons = ["Rifle"]

                                                                        BB "Of course anything for the military I am a patriot."

                                                                        BB "Now get out there and restore order!"

                                                                        jump loothouseneighchoice

                                                                    else:

                                                                        BB "WAIT, if you were actually in the military you wouldn't need my gun, YOU COMMIE."

                                                                        scene black

                                                                        "{b}YOU DIED{/b}"

                                                                        jump bunkerguychoice

                                                                "No, I used to be but after the bombs dropped I went into a Vault.":

                                                                    BB "Oh so you were a coward and ran when the commie's attacked."

                                                                    BB "Get out of my bunker."

                                                                    jump loothouseneighchoice

                                                                "Ignore question : how long have you been down here?":

                                                                    BB "Im not sure, its had to have been atleast 10 years."

                                                                    BB "Shortly after the bombs dropped things went to shit, the military lost control and food became scarce."

                                                                    BB "I was scared things were going to get worse so I built this bunker and haven't left since."

                                                                    BB "Now get out of bunker before I shoot you."

                                                                    jump loothouseneighchoice
                                                    
                                                    elif "Vault Jumpsuit" in clothes:

                                                        BB "Wait, your one of those vault dwellers."

                                                        BB "I haven't seen one of you guys in a while. Its had to have been at least 10 years."

                                                        "You've seen another vault dweller before?, what did he say?"

                                                        BB "He said he was some overseer of the vault on the hill but thats all I remember."

                                                        "Are you sure that's all you remember?"

                                                        BB "I think he said something about talking to a Mr. Handy, now get out of my bunker, you have your own."

                                                        jump loothouseneighchoice

                                                    else:

                                                        "I just stumbled opun this place I dont mean any harm."

                                                        BB "I haven't seen anyone in a while. Its had to have been at least 10 years."

                                                        "You've seen another person?, what did he look like?"
                                                        
                                                        BB "He was in a vault dweller outfit."

                                                        "What did he say to you?"

                                                        BB "He said he was some overseer of the vault on the hill but thats all I remember."

                                                        "Are you sure that's all you remember?"

                                                        BB "I think he said something about talking to a Mr. Handy, now get out of my bunker."

                                                        jump loothouseneighchoice
                                                
                                                "No, its to risky, go back.":
                                                    
                                                    jump loothouseneighchoice


                                "Go Back.":

                                    jump loothouseneighchoice

                    "loot the blue house.":

                        scene specialbook

                        "You look around and find a book that has the title: you are SPECIAL."

                        menu:
                            
                            "You read the book and it says to pick a special trait."

                            "Luck":

                                $ special = ["Luck"]
                            
                            "Perception":

                                $ special = ["Perception"]
                            
                            "Agility":

                                $ special = ["Agility"]
                            
                            "Charisma":

                                $ special = ["Charisma"]
                            
                            "Intelligence":

                                $ special = ["Intelligence"]
                            
                            "Endurance":

                                $ special = ["Endurance"]

                            "Strength":

                                $ special = ["Strength"]
                        
                        jump loothouseneighchoice
                    
                    "Go back.":
                        
                        jump neighborhouseschoice

        "Head Back to My House.":

            jump neighborhoodchoice

label pathtoboston:

    scene roadtoboston

    "Your on your way to Boston when you see a Red Rocket Truck stop and theres a wastelander in distress there."

    menu:

        "What should I do?"

        "Dont stop and keep walking.":

            jump pathtoboston2
        
        "Stop and check out the Red Rocket Truck Stop.":
            
            jump redrocket

label redrocket:

    scene redrocket

    "You stop to check out the red rocket and see a dog, a women in distress, and building with possible loot."

    label redrocketchoice:

        scene redrocket

        menu:

            "What should I check out first?"

            "The dog.":

                scene dog

                "The dog seems friendly."

                DM "WOOF!"

                "His collar says Dogmeat on it."

                menu:

                    "he seems friendly and seems to want to follow me, should I let him?"

                    "Yes, he can come with me.":
                        
                        DM "WOOF!"

                        $ companion = ["Dog"]

                        "You have gained the companion Dogmeat."

                        jump redrocketchoice
                    
                    "No, who likes dogs.":

                        jump redrocketchoice


            "The woman.":

                scene nexttoredrocket

                show womanindistress

                DW "Please help me!"

                "What's wrong, you seem fine."

                DW "A molerat took my son!"

                DW "Can you get him back for me?"

                label womanchoice:

                    scene nexttoredrocket

                    show womanindistress

                    menu:

                        "Should I help this woman get her son back?"

                        "Yes":

                            "Sure, I can help you where's your son?"

                            DW "The molerat took him behind the Red Rocket!"

                            label moleratchoice:

                                scene molerat
                            
                                menu:

                                    "You see the molerat, and he seems more dangerous than you first thought, what should I do?."

                                    "Attack molerat with weapon: requires a weapon":

                                        "You pull out your weapon and attack the molerat"

                                        $ success = renpy.random.randint(1,10)

                                        if "Rifle" in weapons:

                                            "You attack the molerat with a rifle."

                                            "You killed the molerat"

                                            $ queststatus = ["Complete"]
                                        
                                        elif "Shotgun" in weapons:

                                            "You attack the molerat with a shotgun."

                                            if success < 10:
                                                
                                                "You killed the molerat"

                                                $ queststatus = ["Complete"]
                                            
                                            else:

                                                scene black

                                                "{b}YOUR ARE DEAD{/b}"

                                                jump womanchoice
                                        
                                        elif "Pistol" in weapons:

                                            "You attack the molerat with a pistol."

                                            if success < 8:
                                                
                                                "You killed the molerat"

                                                $ queststatus = ["Complete"]
                                            
                                            else:

                                                scene black

                                                "{b}YOUR ARE DEAD{/b}"

                                                jump womanchoice
                                        
                                        elif "Melee" in weapons:

                                            "You attack the molerat with a melee weapon"

                                            if "Strength" in special:

                                                if success < 7:

                                                    "You killed the molerat"

                                                    $ queststatus = ["Complete"]
                                                
                                                else:

                                                    scene black

                                                    "{b}YOUR ARE DEAD{/b}"

                                                    jump womanchoice

                                            elif success < 6:
                                                
                                                "You killed the molerat"

                                                $ queststatus = ["Complete"]
                                            
                                            else:

                                                scene black

                                                "{b}YOUR ARE DEAD{/b}"

                                                jump womanchoice
                                        
                                        else: 

                                            "You dont have a weapon to attack."

                                            jump womanchoice
                                    
                                    "Attack molerat with fists":

                                        "You ready your fists to attack the molerat"

                                        $ success = renpy.random.randint(1,10)

                                        if "Strength" in special:

                                            if success < 5:

                                                "You killed the molerat"

                                                $ queststatus = ["Complete"]

                                        elif success < 3:

                                            "You killed the molerat"

                                            $ queststaus = ["Complete"]
                                        
                                        else:
                                            
                                            scene black

                                            "{b}YOUR ARE DEAD{/b}"

                                            jump womanchoice
                                    
                                    "Have your companion attack the molerat":

                                        $ success = renpy.random.randint(1,10)

                                        if "Dogmeat" in companion:

                                            "Your Companion Dogmeat Attacks The Molerat."

                                            if success < 8:
                                                
                                                "Your companion killed the molerat"

                                                $ queststatus = ["Complete"]
                                            
                                            else:

                                                "Your companion failed and is too injured to try again."

                                                jump womanchoice
                                        
                                        else: 
                                            
                                            "You don't have a companion."

                                            jump womanchoice
                                    
                                    " I saved your son from the molerat":

                                        if queststatus == "Complete":

                                            DW "Thank you so much! here are 100 caps as a token of my gratitude."

                                            $ caps = caps + 100

                                            "Caps, why would I want caps?"

                                            DW "Caps are the currency of Common Wealth, what do you live under a rock?"

                                            "Sorta."

                                            "Thank you for the reward."

                                            $ radiostatus = ["SavedSon"]

                                            jump redrocketchoice

                                        else: 
                                            
                                            DW "You liar, you haven't saved him yet."

                                            jump womanchoice
                                            
                                    "Run away":

                                        jump redrocketchoice
   
                        "No":

                            "Sorry, lady your on your own."

                            jump redrocketchoice

            "The Bulding.":

                scene truckstopinterior

                "You enter the truck stop and its in pretty good condition."

                label truckstopchoice:

                    scene truckstopinterior

                    "Should I enter the garage, the back room, or the store front?"

                    "Enter the Garage":

                        scene garage

                        "You search the garage and dont find much"

                        "There's a bunch of car parts but I haven't seen any fixable cars."

                        jump truckstopchoice

                    "Enter the Backroom":

                        scene backroom

                        "There doesn't seem to be any loot in the room."

                        "However, there is a radio in the corner of the room."

                        scene radio

                        "You listen in and a news station called Diamond City Radio is discussing a vault dweller spotting near the vault."

                        jump truckstopchoice

                    "Check the Store front":

                        scene storefront

                        "You check the store front and only find rotton and expired food."

                        jump truckstopchoice
                    
                    "Go Back.":
                        
                        return redrocketchoice
            
            "Go Back.":

                jump pathtoboston2

label pathtoboston2:

    $ queststatus = []

    scene pathtoboston2

    



