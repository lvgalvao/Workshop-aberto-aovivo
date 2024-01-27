from frontend import ExcelValidadorUI
from backend import process_excel, save_dataframe_to_sql

def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        df, result, errors = process_excel(uploaded_file)
        ui.display_results(result, errors)

        if result and not errors and ui.display_save_button():
            save_dataframe_to_sql(df)
            ui.display_success_message()

if __name__ == "__main__":
    main()