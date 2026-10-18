

<!--
Title: Awesome Core ML Models
Description: A curated list of machine learning models in Core ML format.
Author: Kedan Li
-->
<p align="center">
<img src="images/coreml.png" width="329" height="295"/>
</p>


Since iOS 11, Apple released Core ML framework to help developers integrate machine learning models into applications. [The official documentation](https://developer.apple.com/documentation/coreml)

We've put up the largest collection of machine learning models in Core ML format, to help  iOS, macOS, tvOS, and watchOS developers experiment with machine learning techniques.

If you've converted a Core ML model, feel free to submit a [pull request](https://likedan/Awesome-CoreML-Models/compare).

Recently, we've included visualization tools. And here's one [Netron](https://lutzroeder.github.io/Netron).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://sindresorhus/awesome)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

# Models

## Image - Metadata/Text
*Models that take image data as input and output useful information about the image.*
* **TextDetection** - Detecting text using Vision built-in model in real-time. [Download]() | [Demo](https://tucan9389/TextDetection-CoreML) | [Reference](https://developer.apple.com/documentation/vision)
* **PhotoAssessment** - Photo Assessment using Core ML and Metal. [Download](https://yulingtianxia/PhotoAssessment/blob/master/PhotoAssessment-Sample/Sources/NIMANasnet.mlmodel) | [Demo](https://yulingtianxia/PhotoAssessment) | [Reference](https://arxiv.org/abs/1709.05424)
* **PoseEstimation** - Estimating human pose from a picture for mobile. [Download](https://edvardHua/PoseEstimationForMobile/tree/master/release) | [Demo](https://tucan9389/PoseEstimation-CoreML) | [Reference](https://edvardHua/PoseEstimationForMobile)
* **MobileNet** - Detects the dominant objects present in an image. [Download](https://hollance/MobileNet-CoreML/raw/master/MobileNet.mlmodel) | [Demo](https://hollance/MobileNet-CoreML) | [Reference](https://arxiv.org/abs/1704.04861)
* **Places CNN** - Detects the scene of an image from 205 categories such as bedroom, forest, coast etc. [Download](https://hollance/MobileNet-CoreML/raw/master/MobileNet.mlmodel) | [Demo](https://chenyi1989/CoreMLDemo) | [Reference](http://places.csail.mit.edu/index.html)
* **Inception v3** - Detects the dominant objects present in an image. [Download](https://yulingtianxia/Core-ML-Sample/blob/master/CoreMLSample/Inceptionv3.mlmodel) | [Demo](https://yulingtianxia/Core-ML-Sample/) | [Reference](https://arxiv.org/abs/1512.00567)
* **ResNet50** - Detects the dominant objects present in an image. [Download](https://ytakzk/CoreML-samples/blob/master/CoreML-samples/Resnet50.mlmodel) | [Demo](https://ytakzk/CoreML-samples) | [Reference](https://arxiv.org/abs/1512.03385)
* **VGG16** - Detects the dominant objects present in an image. [Download](https://docs-assets.developer.apple.com/coreml/models/VGG16.mlmodel) | [Demo](https://alaphao/CoreMLExample) | [Reference](https://arxiv.org/abs/1409.1556)
* **Car Recognition** - Predict the brand & model of a car. [Download](https://likedan/Core-ML-Car-Recognition/blob/master/Convert/CarRecognition.mlmodel) | [Demo](https://ytakzk/CoreML-samples) | [Reference](http://mmlab.ie.cuhk.edu.hk/datasets/comp_cars/index.html)
* **YOLO** - Recognize what the objects are inside a given image and where they are in the image. [Download](https://hollance/YOLO-CoreML-MPSNNGraph/blob/master/TinyYOLO-CoreML/TinyYOLO-CoreML/TinyYOLO.mlmodel) | [Demo](https://hollance/YOLO-CoreML-MPSNNGraph) | [Reference](http://machinethink.net/blog/object-detection-with-yolo)
* **AgeNet** - Predict a person's age from one's portrait. [Download](https://drive.google.com/file/d/0B1ghKa_MYL6mT1J3T1BEeWx4TWc/view?usp=sharing) | [Demo](https://cocoa-ai/FacesVisionDemo) | [Reference](http://www.openu.ac.il/home/hassner/projects/cnn_agegender/)
* **GenderNet** - Predict a person's gender from one's portrait. [Download](https://drive.google.com/file/d/0B1ghKa_MYL6mYkNsZHlyc2ZuaFk/view?usp=sharing) | [Demo](https://cocoa-ai/FacesVisionDemo) | [Reference](http://www.openu.ac.il/home/hassner/projects/cnn_agegender/)
* **MNIST** - Predict handwritten (drawn) digits from images. [Download](https://ph1ps/MNIST-CoreML/raw/master/MNISTPrediction/MNIST.mlmodel) | [Demo](https://ph1ps/MNIST-CoreML) | [Reference](http://yann.lecun.com/exdb/mnist/)
* **EmotionNet** - Predict a person's emotion from one's portrait. [Download](https://drive.google.com/file/d/0B1ghKa_MYL6mTlYtRGdXNFlpWDQ/view?usp=sharing) | [Demo](https://cocoa-ai/FacesVisionDemo) | [Reference](http://www.openu.ac.il/home/hassner/projects/cnn_emotions/)
* **SentimentVision** - Predict positive or negative sentiments from images. [Download](https://drive.google.com/open?id=0B1ghKa_MYL6mZ0dITW5uZlgyNTg) | [Demo](https://cocoa-ai/SentimentVisionDemo) | [Reference](http://www.sciencedirect.com/science/article/pii/S0262885617300355?via%3Dihub)
* **Food101** - Predict the type of foods from images. [Download](https://drive.google.com/open?id=0B5TjkH3njRqnVjBPZGRZbkNITjA) | [Demo](https://ph1ps/Food101-CoreML) | [Reference](http://visiir.lip6.fr/explore)
* **Oxford102** - Detect the type of flowers from images. [Download](https://drive.google.com/file/d/0B1ghKa_MYL6meDBHT2NaZGxkNzQ/view?usp=sharing) | [Demo](https://cocoa-ai/FlowersVisionDemo) | [Reference](http://jimgoo.com/flower-power/)
* **FlickrStyle** - Detect the artistic style of images. [Download](https://drive.google.com/file/d/0B1ghKa_MYL6meDBHT2NaZGxkNzQ/view?usp=sharing) | [Demo](https://cocoa-ai/StylesVisionDemo) | [Reference](http://sergeykarayev.com/files/1311.3715v3.pdf)
* **RN1015k500** - Predict the location where a picture was taken. [Download](https://s3.amazonaws.com/aws-bigdata-blog/artifacts/RN1015k500/RN1015k500.mlmodel) | [Demo](https://awslabs/MXNet2CoreML_iOS_sample_app) | [Reference](https://aws.amazon.com/blogs/ai/estimating-the-location-of-images-using-mxnet-and-multimedia-commons-dataset-on-aws-ec2)
* **Nudity** - Classifies an image either as NSFW (nude) or SFW (not nude)
 [Download](https://drive.google.com/open?id=0B5TjkH3njRqncDJpdDB1Tkl2S2s) | [Demo](https://ph1ps/Nudity-CoreML) | [Reference](https://yahoo/open_nsfw)
* **TextRecognition (ML Kit)** - Recognizing text using ML Kit built-in model in real-time. [Download]() | [Demo](https://tucan9389/TextRecognition-MLKit) | [Reference](https://firebase.google.com/docs/ml-kit/ios/recognize-text)
* **ImageSegmentation** - Segment the pixels of a camera frame or image into a predefined set of classes. [Download](https://developer.apple.com/machine-learning/models/) | [Demo](https://tucan9389/ImageSegmentation-CoreML) | [Reference](https://tensorflow/models/tree/master/research/deeplab)
* **DepthPrediction** - Predict the depth from a single image. [Download](https://developer.apple.com/machine-learning/models/) | [Demo](https://tucan9389/DepthPrediction-CoreML) | [Reference](https://iro-cp/FCRN-DepthPrediction)

## Image - Image
*Models that transform images.*
* **HED** - Detect nested edges from a color image. [Download](https://s1ddok/HED-CoreML/blob/master/HED-CoreML/Models/HED_so.mlmodel) | [Demo](https://s1ddok/HED-CoreML) | [Reference](http://dl.acm.org/citation.cfm?id=2654889)
* **AnimeScale2x** - Process a bicubic-scaled anime-style artwork [Download](https://imxieyi/waifu2x-ios/blob/master/waifu2x/models/anime_noise0_model.mlmodel) | [Demo](https://imxieyi/waifu2x-ios) | [Reference](https://arxiv.org/abs/1501.00092)

## Text - Metadata/Text
*Models that process text data*
* **Sentiment Polarity** - Predict positive or negative sentiments from sentences. [Download](https://cocoa-ai/SentimentCoreMLDemo/raw/master/SentimentPolarity/Resources/SentimentPolarity.mlmodel) | [Demo](https://cocoa-ai/SentimentCoreMLDemo) | [Reference](http://boston.lti.cs.cmu.edu/classes/95-865-K/HW/HW3/)
* **DocumentClassification** - Classify news articles into 1 of 5 categories. [Download](https://toddkramer/DocumentClassifier/blob/master/Sources/DocumentClassification.mlmodel) | [Demo](https://toddkramer/DocumentClassifier) | [Reference](https://toddkramer/DocumentClassifier/)
* **iMessage Spam Detection** - Detect whether a message is spam. [Download](https://gkswamy98/imessage-spam-detection/blob/master/MessageClassifier.mlmodel) | [Demo](https://gkswamy98/imessage-spam-detection/tree/master) | [Reference](http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/)
* **NamesDT** - Gender Classification using DecisionTreeClassifier [Download](https://cocoa-ai/NamesCoreMLDemo/blob/master/Names/Resources/NamesDT.mlmodel) | [Demo](https://cocoa-ai/NamesCoreMLDemo) | [Reference](http://nlpforhackers.io/)
* **Personality Detection** - Predict personality based on user documents (sentences). [Download](https://novinfard/profiler-sentiment-analysis/tree/master/ios_app/ProfilerSA/ML%20Models) | [Demo](https://novinfard/profiler-sentiment-analysis/) | [Reference](https://novinfard/profiler-sentiment-analysis/blob/master/dissertation-v6.pdf)
* **BERT for Question answering** - Swift Core ML 3 implementation of BERT for Question answering [Download](https://huggingface/swift-coreml-transformers/blob/master/Resources/BERTSQUADFP16.mlmodel) | [Demo](https://huggingface/swift-coreml-transformers#-bert) | [Reference](https://huggingface/pytorch-transformers#run_squadpy-fine-tuning-on-squad-for-question-answering)
* **GPT-2** - OpenAI GPT-2 Text generation (Core ML 3) [Download](https://huggingface/swift-coreml-transformers/blob/master/Resources/gpt2-512.mlmodel) | [Demo](https://huggingface/swift-coreml-transformers#-gpt-2) | [Reference](https://huggingface/pytorch-transformers)
## Miscellaneous
* **Exermote** - Predicts the exercise, when iPhone is worn on right upper arm. [Download](https://Lausbert/Exermote/tree/master/ExermoteInference) | [Demo](https://Lausbert/Exermote/tree/master/ExermoteInference) | [Reference](http://lausbert.com/2017/08/03/exermote/)
* **GestureAI** - Recommend an artist based on given location and genre. [Download](https://goo.gl/avdMjD) | [Demo](https://akimach/GestureAI-CoreML-iOS) | [Reference](https://akimach/GestureAI-iOS/tree/master/GestureAI)
* **Artists Recommendation** - Recommend an artist based on given location and genre. [Download](https://agnosticdev/Blog-Examples/blob/master/UsingCoreMLtoCreateASongRecommendationEngine/Artist.mlmodel) | [Demo]() | [Reference](https://www.agnosticdev.com/blog-entry/python/using-scikit-learn-and-coreml-create-music-recommendation-engine)
* **ChordSuggester** - Predicts the most likely next chord based on the entered Chord Progression. [Download](https://carlosmbe/Mac-CoreML-Chord-Suggester/blob/main/MLChordSuggester.mlpackage.zip) | [Demo](https://carlosmbe/Mac-CoreML-Chord-Suggester/tree/main) | [Reference](https://medium.com/@huanlui/chordsuggester-i-3a1261d4ea9e)

## Speech Processing
* **Streaming ASR** – Real-time streaming speech recognition engine for iOS. Uses Fast Conformer + CTC, runs fully on device.  
  [Download](https://Otosaku/OtosakuStreamingASR-iOS/releases) | [Demo](https://Otosaku/OtosakuStreamingASR-iOS) | [Reference](https://Otosaku/OtosakuStreamingASR-iOS)
* **Keyword Spotting (KWS)** – On-device keyword spotting engine using lightweight CRNN architecture, optimized for mobile devices.  
  [Download](https://Otosaku/OtosakuKWS-iOS/releases) | [Demo](https://Otosaku/OtosakuKWS-iOS) | [Reference](https://Otosaku/OtosakuKWS-iOS)

# Visualization Tools
*Tools that help visualize CoreML Models*
* [Netron](https://lutzroeder.github.io/Netron)

# Supported formats
*List of model formats that could be converted to Core ML with examples*
* [Caffe](https://apple.github.io/coremltools/generated/coremltools.converters.caffe.convert.html)
* [Keras](https://apple.github.io/coremltools/generated/coremltools.converters.keras.convert.html)
* [XGBoost](https://apple.github.io/coremltools/generated/coremltools.converters.xgboost.convert.html)
* [Scikit-learn](https://apple.github.io/coremltools/generated/coremltools.converters.sklearn.convert.html)
* [MXNet](https://aws.amazon.com/blogs/ai/bring-machine-learning-to-ios-apps-using-apache-mxnet-and-apple-core-ml/)
* [LibSVM](https://apple.github.io/coremltools/generated/coremltools.converters.libsvm.convert.html)
* [Torch7](https://prisma-ai/torch2coreml)

# The Gold
*Collections of machine learning models that could be converted to Core ML*

* [Caffe Model Zoo](https://BVLC/caffe/wiki/Model-Zoo) - Big list of models in Caffe format.
* [TensorFlow Models](https://tensorflow/models) - Models for TensorFlow.
* [TensorFlow Slim Models](https://tensorflow/models/tree/master/research/slim/README.md) - Another collection of TensorFlow Models.
* [MXNet Model Zoo](https://mxnet.incubator.apache.org/model_zoo/) - Collection of MXNet models.

*Individual machine learning models that could be converted to Core ML. We'll keep adjusting the list as they become converted.*
* [LaMem](https://MiyainNYC/Visual-Memorability-through-Caffe) Score the memorability of pictures.
* [ILGnet](https://BestiVictory/ILGnet) The aesthetic evaluation of images.
* [Colorization](https://richzhang/colorization) Automatic colorization using deep neural networks.
* [Illustration2Vec](https://rezoo/illustration2vec) Estimating a set of tags and extracting semantic feature vectors from given illustrations.
* [CTPN](https://tianzhi0549/CTPN) Detecting text in natural image.
* [Image Analogy](https://msracver/Deep-Image-Analogy) Find semantically-meaningful dense correspondences between two input images.
* [iLID](https://twerkmeister/iLID) Automatic spoken language identification.
* [Fashion Detection](https://liuziwei7/fashion-detection) Cloth detection from images.
* [Saliency](https://imatge-upc/saliency-2016-cvpr) The prediction of salient areas in images has been traditionally addressed with hand-crafted features.
* [Face Detection](https://DolotovEvgeniy/DeepPyramid) Detect face from image.
* [mtcnn](https://CongWeilin/mtcnn-caffe) Joint Face Detection and Alignment.
* [deephorizon](https://scottworkman/deephorizon) Single image horizon line estimation.

# Contributing and License
* [See the guide](https://likedan/Awesome-CoreML-Models/blob/master/.github/CONTRIBUTING.md)
* Distributed under the MIT license. See LICENSE for more information.
