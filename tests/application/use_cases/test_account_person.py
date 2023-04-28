from sqlalchemy.orm import Session

from src.application.use_cases.account_person import AccountPersonUseCase
from src.domain.entities.person import PersonCreate


class TestAccountPersonUseCase:

    def test_when_creating_a_new_person_should_return_the_created_person_with_its_id(self, mocker):
        mock_db = mocker.Mock(spec=Session)
        use_case = AccountPersonUseCase(mock_db)

        user_data = {
            "first_name": "João",
            "last_name": "das Neves",
            "birthday": "1991-09-91",
            "password": "*****",
            "username": "joao_das_neves",
            "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
        }

        user = PersonCreate(**user_data)

        created_person = use_case.create_person(user)
        assert created_person.user_id == '70c881d4a26984ddce795f6f71817c9cf4480e79'



