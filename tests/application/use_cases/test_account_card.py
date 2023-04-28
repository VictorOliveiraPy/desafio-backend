from sqlalchemy.orm import Session

from src.application.use_cases.account_card import AccountCardUseCase
from src.domain.entities.account import CardCreate


class TestAccountCardUseCase:

    def test_when_creating_a_new_card_should_return_the_created_card_with_its_id(self, mocker):
        mock_db = mocker.Mock(spec=Session)
        use_case = AccountCardUseCase(mock_db)

        card_data = {
            "id": "70c881d4a26984ddce795f6f71817c9cf4480e79",
            "title": "Cartão 1",
            "pan": "5527952393064634",
            "expiry_mm": "03",
            "expiry_yyyy": "2022",
            "security_code": "656",
            "date": "26/11/2015"
        }

        card = CardCreate(**card_data)
        created_card = use_case.create_card(card)

        assert created_card.id == '70c881d4a26984ddce795f6f71817c9cf4480e79'
