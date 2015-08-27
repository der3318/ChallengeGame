# 2015 臺大椰林資訊營 AI Challenge - API使用說明
## 遊戲方式：
在 Challenge 資料夾下開啟 cmd ，並輸入：
```
python3 main.py
```

* 真人對戰:

    player 0(左上角 Tzuki) : `wasd`

    player 1(左下角 Superman) : `tfgh`

    player 2(右上角 Cactus) : `ijkl`

    player 3(右下角 Pusheen) : `↑ ↓ → ←` 


* 要使用AI進行對戰:

    輸入

    ```
    python3 main.py 101 _ 102 _
    ```

    即可開啟 team101(當成player 0) 與 team102(當成player 2) 的 AI 進行遊戲，不足或是底線的部份以手動控制補齊

## AI 基礎
* 所有的 AI 程式碼都必須寫在 AI 這個資料夾中，檔名為"teamXXX.py"，其中，XXX為AI名稱（英文數字並用，字數10字內為佳），AI名稱會出現在記分板上面


## helper —— 取得場上資訊
helper 裏面有大量函式幫助你獲得目前場上的資訊！


※ 位置都是指迷宮上的棋盤格座標 : (x, y) 0 <= x < 19 , 0 <= y < 11，左上為(0, 0)，右下為(19, 11)
※ 方向只有上下左右: (1, 0), (-1, 0), (0, 1), (0, -1)


## 地圖info

* helper.getMapInfo() : 獲得整張地圖資訊(每個格子上有什麼)
* helper.getShortestPath(pos_a, pos_b, dir_a = (1, 0)) : 在pos_a以dir_a這個方向要走到pos_b的最短路
* helper.calcFoodOnPath(pos_a , [dir]) : 從pos_a開始沿著[dir]這條路一直走可以吃到多少食物(假設路上都不會遇到其他人)
* helper.getKNearestFood(pos, K) : 獲得離pos最近(對走路的距離來說)的K個食物位置的list


### Example

```python
game_map = self.helper.getMapInfo()
print( game_map )
# 輸出一個由字串組成的二維list
# (x, y)有牆壁 : game_map[ x ][ y ] = "BLOCK"
#       空道路 :                    = "ROAD"
#       食物   :                    = "FOOD"
#       其他人 :                    = "PLAYER"
#       我自己 :                    = "ME"
 
path = self.helper.getShortestPath( ( 8 , 3 ) , ( 4 , 2 ) , ( -1 , 0 ) )
# 在(8,3)這格面對左邊走到(4,2)
print( path )
# 輸出 : [(-1, 0), (-1, 0), (-1, 0), (-1, 0), (0, -1)]
# 代表( 8 , 3 )沿著這個方向一次一次走就可以走到( 4 , 2 )

count_food = self.helper.calcFoodOnPath( ( 8 , 3 ) , [ ( -1 , 0 ) , ( -1 , 0 ) , ( 0 , -1 ) ] )
print( count_food )
# example 輸出 : 2
# 如果傳進去的path是不合法的(走到牆壁走到迷宮外面)那結果不保證正確與合理

foods_list = self.helper.getKNearestFood( ( 8 , 3 ) , 4 )
print( foods_list )
# example輸出 : [(9, 3), (7, 3), (6, 3), (6, 2)]
# 如果傳進去的K超過現在出現在地圖上的食物數量，那只會回傳地圖上全部食物位置的list
```

## 自己info

* helper.getMyPosition() : 獲得自己的位置
* helper.getMyDirection() : 獲得自己當前面對的方向
* helper.getMyScore() : 獲得自己當前的分數
* helper.checkMeDead() : 檢查我是不是死了(回傳True或False)
* helper.checkMeStopped() : 檢查我是不是卡在某個點上沒有在動(回傳True或False)
* helper.getFacingPlayer(dir) : 我朝dir這個方向的**直線上**有哪些玩家
* helper.getFacingPlayer(dir, pos) : 從pos這個位置朝dir這個方向的**直線上**有哪些玩家
* helper.checkDirection(dir) : 檢查我可不可以走dir這個方向(回傳True或False)，撞牆或回頭都算不能走（死亡時被關在中間，是個特殊空間，回傳值永遠為False）
* helper.getNearPlayer() : 獲得將其他玩家按照到自己的最短距離由小排到大的list，**不包括死掉的玩家**
* helper.getTopPlayer() : 獲得將其他玩家按照她的分數由大排到小的list
* helper.getDeadPlayer() : 獲得其他是死掉的玩家組成的list
* helper.getLivePlayer() : 獲得其他是活著的玩家組成的list

### Example

