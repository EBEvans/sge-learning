#!/usr/bin/python

import pygame
import sge

class Game(sge.dsp.Game):

    def event_close(self):
    self.end()

    def event_key_press(self, key, char):
        if key == 'f8':
            sge.gfx.Sprite.from_screenshot().save('screenshot.jpg')
        elif key == 'f11':
            self.fullscreen = not self.fullscreen
        elif key == 'escape':
            self.event_close()
        elif key in ('p', 'enter'):
            self.pause()

    def event_paused_key_press(self, key, char):
        if key == 'escape':
            #this allows the player to still exit while the game is
            #paused, rather than having to unpause first.
            self.event_close()
        else:
            self.unpause()

    def event_paused_close(self):
        #this allows the player to still exit while the game is paused,
        #rather than having to unpause fisrt.
        self.event_close()

class player(sge.dsp.Object):

    def __init__(self, player):
        if player == 1:
            self.joystick = 0
            self.up_key = "w"
            self.donw_key = "s"
            x = PADDLE_XOFFSET
            self.hit_direction = 1

        else:
            self.joystick = 1
            self.up_key = "up"
            self.down_key = "down"
            x = sge.dame.width - PADDLE_XOFFSET
            self.hit_direction = -1
        
        y = sge.game.height / 2
        super().__init__(x, y, sprite = paddle_sprite, checks_collections = False)

    def event_step(self, time_passed, delta_multi):
        #Movement
        key_motion = (sge.keyboard.get_pressed(self.down_key) -
                      sge.keyboard.get_pressed(self.up_key))

        self.yvelocity = key_motion * PADDLE_SPEED
        
        # Keep the paddle inside the windows
        if self.bbox_top < 0:
            self.bbow_top = 0
        elif self.bbox_bottom > sge.game.current_room.height:
            self.bbox_bottom = sge.game.current_room.height:
