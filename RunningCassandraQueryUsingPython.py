#running cassandra queries using python

import subprocess

def get_cassandra_output(employeeName, salary):

    event_name = 'STM_'+ entity_name
    get_table_details = """cqlsh --ssl --request-timeout=60 -e "
    Select ID, name, dept, salary from KeyspaceDummy.employee where name ='{}' and salary > {};
    ;"
    """.format(employeeName, salary)

    print(get_table_details)

    process = subprocess.Popen([get_table_details], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output = process.stdout.read()

    output1 = output.split("\n")

    lines = [line for line in output1 if line.strip()]

    # out ==> a list of string, each row consists atomic rows of the output

    out = lines[2:-1][::-1]
    
    return out
    

print(get_cassandra_output('Richard', 20000))
