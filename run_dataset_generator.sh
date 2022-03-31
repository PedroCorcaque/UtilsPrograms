my_problematic_files() {
    for filename in `ls /home/pedro/Workspace/Aeroscan/data/allModelsForDatasets/stepFiles | sort -n`
    do
        echo "arquivo: ${filename}"
        mv /home/pedro/Workspace/Aeroscan/data/allModelsForDatasets/stepFiles/${filename} /home/pedro/Workspace/Aeroscan/data/allModelsForDatasets/fatal_error_files/
        break
    done
}

while [ true ]; do
    python /home/pedro/Workspace/Aeroscan/3DGeometryDatasetGenerator/dataset_generator.py /home/pedro/Workspace/Aeroscan/data/allModelsForDatasets/stepFiles/ /home/pedro/Workspace/Aeroscan/data/dataset_gmsh_v01/ -mg gmsh -nuhd -nud -ms 20
    retVal=$?
    if [ $retVal -eq 139 ]; then
        # segmentation fault = kill code 139
        my_problematic_files
    fi
    if [ $retVal -eq 0 ]; then
        break
    fi
done