import random

cards21 = [
    "Blackjack! Too perfect… makes me wonder if you stacked the deck.",
    "Blackjack! Quick and clean... maybe a little too clean for comfort.",
    "Blackjack! Funny how the cards fall just right when you’re holding them.",
    "Blackjack! Smooth as silk… almost like you knew what was coming.",
    "Blackjack! Perfect timing… suspiciously perfect, if you ask me.",
    "Blackjack! Crisp, precise... almost like someone gave the deck a nudge.",
    "Blackjack! Impressive… though I’ll be watching your hands closely.",
    "Blackjack! Came together too neatly… makes me wonder what trick you’re hiding.",
    "Blackjack! Celebrate it, sure… but I’ll be checking the shuffle next time.",
    "Blackjack! Almost guaranteed win... until you see the other has 21 too.",
    ]


cards20 = [
    "Twenty, solid ground but not quite the summit.",
    "So close to perfect… yet one step shy of glory.",
    "Twenty looks strong, though I’ve seen it falter.",
    "A hand worth respect, but not untouchable.",
    "Twenty, tempting you to relax, but the game isn’t over.",
    "Sharp and steady, though perfection still lies ahead.",
    "Strong enough to make you smile, but I’ve seen smiles fade here.",
    "Twenty, the kind of hand that wins… or breaks hearts.",
    "Impressive, though the shadow of twenty one looms large.",
    "So near to Blackjack, yet sometimes that’s the cruelest place to stand."
]


cards19 = [
    "Respectable enough, though I wonder if you’ll risk another.",
    "Strong hand, but sometimes the best hands still reach for more.",
    "Nineteen, close to the peak… maybe you want to climb higher.",
    "with this start, who knows, maybe you will break even with the casino in the end.",
    "I’ve seen nineteen turn greedy before, maybe you’ll try your luck too.",
    "Feels steady, nothing unusual here.",
    "Solid presence, clear enough to stand on its own.",
    "Nineteen, impressive, though nothing lasts forever.",
    "Looks like a winner, until the next card whispers otherwise.",
    "19, i remember having that..."
]


cards18 = [
    "Looks confident, but I’ve seen plenty collapse right here.",
    "Eighteen, strong enough… though one more card might make it perfect.",
    "Feels steady, yet the thought of more lingers.",
    "Solid hand, yet there are ways to improve it.",
    "I’ve watched players stretch eighteen before, sometimes it pays, sometimes it ruins them.",
    "Good enough, nothing unusual in this hand.",
    "Eighteen, respectable, though not remarkable.",
    "Looks fine, neither weak nor overwhelming.",
    "A hand that sits quietly, waiting for its fate.",
    "I once counted eighteen chips before losing them all, strange how numbers stick with me."
]


cards17 = [
    "Seventeen, decent… though one more card could change everything.",
    "Looks steady, but I’ve seen players chase higher before.",
    "Strong enough, yet the thought of twenty one is hard to resist.",
    "Feels safe, though safety rarely wins big.",
    "I’ve watched seventeen turn bold, sometimes it shines, sometimes it burns.",
    "Clear hand, what else can i say.",
    "Seventeen, respectable, though not remarkable.",
    "lucky 7 comes with a 1, i wonder where it will go from here.",
    "if you draw, you might win it, or swing it.",
    "i was going to say something funny about 17, but than i remembered i hate this number"
]


cards16 = [
    "Sixteen, not bad… though one more card could make it dangerous in the best way.",
    "Looks steady, but I’ve seen players stretch it and smile until the bust comes.",
    "Strong enough, yet the whisper of seventeen is hard to ignore.",
    "Feels like a hand waiting to be tested, doesn’t it?",
    "I’ve watched sixteen turn greedy, sometimes it climbs, sometimes it crashes.",
    "Clear hand, sitting quietly without fuss.",
    "Sixteen, ordinary, nothing to brag about.",
    "Sixteen, Looks fine at bast.",
    "A hand that passes without much attention.",
    "how i hate when i get 16, i almost feel sorry for you, but just almost."
]


