import yaml
import argparse, os
from tqdm import tqdm
from pathlib import Path

POSSIBLE_CURVES = ['line', 'circle', 'ellipse', 'bspline']
POSSIBLE_SURFACES = ['plane', 'cone', 'cylinder', 'revolution', 'extrusion', 'bspline', 'torus']
POSSIBLE_FORMATS = ['.yml', '.yaml']

def list_files(input_dir: str, formats: list, return_str=False) -> list:
    files = []
    path = Path(input_dir)
    for file_path in path.glob('*'):
        if file_path.suffix.lower() in formats:
            files.append(file_path if not return_str else str(file_path))
    return sorted(files)

def loadYAML(features_name: str):
    with open(features_name, 'r') as f:
        data = yaml.load(f, Loader=yaml.Loader)
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="find the curves and surfaces types in features files.")
    parser.add_argument('input_file', type=str, help="input path of file or directory")
    parser.add_argument('-c', '--curves', type=str, default='all', help=f'curves to find. Possible curves: {POSSIBLE_CURVES}.')
    parser.add_argument('-s', '--surfaces', type=str, default='all', help=f'surfaces to find. Possible surfaces: {POSSIBLE_SURFACES}.')
    args = vars(parser.parse_args())

    input_path = args['input_file']
    curves = args['curves']
    surfaces = args['surfaces']
    
    if not curves or not surfaces:
        print('No one curve or surface chosen.')
        exit()

    if os.path.exists(input_path):
        if os.path.isdir(input_path):
            files = list_files(input_path, POSSIBLE_FORMATS)
        else:
            files = [input_path]
    else:
        print('[Generator Error] Input path not found')
        exit()
    
    with open('output_file.txt', 'w') as out_file:
        for file in tqdm(files):
            types_found = {}
            file = str(file)

            data_file = loadYAML(features_name=file)
            
            if curves:
                for curve in data_file['curves']:
                    if curve['type'].lower() in curves:
                        if curve['type'] not in types_found.keys():
                            types_found[curve['type']] = 1
                        else:
                            types_found[curve['type']] += 1
            
            if surfaces:
                for surface in data_file['surfaces']:
                    if surface['type'].lower() in surfaces:
                        if surface['type'] not in types_found.keys():
                            types_found[surface['type']] = 1
                        else:
                            types_found[surface['type']] += 1

            if types_found:
                out_file.write(f'File: {file}:\n')
                for key, value in types_found.items():
                    out_file.write(f'\t{value} {key} found.')
                out_file.write('\n\n')
