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

# The game starts here.

label start:
    $ caps = 0
    $ items = []
    #play music #Fallout intro music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room #fallout

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy #VAULT OVERSEER

    # These display lines of dialogue.

    VO "Holy crap! the bombs just dropped!"

    VO "Hurry up and make your way into the vault its our only safety! Thank Goodness for Vault-Tec."

label safetyordeath:

    menu:
        "Should I trust my life with Vaul-Tec or should I hop into this conviently placed Pulowski Preservation Shelter"

        "Enter the vault.":

            jump vaultEntrance

        "Ill be better off in the Pulowski Chamber":

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
    $ items = ["vault jumpsuit"]
    VSC1 "Follow me this way towards our decontamination chambers."

    scene insidecryopod

    VSC1 "You're just going to feel a little blast of cold air"

    "{b}YOU ARE FROZEN{/b}"

    jump vaultExit



  
