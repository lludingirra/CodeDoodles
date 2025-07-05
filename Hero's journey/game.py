import sys
import time
import os
from os import system

# --- Game Constants ---
CONTINUE_PROMPT = " [ Press Enter to continue... ]"
TYPING_SPEED = 0.01  # Delay for character-by-character text display
WALK_ANIMATION_STEPS = 10
RUN_ANIMATION_STEPS = 10
WALK_ANIMATION_DELAY = 0.0375
RUN_ANIMATION_DELAY = 0.0375

# --- ASCII Art Frames ---
# Each frame is a list of strings representing lines of the ASCII art
# Original walking_frames ASCII art (translated to English comments)
walking_frames = [
    [
        # ----------Frame I---------- #
        f"             `-:-`          ",
        f"            -ydddy.         ",
        f"            +ddddm/         ",
        f"            .ohhh+`         ",
        f"           `.:++.           ",
        f"         `:sdddds`          ",
        f"        `odoymmmd+`         ",
        f"        :do sdddshy+.`      ",
        f"        oy. ohyy-.:oy+`     ",
        f"        ``  sysho.          ",
        f"           .ys./ys.         ",
        f"          `yd/` /dh.        ",
        f"        `/yds`  `odh.       ",
        f"      .ohhs:     `yds       ",
        f"      ./:.        .so`      ",

    ],
    [
        # ---------Frame II---------- #
        f"              `.-.`         ",
        f"             .shddy-        ",
        f"             odmmmdy        ",
        f"             .shdhy-        ",
        f"             `:++-`         ",
        f"           `+hddd/          ",
        f"          `yhhddmy`         ",
        f"          :m+yddmds.`       ",
        f"          -dohmmd+yy+.      ",
        f"           +odmdds..-`      ",
        f"            `hmo+hy-        ",
        f"           `:hd-`ody`       ",
        f"       `/+oshy/  -dd-       ",
        f"       .sso/-`   :dh.       ",
        f"                 /s/        "

    ],
    [
        # --------Frame III---------- #
        f"               `..`         ",
        f"              /yhdh+`       ",
        f"             .hmmmmm-       ",
        f"             `+hddho`       ",
        f"              `:+:.         ",
        f"            `:yddy`         ",
        f"            /dmmmy`         ",
        f"            ydmddh.         ",
        f"            +ddmmds-        ",
        f"            `sdmdmdy`       ",
        f"             .hmyhd+        ",
        f"           ``.hd+/dm.       ",
        f"         /syyhy+`:hm-       ",
        f"         -//:.`  ody        ",
        f"                `oo`        "
    ],
    [
        # ---------Frame IV---------- #
        f"               .--.         ",
        f"              .sdddh/       ",
        f"              /dmmdmd       ",
        f"              `+yhhs-       ",
        f"               ./+-         ",
        f"              :hdd+`        ",
        f"             `yddd+         ",
        f"             .dmmm+         ",
        f"             `ydmms`        ",
        f"              +dmmd:        ",
        f"              `/hdy.        ",
        f"               `:md.        ",
        f"             .oyddd.        ",
        f"             .+:/my`        ",
        f"                :s:         "
    ],
    [
        # ---------Frame V----------- #
        f"                ./+/-       ",
        f"               -hdddh/      ",
        f"               :dddddo      ",
        f"               `:syy/`      ",
        f"                :oo-        ",
        f"               .dmms        ",
        f"               /mmmo        ",
        f"               +mmd+        ",
        f"               oddm+        ",
        f"               /dmdy.       ",
        f"               `ohhy.       ",
        f"               `odmd:       ",
        f"               -ddms`       ",
        f"               sdh+`        ",
        f"               so`          "
    ],
    [
        # ---------Frame VI---------- #
        f"                `://-       ",
        f"               `yddddo      ",
        f"               .dmmmmh      ",
        f"                :shyo.      ",
        f"               `-+o/        ",
        f"              `odmdy`       ",
        f"              +mmmmh.       ",
        f"              dmmmddo.      ",
        f"              hdddmshy/`    ",
        f"              :yhmm/.+s.    ",
        f"               `ommh-       ",
        f"               .hdsdy`      ",
        f"              .yd+ sd+      ",
        f"            `/hd/` .dd.     ",
        f"            .oo-    /s-     ",
    ]
]
# Original running_frames ASCII art (translated to English comments)
running_frames = [
    [
        # ---------------Frame I-----------------#
        f"                .-.                   ",
        f"              -yhddy:                 ",
        f"             `ydddmmy`                ",
        f"              :yhdhy/                 ",
        f"             .-:/:.`                  ",
        f"         `-+yhdddy.   ``              ",
        f"        `sds-odmmmy-.+ys`             ",
        f"        sd/  odddyyyyy+.              ",
        f"        +:` `syyy-`..`                ",
        f"            -yyyy/`                   ",
        f"           -sy:.+ys-                  ",
        f"     ```.-ody-` `+dd:                 ",
        f"    -yhhhhy+.     /dd/                ",
        f"    `:::-.         :hh:               ",
        f"                    -hh`              ",
        f"                     ..               "
    ],
    [
        # ---------------Frame II----------------#
        f"                 `                    ",
        f"              `+yhho.                 ",
        f"              odmmdds`                ",
        f"              :hdddh/                 ",
        f"             `.://:.                  ",
        f"          `:oyhdhs`                   ",
        f"         .yh+odmmd/                   ",
        f"         sd+ sddddd/::/`              ",
        f"        .hm.`hmdm//oo+/`              ",
        f"        `:/ -hmmd-                    ",
        f"            +dd+dy-                   ",
        f"      --.``-hd+`+hh.                  ",
        f"     .yhhyyhh/` .hm+                  ",
        f"      `.:::-`   -hm/                  ",
        f"                +dd.                  ",
        f"                :o:                   "
    ],
    [
        # ---------------Frame III---------------#
        f"              -ohhs:`                 ",
        f"             -hmmmdd+                 ",
        f"             .sdmmdh-                 ",
        f"              `://:.                  ",
        f"            ./shy:                    ",
        f"           :hdmmd/                    ",
        f"          :dddmmd/                    ",
        f"          smydmdmh+.`                 ",
        f"          +dhddmh+syo`                ",
        f"          `-/dmmd/`.`                 ",
        f"         ````smddh`                   ",
        f"        .sssyhd+dd.                   ",
        f"        `/+++:.:dh.                   ",
        f"              +dd:`                   ",
        f"              /o:                     "
    ],
    [
        # ---------------Frame IV----------------#
        f"                `..`                  ",
        f"              `/hddho`                ",
        f"              -dmdmmd+                ",
        f"              `ohddhs.                ",
        f"               .:/-.`                 ",
        f"              :ydh/                   ",
        f"             :dddd:                   ",
        f"             ymmdd-                   ",
        f"             hmdmh`                   ",
        f"             omdmh-                   ",
        f"             .ydmd:                   ",
        f"              .ymds`                  ",
        f"             -+hmdy.                  ",
        f"             +hdd/`                   ",
        f"             `yd+                     ",
        f"             `//                      "
    ],
    [
        # ---------------Frame V-----------------#
        f"                 .:/:`                ",
        f"                +hdddy-               ",
        f"               `ymdddmo               ",
        f"                :syhy+`               ",
        f"                -++:`                 ",
        f"              `odmdy                  ",
        f"             `ymdmmo                  ",
        f"             :ddmdmo`                 ",
        f"             `ymddddo.                ",
        f"              :dmmh:oo                ",
        f"              `+ddy/``                ",
        f"               /hydd:                 ",
        f"              -hhodd-                 ",
        f"             :ddohdo`                 ",
        f"            :hd/.::`                  ",
        f"            `:-                       "
    ],
    [
        # ---------------Frame VI----------------#
        f"                  `:::`               ",
        f"                 /hdmdh/              ",
        f"                `ymmmdmy              ",
        f"                 -shhhs-              ",
        f"                `-/+-`                ",
        f"              `:yddds`                ",
        f"             `sdddmmy`                ",
        f"            `smsymddd/-/s+            ",
        f"            -dd-hdddooso/.            ",
        f"            -yo-ddmh-                 ",
        f"             ` +my+hh+`               ",
        f"              -dd- .sdy.              ",
        f"            `/dd/`  `ymy`             ",
        f"          -/ydy:     -dd:             ",
        f"         `sh+-`       sy-             "
    ]
]
# Original enemies ASCII art (translated to English comments)
enemy_arts = [
    # Photo I , Beast #
    [
        f"                                              -+ydmNMNNdyo:`                MMM/   yMM         MMo                                  /MMM         :mMMMMd+.                     yMMM-      ",
        f"                                           .sNMMMmhhyyhmMMMMy:              MMM/   yMM   .+yyo-MMo :o/`+y- -oyys/`  :s+-oyyo.       /MMM        /MMMm+.                        /MMM/      ",
        f"                                         `sMMMh/`        :sNMMd-            MMM/   yMM  :NNo::sMMo oMNdss-yMy::oMm. oMMs::hMN`      /MMM       /MMMm. .mMmo`                .. -MMMy      ",
        f"                                        .mMMh.             `oMMM/           MMM/   yMM  hMy    NMo oMM.  :MMhhhhNMy oMM   -MM`      /MMM      -MMMm.  .yMMMMy:        .:+ymMMMm MMMy      ",
        f"                                        mMMs  .ymy.     :dmo :MMM-          MMM/   yMM  yMd`  .MMo oMM   .MM-```-:. oMM   -MM`      /MMM      yMMM-     .omMMMm.  `odNMMMMMMmh/ MMMy      ",
        f"                                       /MMm   .mMm.     /NMy  sMMh          MMM/   yMM  `yNmhhhmMo oMM    /dNhhdNy` oMM   -MM`      /MMM      MMMm         /ymy.  -NMMNdy+-`    MMMy      ",
        f"                                       sMMy                   /MMN          MMM/   ```    `-:. ..`  ``      .-:-`    ``    ``       /MMM      mMMM`                `..         /MMMs      ",
        f"                                       oMMd                   +MMd          MMM/                                                    /MMM/      ",
        f"                                       .NMM:     ........    `mMM+          MMM/                   :mmd/ `ommm                      /MMM      .MMMm   .ymy:                    hMMM-      ",
        f"                                        /MMM/    yyyyyyyy   -mMMy           MMM/                   -NMMMmNMMMm                      /MMM       yMMMo  .mMMMm/`     -odMN/    `yMMMd       ",
        f"                                         :mMMd/`          -yMMMo            MMM/                    `oMMMMMm/                       /MMM       `mMMM/   /yMMMNo-/ymMMMMm:   /NMMN+        ",
        f"                                          `+mMMMds+////oyNMMNs.             MMM/                     +MMMMMN.                       /MMM        .mMMMo    .sNMMMMMMMh+.   .yMMMd.         ",
        f"                                             -odNMMMMMMMMmy/`               MMM/                   .hMh/.-/mMo                      /MMM         `yMMMm/`   `+mMmy:`    `oNMMN/           ",
        f"                                                 `-MMMh.                    MMM/                   .o/     `+o                      /MMM           :mMMMNyo-.       `/osNMMNo`            ",
        f"                                                   MMMy                     MMM/  `///////:.                                        /MMM             -yNMMMMMNmmmmmmMMMMMNo`              ",
        f"                                                   MMMy                     MMM/  MMmyyyhNN+                                 yms    /MMM               /MMMmNMMMMMMMMNMMM-                ",
        f"                                                   MMMy                     MMM/  MMo    dMy   .+oso:`   .+osoo/`  ./oss+: `/dMd/-  /MMM               /MMM/         :MMMd                ",
        f"                                                   MMMy                     MMM/  MMdyyyhMd.  sNh+/sNd. -hd:.-dMs `mMo..yd+`/dMd/-  /MMM               sMMM/          hMMM/               ",
        f"                                                   MMMy                     MMM/  MMh///+hNd.-MMyyyyNMs .+sysymMh  sdmmdhs-  hMy    /MMM               yMMM           .MMMm               ",
        f"                                                   MMMy                     MMM/  MMo    /MM:-MM:...:/. yMd-.`hMh .yy..:hMN  hMy    /MMM               yMMM            sMMMo              ",
        f"                          .........................MMMh.....................MMM/  MMNmmmdmd+  +mmysymy` /mmsoodNh  odhsshd/  omNm+  /MMM...............hMMM............-NMMM-.............",
        f"                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/                                                    /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        f"                          ooooooooooooooooooooooooooooooooooooooooooooooooooooo.                                                    .ooooooooooooooooooooooooooooooooooooooooooooooooooooo"
    ],
    # Photo II , Rock #
    [
        f"                                              -+ydmNMNmdyo:                 MMM/                                                    /MMM        yMMMMm`                 oMMMMMd           ",
        f"                                           .smMMMmhyyyhmMMMNy-              MMM/                                                    /MMM        yMMMMy    -//.     ..`   :MMMMM           ",
        f"                                         `sMMMy/`        -sNMMh.            MMM/    `mm.       mm.                                  /MMM        oMMMMh   sMMMM-  .NMMM+   MMMMM           ",
        f"                                        .mMMh.              oMMN:           MMM/    .MM-   -:- MM. -- .:   -::`   .-`.::.           /MMM        /MMMMM`  +MMMN.  -MMMMs  `MMMMM           ",
        f"                                        dMMs  .ymy.     :dmo :MMM-          MMM/    .MM- /NmoohMM. MMhhy`sNyosNh` hMdsodMs          /MMM         NMMMM+   `..     .//-   /MMMMN           ",
        f"                                       /MMm   .mMm.     /NMy  sMMh          MMM/    .MM- MM.   NM. MM-  /MNyyymMs hM+  :Mm          /MMM         sMMMMm    -//////-      yMMMMy           ",
        f"                                       yMMy                   /MMN          MMM/    .MM- mM/  .MM. MM   -Mm`  -/. hM/  :Mm          /MMM         .MMMMM+  sMMMMMMMMs    .MMMMM/           ",
        f"                                       +MMh                   +MMd          MMM/    `mm. .ymmhyhm. mm    :hmddd+  sm:  -mh          /MMM          sMMMMN. +MMMMMMMM+   -mMMMMMmh+-        ",
        f"                                       `NMM:     ........    `mMM/          MMM/                                                    /MMM        `:yMMMMMm- `......` `/yMMMMMMMMMMMNy.     ",
        f"                                        :MMM/    yyyyyyyy   .mMMy           MMM/                                                    /MMM      .yNMMMMMMMMMhyoo+/+oymMMMMMMMhydMMMMMMMy`   ",
        f"                                         -mMMd/           -yMMM+            MMM/                    /MMNo`.yMMM                     /MMM    `oMMMMMMNmMMMMMMMMMMMMMMMMMMNy.   `/yMMMMMm:  ",
        f"                                           +mMMNhs+////oyNMMNs.             MMM/                    .mMMMNMMMMy                     /MMM   /NMMMMMh/  -sdmMMMMMMMMMMmy+-         :NMMMMMy`",
        f"                                             -odNMMMMMMMMmy/`               MMM/                      /MMMMMm.                      /MMM `sMMMMMm/          `.....`        ....   `yMMMMMN",
        f"                                                 `-MMMh.                    MMM/                     `yMMMMMM/                      /MMM`dMMMMMs`   .+yyyyys.             dMMMMm/`  :mMMMM",
        f"                                                   MMMy                     MMM/                    .mMs. `-dMy                     /MMMhMMMMM+   .yMMMMMMMMy             MMMMMMMN+   hMMM",
        f"                                                   MMMy                     MMM/                    ./.      :/                     /MMMMMMMM+   yMMMMMMMMMM+             dMMMMMMMMm- `yMM",
        f"                                                   MMMy                     MMM/         +MMMMMMmh-                     mM/         /MMMMMMN-   yMMMMMydMMMM/             yMMMMMMMMMM+  +N",
        f"                                                   MMMy                     MMM/         +Mm    yMd   ./++:`    -/o+:   mM/ `//`    /MMMMMN.   yMMMMM/ yMMMM/             yMMMM+hMMMMMd` .",
        f"                                                   MMMy                     MMM/         +MNooooNd:  yMs//hM+ .mN+/+Nm. mM/oNy-     /MMMMM-   .MMMMM/  mMMMM/             mMMMM/ +NMMMMm. ",
        f"                                                   MMMy                     MMM/         +MN///+NN/ :Mm   `MM yMo       mMMNN:      /MMMMy    sMMMMm   MMMMM-             MMMMM.  -NMMMMN-",
        f"                          .........................MMMh.....................MMM/         +Mm    oMh `NM:  +Md /Md. .hd. mM/`dMs     /MMMm-....NMMMMs..:MMMMM..............MMMMM....:mMMMMh",
        f"                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/         :ys    -yy  `ohddy/   -shdhs.  sy-  oyo    /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        f"                          ooooooooooooooooooooooooooooooooooooooooooooooooooooo.                                                    .ooooooooooooooooooooooooooooooooooooooooooooooooooooo"],
    # Photo III , Draco #
    [
        f"                                              -+ydmNMNmdyo:                 MMM/                                                    /MMM                 -yMMMNmmhyo:`                    ",
        f"                                           .smMMMmhyyyhmMMMNy-              MMM/                                                    /MMM                /MMmmNMMMMMMMMy.                  ",
        f"                                         `sMMMy/`        -sNMMh.            MMM/    `mm.       mm.                                  /MMM              :./dMNo`  .-/ymMMMy.                ",
        f"                                        .mMMh.              oMMN:           MMM/    .MM-   -:- MM. -- .:   -::`   .-`.::.           /MMM             sMmMd+hNNo` .+- /mMMMs               ",
        f"                                        dMMs  .ymy.     :dmo :MMM-          MMM/    .MM- /NmoohMM. MMhhy`sNyosNh` hMdsodMs          /MMMy/`          :NMMMMMMMMNo -shy:yMMMy              ",
        f"                                       /MMm   .mMm.     /NMy  sMMh          MMM/    .MM- MM.   NM. MM-  /MNyyymMs hM+  :Mm          /MMMMMNy/`        `+mMMMy:/oo    .. mMMM:             ",
        f"                                       yMMy                   /MMN          MMM/    .MM- mM/  .MM. MM   -Mm`  -/. hM/  :Mm          /MMMyNMMMNy/`       `oNMMNo`        .MMMm`            ",
        f"                                       +MMh                   +MMd          MMM/    `mm. .ymmhyhm. mm    :hmddd+  sm:  -mh          /MMM  :yNMMMMh+-      `yMMMN+        sMMMy            ",
        f"                                       `NMM:     ........    `mMM/          MMM/                                                    /MMM     :smMMMMMds/-`  -MMMM-        NMMM.           ",
        f"                                        :MMM/    yyyyyyyy   .mMMy           MMM/                                                    /MMM   ./:  -+hmMMMMMMdhyMMMM.        sMMMd       `.//",
        f"                                         -mMMd/           -yMMM+            MMM/                    /MMNo`.yMMM                     /MMM  :MMMd/`   ./oymMMMMMMMM         .MMMMmyyymmMMMMM",
        f"                                           +mMMNhs+////oyNMMNs.             MMM/                    .mMMMNMMMMy                     /MMM   omMMMMds/.    `:yydmy.          /MMMMMMMMMMmmys",
        f"                                             -odNMMMMMMMMmy/`               MMM/                      /MMMMMm.                      /MMM     :ymMMMMMMmhs/-                 .////-..`    .",
        f"                                                 `-MMMh.                    MMM/                     `yMMMMMM/                      /MMM   .yy/ ./shmMMMMMMMy                      `:/symM",
        f"                                                   MMMy                     MMM/                    .mMs. `-dMy                     /MMM   yMMMh/.   `./shmmo                    /NMMMMMMM",
        f"                                                   MMMy                     MMM/                    ./.      :/                     /MMM/   /mMMMMmy+/.`                         /NMmyo/.`",
        f"                                                   MMMy                     MMM/  .MMMMMNds-                                        /MMMMy-   -smMMMMMMMNmyyo//:                          ",
        f"                                                   MMMy                     MMM/  .MM-  `+MM/ ./:.// .+syyo-   `:+o/.    -/o+:      /MMMMMMms:`  `:+symNMMMMMMMMy                   `-//+y",
        f"                                                   MMMy                     MMM/  .MM-    yMh /MNho/ yy:.-MM. /Nd//yMy .mN+/+Nm-    /MMM/hMMMMMdy+:.    `.:/ooo+`                  -NMMMMM",
        f"                                                   MMMy                     MMM/  .MM-    hMy /Md    /ssssMM- NM-      yMo   /Mh    /MMM  `/ymMMMMMMMmyyoo+/:                      `oyyyo+",
        f"                          .........................MMMh.....................MMM/  .MMo///hMd` /Mh   /Mm  -MM- yMs  :my /Md. `hM+    /MMM......:+ydNMMMMMMMMMMy............................",
        f"                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/  `yyyyyso-   -y+   `ohdhosy-  /yddh+`  -shdhs-     /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        f"                          ooooooooooooooooooooooooooooooooooooooooooooooooooooo.                                                    .ooooooooooooooooooooooooooooooooooooooooooooooooooooo"]
]
# --- Game Story ---
# Each item is a list: [text_to_display, prompt_after_text]
game_story = [
    ["Years and years ago, there was a kingdom named Pagenra. ", CONTINUE_PROMPT],
    ["This kingdom had a prince named Idren, who had just turned 18. ", CONTINUE_PROMPT],
    [
        "But Idren couldn't rejoice in this situation. Because according to tradition, a prince who turns 18 is tasked with going to the cave of the sleeping dragon, a subject of legends for years, and taking something from its treasure. ",
        CONTINUE_PROMPT,
    ],
    ["Time passed, Idren prepared, and set off on a journey towards the dragon's lair. ", CONTINUE_PROMPT],
    ["Running\n", CONTINUE_PROMPT], # Special marker for running animation
    [
        "He stopped in front of a cave that sent shivers down one's spine even before entering, lit his torch, and slowly approached inside. ",
        CONTINUE_PROMPT,
    ],
    ["And suddenly, something Idren couldn't comprehend appeared before him.", CONTINUE_PROMPT],
    ["Beast", CONTINUE_PROMPT], # Special marker for Beast encounter
    ["Idren continued his journey, disoriented and tired.", CONTINUE_PROMPT],
    ["Walking\n", CONTINUE_PROMPT], # Special marker for walking animation
    [
        "He couldn't understand anything. What kind of place had he come to? He had never seen such a creature in his life (referring to the Beast). But his father, King Caliz II, had told him that such things would appear here before he came. ",
        CONTINUE_PROMPT,
    ],
    [
        "He too had come here in his time. Caliz II had changed a lot after coming from there, at least that's what the people said. ",
        CONTINUE_PROMPT,
    ],
    ["He hadn't even had time to catch his breath when he saw a stone entity standing before him.", CONTINUE_PROMPT],
    ["And suddenly, Idren had a vision: if he attacked the thing in front of him, he would die...", CONTINUE_PROMPT],
    ["Rock", CONTINUE_PROMPT], # Special marker for Rock encounter
    ["Idren proceeded a little further...", CONTINUE_PROMPT],
    ["Walking\n", CONTINUE_PROMPT], # Special marker for walking animation
    ["And Idren saw the dragon from those undying legends, enchanted by its majesty.", CONTINUE_PROMPT],
    ["The dragon named Draco was as majestic and powerful as the rumors said. ", CONTINUE_PROMPT],
    ["He moved forward silently so as not to wake Draco. ", CONTINUE_PROMPT],
    ["Draco", CONTINUE_PROMPT], # Special marker for Draco encounter
    ["He had succeeded, Idren emerged from the cave with a diamond the size of his hand...", CONTINUE_PROMPT],
    ["Just in case, he ran away from the vicinity of the cave. ", CONTINUE_PROMPT],
    ["Running\n", CONTINUE_PROMPT], # Special marker for running animation
    ["When he arrived in the city, Idren was exhausted. Those who saw him cheered with joy, and the crowd grew. ",
     CONTINUE_PROMPT],
    ["After all, their prince was worthy of becoming the future king...\n", "Game Over :'(",], # End game message
]

# --- Game Classes ---
class Character:
    """Base class for game characters."""
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

class Hero(Character):
    """Represents the player's character."""
    def __init__(self, health, attack, defense):
        super().__init__("Idren", health, attack, defense)

class Monster(Character):
    """Represents a generic monster."""
    pass # No specific attributes beyond Character for now

# --- Game Entities ---
# Initialize characters with their stats
hero = Hero(100, 50, 20)
beast = Monster("Beast the II.", 25, 10, 5)
rock = Monster("The Great Rock", 1000, 0, 10) # Rock has high health, no attack
draco = Monster("Draco", "?????", "?????", "?????") # Draco's stats are a mystery

# --- Utility Functions ---
def clear_screen():
    """Clears the console screen based on the operating system."""
    system('cls' if os.name == 'nt' else 'clear')

def print_text_slowly(text, delay=TYPING_SPEED):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def wait_for_input(prompt):
    """Displays a prompt and waits for user to press Enter."""
    print_text_slowly(prompt)
    input() # Waits for Enter

def display_ascii_art(art_frames, animation_delay, horizontal_offset_multiplier=0):
    """
    Displays ASCII art frames as an animation.
    Args:
        art_frames (list of list of str): List of ASCII art frames.
        animation_delay (float): Delay between frames.
        horizontal_offset_multiplier (int): Multiplier for horizontal movement.
    """
    clear_screen()
    # The range for animation steps is hardcoded in original code (10), keeping it.
    for i in range(WALK_ANIMATION_STEPS):
        for frame in art_frames:
            for line in frame:
                print(" " * i * horizontal_offset_multiplier + line)
            time.sleep(animation_delay)
            clear_screen()

def display_character_stats(opponent):
    """Displays hero's and opponent's stats side-by-side."""
    print("\n" + " " * 26 + f"{hero.name}" + " " * (106 - len(str(hero.name))) + f"{opponent.name}")
    print(" " * 26 + f"Health : {hero.health}" + " " * (97 - len(str(hero.health))) + f"{opponent.health}")
    print(" " * 26 + f"Attack : {hero.attack}" + " " * (96 - len(str(hero.attack))) + f"{opponent.attack}")
    print(" " * 26 + f"Defense : {hero.defense}" + " " * (97 - len(str(hero.defense))) + f"{opponent.defense}")
    print()

# --- Game Logic ---
def handle_beast_encounter():
    """Handles the encounter with the Beast."""
    clear_screen()
    print_photo(0)  # Display Beast's ASCII art
    display_character_stats(beast)

    print(" " * 26 + "1. Attack")
    print(" " * 26 + "2. Talk")
    print(" " * 26 + "3. Try to sneak past")
    print()

    choice = input(" " * 26 + "What do you want to do: ")

    if choice == "1":
        print_text_slowly(" " * 26 + "Beast the II. : AAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        beast.health -= (hero.attack - beast.defense)
        print(" " * 26 + f"Beast the II's Health : {beast.health}\n")
        if beast.health <= 0: # Changed to <= 0 to account for possible overkill
            print_text_slowly(" " * 26 + "Beast the II. is dead...\n")
        # In this simple game, even if Beast dies, the story continues.
        # For more complex combat, you'd add a loop for battle.

    elif choice == "2":
        print_text_slowly(" " * 26 + "Idren : Hello !?\n")
        print_text_slowly(" " * 26 + "Beast the II. : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        print(" " * 26 + "1. Attack")
        print(" " * 26 + "2. Try to sneak past")
        print()
        sub_choice = input(" " * 26 + "What do you want to do: ")

        if sub_choice == "1":
            print_text_slowly(" " * 26 + "Beast the II. : AAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
            beast.health -= (hero.attack - beast.defense)
            print(" " * 26 + f"Beast the II's Health : {beast.health}\n")
            if beast.health <= 0:
                print_text_slowly(" " * 26 + "Beast the II. is dead...\n")
        elif sub_choice == "2":
            print_text_slowly(" " * 26 + "You walked past the Beast, it couldn't see you because it was blind.\n")

    elif choice == "3":
        print_text_slowly(" " * 26 + "You walked past the Beast, it couldn't see you because it was blind.\n")
    else:
        print_text_slowly(" " * 26 + "You hesitated, and the Beast ignored you. You decided to move on.\n") # Default action for invalid input

    wait_for_input("") # Wait for user input to clear screen
    clear_screen()

def handle_rock_encounter():
    """Handles the encounter with the Rock."""
    clear_screen()
    print_photo(1)  # Display Rock's ASCII art
    display_character_stats(rock)

    print(" " * 26 + "1. Attack")
    print(" " * 26 + "2. Try to sneak past") # Changed from 3 to 2 for sequential numbering
    print()

    choice = input(" " * 26 + "What do you want to do: ")

    if choice == "1":
        # Attacking the rock leads to Game Over
        print_text_slowly(" " * 26 + "You fought for days and collapsed from exhaustion. You died. Because it was just a rock. Game Over :(\n")
        sys.exit() # Terminate the game
    elif choice == "2": # Corrected choice from "3" to "2"
        print_text_slowly(" " * 26 + "You walked past the Rock, it was just a stone...\n")
    else:
        print_text_slowly(" " * 26 + "You paused, then decided it was best to simply walk around the large stone.\n")

    wait_for_input("")
    clear_screen()

def handle_draco_encounter():
    """Handles the encounter with Draco."""
    clear_screen()
    print_photo(2)  # Display Draco's ASCII art
    display_character_stats(draco)

    print(" " * 26 + "You realized attacking was not an option. You silently stole a diamond the size of your hand from its treasure.\n")
    print()
    wait_for_input(" " * 26 + "Press Enter to continue your escape...")
    clear_screen()

def run_story():
    """Iterates through the game story, handling special events and text display."""
    for story_segment in game_story:
        main_text = story_segment[0]
        action_prompt = story_segment[1]

        clear_screen()

        # Handle special story markers for animations and encounters
        if main_text == "Beast":
            handle_beast_encounter()
        elif main_text == "Rock":
            handle_rock_encounter()
        elif main_text == "Draco":
            handle_draco_encounter()
        elif main_text == "Walking\n":
            display_ascii_art(walking_frames, WALK_ANIMATION_DELAY, 4)
        elif main_text == "Running\n":
            display_ascii_art(running_frames, RUN_ANIMATION_DELAY, 8)
        else:
            # For regular story text
            print_text_slowly(main_text)
            wait_for_input(action_prompt)

# This function was not defined but used in original code, fixing it.
def print_photo(integer) :
    """Prints the ASCII art for the specified enemy."""
    for line in enemy_arts[integer]:
        print(line)

# --- Main Game Execution ---
if __name__ == "__main__":
    clear_screen()
    print_text_slowly("Welcome to the game. Press Enter to start the adventure.")
    input()
    clear_screen()

    run_story()

    # Final game over message, handled by the last story segment
    print_text_slowly(game_story[-1][0])
    print_text_slowly(game_story[-1][1])