cards15 = [
    "Fifteen, some call it the edge, others call it the trap.",
    "A hand that looks quiet, waiting for whatever comes next.",
    "Not weak, not strong, just sitting in the middle.",
    "Fifteen, steady enough, though I’ve seen players stretch it.",
    "It’s a number that makes people wonder if they should risk more.",
    "Clear enough, nothing unusual here.",
    "This hand doesn’t shout, it just lingers.",
    "Fifteen sits in the middle, neither proud nor ashamed.",
    "Numbers like this pass by without much attention.",
    "Fifteen is a nice number, i always liked the look of this number."
]


cards14 = [
    "Fourteen, some players see it as a fork in the road.",
    "It’s a hand that makes people pause, wondering if they should lean forward or sit back.",
    "Balanced enough, though not the kind of number that brags.",
    "Fourteen sits quietly, neither threatening nor comforting.",
    "Sometimes this hand feels like waiting in line, not knowing what’s at the counter.",
    "It’s steady, nothing flashy, just there.",
    "A hand that blends into the table, unnoticed until it matters.",
    "Fourteen has a way of being forgettable, yet it lingers.",
    "Numbers like this drift past without much fuss.",
    "I once counted fourteen cracks in the ceiling above me, and wondered if the place would hold another night."
]


cards13 = [
    "Unlucky thirteen, the number everyone whispers about.",
    "It’s known to be unlucky, but luck doesn’t care what people say.",
    "Some call it cursed, others call it just another hand.",
    "Thirteen sits heavy, like a rumor waiting to be tested.",
    "stories say it is unlucky number, Will you be a man of stories, or a man of risk?",
    "It’s a hand that makes people hesitate, not because of math, but because of myth.",
    "Thirteen doesn’t shout, it just lingers with a shadow.",
    "Some players laugh at superstition, others fold to it.",
    "Numbers like this carry weight, even if it’s only in the mind.",
    "13, i wonder how it will effect my luck..."
]


cards12 = [
    "Twelve, some say it’s the start of the climb, others call it the waiting room.",
    "It’s a hand that makes people wonder if patience is wiser than risk.",
    "Balanced enough, though not the kind of number that brags.",
    "Twelve sits quietly, maybe too quiet.",
    "Sometimes this hand feels like a pause before the real game begins.",
    "It’s steady, nothing flashy, just there.",
    "A hand that blends into the table, unnoticed until it matters.",
    "Twelve has a way of being overlooked, yet it lingers.",
    "hands like this sometimes not worth remembering.",
    "12, funny, like the number of hours i work here everyday."
]


cards11 = [
    "Eleven… looks sweet, but sweet things rot fast.",
    "A tidy little number, pretending it’s safe.",
    "Balanced? Sure. Balanced like a chair with one loose leg.",
    "Eleven sits there, smug, like it knows you’ll trip.",
    "Feels solid, though solid things sink too.",
    "Nothing loud, just a quiet hand with sharp teeth.",
    "Eleven hums like a secret, and secrets never end well.",
    "It lingers, not proud, not ashamed… just waiting.",
    "Numbers like this smile too easily, and I don’t trust smiles.",
    "Eleven, Eleven, Eleven, looks like this is what you get..."
]


cards10 = [
    "Ten… ah, the darling of the table, let's pretend it is solid.",
    "Looks neat, but neat things crack the loudest.",
    "Balanced? Please. Balance is just another way to fall evenly.",
    "Ten sits there, with a look that says you won't win, will you let it tell you what to do?.",
    "Feels like a locked door — you can knock, but it won’t.",
    "Quiet hand, sure… quiet like a snake in the grass.",
    "Ten hums under its breath, and I don’t like the tune.",
    "It lingers, pretending to be harmless, but I see the teeth.",
    "Numbers like this grin too wide, and wide grins hide knives.",
    "I once counted ten nails in this table, and wondered who hammered the last one."
]


cards9 = [
    "Nine… small enough to look safe, dangerous enough to fool you.",
    "It pretends to be harmless, but harmless things bite hardest.",
    "Balanced? Ha. Balance is just the calm before the stumble.",
    "Nine sits crooked, like a chair missing a screw.",
    "Feels like a step that creaks louder than the rest.",
    "Quiet hand, sure… quiet like a trap waiting to snap.",
    "Nine hums low, like a warning you don’t want to hear.",
    "It lingers, not proud, not ashamed… just suspicious.",
    "Numbers like this grin sideways, and sideways grins never mean good news.",
    "I once counted nine locks the casino door, and still didn’t feel safe behind it."
]


