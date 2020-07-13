import os


class GamesManager:

    game = None
    utils = None
    config = None

    def translate_folder(self, folder):
        folder_input_path = '{0}{1}'.format(self.input_path, folder)
        folder_output_path = '{0}{1}'.format(self.output_path, folder)
        amount_of_files = (len(os.listdir(folder_input_path)))
        index = 0

        for internal_path in os.listdir(folder_input_path):
            index += 1
            for file in os.listdir('{0}\\{1}'.format(folder_input_path, internal_path)):
                if file[4:] == '.jet':
                    data = self.utils.read_json('{0}\\{1}\\{2}'.format(folder_input_path, internal_path, file))
                    for v in self.config['games'][self.game]['filenames']['{0}'.format(folder)]['v']:
                        data['fields'][v]['v'] = self.utils.translate(data['fields'][v]['v'])
                    print("{0} - {1}% - {2}".format('{0}({1})'.format(folder, internal_path),
                                                    int((index / amount_of_files) * 100), data))
                    self.utils.write_json(data, '{0}\\{1}'.format(folder_output_path, internal_path), file)

    def translate_file(self, file, file_config, special_characters=None):
        file_index = 0
        file_name = file[:-4]
        data = self.utils.read_json("{0}\\{1}".format(self.input_path, file))

        if file_config['episodeid'] > 0:
            data['episodeid'] = self.config['games'][self.game]['filenames']['{0}'.format(file[:-4])]['id']

        amount_of_lines = len(data['content'])
        index = 0
        for line in data['content']:
            index += 1

            for string in self.config['games'][self.game]['filenames'][file_name]['strings']:
                line[string] = self.utils.translate(line[string], special_characters=special_characters)

            for key in self.config['games'][self.game]['filenames'][file_name]['dicts']:
                if key in line.keys():
                    for t in line[key]:
                        line[key][t] = self.utils.translate(line[key][t], special_characters=special_characters)

            print("{0} - {1}% - {2}".format(file_name, int((index / amount_of_lines) * 100), line))
        self.utils.write_json(data, self.output_path, file)

    def __init__(self, config, utils, game):
        self.game = game
        self.config = config
        self.utils = utils
        self.input_path = "{0}\\{1}\\content\\".format(config['input_path'], config['games'][game]['path'])
        self.output_path = "{0}\\{1}\\content\\".format(config['output_path'], config['games'][game]['path'])
        special_characters = None

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        self.utils.translate_menus(config, game)
        for file in config['games'][game]['filenames']:
            if os.path.isfile('{0}\\{1}'.format(file, '.jet')) and file['translate']:
                if 'special_characters' in config['games'][game]['filenames'][file]:
                    special_characters = config['games'][game]['filenames'][file]['special_characters']
                self.translate_file('{0}\\{1}'.format(file, '.jet'), config['games'][game]['filenames'][file], special_characters=special_characters)
                if file['has_folder']:
                    self.translate_folder(file)