# Melvor Astrology Roll-All sum chance
Warning: from my understanding, Astrology was reworked, so this script is no longer relevant or correct. It is kept there just in case someone needs it later.  
This script calculates the chance to get the desired percentage or higher with the Roll All button.  
It only calculates the rolls of one mod. It cannot calculate the rolls of several different mods at the same time.

Arguments:

`-s, --number-of-slots` - The number of Standard or Unique slots that you've unlocked in the game and for which you want to calculate the probability. Minimum 1, maximum 3. The default value is 3.

`-o, --number-of-options` - The number of mods that one slot can roll. For instance, if a slot can roll three different modifiers you put 3 in this field. The default value is 4.

`-p, --desired-percentage` - The sum of all rolls for your desired mod. Minimum 1, maximum 15. The default value is 10.

`-t, --number-of-trials` - The number of rolls the script will do to figure out the chance. The default is 100,000.
