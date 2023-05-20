# 基于对抗式结构化语义构建的主动学习算法

## 1. 算法描述
在跨模态场景下针对图像描述任务的主动学习，利用目标检测模型提取视觉模态的关键区域特征，通过关键词表对描述文本进行细粒度建模，学习文本模态的结构化表征，并利用该表征在粗粒度重建中更新表征学习部分，最终通过对抗判别机制选取语义多样且具备高标注价值的跨模态样本进行标注，显著提升主动学习的采样质量和目标性能。

## 2. 环境依赖及安装
该框架所需的环境依赖如下：

- torch >= 1.6.0
- torchvision >= 0.9.1
- numpy == 1.19.2
- tqdm >= 4.31.1
- Pillow == 8.0.1
- matplotlib == 3.3.2
- scipy == 1.5.2
- seaborn >= 0.11.0
- scikit-learn == 0.23.2
- six == 1.15.0
- h5py == 2.8
- nltk == 3.3

建议使用anaconda或pip配置环境。例如：
```
pip install numpy==1.19.2
pip install tqdm==4.31.1
pip install torch==1.6.0
pip install torchvision == 0.9.1
...
```

## 3. 运行示例

### 代码准备

1. 创建文件夹 'data' 和 'final_dataset'
```
mkdir data final_dataset
```

2. 下载数据
```
wget http://images.cocodataset.org/zips/train2014.zip
wget http://images.cocodataset.org/zips/val2014.zip
mv ./*.zip ./data/
wget http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip
mv ./*.zip ./bottom-up_features/
cd ./data/ ; unzip "*.zip"
cd ../bottom-up_features/ ; unzip "*.zip"
python tsv.py; cp ./*.* ../final_dataset/
cd ..; python create_input_files.py
```

3. 安装测试工具
```
cd nlg_eval_master
pip install -e .
nlg-eval --setup
```


### 3. 模型训练
运行以下的脚本，可以训练主动学习模型，挑选样本，样本选择的比例在脚本中设置。

1. 依次运行以下的代码，得到2%到9%的采样结果，训练采样结果会存储在./$selection_ratio$ 文件夹下，其中$selection_ratio$表示采样的比例，取值范围为{2,3,4,5,6,7,8,9}：
```
python train.py 2
python train.py 3
...
python train.py 9 
```

2. 运行以下代码，测试2到9的采样比例的结果。其中，epoch请分别参考对应的采样比例文件夹下的模型的训练epoch：
```bash
python eval.py 2 40
python eval.py 3 40
...
python eval.py 9 40
```



## 4. 论文/专利成果
> Beichen Zhang, Liang Li, Li Su, Shuhui Wang, Jincan Deng, Zheng-Jun Zha and Qingming Huang. Structural Semantic Adversarial Active Learning for Image Captioning. ACM MM 2020 (Oral)



