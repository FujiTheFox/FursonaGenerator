from PIL import Image, ImageFont, ImageDraw 
import random
import time

############################CONFIG#####################
font = ImageFont.truetype(".\Images/Fonts/Roboto-Regular.ttf", 40)


Fursonanames = ["Wolf" , "BlueWolf" , "Amazing wolf" , "Wolf Proto"]
randomanme = random.choice(Fursonanames)

randomhead = random.randint(1 , 3)
randombackground = random.randint(1 ,4)
randomhands = random.randint(1 ,3)
randomlegs = random.randint(1 , 4)
randombody =  random.randint(1, 5)




template = Image.open(fr".\Images/templates/1.gif").convert("RGBA")
headdesgin = Image.open(fr".\Images/main/Head/1.gif").convert("RGBA")
background = Image.open(fr".\Images/backgroundimages/{randombackground}.gif").convert("RGBA")
hands = Image.open(fr".\Images/main/Arms/{randomhands}.gif").convert("RGBA")
legs = Image.open(fr".\Images/main/Legs/{randomlegs}.gif").convert("RGBA")
bodydesgin = Image.open(fr".\Images/main/Body/{randombody}.gif").convert("RGBA")

######################End of config##################


print ("---------------------------------------------")
print ("- 1. Full fursona with generated infomation -")
print ("- 2. Full fursona with Empty Infomation     -")
print ("- 3. Generate fursona without any text      -")
print ("- 4. Fursona without background             -")
print ("- 5. List all the credits                   -")
print ("- 6. Shows the version of this app          -")
print ("---------------------------------------------")
print ("")

option = input("Enter an Option > ") 
if option == "1": 
    print ("Generating a full fursona for you :)")

    ###############################
    # This combies layers togeter #
    ###############################

    backgroundandtemplate = Image.alpha_composite(background , template)
    headdesginandbackground = Image.alpha_composite(backgroundandtemplate, headdesgin)
    someething =  Image.alpha_composite(headdesginandbackground, hands)
    iguess = Image.alpha_composite(someething , legs)
    bodystage = Image.alpha_composite(iguess, bodydesgin)

    ###################################
    # This adds the text to the image #
    ###################################

    draw = ImageDraw.Draw(bodystage)
    draw.text((0, 0),f"Name: {randomanme}",(255,255,255),font=font)
    draw.text((0, 40),f"Age: {random.randint(10, 35)}",(255,255,255),font=font)
    draw.text((0, 80),f"",(255,255,255),font=font)



    ###################################
    # Saves the image                 #
    ###################################
    bodystage.save('.\Images/done/fursona.gif', 'gif')


    print ("Your fursona has been generated   yw    (Look in the done folder)")
    time.sleep(5)




elif option == "2": 
    print ("Generating a full fursona with empty text (so you can fill it in)")

    ###############################
    # This combies layers togeter #
    ###############################

    backgroundandtemplate = Image.alpha_composite(background , template)
    headdesginandbackground = Image.alpha_composite(backgroundandtemplate, headdesgin)
    someething =  Image.alpha_composite(headdesginandbackground, hands)
    iguess = Image.alpha_composite(someething , legs)
    bodystage = Image.alpha_composite(iguess, bodydesgin)

    ###################################
    # This adds the text to the image #
    ###################################

    draw = ImageDraw.Draw(bodystage)
    draw.text((0, 0),f"Name: ___________",(255,255,255),font=font)
    draw.text((0, 40),f"Age: ___________",(255,255,255),font=font)
    draw.text((0, 80),f"",(255,255,255),font=font)


    ###################################
    # Saves the image                 #
    ###################################
    bodystage.save('.\Images/done/fursona.gif', 'gif')


    print ("Your fursona has been generated   yw    (Look in the done folder)")
    time.sleep(5)









    
elif option == "3": 
    print ("Generating Only Fursona Without any text (just clear fursona)")




    ###############################
    # This combies layers togeter #
    ###############################

    backgroundandtemplate = Image.alpha_composite(background , template)
    headdesginandbackground = Image.alpha_composite(backgroundandtemplate, headdesgin)
    someething =  Image.alpha_composite(headdesginandbackground, hands)
    iguess = Image.alpha_composite(someething , legs)
    bodystage = Image.alpha_composite(iguess, bodydesgin)




    ###################################
    # Saves the image                 #
    ###################################
    bodystage.save('.\Images/done/fursona.gif', 'gif')


    print ("Your fursona has been generated   yw    (Look in the done folder)")
    time.sleep(5)
elif option == "4": 
    print ("Generating  Fursona Without Background")
    ###############################
    # This combies layers togeter #
    ###############################


    headdesginandbackground = Image.alpha_composite(template, headdesgin)
    someething =  Image.alpha_composite(headdesginandbackground, hands)
    iguess = Image.alpha_composite(someething , legs)
    bodystage = Image.alpha_composite(iguess, bodydesgin)




    ###################################
    # Saves the image                 #
    ###################################
    bodystage.save('.\Images/done/fursona.gif', 'gif')


    print ("Your fursona has been generated   yw    (Look in the done folder)")
    time.sleep(5)
elif option == "5": 
    print ("Fujithefox programer (the person who made this fursona possible")
    print ("drawmanWLHA Artist (Made the fursona character)")
elif option == "6": 
    print ("Version 0.0.20")
else: 
    print("Please enter the correct number") 




