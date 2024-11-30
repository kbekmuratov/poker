class Stats:
    def __init__(self, file_name='stats.txt'):
        self.file_name = file_name

        self.combinations = {
            'Royal Flush': 0,
            'Straight Flush': 0,
            'Four of a Kind': 0,
            'Full House': 0,
            'Flush': 0,
            'Straight': 0,
            'Three of a Kind': 0,
            'Two Pairs': 0,
            'Pair': 0,
            'High Card': 0
        }

        try:
            file = open(self.file_name, 'r')
            for line in file:
                combinations, count = line.strip().split(': ')
                self.combinations[combinations] = int(count)
            file.close()
        except FileNotFoundError:
            print('File is not find')
        except:
            print('Error')

    def save_stats(self):
        file = open(self.file_name, 'w')
        for combo, count in self.combinations.items():
            file.write(f'{combo}: {count}\n')
        file.close()

    def update_stats(self, combination):
        if combination in self.combinations:
            self.combinations[combination] += 1
        else:
            print(f'Combination {combination} was not find.')

    def show_stats(self):
        print('\nStatistics: ')
        print('='*50)
        for combo, count in self.combinations.items():
            print(f'{combo:<20} | {count:10}')
            print('-'*50)