cards8 = [
    "Eight… ah, the polite little number, bowing before it stabs you.",
    "Looks steady, but steady is just another word for boring failure.",
    "Balanced? Sure, balanced like a rope over a pit.",
    "Eight sits smug, pretending it’s ordinary — ordinary is the best disguise.",
    "Sideways it is infinity, but like this, not that much",
    "Quiet hand, yes… almost like the hand fear of something.",
    "Eight hums low, like it’s laughing under its breath.",
    "you start small now, but 2 wrong cards are the end from here.",
    "Numbers like this wink at you, and I never trust a wink, it looks like eyes, you see it too?",
    "Eight, like the cracks in the floorboards, i swear something moved under one of them."
]


cards7 = [
    "Seven… they call it lucky, but luck is just another word gamblers use before they lose.",
    "Ah, the famous seven — shines like gold until you realize it’s painted tin.",
    "People whisper about lucky sevens, but I hear whispers from the unlucky ones louder.",
    "Seven sits there, pretending to be a charm, though charms break faster than bones.",
    "It looks like fortune, but fortune is a cruel dealer, and I should know.",
    "Seven hums with promise, though promises are the cheapest currency at this table.",
    "Lucky? Maybe. Or maybe it’s just the bait dangling on the hook.",
    "Seven grins wide, daring you to believe in rumors — are you a man of stories or of risk?",
    "It lingers with superstition, but superstition doesn’t pay the bill when you lose.",
    "I once counted seven stars above me, and one fell... lucky for the sky... unlucky for me."
]


cards6 = [
    "Six… halfway to nowhere, the kind of number that thinks it matters but never does.",
    "They call it small, they call it weak — I call it the hand that laughs when you underestimate it.",
    "Six sits crooked, like a chair that wobbles no matter how many times you fix it.",
    "It is great for a dice roll, seems like you picked the wrong game.",
    "It feels like a pebble in your shoe — tiny, irritating, and somehow the only thing you notice.",
    "A six, same as the chance of you getting more moany than you lost here.",
    "vary low, don't you think? at list you cannot go lower than that, ho right, you can.",
    "this can be good, or be bed, i can guess what it will be for you.",
    "is it low? yes, does it metter if it is all comes to luck, not so much.",
    "fun fact, i cannot recall rolling a 6 in a die my entire life."
]


cards5 = [
    "Five… halfway, stuck in the middle, not strong enough to impress, not weak enough to pity.",
    "It sits there like it wants to matter, but it doesn’t, i can relate to that.",
    "Five is the kind of hand that makes you shrug — nothing more, nothing less.",
    "Balanced? No. It’s just indecisive, like it can’t pick a side.",
    "Five waits, quiet, pretending it has a plan… it doesn’t.",
    "It lingers, not bold, not shy, just dull.",
    "Five is ordinary, and ordinary is the easiest way to lose.",
    "Numbers like this don’t shine, they fade before you notice them.",
    "Five looks steady, many thinks look different than they are.",
    "I did get a lot of 5 in my dice rolls, but never a six."
]


cards4 = [
    "Four… small enough to be ignored, which is exactly why I don’t ignore it.",
    "It sits there, quiet, like it’s waiting for someone to make the mistake of calling it harmless.",
    "Not impressive, not threatening, just dull, and dull is the easiest way to lose.",
    "It lingers at the edge of the table, pretending it doesn’t matter, but I’ve seen that trick before.",
    "Four, looks good as a cards with 4 corners, but not much in play.",
    "It’s the kind of hand that makes me smirk, because I know it’s already doomed.",
    "Nothing bold, nothing shy, just a number that thinks it deserves attention.",
    "Four hums under its breath, and I don’t like the sound of it.",
    "so low there is basically one option from here, even this luck took from you.",
    "i wonder why so much things come in fours, even here."
]


