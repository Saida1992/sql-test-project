import os
import glob

def check_sql_files():
    sql_files = glob.glob("**/*.sql", recursive=True)
    errors_found = False

    for file_path in sql_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().upper()
            
            # Sadə nümunə: Eyni CTE daxilində təkrar cədvəl çağırışını yoxlamaq
            # Öz şərtlərinizi buraya əlavə edə bilərsiniz
            if content.count("FROM EMPLOYEES") > 1:
                print(f"XƏTA: {file_path} faylında 'Employees' cədvəli təkrarən əsassız çağrılıb!")
                errors_found = True

    if errors_found:
        print("SQL kod yoxlamasından keçmədi! Qaydalar pozulduğu üçün merge qadağandır.")
        exit(1)
    else:
        print("Bütün SQL yoxlamaları uğurla keçdi!")
        exit(0)

if __name__ == "__main__":
    check_sql_files()
