import argparse

parser = argparse.ArgumentParser(
                    prog= 'Mon Programme',
                    description='Affichage emoji'
                    )

parser.add_argument('-n', '--nombre', default=5, dest='nombre')
args=parser.parse_args()

for i in range(0, int(args.nombre)):
    print("\U0001f600")