cards3 = [
    "Three… now this is low, so low it barely deserves a seat at the table.",
    "It sits there like a joke, waiting for someone to laugh, but no one does.",
    "Three is the kind of hand that makes me roll my eyes before I even deal the next card.",
    "Not strong, not clever, just small enough to be annoying.",
    "It lingers like background noise, buzzing without purpose.",
    "Three doesn’t shine, doesn’t fade, it just wastes space.",
    "It hums like it wants attention, but I’m not giving it any.",
    "Numbers like this don’t impress, they irritate.",
    "Three looks ordinary, and ordinary is the easiest way to lose without noticing.",
    "Why starting so low is even an option?"
]


cards2 = [
    "Two aces… rare, powerful at first glance, but together they shrink into weakness.",
    "Strong in theory, but side by side they drag each other down to nothing more than 2.",
    "Two aces, a hand that should roar, yet both end up whispering like cowards.",
    "Rare sight, yes, but strength fades fast when one ace chains the other to 1.",
    "Two aces together, and suddenly neither feels mighty anymore.",
    "They enter the table like kings, but leave it like beggars with a limping leg.",
    "Two aces, rare and proud, until they cancel each other’s glory and fall flat.",
    "It looks like fortune, but fortune laughs when strength collapses into weakness.",
    "Two aces side by side, both forced to bow, both stripped of their crown.",
    "I’ve had two rare things myself once… and just like these aces, they both turned into nothing but 1s."
]



cards = {
    2: cards2,
    3: cards3,
    4: cards4,
    5: cards5,
    6: cards6,
    7: cards7,
    8: cards8,
    9: cards9,
    10: cards10,
    11: cards11,
    12: cards12,
    13: cards13,
    14: cards14,
    15: cards15,
    16: cards16,
    17: cards17,
    18: cards18,
    19: cards19,
    20: cards20,
    21: cards21,
}


lose_100 = [
    "Scooping the full hundred… the table feels mine now.",
    "Chips flooding in… one hundred straight into my pocket.",
    "Gathering the pile… a hundred, stacked like proof of my win.",
    "Claiming the swing… one hundred ringing louder than any applause.",
    "Pressing the win… a hundred rattles sharp, even sharper for you to lose them.",
    "one hundred chips, The share towering!what a momentum.",
    "what a momentum, for me, and a big downfall for you.",
    "A sweep this size, i will take that.",
    "One hundred, for me, you shouldn't have.",
    "A big 100 win for me, clicks tight, locked where it belongs."
]



lose_99 = [
    "Scooping the stack… I win, and the table knows it.",
    "Chips flooding in... well, my pocked, it feels more heavy now if you know what i mean.",
    "Gathering the pile… I win, nothing sweeter than this weight.",
    "Claiming the swing… I win, echoes sharp, isn't it?",
    "Pressing the win, and getting it!",
    "With this win alone i can make a fine tower already.",
    "wining big, once again.",
    "What a big lose for you, and a big win for me.",
    "I can definitely see myself getting used to it",
    "i could lose big, or win big, and in the end, look what ended up."
]




lose_90 = [
    "Scooping the stack… feels like the table finally admits who runs it.",
    "Chips piling in… the sound I could listen to all night.",
    "Gathering the pile… nothing sweeter than watching it settle my way.",
    "Claiming the swing… echoes like applause meant only for me.",
    "Pressing the win… like a good song, i will come up many more times.",
    "The share towering… crooked monument, and my name carved on it.",
    "Holding the drift… smoke rising, looks almost celebratory.",
    "A sweep this size… hums steady, like the room knows I own it.",
    "The pile settling… neat rows, stacked like proof of my hand.",
    "Pulling again… clicks tight, another reminder I don’t miss."
]


lose_80 = [
    "Scooping a stack… sounds like bricks shifting in a wall.",
    "Chips piling in… rhythm of drums that don’t stop.",
    "Dropping a heap… like sand pouring through a broken hourglass.",
    "Gone already… louder than shutters slamming in a storm.",
    "Pressing the bet… rattles like iron bars locking shut.",
    "The share stacking taller… crooked monument rising in silence.",
    "Letting them drift… smoke curling from a fire that won’t die.",
    "A swing this size… hums like engines grinding in the dark.",
    "The pile crossing over… neat as a ritual repeated too many times.",
    "Pulling again… clicks for you like gears tightening with no release."
]



