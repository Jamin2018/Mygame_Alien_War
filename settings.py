class Settings():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船设置

        self.ship_limit = 3

        # 飞船子弹设置

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5

        # 外星人速度设置

        self.fleet_drop_speed = 10


        # 加快游戏节奏
        self.speedup_scale = 1.1
        # 提高外星人点数
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 1.5  # 设置移动速度
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        #记分
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale) # 显示整数



