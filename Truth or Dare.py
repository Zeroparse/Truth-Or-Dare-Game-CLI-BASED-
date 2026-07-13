import random
truth = {
    'male': [
        'What is the most awkward or embarrassing thing that has ever happened to you during a romantic moment?',
        'Have you ever accidentally sent a text meant for a crush or partner to a parent or a group chat?',
        'What is your biggest, strangest turn-on that you rarely admit to anyone?',
        'Where is the riskiest or most public place you’ve ever hooked up with someone?',
        'Who in this room would you most want to be trapped in an elevator with for an hour?',
        'Have you ever faked being awake or asleep just to avoid an awkward situation in bed?',
        'What is the absolute weirdest thing you’ve ever done when you were home completely alone?',
        'Have you ever peed in a swimming pool or the shower? (Be honest!)',
        'If you had to wear one of your friend\'s underwear for a day, whose would you pick and why?',
        'What’s the most embarrassing thing your parents have ever caught you doing?',
        'Have you ever skipped washing your hands after using a public restroom because no one was looking?',
        'What is the longest you’ve ever gone without showering or changing your underwear?',
        'What is the most embarrassing song or artist on your current playlist?',
        'Have you ever practiced a facial expression or a conversation in the mirror?',
        'What is a "guilty pleasure" movie or TV show that you secretly love?',
        'Have you ever pretended to know how to fix something when you actually had no idea what you were doing?',
        'What is the dumbest thing you have ever done on a dare or to impress someone'
    ],
    'female': [
        'What is the weirdest habit you have when you are completely alone in your room?',
        'Have you ever worn the same bra for a week straight without washing it?',
        'What is your go-to fake excuse to get out of a terrible date or a social plan?',
        'Have you ever stalked someone on social media and accidentally liked a photo from three years ago?',
        'What is the most ridiculous or dramatic lie you’ve told just to get attention from a crush?',
        'Have you ever practiced kissing on your pillow or a stuffed animal? (Be honest!)',
        'What is the most awkward or embarrassing thing that has ever happened to you in the bedroom?',
        'Where is the riskiest or most unusual public place you’ve ever gotten intimate with someone?',
        'Have you ever sent a spicy text message or photo to the completely wrong person?',
        'Who is the most unexpected or scandalous person you have ever had a crush on?',
        'What is your biggest, weirdest turn-on that sounds crazy out loud?',
        'Have you ever pretended to be drunker than you were just to have an excuse to be flirty?',
        'Have you ever sniffed your own dirty laundry to see if it was clean enough to wear again?',
        'What is the grossest thing you do on a regular basis when nobody else is looking?',
        'If you had to pick one person in this room to share a toothbrush with, who would it be?',
        'Have you ever accidentally let out a loud fart in front of someone you were trying to impress?',
        'What is the absolute weirdest thing you\'ve ever used as a makeshift bathroom when you couldn\'t find one?',
        'Have you ever practiced a fake laugh or a "cute" sneeze to make yourself seem more attractive?',
        'What is the wildest, most inappropriate dream you\'ve ever had about someone in this room?',
        'Have you ever hooked up with someone and completely forgotten their name the next day?',
        'What is your absolute favorite, most scandalous thing to do in bed that you rarely talk about?',
        'Have you ever gotten caught naked or in the middle of a spicy moment by a family member or roommate?',
        'If your sex life was a movie title, what would it be and why is it hilarious?',
        'What is the most embarrassing song or audio track you\'ve ever accidentally blasted from your phone while trying to set a mood?'
    ]
}

