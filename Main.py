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
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [3, 4, 6, 8, 10, 12, 13],
                    "id": 1353
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
utils.refresh_output('{0}\\{1}'.format(config['input_path'], 'assets'),
                     '{0}\\{1}'.format(config['output_path'], 'assets')
                     )


for game in config['games'].keys():
    print(game)


utils.zip(config['output_path'])
utils.format_file('assets.zip', input_path=config['output_path'], output_path=config['input_path'])
utils.remove_file(config['output_path'], 'assets.zip')
