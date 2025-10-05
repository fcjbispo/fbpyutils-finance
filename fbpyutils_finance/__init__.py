import os
import fbpyutils

from dotenv import load_dotenv


from fbpyutils import file as F

_ = load_dotenv()

_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

USER_CVM_DIR = os.path.sep.join([os.path.expanduser("~"), ".cvm"])

CERTIFICATES = {
    f.split(os.path.sep)[-1].split(".")[0]: f for f in F.find(_ROOT_DIR, "*.pem")
}

MARKET_INFO = [
    {
        "region": "América",
        "market": "BVMF",
        "name": "B3 - Bolsa de Valores do Brasil e Mercado de balcão",
        "delay": "15",
        "timezone": "America/Sao_Paulo",
    },
    {
        "region": "América",
        "market": "NASDAQ",
        "name": "NASDAQ Last Sale",
        "delay": "Em tempo real*",
        "timezone": "America/New_York",
    },
    {
        "region": "América",
        "market": "NYSE",
        "name": "NYSE",
        "delay": "Em tempo real*",
        "timezone": "America/New_York",
    },
    {
        "region": "América",
        "market": "NYSEARCA",
        "name": "NYSE ARCA",
        "delay": "Em tempo real*",
        "timezone": "America/New_York",
    },
    {
        "region": "América",
        "market": "NYSEAMERICAN",
        "name": "NYSE American",
        "delay": "Em tempo real*",
        "timezone": "America/New_York",
    },
]


# Setup logger and environment first
fbpyutils.setup(os.path.join(_ROOT_DIR, "app.json"))

env = fbpyutils.get_env()
env.LOG_LEVEL = os.environ.get("FBPY_LOG_LEVEL", "INFO")

logger = fbpyutils.get_logger()
logger.configure_from_env(env)


if not os.path.exists(USER_CVM_DIR):
    os.makedirs(USER_CVM_DIR)
