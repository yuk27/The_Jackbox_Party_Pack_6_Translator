from Utilities import Utils
from GamesManagement import GamesManager

default_config = {
    "input_path": "C:\\Users\\Juan Carlos Solano\\Documents\\Mine\\The Jackbox Party Pack 6",
    "output_path": "",
    "games_path": "games\\",
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
        "LEADERBOARD": "Tabla de Puntos",
        "BADGE_TITLE_FAMILY_MODE": "APTO PARA TODA LA FAMILIA",
        "QUIT": "SALIR"
    },
    "localization_skip_words": ['twitter', 'spice girls', 'sub-zero', 'none', 'a', 'true', 'false', 'superman', 'frozen'],
    "games": {
        "PartyPack": {
            "path": "games\\PartyPack",
            "translate": True,
            "filenames": {}
        },
        "TriviaDeath2": {
            "path": "games\\TriviaDeath2",
            "translate": True,

            "filenames": {
                'QuiplashContent': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['prompt'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [5],
                    "s": [8],
                    "episodeid": 1230
                },
                'TDFinalRound': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": ['choices'],
                    "special_characters": None,
                    "v": [0],
                    "s": [1],
                    "episodeid": 1390
                },
                'TDMindMeld': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": ['choices'],
                    "special_characters": None,
                    "v": [1],
                    "s": [2],
                    "episodeid": 1390
                },
                'TDMirror': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['password'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters":  [['<', '>'], ['[', ']']],
                    "v": [5],
                    "s": [7],
                    "episodeid": 0
                },
                'TDMirrorTutorial': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['password'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": None,
                    "v": [],
                    "s": [],
                    "episodeid": 0
                },
                'TDQuestion': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": ['choices'],
                    "special_characters": None,
                    "v": [],
                    "s": [],
                    "episodeid": 1391
                },
                'TDQuestionBomb': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [],
                    "s": [],
                    "episodeid": 1391
                },
                'TDQuestionHat': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": ['choices'],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [2, 3, 4],
                    "s": [],
                    "episodeid": 1392
                },
                'TDQuestionKnife': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": ['choices'],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [],
                    "s": [],
                    "episodeid": 1394
                },
                'TDQuestionMadness': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['text'],
                    "dicts": [],
                    "dict_arrays": ['choices'],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [],
                    "s": [],
                    "episodeid": 1395
                 },
                'TDQuestionWig': {
                     "translate": True,
                     "has_folder": False,
                     "strings": ['text'],
                     "dicts": [],
                     "dict_arrays": ['choices'],
                     "special_characters": [['<', '>'], ['[', ']']],
                     "v": [],
                     "s": [],
                     "episodeid": 1389
                },
                'TDSequel': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['text'],
                    "dicts": ['text'],
                    "dict_arrays": ['choices'],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [],
                    "s": [],
                    "episodeid": 0
                }
            },
        }
    }
}

utils = Utils()
config = utils.create_config(default_config)
#utils.refresh_output(config['input_path'], config['output_path'])

for game in config['games'].keys():
    if config['games'][game]['translate']:
        print('Translating: {0}'.format(game))
        gamesManager = GamesManager(config, utils, game)
    else:
        print('{0} was skipped'.format(game))