```python

my_pos = self.helper.getMyPosition()
print( my_pos ) # 輸出 : (8, 3)

my_dir = self.helper.getMyDirection()
print( my_dir ) # 輸出 : (-1, 0)

my_score = self.helper.getMyScore()
print( my_score ) # 輸出 : 15

am_i_dead = self.helper.checkMeDead()
print( am_i_dead ) # 輸出 : False

am_i_stuck = self.helper.checkMeStopped()
print( am_i_stuck ) # 輸出 : False

facing_player = self.helper.getFacingPlayer( ( -1 , 0 ) )
print( facing_player ) # 輸出 : [1, 3]

can_i_go_left = self.helper.checkDirection( ( -1 , 0 ) )
print( can_i_go_left ) # 輸出 : False

players = self.helper.getNearPlayer()
print( players ) # 輸出 : [2, 1, 3]
players = self.helper.getTopPlayer()
print( players ) # 輸出 : [1, 3, 2]
players = self.helper.getDeadPlayer()
print( players ) # 輸出 : [1]
players = self.helper.getLivePlayer()
print( players ) # 輸出 : [2, 3]

```

## 其他玩家info

* helper.getPlayerPosition(player_id) : 獲得玩家player_id當前的位置
* helper.getPlayerScore(player_id) : 獲得玩家player_id當前的分數
* helper.getPlayerDirection(player_id) : 獲得玩家player_id面對的方向
* helper.checkPlayerDead(player_id) : 檢查玩家player_id是否死了(回傳True或False)
* helper.checkPlayerStopped(player_id) : 檢查玩家player_id是否卡在某個點沒有動(回傳True或False)
* helper.getEatScore(player_id) : 我撞到玩家player_id可以得到的分數，> 0代表我可以吃掉他得幾分，< 0代表我被他吃掉失幾分，= 0代表我跟他什麼事都不發生
* helper.getPlayerMustBe(player_id) : 獲得玩家player_id接下來**一定**會走到的地方和方向，如果沒有一定會走到的點，則回傳點(0, 0)與方向(0, -1)，例如他接下來一定會依序走過abcd四個點，會回傳他到達d點的位置和到達d點時的方向


### Example

```python

p1_pos = self.helper.getPlayerPosition( 1 )
print( p1_pos ) # 輸出 : (10, 3)

p1_dir = self.helper.getMyDirection( 1 )
print( p1_dir ) # 輸出 : (-1, 0)

p1_score = self.helper.getPlayerScore( 1 )
print( p1_score ) # 輸出 : 10

is_p1_dead = self.helper.checkPlayerDead( 1 )
print( is_p1_dead ) # 輸出 : False

is_p1_stuck = self.helper.checkPlayerStopped( 1 )
print( is_p1_stuck ) # 輸出 : False

eat_p1_score = self.helper.getEatScore( 1 )
print( eat_p1_score ) # 輸出 : -10
# 我要是撞到player 1我會死掉並且扣10分

( p1_must_pos , p1_must_pos_dir ) = self.helper.getPlayerMustBe( 1 )
print( p1_must_pos ) # 輸出 : (6, 3)
print( p1_must_pos_dir ) # 輸出 : (-1, 0)
# player 1要是沒被吃掉，就一定會走到(6, 3)，並且在走到(6, 3)時面對(-1, 0)的方向
# 這可以用來設計堵人的AI
# 要是該玩家卡住，或是處在可以選擇的路口則回傳((0, 0), (0, -1))

```


## 求神問卜

* helper.askGodDirection(god_name) : 問god_name這個神給個方向
* helper.askGodPosition(god_name) : 問god_name這個神給個位置，神會保證這個位置**一定不是**牆壁

### Example

```python

blah_dir = self.helper.askGodDirection('tenyoku8478')
print( blah_dir ) # 輸出 : (1, 0)

blah_pos = self.helper.askGodPosition('der3318')
print( blah_pos ) # 輸出 : (1, 4)

```

## SKILL呼叫
* 發動技能「More Eggs」
    * 效果： 蛋黃哥的分數變為兩倍（只有自己有效果）
    * 持續時間： 5秒
    * 使用方法： `helper.SkillBonus()`

* 發動技能「Lullaby」
    * 效果： 所有的敵方玩家將會被暈眩（無法操控、無法移動）
    * 持續時間： 3秒
    * 使用方法： `helper.SkillDizzy()`

* 發動技能「Mega Punch」
    * 效果： 所有的非死亡敵方玩家將會受到迷惑（無法操控、隨機亂跑）
    * 持續時間： 3秒
    * 使用方法： `helper.SkillConfuse()`

* 發動技能「Egg Vacuum」
    * 效果： 吃掉周圍的蛋黃哥並獲得分數
    * 範圍： 以角色為中心，曼哈頓距離<=4的平面空間
    * 使用方法： `helper.SkillEatNear()`

* 發動技能「Rocket of Doom」
    * 效果： 發射火箭，擊殺最高分的非死亡敵對玩家（擊殺後可掠奪對方5分）
    * 使用方法： `helper.SkillShoot()`

* 取得目前場上的技能冷卻時間
    * 說明：技能施放的冷卻時間為10秒（所有技能、不分敵我共用冷卻時間），如果在冷卻時呼叫技能，該技能會等到場上冷卻時間結束後才被施放
    * 效果： 取得目前場上的技能冷卻時間，回傳一個非負整數，單位為秒
    * 使用方法： `helper.getSkillCoolTime()`

## AI 回傳值
* AI_DIR_UP: AI往上走
* AI_DIR_DOWN: AI往下走
* AI_DIR_LEFT: AI往左走
* AI_DIR_RIGHT: AI往右走


