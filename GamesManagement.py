import os


class GamesManager:

    game = None
    utils = None
    config = None

    def translate_single_structure(self, file, special_characters=None):
        file_name = file[:-4]
        data = self.utils.read_json("{0}\\{1}".format(self.input_path, file))

        if self.config['games'][self.game]['filenames'][file_name]['episodeid'] > 0:
            data['episodeid'] = self.config['games'][self.game]['filenames']['{0}'.format(file[:-4])]['episodeid']

        amount_of_lines = len(data['content'])
        index = 0
        for line in data['content']:
            index += 1
            for string in self.config['games'][self.game]['filenames'][file_name]['strings']:
                line[string] = self.utils.translate(line[string], special_characters=special_characters)
            print("{0} - {1}% - {2}".format(file_name, int((index / amount_of_lines) * 100), line))
        self.utils.write_json(data, self.output_path, file)

    def translate_folder(self, folder, special_characters=None):
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
                    for s in self.config['games'][self.game]['filenames']['{0}'.format(folder)]['s']:
                        data['fields'][s]['s'] = self.utils.translate(data['fields'][s]['s'], special_characters=special_characters)
                    print("{0} - {1}% - {2}".format('{0}({1})'.format(folder, internal_path),
                                                    int((index / amount_of_files) * 100), data))
                    self.utils.write_json(data, '{0}\\{1}'.format(folder_output_path, internal_path), file)

    def translate_file(self, file, file_config, special_characters=None):
        file_name = file[:-4]
        data = self.utils.read_json("{0}\\{1}".format(self.input_path, file))

        if file_config['episodeid'] > 0:
            data['episodeid'] = self.config['games'][self.game]['filenames']['{0}'.format(file[:-4])]['episodeid']

        amount_of_lines = len(data['content'])
        index = 0
        for line in data['content']:
            index += 1

            for string in self.config['games'][self.game]['filenames'][file_name]['strings']:
                line[string] = self.utils.translate(line[string], special_characters=special_characters)

            for internal_dict in self.config['games'][self.game]['filenames'][file_name]['dicts']:
                if internal_dict in line.keys():
                    for t in line[internal_dict].keys():
                        line[internal_dict][t] = self.utils.translate(line[internal_dict][t], special_characters=special_characters)

            if 'arrays' in self.config['games'][self.game]['filenames'][file_name].keys():
                for array in self.config['games'][self.game]['filenames'][file_name]['arrays']:
                    for i in range(0, len(array)):
                        array[i] = self.utils.translate(array[i], special_characters=special_characters)

            for key in self.config['games'][self.game]['filenames'][file_name]['dict_arrays']:
                if key in line.keys():
                    for t in range(0, len(line[key])):
                        for v in line[key][t].keys():
                            line[key][t][v] = self.utils.translate(line[key][t][v], special_characters=special_characters)

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
            if os.path.isfile('{0}{1}{2}'.format(self.input_path, file, '.jet')) and config['games'][game]['filenames'][file]['translate']:
                if 'special_characters' in config['games'][game]['filenames'][file]:
                    special_characters = config['games'][game]['filenames'][file]['special_characters']
                if 'single_structure' in config['games'][game]['filenames'][file].keys() and config['games'][game]['filenames'][file]['single_structure']:
                    self.translate_single_structure('{0}{1}'.format(file, '.jet'), special_characters=special_characters)
                else:
                    self.translate_file('{0}{1}'.format(file, '.jet'), config['games'][game]['filenames'][file], special_characters=special_characters)
                    if config['games'][game]['filenames'][file]['has_folder']:
                        self.translate_folder(file, special_characters)