dare = {
    'male': [
        'Give the person to your left a 30-second passionate hickey wherever they choose.',
        'Blindfold yourself, let someone in the room kiss you on the lips, and guess who it was.',
        'Let the person to your right reach inside your pants and leave their hand there for one full round.',
        'Sit lap-to-lap with the person of your choice and whisper the dirtiest thing you want to do to them in their ear.',
        'Take off your shirt and let the person to your left trace a naughty word on your bare chest using only their tongue.',
        'Lie down on your back and let the person sitting opposite you dry-hump you for 15 seconds.',
        'Exchange a piece of clothing with the person of the opposite sex, but you both have to strip it off right here in the room.',
        'Give a 1-minute, incredibly detailed description of the best sexual experience you’ve ever had to the entire room.',
        'Let the person to your right sit straddling your lap for the next two rounds of the game.',
        'Slowly undo three buttons on your shirt (or take it off) using only your teeth on someone else\'s clothing.',
        'Kiss the inner thigh of the person sitting to your left, getting as high up as they will allow.',
        'Pick someone in the room to go into a dark room or closet with you for "Two Minutes in Heaven" right now.',
        'Let the group choose two people in the room who have to French kiss you at the exact same time.',
        'Take a shot of alcohol directly off the chest, stomach, or neck of the person sitting opposite you.',
        'Let someone of your choice put their hand down your pants and grab whatever they find for 10 seconds.',
        'Seductively bite the earlobe of the person to your right and moan quietly while doing it.',
        'Spend the next round of the game lying completely flat on the floor with someone else lying directly on top of you.',
        'Let the person to your left use their bare hands to feel up your chest and stomach underneath your shirt for 30 seconds.',
        'Lock lips with the person you find most attractive in this room for a continuous 10-second count.',
        'Show the room the last spicy, adult photo or video you saved or sent on your phone.',
        'Let the person sitting next to you spank you as hard as they want three times in a row.',
        'Suck on the finger of the person to your right for 15 seconds while making intense eye contact.',
        'Let the group vote on which two people in the room you have to make out with for 5 seconds each.',
        'Unbutton the pants of the person sitting closest to you using only your teeth.'
    ],
    'female': [
        'Put on a blindfold, let the guy of your choice sit in front of you, and try to guess what part of his body your lips are touching.',
        'Suck on an ice cube for 10 seconds, then immediately unzip the guy opposite you and give him a freezing cold blowjob simulation through his underwear.',
        'Sit straddling a guy\'s lap facing away from him, and let him reach around to fondle your breasts while you answer questions for the next round.',
        'Pick a guy and let him use his teeth to pull your panties down to your ankles right here in the room.',
        'Give a detailed, audio-only performance of what you sound like when you are reaching your climax, using the microphone on someone\'s phone.',
        'Let the guy to your right slide his hand directly between your thighs and find your sweet spot, holding it there for a full 60 seconds.',
        'Lie flat on the table or floor and let the guy you find most attractive trace a line of alcohol from your belly button down to your underwear line and lick it off.',
        'Go into the bathroom or a dark room with the guy of your choice and let him take a scandalous photo of you that only he gets to keep.',
        'Unbutton your shirt completely and let the guy to your left use his tongue to locate and swirl around both of your nipples.',
        'Sit on a guy\'s lap and rub yourself against his crotch until he admits out loud that he is starting to get hard.',
        'Let the group nominate one guy who gets to grab you by the hair and give you a rough, dominant make-out session for 15 seconds.',
        'Squeeze a dollop of whipped cream (or pour a drink) onto a guy\'s package over his pants and lick every single drop off.',
        'Let the guy sitting opposite you slip his hand completely inside your bra and play with your nipples for the next two rounds.',
        'Pick a guy to stand behind you and dry-hump you aggressively from behind while you try to read a recipe out loud without laughing.',
        'Take a sip of a drink, hold it in your mouth, and transfer it to the guy of your choice via a deep, sloppy French kiss without spilling a drop.',
        'Let the guy to your left lift you up against the wall while you wrap your legs around his waist, holding that position for 20 seconds.',
        'Show the room exactly how deep you can take a banana or cucumber down your throat without gagging.',
        'Let a guy blindfold you, pull out his package, and gently press it against your lips or cheek so you can guess who it belongs to.',
        'Strip down to completely nothing from the waist down and sit on a towel on the lap of the guy you like most for one round.',
        'Whisper the exact text message you would send to a guy if you wanted him to come over for a completely no-strings-attached hookup right now.',
        'Let the guy to your right reach his bare hand under your clothing to find your bare ass, and let him give it a hard, leaving-a-mark slap.',
        'Get on all fours on the floor and let the guy behind you smack your ass while talking dirty to you like you\'ve been bad.',
        'Spend the next round of the game sitting completely naked from the waist up, using only your hands (or a guy\'s hands) to cover yourself.',
        'Let the guy of your choice unbutton his pants completely, then slide your bare hand inside his underwear to stroke him for 15 seconds.'
    ]
}

random_sel = [truth, dare]



def main():
    print(f'TRUTH OR DARE 😈 \nHere are the rules: \n1. Once your Truth or Dare is assigned, you cannot switch options. You are locked in\n2. No bail outs!\n3. Truths must be specific and complete. Vague or "I don\'t remember" answers are a fail; the group can force a Dare instead \n4. All Dares must be completed within five minutes of being assigned, or you fail \n5. The host can immediately cancel any Dare that is dangerous, illegal, or destructive, and issue a replacement \n6. Enter Q at anytime to end the game\n Enjoy 💦\n')
    player_counts = int(input('How many Players? '))
    player_data = prompt_players(player_counts)
    #print(player_data)
    game_prompt(player_data)





def prompt_players(counts):
    player_list = []
    for i in range(counts):
        print(f'Player {i + 1}')
        player_name = input('First Name: ').strip()
        player_gender = input('Male of Female: ').strip()
        player_info = (player_name, player_gender)
        player_list.append(player_info)
    return(player_list)

def game_prompt(n):
    while True:
        for index, char in enumerate(n):
             print(f'{char[0].title()}, Your Turn!')
             prompt = input('Truth or Dare? ').lower()
             gender = char[1].lower()
             print(choose_mode(prompt, gender))


def choose_mode(prompt, gender):
    match prompt[0]:
         case 't':
              question = random.choice(truth[gender])
              return question
         case 'd':
              question = random.choice(dare[gender])
              return question
         case _:
            print('Try a valid response next time! Here\'s a random selection')
            question = random.choice(random.choice(random_sel)[gender])
            return question



main()

