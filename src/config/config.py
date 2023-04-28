import logging
import os

from pydantic import AnyUrl, BaseSettings

logging.basicConfig(level=logging.INFO)
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    title: str = "Desafio Backend"
    description: str = "O desafio consiste em criar uma API REST para uma Conta Digital, onde o usuário poderá " \
                       "realizar pagamentos para seus amigos e adicionar cartões de crétido, que será consumida por " \
                       "um aplicativo (Android e iOS). Onde o usuário irá cadastrar/listar/editar/apagar um cartão " \
                       "quando desejar e transferir e listar o extrato de pagamentos."
    version: str = "1.0.0"
    debug: bool = False
    testing: bool = False

    DATABASE_URL: AnyUrl = os.environ.get("DATABASE_URL")
    DATABASE_CONNECT_DICT: dict = {}


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
