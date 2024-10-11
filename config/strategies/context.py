from config.strategies.pasargad_company.pasargad_strategy import PasargadStrategy


class StrategyContext:

    def __init__(self, company_name):
        self.strategy = self.get_strategy(company_name)

    def get_strategy(self, company_name):
        if company_name == 'pasargad':
            return PasargadStrategy()
        else:
            raise ValueError('Unknown insurance company')

    def process(self, section, data):
        is_valid, errors, formatted_data = self.strategy.process(section, data)
        return is_valid, errors, formatted_data
