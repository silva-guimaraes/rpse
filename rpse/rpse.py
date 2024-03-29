# import sys
import os
import pysubs2
import argparse
from pathlib import Path

# todo:
# opção de undo
# adicionar suporte para arquivos zip


def fetch_remaining_files(input_file, excluded, sort=True):

    # um objeto path do arquivo em si
    first_file = Path(input_file)

    # um objeto path do diretorio onde o arquivo fica, que deve incluir
    # todos os outros
    # episodios/legendas
    file_dir = Path(os.path.dirname(first_file))

    ret = []
    # iterar todos os outros arquivos no diretorio e juntar em uma lista os
    # com a mesma extensão
    for i in file_dir.iterdir():
        if i.suffix == first_file.suffix:
            ret.append(Path(i))

    for i in excluded:
        ret.remove(i)
    if sort:
        ret.sort()

    # excluir todos os arquivos que vierem antes do arquivo indicado,
    # caso algum
    try:
        first_file_index = ret.index(first_file)
    except ValueError:
        print('arquivo "' + first_file + '" inexistente')
        exit(1)

    return ret[first_file_index:]


def read_parse_textfile(file):

    ret = []
    try:
        with open(file) as file:
            for line in file:
                ret.append(Path(line.rstrip()))

    except FileNotFoundError:
        print('arquivo "' + file + '" inexistente')
        exit(1)

    return ret


# def fetch_zip(input_zip):
#     input_zip = zipfile.ZipFile(input_zip)
#     print(input_zip.infolist())


# def handle_input_dir(input_dir):
#     if (zipfile.is_zipfile(input_dir)):
#         fetch_zip(input_dir)


def print_files(f):
    for i in f:
        print(i)


def main():

    parser = argparse.ArgumentParser(
        prog='rpse', description='renomear e parear arquivos de legendas com \
episódios')
    parser.add_argument('ep', metavar='ep', type=str, nargs=1)
    parser.add_argument('sub', metavar='sub', type=str, nargs=1)
    parser.add_argument('-p', '--preview', action='store_true')
    parser.add_argument('-o', '--order', action='store_true')
    parser.add_argument('-d', '--delay', nargs=1, default=[0], type=int)
    parser.add_argument('-e', '--exclude', default=[], type=str, nargs='+')
    parser.add_argument('-txt', '--txtfile', action='store_true')

    namespace = parser.parse_args()

    delay = namespace.delay[0]
    excluded = namespace.exclude
    f_ep = namespace.ep[0]
    f_sub = namespace.sub[0]

    if (namespace.txtfile):
        eps = read_parse_textfile(f_ep)
        subs = read_parse_textfile(f_sub)
    else:
        eps = fetch_remaining_files(f_ep, excluded)
        subs = fetch_remaining_files(f_sub, excluded)

    if (namespace.preview):
        print_files(eps)
        print_files(subs)
        print(len(eps))
        print(len(subs))
        exit(0)

    sub_suffix = subs[0].suffix

    for i in range(min(len(eps), len(subs))):

        if namespace.order:
            order = f'{i + 1:02d}_'
            ep_basename = order + eps[i].name
            ep_new_name = eps[i].parent / Path(ep_basename)
            eps[i].rename(ep_new_name)
        else:
            ep_new_name = eps[i]

        sub_new_name = subs[0].parent / Path(ep_new_name.stem + sub_suffix)

        subs[i].rename(sub_new_name)

        if (delay != 0):
            s = pysubs2.load(sub_new_name)
            for line in s:
                line.start += delay
                line.end += delay

            s.save(sub_new_name)


if __name__ == "__main__":
    main()
