from Utilities import Utils
from GamesManagement import GamesManager

default_config = {
    "input_path": "",
    "output_path": "",
    "games_path": "assets\\games\\",
    "language": "es",
    "localization_forced_ins": {
        'LANGUAGE_NAME': 'Español',
        'BACK': 'ATRAS',
        'CLOSE': 'CERRAR',
        'ON': 'ENCENDIDO',
        'BACK_TO_PACK': 'ATRAS',
        'GO_TO': 'VE A',
        'PRESS': 'PULSA',
        'EVERYBODYS_IN': 'TODOS LISTOS',
        'UNHIDE': 'MOSTRAR',
        "SETTINGS_VOLUME_DESCRIPTION": "Haz que el juego suene ALTO o BAJO.",
        'VOLUME_DESCRIPTION': 'Haz que el juego suene ALTO o BAJO.',
        'TWITCH_REQUIRED': 'Requerir cuenta en TWITCH',
        "BLIND_BRACKET": "BRAKET CIEGO",
        "TRIPLE_BLIND_BRACKET": "BRACKET CIEGO TRIPLE",
        "BRACKET_WINNERS": "GANADORES DEL BRACKET",
        "LEADERBOARD": "Tabla de Puntos",
        "BADGE_TITLE_FAMILY_MODE": "APTO PARA TODA LA FAMILIA",
        "MENU_GAME_NAME_1": "Fibber 3",
        "QUIT": "SALIR"
    },
    "localization_skip_words": ['twitter', 'spice girls', 'sub-zero', 'none', 'a', 'true', 'false'],
    "games": {
        "PartyPack": {
            "path": "assets\\games\\PartyPack",
            "translate": False,
            "filenames": {}
        },
        "Bracketeering": {
            "path": "assets\\games\\Bracketeering",
            "translate": False,

            "filenames": {
                'BRKPrompt': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['category'],
                    "dicts": ['prompt'],
                    "dict_arrays": ['decoys', 'twists', 'facts'],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [],
                    "s": [15, 16, 17, 19, 21],
                    "episodeid": 1353
                }
            }
        },
        "Fibbage3": {
            "path": "assets\\games\\Fibbage3",
            "translate": False,

            "filenames": {
                'fibbageshortie': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['category'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [5, 7, 8, 9, 10, 11, 12, 13, 14],
                    "s": [15, 16, 18, 19],
                    "episodeid": 1307
                },
                'fibbagespecial': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['category'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [5, 7, 8, 9, 10, 11, 12, 13, 14],
                    "s": [15, 16, 18, 19],
                    "episodeid": 1317
                },
                'finalfibbage': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['category'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [5, 7, 8, 9, 10, 11, 12, 13, 14],
                    "s": [15, 16, 18, 19],
                    "episodeid": 1313
                },
                'tmishortie': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['personal'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [5, 7, 8, 9, 10, 11, 12, 13, 14],
                    "s": [15, 16, 18, 19],
                    "episodeid": 1309
                }
            }
        },
        "MonsterMingle": {
            "path": "assets\\games\\MonsterMingle",
            "translate": True,

            "filenames": {
                'MMMonster': {
                    "translate": False,
                    "has_folder": False,
                    "strings": ['name', 'shortDescription', 'description', 'selfDescription'],
                    "dicts": ['powerpopup', 'epitaph', 'hint'],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [],
                    "s": [],
                    "episodeid": 0
                },
                'MMMonsterAudienceAnswer': {
                    "translate": True,
                    "has_folder": True,
                    "single_structure": True,
                    "strings": ['answer'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": None,
                    "v": [],
                    "s": [],
                    "episodeid": 0
                }
            }
        }
    }
}

utils = Utils()
config = utils.create_config(default_config)
utils.format_file('assets.bin', input_path=config['input_path'])
utils.unzip_assets(config)
utils.remove_file(config['input_path'], 'assets.zip')
utils.refresh_output('{0}\\{1}'.format(config['input_path'], 'assets'),'{0}\\{1}'.format(config['output_path'], 'assets'))

for game in config['games'].keys():
    if config['games'][game]['translate']:
        print('Translating: {0}'.format(game))
        gamesManager = GamesManager(config, utils, game)
    else:
        print('{0} was skipped'.format(game))

utils.zip(config['output_path'])
#utils.format_file('assets.zip', input_path=config['output_path'], output_path=config['input_path'])
#utils.remove_file(config['output_path'], 'assets.zip')
