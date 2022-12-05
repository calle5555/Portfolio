import random
from turtle import pos

class Puzzle():
    def __init__(self, dimension, initial=None, goal=None):
        
        # No point in playing the game
        if dimension < 2:
            raise ValueError

        # Check to see if the initial value is passed
        if initial and len(initial) != dimension:
            raise ValueError

        # Check to see if the goal value is passed
        if goal and len(goal) != dimension:
            raise ValueError  

        self.last_action = 'Down'
        self.dimension = dimension
        self.state = initial
        if not initial:
            self.state = [i for i in range(0, pow(dimension, 2))]
        
        self.goal = goal
        if not goal:
            self.goal = reversed(self.state)

        self.state = tuple(self.state)
        self.goal = tuple(self.goal)

    def possible_actions(self):
        poss_actions = ['Up', 'Down', 'Left', 'Right']
        blank_pos = self.state.index(0)
        
        if (blank_pos + 1) % self.dimension == 0:
            poss_actions.remove('Right')

        if blank_pos % self.dimension == 0:
            poss_actions.remove('Left')

        if blank_pos < self.dimension:
            poss_actions.remove('Up')

        if blank_pos > len(self.state) - self.dimension - 1:
            poss_actions.remove('Down')

        return tuple(poss_actions)

    def make_move(self, action):
        poss_actions = {'Up': -self.dimension, 'Down' : self.dimension, 'Left' : -1, 'Right' : 1}
        blank_pos = self.state.index(0)
        self.state = list(self.state)

        self.state[blank_pos], self.state[blank_pos + poss_actions[action]] = self.state[blank_pos + poss_actions[action]], self.state[blank_pos]

        self.state = tuple(self.state)
        self.last_action = action

    def check_goal(self):
        return self.state == self.goal

    def scramble_board(self):
        rev_actions = {'Up': 'Down', 'Down' : 'Up', 'Left' : 'Right', 'Right' : 'Left'}

        for _ in range(pow(self.dimension, 4)):
            poss_act = self.possible_actions()

            if(rev_actions[self.last_action] in poss_act):
                tmp = list(poss_act)
                tmp.remove(rev_actions[self.last_action])
                poss_act = tuple(tmp)
            
            self.make_move(random.choice(poss_act))

    def print_board(self):
        print('')
        for i in range (0, pow(self.dimension, 2)):
            if(i % self.dimension == 0):
                print("")
            
            print(f"{self.state[i]} ", end='')

    def heuristic(self):
        pass


def main():
    try:
        puzzle = Puzzle(3)
    except ValueError:
        print("Try different starting values")

    puzzle.print_board()
    puzzle.scramble_board()
    puzzle.print_board()

if __name__ == '__main__':
    main()