lose_70 = [
    "Scooping a stack… feels like payday on a slow night.",
    "Chips piling in… reminds me of when luck actually listens.",
    "Dropping a heap… almost like the table owed me rent.",
    "Gone already… echoes louder than the shuffle itself.",
    "Pressing the bet… sounds like coins rattling in a tin can.",
    "My share stacking taller… looks like a crooked tower ready to lean.",
    "Letting them drift… feels like watching smoke curl and fade.",
    "A sharp swing… same rhythm as a clock that skips a beat.",
    "The pile crossing over… neat as a trick I’ve seen too many times.",
    "Pulling again… makes me think of how easy it is to win with you"
]



lose_60 = [
    "Scooping a heavy stack… you sitting still and watching it vanish?",
    "Chips piling my way… silence holds while it happens i see.",
    "Dropping a heap… fixed to me as I claim it clean.",
    "Gone already… sitting still and watching the side hollow out.",
    "Pressing the bet… motionless while the stack shifts higher.",
    "The share is mine… why you quiet as I stacks taller.",
    "Letting them drift? funny how I gathered right under steady eyes.",
    "A good swing, for me, definitely not for you.",
    "The pile crossing over to me like a charm.",
    " chips Pulled to me again, it gets easier every single time."
]



lose_50 = [
    "So I scooped a heap… and you just sat here watching it vanish.",
    "Chips stacked my way, while you sat and let it happen.",
    "You dropped a pile, and I claimed it clean while you stared.",
    "That’s gone… you sat still and watched your side hollow out.",
    "I pressed and took the bet… you didn’t even move.",
    "The share is mine… you sat quiet while I stacked it higher.",
    "You let them drift, and I gathered the lot right under your eyes.",
    "That’s a heavy stack gone… and you just sat through it.",
    "The pile crossed over to me… you didn’t lift a hand.",
    "So I pulled from you the bet… and you sat there letting me get used to this."
]



lose_40 = [
    "So I scooped a pile… you watched it go.",
    "Chips moved my way, enough to weigh you down.",
    "You dropped a stack, and I claimed it clean.",
    "That’s gone… your side looks cut short.",
    "I pressed, and took what happened to you, too bed",
    "the share is mine, add it to the pile",
    "You let them slide, and I gathered them all.",
    "That’s a stack gone… not small enough to ignore.",
    "The pile crossed over to my side.",
    "So I pulled from you the bet, i can get used to this."
]



lose_30 = [
    "So I scooped a stack… looks like you blinked.",
    "Chips moved my way, enough to sting a little?",
    "You dropped a pile, and I didn’t miss it.",
    "That’s gone… your side feels lighter now.",
    "I pressed and took what was open… simple.",
    "So I claimed the prize… yours no longer.",
    "You let them slide, and I caught them all.",
    "That’s a stack gone, small but mine.",
    "A pile crossed over… I’ll keep it closer.",
    "So you just going to let me take this small wins?."
]



lose_20 = [
    "So I skimmed more than a few… you left them open.",
    "Chips slid my way, enough to notice.",
    "You dropped a stack, and I caught it clean.",
    "That’s gone… you're pile looks lighter.",
    "I pressed and took a cut… simple as that.",
    "So I claimed a slice… yours no longer.",
    "You let them slip, and I was waiting.",
    "That’s a pocketful gone… the table tilts my way.",
    "A stack moved across… i'll keep that in mind",
    "So I pulled some of you, time for more."
]




lose_10 = [
    "So I skimmed a few… you didn’t guard them.",
    "Chips slid my way, just enough to remind you.",
    "You dropped a handful, and I caught them clean.",
    "That’s a slice off your stack… small, but it shows.",
    "I pressed and took a few… easy pickings.",
    "So I carved into your pile… barely effort.",
    "You let them slip, and I was waiting.",
    "That’s a pocketful gone… the table remembers.",
    "A few moved across… I’ll keep pressing.",
    "So I claimed a handful… time to claim more."
]



