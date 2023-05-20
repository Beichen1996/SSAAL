<h1> Structural Semantic Adversarial Active Learning for Image
Captioning</h1>



<h2> Requirements </h2>

GPU设备，支持CUDA9.5以上<br>

 torch >= 1.6.0
 torchvision >= 0.9.1
 numpy == 1.19.2
 tqdm >= 4.31.1
 Pillow == 8.0.1
 matplotlib == 3.3.2
 scipy == 1.5.2
 seaborn >= 0.11.0
 scikit-learn == 0.23.2
 six == 1.15.0
 h5py == 2.8
 nltk == 3.3

<h2> Data preparation </h2>

Create a folder called 'data'

Create a folder called 'final_dataset'

Download the MSCOCO <a target = "_blank" href="http://images.cocodataset.org/zips/train2014.zip">Training</a> (13GB)  and <a href=http://images.cocodataset.org/zips/val2014.zip>Validation</a> (6GB)  images. 

Also download Andrej Karpathy's <a target = "_blank" href=http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip>training, validation, and test splits</a>. This zip file contains the captions.

Unzip all files and place the folders in 'data' folder.

<br>

Next, download the <a target = "_blank" href="https://imagecaption.blob.core.windows.net/imagecaption/trainval_36.zip">bottom up image features</a>.

Unzip the folder and place unzipped folder in 'bottom-up_features' folder.  

<br>

Next type this command in a python 2 environment: 
```bash
python bottom-up_features/tsv.py
```

This command will create the following files - 
<ul>
<li>An HDF5 file containing the bottom up image features for train and val splits, 36 per image for each split, in an I, 36, 2048 tensor where I is the number of images in the split.</li>
<li>PKL files that contain training and validation image IDs mapping to index in HDF5 dataset created above.</li>
</ul>

Move these files to the folder 'final_dataset'.

<br>

Next, type this command: 
```bash
python create_input_files.py
```

This command will create the following files - 
<ul>
<li>A JSON file for each split containing the order in which to load the bottom up image features so that they are in lockstep with the captions loaded by the dataloader.</li>
<li>A JSON file for each split with a list of N_c * I encoded captions, where N_c is the number of captions sampled per image. These captions are in the same order as the images in the HDF5 file. Therefore, the ith caption will correspond to the i // N_cth image.</li>
<li>A JSON file for each split with a list of N_c * I caption lengths. The ith value is the length of the ith caption, which corresponds to the i // N_cth image.</li>
<li>A JSON file which contains the word_map, the word-to-index dictionary.</li>
</ul>

<br>

Next, go to nlg_eval_master folder and type the following two commands:
```bash
pip install -e .
nlg-eval --setup
```
This will install all the files needed for evaluation.

<h2> Training </h2>

Run the following script to training the active learning model and select samples, the ratio of selected sample is in the last of the script:
```bash
python train.py 2
```
With this script, you can get the 2% active learning selection, then you can run the following scripts to select 3% to 9% samples:
```bash
python train.py 3
python train.py 4
...
python train.py 9 
```
The training results of the selected samples are stored in ./$selection_ratio$, $selection_ratio$ = {2,3,4,5,6,7,8,9}.


<h2> Evaluation </h2>

To evaluate the selection, run the following script. please set the ratio of selected sample and train epoch in the script:
```bash
python eval.py 2 40
```
This script will evaluate the 2% selected samples in 40 epoch. The epoch number please refer to the filename under ./$selection_ratio$
Then, you can run the following scripts to test 3% to 9% samples:
```bash
python eval.py 3 40
python eval.py 4 40
...
python eval.py 9 40
```
