import csv

with open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\stocks.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector)  # saltar encabezado

    with open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\Output.csv", "w", newline="") as salida:
        f_out = csv.writer(salida)

        # Nuevo encabezado
        f_out.writerow(["Company Name", "PE Ratio", "PB Ratio"])

        for fila in lector:
            company = fila[0]              # texto (string)
            numbers = list(map(float, fila[1:]))  # convierte lo demás en números (floats)

            price = numbers[0]
            e_p_share = numbers[1]
            b_value =numbers[2]

            pe_ratio= round(price/e_p_share,2)
            pto_ratio= round(price/b_value,2)
            #f_out.write(company + "," + str(e_p_share)+ "," + str(b_value) + '\n')
            f_out.writerow([company, pe_ratio, pto_ratio])
#f_out.close()

with open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\Output.csv", "r") as archivo:
    print(archivo.read())
