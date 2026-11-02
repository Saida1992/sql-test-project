import os
import glob

def check_sql_files():
    # Repozitoriyadakı bütün .sql fayllarını tapırıq
    sql_files = glob.glob("**/*.sql", recursive=True)
    errors_found = False

    for file_path in sql_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().upper()
            
            # Meyar 1: CTE daxilində təkrar cədvəl çağırışı (məsələn, Employees cədvəli)
            if content.count("FROM EMPLOYEES") > 1 or content.count("JOIN EMPLOYEES") > 1:
                print(f"❌ XƏTA: {file_path} faylında 'Employees' cədvəli təkrarən əsassız çağrılıb!")
                errors_found = True
                
            # Meyar 2: SELECT * tətbiqi qadağası (performans üçün)
            if "SELECT *" in content:
                print(f"❌ XƏTA: {file_path} faylında 'SELECT *' istifadə olunub! Sütun adlarını dəqiq qeyd edin.")
                errors_found = True

    if errors_found:
        print("\nSQL kod yoxlamasından keçmədi! Merge bloklanır.")
        exit(1) # Exit 1 olduqda GitHub Action FAIL verir və Merge bloklanır
    else:
        print("\nBütün SQL yoxlamaları uğurla keçdi!")
        exit(0)

if __name__ == "__main__":
    check_sql_files()