lose_1 = [
    "So I took one… mighty collapse, huh?",
    "Chips shifted my way, a whole single piece.",
    "You dropped one, and I’ll treasure it forever.",
    "That’s one gone… try not to cry.",
    "I pressed and stole a chip, call it a triumph.",
    "So I carved one out… legendary robbery.",
    "You let one slip, and I made history.",
    "That’s a single chip, but I’ll brag all night.",
    "One moved across the table… I’ll frame it.",
    "So I claimed one… the pile’s mine now, obviously."
]


#whan the dealer loses below
win_100 = [
    "So you took the full hundred… don’t think it ends here.",
    "Chips stacked in your favor, the table looks stripped bare.",
    "You hit me with the max, and the count shows it, yet still not enough to end me",
    "the round is yours, but not the game...",
    "You really pressed all the way, we have a game now.",
    "Chips in your hands, the biggest swing you’ll see.",
    "So you grabbed a good win, don’t mistake it for victory.",
    "You made the move everyone waits for, yet you didn't even won..",
    "Did that just happen.......",
    "That’s the hardest blow you can throw, and even this is not enough"
]

win_99 = [
    "Scooping away… feels like the table carving me hollow.",
    "Chips pouring out… rhythm sharp, each sound cuts deeper.",
    "Dropping the heap… like watching bricks pulled from a wall I built.",
    "Gone already… echoes sting, louder than I can stand.",
    "Pressing the bet… rattles like chains I can’t shake off.",
    "this will take time to come back from this.",
    "the chips just drifting from me, more and more far away.",
    "A sweep this size… hums low, like engines choking out their last breath.",
    "The pile crossing over, not showing me any mercy.",
    "Yes, go ahead, just take all of this chips from me, don't let me bother you...."
]



win_90 = [
    "So you dragged nearly a hundred off me… don’t think it’s finished.",
    "Chips stacked in your favor, the table looks tilted now.",
    "You hit hard i will give you that, but still not enough to end me.",
    "That’s your strike, but the pile isn’t gone.",
    "You pressed deep, the count speaks for itself, but not for me.",
    "Chips in your hands, more than anyone should take in one swing.",
    "So you grabbed a lot, lets see how you will when the opposite will happen.",
    "You made you're move, now for mine.",
    "Did that just happen? The stack looks carved thin.",
    "That’s a heavy blow, the kind that leaves marks..."
]


win_80 = [
    "So you dragged a mountain off me… don’t think it’s over.",
    "Chips in your hands, but I’m still breathing.",
    "You hit me hard, yet the table isn’t yours.",
    "That’s your big strike, not my finish.",
    "You pulled off a gamble, I’ll give you that… but I’m not done.",
    "Chips shifted your way, and it stings more than I’ll admit.",
    "So you struck deep, but I’m still here dealing.",
    "You shocked me with that one… still not enough to break me.",
    "That’s a heavy blow, but I’m not folding.",
    "You got lucky, let's see how long this will last."
]





win_70 = [
    "So you took a serious cut… don’t think it’s enough.",
    "Chips gone to you, but the stack still stands.",
    "You pressed hard against me, but I’m not folding.",
    "That’s your gain, not my finish.",
    "You carved deep, but the game isn’t yours.",
    "Chips in your hands, yet I’m still dealing.",
    "So you grabbed plenty… don’t mistake it for victory.",
    "You made progress against me, but the pile remains.",
    "Did that just happen… still not enough to break me.",
    "That’s a big slice, but I’m not done."
]


win_60 = [
    "So you took a big slice… don’t think it’s over.",
    "Chips gone to you, but the stack still stands.",
    "You carved into me, not enough to break me.",
    "That’s a cut you made, not the finish.",
    "You pressed hard against me, but I’m still here.",
    "Chips in your hands, yet the game isn’t yours.",
    "So you grabbed plenty… don’t mistake it for victory.",
    "You scratched deeper, but I’m not folding.",
    "That’s your gain, not my end.",
    "You made progress against me, but the pile remains."
]



