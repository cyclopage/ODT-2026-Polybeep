import time
import random
from config import *


class GameMode:
    def __init__(self, name, depth, player_kill, ai_kill, ai_revives, randomness, bloodlust):
        self.name = name
        self.depth = depth           
        self.player_kill = player_kill  
        self.ai_kill = ai_kill          
        self.ai_revives = ai_revives    
        self.randomness = randomness    
        self.bloodlust = bloodlust      #penalty value for split moves (1-3)

#character definitions and modifier values
DRUID  = GameMode("DRUID",  1, 5, 5, False, 20, 1)  #low penalty to split
TANK   = GameMode("TANK",   1, 5, 6, False, 30, 1)  #higher random chance to break loops that form with 5 points
WRAITH = GameMode("WRAITH", 2, 5, 5, True,  20, 2)  #medium split penalty, gets revive tokens
ORACLE = GameMode("ORACLE", 5, 5, 5, False, 1,  1)  #low aggression and randomness, large search depth

MODES = {'druid': DRUID, 'tank': TANK, 'wraith': WRAITH, 'oracle': ORACLE}


class Hand:
    def __init__(self):
        self.value = 1
        self.alive = True
    
    def receive_attack(self, incoming, kill_at):
        if not self.alive:
            return False
        self.value += incoming
        #wrap or kill depending on result
        if self.value >= kill_at:
            self.value -= kill_at
            if self.value == 0:
                self.alive = False
                return True  #hand died
        return False
    
    def set_value(self, v, kill_at):
        #used for splits - clamp and check if hand should die
        if v >= kill_at:
            v -= kill_at
        self.value = v
        self.alive = (v > 0)
    
    def revive(self):
        self.value = 1
        self.alive = True


class Player:
    def __init__(self):
        self.hands = [Hand(), Hand()]
    
    def is_dead(self):
        return all(not h.alive for h in self.hands)
    
    def total(self):
        #sum of all living hand values, used for split calculations
        return sum(h.value for h in self.hands if h.alive)


def get_attacks(attacker, defender):
    #return all valid attack combos between living hands
    moves = []
    for ai, ah in enumerate(attacker.hands):
        if not ah.alive:
            continue
        for ti, th in enumerate(defender.hands):
            if th.alive:
                moves.append(('A', ai, ti))
    return moves


def get_splits(player, kill_at):
    #generate all valid ways to redistribute finger total across both hands
    #filters out no-ops, duplicates, and illegal revives
    moves = []
    total = player.total()
    current = (player.hands[0].value, player.hands[1].value)
    seen = set()
    for left in range(total + 1):
        right = total - left
        al = left - kill_at if left >= kill_at else left
        ar = right - kill_at if right >= kill_at else right
        if (al, ar) == current or (al, ar) in seen:
            continue
        one_dead = (current[0] == 0) != (current[1] == 0)
        would_kill = (al == 0) != (ar == 0)
        if one_dead and would_kill:
            continue  #can't use a split to revive a dead hand
        seen.add((al, ar))
        seen.add((ar, al))
        moves.append(('S', al, ar))
    return moves


def get_all_moves(attacker, defender, kill_at):
    return get_attacks(attacker, defender) + get_splits(attacker, kill_at)


def copy_state(ai, human, ai_kill, player_kill, bloodlust):
    #snapshot of game state for minimax - works on dicts not objects
    return {
        'ai': [h.value if h.alive else 0 for h in ai.hands],
        'human': [h.value if h.alive else 0 for h in human.hands],
        'ai_kill': ai_kill,
        'player_kill': player_kill,
        'bloodlust': bloodlust,
        'last_move_type': None
    }


def is_dead(state, who):
    return all(v == 0 for v in state[who])


def apply_move(state, move, attacker, defender):
    #returns a new state dict after applying the move, doesn't mutate original
    s = {
        'ai': list(state['ai']),
        'human': list(state['human']),
        'ai_kill': state['ai_kill'],
        'player_kill': state['player_kill'],
        'bloodlust': state['bloodlust'],
        'last_move_type': move[0]
    }
    
    if move[0] == 'A':
        _, ah, dh = move
        s[defender][dh] += s[attacker][ah]
        if s[defender][dh] >= (s['ai_kill'] if defender == 'ai' else s['player_kill']):
            s[defender][dh] -= (s['ai_kill'] if defender == 'ai' else s['player_kill'])
    else:
        _, left, right = move
        s[attacker] = [left, right]
    
    return s


def get_state_moves(state, attacker, defender):
    #same as get_all_moves but operates on state dicts instead of Player objects
    moves = []
    kill_at = state['ai_kill'] if attacker == 'ai' else state['player_kill']
    for ai in range(2):
        if state[attacker][ai] == 0:
            continue
        for di in range(2):
            if state[defender][di] > 0:
                moves.append(('A', ai, di))
    total = sum(state[attacker])
    current = tuple(state[attacker])
    seen = set()
    for left in range(total + 1):
        right = total - left
        al = left - kill_at if left >= kill_at else left
        ar = right - kill_at if right >= kill_at else right
        if (al, ar) == current or (al, ar) in seen:
            continue
        one_dead = (current[0] == 0) != (current[1] == 0)
        would_kill = (al == 0) != (ar == 0)
        if one_dead and would_kill:
            continue
        seen.add((al, ar))
        seen.add((ar, al))
        moves.append(('S', al, ar))
    return moves


def minimax(state, depth, is_ai_turn, alpha, beta):
    #terminal conditions - bonus/penalty for winning deeper in the tree
    if is_dead(state, 'ai'):
        return -100 - depth
    if is_dead(state, 'human'):
        return 100 + depth
    if depth == 0:
        #heuristic: prefer low hand values for ai, high for human
        score = 0
        for v in state['ai']:
            if v > 0: score += (10 - v)
        for v in state['human']:
            if v > 0: score -= (10 - v)
        
        #penalise paths that ended in a split - bloodlust pushes AI to attack
        if state['last_move_type'] == 'S':
            score -= (10 * state['bloodlust'])
            
        return score
    
    attacker = 'ai' if is_ai_turn else 'human'
    defender = 'human' if is_ai_turn else 'ai'
    moves = get_state_moves(state, attacker, defender)
    
    if is_ai_turn:
        best = -999
        for m in moves:
            new_state = apply_move(state, m, attacker, defender)
            best = max(best, minimax(new_state, depth - 1, False, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha: break  #prune
        return best
    else:
        best = 999
        for m in moves:
            new_state = apply_move(state, m, attacker, defender)
            best = min(best, minimax(new_state, depth - 1, True, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha: break  #prune
        return best


def ai_choose_move(ai, human, mode):
    moves = get_all_moves(ai, human, mode.ai_kill)
    if not moves: return None
    
    #random move chance keeps gameplay varied and prevents easy counters
    if random.randint(0, 99) < mode.randomness:
        return random.choice(moves)
    
    state = copy_state(ai, human, mode.ai_kill, mode.player_kill, mode.bloodlust)
    best_score = -999
    best_move = moves[0]
    
    for m in moves:
        new_state = apply_move(state, m, 'ai', 'human')
        score = minimax(new_state, mode.depth, False, -999, 999)
        
        #same penalty applied immediately so the AI doesn't split on its current t