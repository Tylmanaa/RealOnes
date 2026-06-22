try:
    # опасный код, который может сломаться (например, попытка открыть файл)
    mistakes=[] 
    with open('server.log', 'r') as file:
        for line in file:
            if 'ERROR' in line or 'CRITICAL' in line:
                mistakes.append(line)
                


    # Здесь file ведет себя как список строк, по которому можно пройтись циклом for

        answer= f"Общее количество ошибок, {len(mistakes)}"
    
        with open('report.txt', 'w') as report_file:
            for log in mistakes:
                report_file.write(log) # \n нужен для переноса строки
            report_file.write(answer)

except FileNotFoundError:
    print('Внимание: Файл с логами не найден.')

