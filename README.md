# CSE 527: Intro to Computer Vision | Final Project
## Topic: Class-agnostic counting using a similarity-aware framework
Final project source code for CSE 527 : Intro to Computer Vision (modified from https://github.com/flyinglynx/Bilinear-Matching-Network/tree/main)

Project Member: Anujay Ghosh
Supervisor: Jingyi Xu
Instructor: Prof. Dimitris Samaras

Dataset Preparation:
Path structure used in our code will be like :
````

checkpoints
├────bmnet+_ep3_epoch300
├────bmnet+_ep3_epoch300_2
├────bmnet+_ep3_epoch300_3
PATH_TO_FSC147_DATASET
├──── gt_density_map_adaptive_384_VarV2
│    ├──── 6146 density maps (.npy files)
│    
├──── images_384_VarV2
│    ├──── 6146 images (.jpg)
│ 
├────annotation_FSC147_384.json (annotation file)
├────ImageClasses_FSC147.txt (category for each image)
├────Train_Test_Val_FSC_147.json (official data splitation file, which is not used in our code)
├────train.txt (We generate the list from official json file)
├────val.txt
├────test.txt

````

Execution of Model: 
````
    cd CODE_DIRECTORY
    python train.py --cfg 'config/{configuration_file_name}.yaml'
````

Integration of Dot Annotations:
Please use the following table to run the commands and replace the config files as necessary:
|Total Exemplars|OG BB| Pseudo BB|Test| |Val| |Model Checkpoint|Config| | |
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
| | | |MAE|MSE|MAE|MSE| |Training|Testing|Validation|
|4|3|3|17.78|100.69|15.76|53.98|bmnet+_ep3_epoch300_3|bmnet+_fsc147_3.yaml|test_bmnet+fsc147_3.yaml|val_bmnet+fsc147_3.yaml|
|5|3|2|16.63|96.36|15.75|55.25|bmnet+_ep3_epoch300_2|bmnet+_fsc147_2.yaml|test_bmnet+fsc147_2.yaml|val_bmnet+fsc147_2.yaml|
|6|3|1|16.41|95.41|16.23|54.25|bmnet+_ep3_epoch300|bmnet+_fsc147.yaml|test_bmnet+fsc147.yaml|val_bmnet+fsc147.yaml|


