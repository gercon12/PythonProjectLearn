'''
def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans
'''


def sliding_window_fixed(input_list, window_size):
    if window_size > len(input_list):
        return None  # No tiene sentido si la ventana es más grande que la lista

    # Calcular la suma inicial de la primera ventana
    window_sum = sum(input_list[0:window_size])
    max_sum = window_sum

    # Recorrer la lista desplazando la ventana
    for right in range(window_size, len(input_list)):
        left = right - window_size
        # Mover la ventana: restar el que sale y sumar el que entra
        window_sum = window_sum - input_list[left] + input_list[right]
        # Guardar el máximo
        max_sum = max(max_sum, window_sum)

    return max_sum


# Ejemplo de uso
nums = [2, 1, 5, 1, 3, 2]
k = 4
print(sliding_window_fixed(nums, k))  # Resultado esperado: 9 (ventana [5,1,3])
