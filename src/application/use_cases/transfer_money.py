from src.repositories.account_card_repository import CreditCardRepository
from src.repositories.person_repository import PersonRepository


class TransferMoney:
    def __init__(
            self,
            person_repository: PersonRepository,
            credit_card_repository: CreditCardRepository,
    ):
        self.person_repository = person_repository
        self.credit_card_repository = credit_card_repository
