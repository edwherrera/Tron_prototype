from Logic import action
from Logic.player import Player
from Logic import exception

import json


def map_player(player_dict):
    try:
        return Player(player_dict['name'], (player_dict['x'], player_dict['y']))
    except KeyError:
        raise InvalidActionFileException("Invalid Player format", player_dict)


def map_action(action_dict, player_list):
    try:
        return action.get_action(
            action_dict['action'], 
            search_player(action_dict['player'], player_list),
            action_dict['amount']
        )
    except KeyError:
        raise InvalidActionFileException("Invalid Action format", action_dict)


def search_player(player_name, player_list):
    try:    
        return [player for player in player_list if player.name == player_name].pop()
    except IndexError:
        raise exception.InvalidActionFileException("'{}' is not a valid player".format(player_name))


def build_player_list(player_list):
    if player_list is None:
        raise InvalidActionFileException("Missing 'players' field")

    return [map_player(player) for player in player_list]


def build_action_list(action_list, player_list):
    if action_list is None:
        raise InvalidActionFileException("Missing 'action' field")

    return [map_action(a, player_list) for a in action_list]
    

def parse_action_file(path):
    with open(path) as action_file:
        action_json = json.load(action_file)
        players = build_player_list(action_json.get('players'))
        actions = build_action_list(action_json.get('actions'), players)

    return { 'players': players, 'actions': actions }
