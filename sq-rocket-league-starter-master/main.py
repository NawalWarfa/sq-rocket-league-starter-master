# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    
    def run(self):

        if self.intent is not None:
            return
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.ball.location.y - self.foe_goal.location.y)

        is_in_front_of_ball = d1 > d2

        if is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.location))
            return
        self.set_intent(short_shot(self.foe_goal.location))

        if self.kickoff_flag: 
            self.set_intent(kickoff())
            return
        
        if self.recovery_flag:
            self.set_intent(recovery())
        
        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            return
    
        if self.me.boost > 97:
            self.set_intent(short_shot(self.foe.goal.location))
            return

        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            self.set_intent(goto(target_boost.location))
            return
        
        if self.foes:
            self.set_intent(super())
            return
        
        
    
