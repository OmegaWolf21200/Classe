class Player :
   def __init__ (self, pseudo, health, attack) :
    self.pseudo = pseudo 
    self.health = health
    self.attack = attack
    def get_pseudo (self):
        return self.pseudo


    def damage (self, damage):
        self.health-= damage
        print ("Aie ... Vous venez de prendre des dégats : " , damage , "!")


player1 = Player ("Graven", 20, 3 )  
player1.damage(3)
print ("Vous avez " , player1.health , "point de vie" )

player2 = Player ("Bob", 20, 5 )  



