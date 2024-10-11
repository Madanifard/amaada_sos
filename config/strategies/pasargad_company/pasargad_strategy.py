from config.strategies.base.insurance_strategy import InsuranceStrategy
from config.strategies.base.insured_strategy import InsuredStrategy
from config.strategies.base.person_strategy import PersonStrategy
from config.strategies.base.plan_strategy import PlanStrategy
from .validates.insured_validate import InsuredValidate
from .validates.insurance_validate import InsuranceValidate
from .validates.person_validate import PersonValidate
from .validates.plan_validate import PlanValidate


class PasargadStrategy(InsuranceStrategy, InsuredStrategy, PersonStrategy, PlanStrategy):

    def insured_process(self, data):
        errors = []
        formatted_data = {}
        check_insured = InsuredValidate()
        is_valid, errors = check_insured.validate(data)
        if is_valid:
            formatted_data = check_insured.format_data(data)
        return is_valid, errors, formatted_data

    def insurance_process(self, data):
        errors = []
        formatted_data = {}
        check_insurance = InsuranceValidate()
        is_valid, errors = check_insurance.validate(data)
        if is_valid:
            formatted_data = check_insurance.format_data(data)
        return is_valid, errors, formatted_data

    def person_process(self, data):
        errors = []
        format_data = {}
        check_person = PersonValidate()
        is_valid, errors = check_person.validate(data)
        if is_valid:
            format_data = check_person.format_data(data)
        return is_valid, errors, format_data

    def plan_process(self, data):
        errors = []
        formatted_data = {}
        check_plan = PlanValidate()
        is_valid, errors = check_plan.validate(data)
        if is_valid:
            formatted_data = check_plan.format_data(data)
        return is_valid, errors, formatted_data

    def process(self, section, data):

        match section.lower():
            case 'insured':
                return self.insured_process(data)
            case 'insurance':
                return self.insurance_process(data)
            case 'person':
                return self.person_process(data)
            case 'plan':
                return self.plan_process(data)
            case _:
                raise Exception('Section Process Is Not Valid')
