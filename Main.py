from Utilities import Utils

default_config = {
    "input_path": "",
    "output_path": "",
    "games_path": "assets\\games\\",
    "language": "es",
    "games": {
        "Bracketeering": {
            "path": "assets\\games\\Bracketeering",
            "translate": True,

            "filenames": {
                'BRKPrompt': {
                    "translate": True,
                    "has_folder": True,
                    "subtitles_index": [],
                    "strings": ['category'],
                    "dicts": ['decoys', 'twists', 'prompt', 'facts'],
                    "v": [3, 4, 6, 8, 10, 12, 13],
                    "id": 1353
                }
            }
        }
    }
}

utils = Utils()
utils.format_file('assets.bin')

