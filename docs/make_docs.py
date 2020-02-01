import subprocess


def run():
    cmd_api = "sphinx-apidoc -f -o . ."
    cmd_doc = "sphinx-build -b html . ./_build"

    for cmd in [cmd_api, cmd_doc]:
        result = res = subprocess.Popen(cmd, shell=True, universal_newlines=False)
        print(result)


if __name__ == '__main__':
    run()
