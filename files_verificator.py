from pathlib import Path

dataset_v01 = Path('/home/pedro/Workspace/Aeroscan/data/dataset_gmsh_v01/')
dataset_v02 = Path('/home/pedro/Workspace/Aeroscan/data/dataset_gmsh_v02/')
dataset_v03 = Path('/home/pedro/Workspace/Aeroscan/data/dataset_gmsh_v03/')
dataset_v04 = Path('/home/pedro/Workspace/Aeroscan/data/dataset_gmsh_v04/')
datasets = [dataset_v01, dataset_v02, dataset_v03, dataset_v04]

def findFilesInDirectory(directory: Path) -> list:

    files = sorted([file.parts[-1] for file in directory.glob('**/*') if file.is_file()])

    if 'config.txt' in files:
        files.pop()
    
    return files

if __name__ == '__main__':

    # List of sets of the files in datasets
    filesOfDataset = []
    for dataset in datasets:

        filesOfDataset.append(set(findFilesInDirectory(directory=dataset)))

    different_files_1withOthers = filesOfDataset[0].difference(filesOfDataset[1], filesOfDataset[2], filesOfDataset[3])
    different_files_2withOthers = filesOfDataset[1].difference(filesOfDataset[0], filesOfDataset[2], filesOfDataset[3])
    different_files_3withOthers = filesOfDataset[2].difference(filesOfDataset[0], filesOfDataset[1], filesOfDataset[3])
    different_files_4withOthers = filesOfDataset[3].difference(filesOfDataset[0], filesOfDataset[1], filesOfDataset[2])

    print('x----------------------------x')
    print(f'Number of files processed by dataset v01: {len(filesOfDataset[0]) / 2}')
    print('Parameters:\n'
            '\t--mesh_generator=gmsh\n'
            '\t--no_use_highest_dim\n'
            '\t--no_use_debug\n'
            '\t--mesh_size=20')
    print(f'only by v01: {different_files_1withOthers}', end='\n\n')
    print(f'Number of files processed by dataset v02: {len(filesOfDataset[1]) / 2}')
    print('Parameters:\n'
            '\t--mesh_generator=gmsh\n'
            '\t--no_use_highest_dim\n'
            '\t--no_use_debug\n'
            '\t--mesh_size=1e22')
    print(f'only by v02: {different_files_2withOthers}', end='\n\n')
    print(f'Number of files processed by dataset v03: {len(filesOfDataset[2]) / 2}')
    print('Parameters:\n'
            '\t--mesh_generator=gmsh\n'
            '\t--no_use_highest_dim\n'
            '\t--no_use_debug\n'
            '\t--mesh_size=1e22\n'
            '\tMeshSizeFromCurvature=15 (Internal Parameter)')
    print(f'only by v03: {different_files_3withOthers}', end='\n\n')
    print(f'Number of files processed by dataset v04: {len(filesOfDataset[3]) / 2}')
    print('Parameters:\n'
            '\t--mesh_generator=gmsh\n'
            '\t--no_use_highest_dim\n'
            '\t--no_use_debug\n'
            '\t--mesh_size=20\n'
            '\tMeshSizeFromCurvature=15 (Internal Parameter)')
    print(f'only by v04: {different_files_4withOthers}', end='\n\n')
    print('x----------------------------x')