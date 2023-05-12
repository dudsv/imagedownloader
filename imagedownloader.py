import os
import time

file_name = input("Digite o nome do arquivo de listagem:\n")
save_folder = input("Digite a pasta de destino onde as imagens devem ser salvas:\n")

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

start_time = time.time()

os.system(f"wget -r -np -nd -P {save_folder} -i {file_name}")

end_time = time.time()
total_time = end_time - start_time

print(f"Finalizado. Tempo total: {total_time:.2f} segundos.")