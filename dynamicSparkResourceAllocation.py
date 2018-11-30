

def get_max_cores_for_task(rows_to_process):
    cores_per_executor = 4
    max_cores = 40
    max_rows = 1000000
    num_cores = cores_per_executor + float(rows_to_process) / float(max_rows) * (max_cores - cores_per_executor)
    num_cores_rounded = int(cores_per_executor * round(num_cores / float(cores_per_executor)))
    print(min(num_cores_rounded, max_cores))
    return min(num_cores_rounded, max_cores)

get_max_cores_for_task(1000000)