win_50 = [
    "So you took a good amount… don’t be confident yet.",
    "Chips off the stack, but the game isn’t yours.",
    "That’s noticeable, not enough to matter.",
    "You carved into the pile, it still stands.",
    "Chips gone, but not victory.",
    "A cut worth mentioning, not worth celebrating.",
    "You pressed harder, but I’m not folding.",
    "Chips missing, don’t start smiling yet.",
    "You made progress, but not enough.",
    "That’s a mark on the stack, nothing more."
]



win_40 = [
    "so you just gonna take it, don't you?",
    "Not small, not big… irritating.",
    "That cut won’t be ignored.",
    "More than crumbs, less than ruin.",
    "I’ll remember this slice.",
    "Not pocket change anymore.",
    "That’s weight off the stack.",
    "Closer to hurting than you think.",
    "A loss worth keeping in mind.",
    "More than I care to admit."
]



win_30 = [
    "So you shaved off a chunk… don’t get too proud.",
    "That’s more than pocket change, I’ll admit.",
    "Looks like you’re nibbling at the stack now.",
    "Keep pressing like this and I might start caring.",
    "That’s not a fortune, but it’s enough to annoy me.",
    "You’re cutting deeper than before, I’ll give you that.",
    "The pile feels lighter… irritating, isn’t it?",
    "I see you’re chipping away, slow but steady.",
    "That’s a decent slice gone, don’t think it scares me.",
    "You’re starting to scratch at the savings, hah."
]




win_20 = [
    "Enough to notice.",
    "Not small, not big… irritating.",
    "That cut won’t be ignored.",
    "More than crumbs, less than ruin.",
    "I’ll remember this slice.",
    "Not pocket change anymore.",
    "That’s weight off the stack.",
    "Closer to hurting than you think.",
    "A loss worth keeping in mind.",
    "More than I care to admit."
]


win_10 = [
    "{} chips gone… don’t spend it all at once.",
    "{} you win this time, I’ll just tighten the belt.",
    "{} chips down, you’re really bleeding me dry, huh?",
    "{} taking my chips i see, not that you took that much.",
    "{} chips slipped away, annoying but survivable.",
    "{} chips shaved off, but i got more where this came from.",
    "{} chips vanished, my savings are starting to sweat.",
    "{} seems like i lost, I’ll grumble but keep dealing.",
    "{} chips gone, maybe I’ll skip breakfast tomorrow.",
    "A few chips lost, and you’re already celebrating?"
]



win_1 = [
    "One chip gone… wow, I’m devastated.",
    "One chip lost, should I start panicking?",
    "One chip down, alert the neighbors!",
    "One chip missing, guess I can’t afford eating today, hah.",
    "One chip slipped away, tragic, really.",
    "One chip shaved off… I’ll survive somehow.",
    "One chip vanished, oh no, my fortune crumbles.",
    "One chip down, what a crushing defeat.",
    "One chip gone, better call the accountant.",
    "A single chip lost, and the drama begins."
]



def get_dealer_lines_lose(chips_lost):
    if chips_lost == 1:
        return lose_1
    elif chips_lost == 100:
        return lose_100
    elif 2 <= chips_lost <= 10:
        return lose_10
    elif 11 <= chips_lost <= 20:
        return lose_20
    elif 21 <= chips_lost <= 30:
        return lose_30
    elif 31 <= chips_lost <= 40:
        return lose_40
    elif 41 <= chips_lost <= 50:
        return lose_50
    elif 51 <= chips_lost <= 60:
        return lose_60
    elif 61 <= chips_lost <= 70:
        return lose_70
    elif 71 <= chips_lost <= 80:
        return lose_80
    elif 81 <= chips_lost <= 90:
        return lose_90
    elif 91 <= chips_lost <= 99:
        return lose_99
    else:
        return None














bet_win_lose = {}


def dealer_line_starting_bet(score):
    return random.choice(cards[score])




logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


opening_logo = """
███████╗
██╔════╝
███████╗
╚════██║
███████║
╚══════╝

 ██████╗ 
██╔═══██╗
██║      
██║      
██╔═══██╗
 ██████╔╝
 ╚═════╝ 
"""

























def dealer_line_bet_win_lose(bet):
    return random.choice(cards[bet])

#note to self, I want to make him say the number at the start after all


