import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Lê as variáveis de ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM vendas', con=DATABASE_URL)

    # Verificar se o DataFrame não está vazio
    assert not df.empty, "O DataFrame está vazio."

    # Verificar o schema (colunas e tipos de dados)
    expected_dtype = {
        'id': 'int64',
        'email': 'object',  # object em Pandas corresponde a string em SQL
        'data': 'datetime64[ns]',
        'valor': 'float64',
        'produto': 'object',
        'quantidade': 'int64',
        'categoria': 'object'
    }

    assert df.dtypes.to_dict() == expected_dtype, "O schema do DataFrame não corresponde ao esperado."

def test_check_usuario_pode_inserir_um_excel_e_receber_uma_mensagem():
    # Configurar o WebDriver
    driver = webdriver.Chrome()  # ou Firefox(), dependendo do seu navegador

    try:
        # Acessar a página do Streamlit
        driver.get("http://localhost:8501")

        # Aguardar para garantir que a página foi carregada
        sleep(3)  # Espera 3 segundos

        # Realizar o upload do arquivo de sucesso
        success_file_path = os.path.abspath("data/correto.xlsx")
        driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

        # Aguardar a mensagem de sucesso
        sleep(3)
        assert "O schema do arquivo Excel está correto!" in driver.page_source

        # Verificar se o botão "Salvar no Banco de Dados" está presente
        save_button = driver.find_element(By.XPATH, "//button[text()='Salvar no Banco de Dados']")
        assert save_button.is_displayed()

    finally:
        driver.quit()