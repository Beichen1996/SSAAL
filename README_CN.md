<h1> Structural Semantic Adversarial Active Learning for Image
Captioning</h1>



<h2> 需求 </h2>

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

<h2> 数据准备 </h2>

创建文件夹，名字为 'data'

创建文件夹，名字为 'final_dataset'


下载MSCOCO <a target = "_blank" href="http://images.cocodataset.org/zips/train2014.zip">训练集  </a> (13GB)和 <a href=http://images.cocodataset.org/zips/val2014.zip>测试集 </a>(6GB)。

下载Andrej Karpathy的<a target = "_blank" href=http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip>训练集和验证集</a>。


解压上述文件，并放置在'data'文件夹下。
<br>

之后，下载<a target = "_blank" href="https://imagecaption.blob.core.windows.net/imagecaption/trainval_36.zip">bottom up</a>特征。

将其解压后，放置在'bottom-up_features' 文件夹。

<br>

在python2环境下运行以下命令：
```bash
python bottom-up_features/tsv.py
```

该命令会创造以下文件 - 
<ul>
<li>一个HDF5文件，包含训练测试的图像特征，每张图片36个特征</li>
<li>PKL 文件，其中包含训练测试文件的图片id。</li>
</ul>

将这些产生的文件转移到 'final_dataset'文件夹.

<br>

运行以下命令: 
```bash
python create_input_files.py
```

该命令会创造四个JSON文件，分别包含index，编码的caption，caption长度，wordtoindex的字典。


<br>

之后，去nlg_eval_master文件夹下，输入以下命令，安装测试工具：
```bash
pip install -e .
nlg-eval --setup
```
这将会安装所有测试所需的工具。

<h2> 训练 </h2>

运行以下的脚本，可以训练主动学习模型，挑选样本，样本选择的比例在脚本中设置：
```bash
python train.py 2
```
使用上述脚本，可以得到2%的主动学习采样结果，之后可以依次运行以下的脚本，得到3%到9%的采样结果：
```bash
python train.py 3
python train.py 4
...
python train.py 9 
```

训练采样结果会存储在./$selection_ratio$ 文件夹下，其中$selection_ratio$表示采样的比例，取值范围为{2,3,4,5,6,7,8,9}。

<h2> 性能验证 </h2>

为了进行性能测试，运行以下的脚本。在脚本中依次输入采样比例和训练模型的epoch：
```bash
python eval.py 2 40
```

该脚本将会验证2%采样在40epoch训练下的性能。epoch的设置，请参考./$selection_ratio$ 文件夹下存储的模型的训练epoch。


之后，可以运行以下的脚本，测试3到9的采样比例的结果。其中，epoch请分别参考对应的采样比例文件夹下的模型的训练epoch：
```bash
python eval.py 3 40
python eval.py 4 40
...
python eval.py 9 40
```
