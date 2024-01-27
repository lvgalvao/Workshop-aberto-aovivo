from frontend import ExcelValidadorUI
from backend import process_excel, save_dataframe_to_sql
from dotenv import load_dotenv
import sentry_sdk

load_dotenv()

sentry_sdk.init(
    dsn="https://f6bcf586f490b9ae2befe4b7a7fc0e15@o4505699197452288.ingest.sentry.io/4506642699059200",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        df, result, errors = process_excel(uploaded_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_wrong_message()
            sentry_sdk.capture_message("Erro ao subir excel")
        elif ui.display_save_button():
            # Se não houver erros e o botão for exibido, exibir o botão e fazer o log
            save_dataframe_to_sql(df)
            ui.display_success_message()
            sentry_sdk.capture_message("Banco de dados foi atualizado")

if __name__ == "__main__":
    main()