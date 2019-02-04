import argparse
import subprocess

def reportTo(nombre, email):
    texto = "Reportando a {}".format(nombre)

    # Say that we are sending a report
    cmd = 'say "{}"'.format(texto)
    subprocess.Popen(['/bin/bash', '-c', cmd])

    # Send the report via mail
    mailCmd = 'echo "{}" | mail -s "New Report" "{}"'.format(texto,email)
    subprocess.Popen(['/bin/bash', '-c', mailCmd])

    print("Sent report to mail {}".format(email))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple processing pipeline')
    parser.add_argument('-n', dest='nombre', default="Pepe", help='your name')
    parser.add_argument('-e', dest='email', default="marc@faable.com", help='your email')

    args = parser.parse_args()

    # Start the python script
    reportTo(args.nombre, args.email)