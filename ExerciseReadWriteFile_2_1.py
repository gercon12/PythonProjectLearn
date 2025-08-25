import csv

with open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\stocks.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector)  # saltar encabezado

    with open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\Output_1.csv', 'w') as f_out:
        f_out.write("Company Name,PE Ratio,PB Ratio\n")

        for fila in lector:
            company = fila[0]              # texto (string)
            numbers = list(map(float, fila[1:]))  # convierte lo demás en números (floats)

            price = numbers[0]
            e_p_share = numbers[1]
            b_value =numbers[2]

            pe_ratio= round(price/e_p_share,2)
            pto_ratio= round(price/b_value,2)
            f_out.write(company + "," + str(pe_ratio)+ "," + str(pto_ratio) + '\n')
f_out.close()

with open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\Output_1.csv", "r") as f:
    print(f.read())
