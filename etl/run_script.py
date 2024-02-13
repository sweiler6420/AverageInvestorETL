import sys
import importlib

def main(script, args):
    print(f"Attempting to run script: {script}")
    print(f"arguments to be passed: {args}")

    try:
        script_import = importlib.import_module(f'scripts.{script}')
        script_import.main(args)

    except ImportError as e:
        print(e)

if __name__ == "__main__":

    script, *args = sys.argv[1:]
    main(script=script, args=args)