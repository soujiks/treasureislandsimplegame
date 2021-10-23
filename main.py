# ASCII art from https://ascii.co.uk/art/island
print('''
 _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction=(input("Left or Right?\n")).lower().strip()
if(direction == "left"):
  to_do=input("Swim or Wait?\n").lower().strip()
  if(to_do == "wait"):
    door=input("Red,Blue or yellow\n").lower().strip()
    if(door == "yellow"):
      print("You win!")
    elif(door == "red"):
       print("You burn.Game over")
    elif(door == "blue"):
       print("Eaten by beast.Game over")
    else:
       print("Game over") 
  else:
    print("Attacked by trouts.Game over")
else:
    print("Fall into hole.Game over")