import os
import sys

def count_files(dir_path):
    text_files = ['txt', 'log', 'doc', 'csv', 'xml', 'html', 'htm', 'sh', 'h', 'c', 'readme', 'conf']
    binary_files = ['pdf', 'jpg', 'zip', 'png', 'bin', 'jpeg', 'gz']
    text_count = {}
    binary_count = {}
    unclassified_count = {}
    total_count = {}
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_type = file.split('.')[-1].lower()
            if file_type in text_files:
                text_count.setdefault(root, {}).setdefault(file_type, 0)
                text_count[root][file_type] += 1
            elif file_type in binary_files:
                binary_count.setdefault(root, {}).setdefault(file_type, 0)
                binary_count[root][file_type] += 1
            else:
                unclassified_count.setdefault(root, {}).setdefault(file_type, 0)
                unclassified_count[root][file_type] += 1
            total_count[root] = total_count.get(root, 0) + 1
            yield
    result = ''
    result += '---------------------------------------\n'
    result += 'Diretorios com mais arquivos TEXTO: \n'
    result += '---------------------------------------\n'
    for dir, count in sorted(text_count.items(), key=lambda x: sum(x[1].values()), reverse=True):
        result += '{}: {} arquivos de texto\n'.format(dir, sum(count.values()))
        for file_type, file_count in count.items():
            result += '  {}: {}\n'.format(file_type, file_count)
    result += '---------------------------------------\n'
    result += 'Diretorios com mais arquivos BINARIOS: \n'
    result += '---------------------------------------\n'
    for dir, count in sorted(binary_count.items(), key=lambda x: sum(x[1].values()), reverse=True):
        result += '{}: {} arquivos binarios\n'.format(dir, sum(count.values()))
        for file_type, file_count in count.items():
            result += '  {}: {}\n'.format(file_type, file_count)
    result += '----------------------------------------------------\n'
    result += 'Diretorios com arquivos com tipos nao classificados:\n'
    result += '----------------------------------------------------\n'
    for dir, count in sorted(unclassified_count.items(), key=lambda x: sum(x[1].values()), reverse=True):
        result += '{}: {} arquivos nao classificados\n'.format(dir, sum(count.values()))
        for file_type, file_count in count.items():
            result += '  {}: {}\n'.format(file_type, file_count)
    max_dir = max(total_count, key=total_count.get)
    result += 'Diretorio com mais arquivos: {} ({} arquivos)\n'.format(max_dir, total_count[max_dir])
    with open('/tmp/resultado.txt', 'w') as f:
        f.write(result)
        print(result)
    print('O resultado foi salvo em: /tmp/resultado.txt')

if __name__ == '__main__':
    dir_path = sys.argv[1]
    for _ in count_files(dir_path):
        pass
