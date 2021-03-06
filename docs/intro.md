﻿# 2015 臺大椰林資訊營 AI Challenge - 遊戲介紹


## 遊戲名稱：
    Sticker Wars


## 遊戲規則：

    像迷宮一般的地圖中，有四隻貼圖角色－Tuzki、Superman、Cactus和Pusheen，他們必須在「3分鐘」內盡可能吃掉蛋黃哥。

    在道路中，會隨機出現蛋黃哥，每吃掉一隻，可以獲得5分。

    不過，每個貼圖角色在探索蛋黃哥的時候，也必須彼此堤防，因為兩隻角色相撞的時候，分數高的角色將會被擊殺，並轉移10點分數到對方身上。


## 地圖構造：

    地圖由「路」、「牆壁」所構成，正中央是死亡的「復活區域」，只能出來不能進去。

    「牆壁」無法通過，因此所有的角色都應循著地圖中的「路」來移動、追殺和探索。


## 角色移動：
* 地圖是平面的，因此會有四個方向可以移動（上、下、左、右）
* 角色沒有辦法掉頭，也沒有辦法在半路停下來
* 如果得到了不合法的方向（例如往牆壁走、回頭走），角色將會沿著原本的方向繼續前進
* 當走到路底撞牆時，如果沒有獲得新的方向，角色會繼續對著牆壁原地踏步


## 蛋黃哥出現的位置：

    所有的「道路」都可能隨機出現美味的蛋黃哥，「牆壁」、「角色身上」或「復活區域」則不會有食物出現。


## 相撞判斷：

    當兩個角色同時走到地圖的某一點，或是彼此穿越時，會發生碰撞。

* 依據碰撞角色的數量、分數高低，會有不同的情況發生
    * 兩人碰撞且分數不同：低分者殺死高者分並奪走10分，如果高分者未滿10分，低分者只會獲得高分者的所有分數並將對方分數歸0
    * 兩人碰撞且分數相同：兩人都不會死亡，也不會發生分數的改變，並且隨機指示兩隻角色不同的離開方向，這個位置的蛋黃哥會自動被清除
    * 多人碰撞且分數最低者只有一人：最低分者會殺死「所有高分者」並奪取分數
    * 多人碰撞且分數最低者有兩人以上：最低分的角色們會殺死「所有高分者」，並「平均分配」奪得的分數，之後再依隨機指示的方向離開


## 死亡與復活：

    死亡的角色，會被送到中央的復活區域，並出現「3秒」的死亡倒數。

    死亡倒數的期間內，角色無法移動，但可以決定待會離開時的方向。

    死亡倒數一結束，就會依著倒數時決定的方向（若無決定，則會隨機分配）離開復活區域，「無法逗留」。

    值得注意的是，為了防止在出口堵人，當角色復活走到「復活區的出口」時，如果沒有獲得合法的移動方向，同樣會被「隨機指示」移動方向


## 特殊技能：

    營期間會獲得遊戲的技能卡片，將卡片交給營隊方登入後，即可使用該技能。

    每個技能的使用會有10秒的冷卻時間，不分技能、不分敵我，共用冷卻時間。
    
    如果在冷卻時間內使用技能，技能會等到場上的冷卻時間結束後才被施放。

* 技能有以下五種：
    * More Eggs：10秒內蛋黃哥的分數變為兩倍（只會自己有效）
    * Lullaby：所有的敵方玩家將會被暈眩5秒（無法操控、無法移動）
    * Mega Punch：所有的非死亡敵方玩家將會受到迷惑5秒（無法操控、隨機亂跑）
    * Egg Vacuum：吃掉周圍的蛋黃哥並獲得分數
    * Rocket of Doom：發射火箭，擊殺最高分的非死亡敵對玩家，並奪取分數
    

