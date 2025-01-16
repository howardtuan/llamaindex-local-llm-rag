Contents lists available at ScienceDirect

Biomedical Signal Processing and Control

journal homepage: www.elsevier.com/locate/bspc

Enhanced-TransUNet for ultrasound segmentation of thyroid nodules
Alper Ozcan a, Ömür Tosun b,∗, Emrah Donmez c, Muhammad Sanwal a
a Akdeniz University, Department of Computer Engineering, Turkey
b Akdeniz University, Department of Management Information Systems, Turkey
c Bandirma Onyedi Eylul University, Department of Software Engineering, Turkey

A R T I C L E I N F O

A B S T R A C T

Keywords:
Artificial learning
Deep learning
Image processing
Thyroid nodule segmentation
Ultrasound image segmentation

Medical image segmentation plays a key role in the early diagnosis and treatment of medical diseases. Thyroid
nodule segmentation is a critical step in early thyroid cancer identification. Accurately segmenting thyroid
nodule areas from ultrasound images is critical for clinical diagnosis and maintaining good health. Because
of the fragile borders of ultrasound images and the complicated structure of thyroid tissue, it is difficult
to correctly separate the delicate outlines of thyroid nodules to provide adequate segmentation findings,
since they either cannot establish exact edges or segment smaller parts. The segmentation of thyroid nodule
images presents some fundamental difficulties. First, the intrinsic locality of convolutional neural network
models places constraints on their ability to capture information about the whole context. Second, the size of
the data sets used for thyroid nodule segmentation frequently makes overfitting more likely. Finally, low-
level characteristics that are important in displaying thyroid borders eventually disappear throughout the
feature encoding process. We provide an effective model called Enhanced-TransUNet for thyroid nodule image
segmentation to overcome these difficulties. The Transformer and UNet concepts are combined in Enhanced-
TransUNet. While the UNet can successfully segregate tiny items, the Transformer can collect information about
the overall environment. In order to condense superfluous characteristics and lower the chance of overfitting,
Enhanced-TransUNet also makes use of an information bottleneck. Comparing our model to contemporary CNN
or UNET based models, experimental findings on the TN3K and DDTI datasets for brain tumor segmentation
tasks show that our model gets equivalent or better results. For the two datasets, the average Dice Score and
HD95 are 82.92, 95.45, and 13.19, 1.09, respectively. Overall, the Enhanced-TransUNet model for thyroid
nodule image segmentation is promising. Even with weak edges and a complicated tissue structure, it can
precisely segment thyroid nodules in ultrasound pictures. Due to its usage of the information bottleneck,
Enhanced-TransUNet is also less prone to overfitting than other models. As a result, an AI-based decision
support system based on this model can be built to reduce workload and misdiagnosis. This system has
significant potential for clinical application by radiologists and surgeons, which can increase clinical diagnostic
accuracy and efficiency.

1. Introduction

The thyroid is located just below the cartilage structure, which
reveals itself with its butterfly-like structure, moves up and down with
swallowing. The thyroid is responsible for the production of hormones
that regulate many functions in the body. The regularity of thyroid
gland functions, which is very important for body health, affects almost
all metabolic processes in the body. The most known of the thyroid
disorders is the formation of nodules. Although a significant portion of
thyroid nodules are benign, it is an important disorder that should be
diagnosed early, as it carries various risks, including cancer.

Today, the use of computer-aided systems in the field of health
is becoming more and more widespread. These systems, as a deci-
sion support system, can provide the specialist physician with the
opportunity to evaluate and diagnose faster. In these systems, machine
learning approaches are generally used. Machine learning approaches
have evolved from machine learning to deep learning methods that
provide more detailed learning. Deep learning accurately processes fea-
tures in a multi-layered network structure instead of traditional feature
extraction approaches in machine learning. Thus, it is possible to obtain
high-level features that better represent the data. Convolutional neural

∗ Corresponding author.

E-mail addresses: alperozcan@akdeniz.edu.tr (A. Ozcan), omurtosun@akdeniz.edu.tr (Ö. Tosun), emrahdonmez@bandirma.edu.tr (E. Donmez),

202151075006@ogr.akdeniz.edu.tr (M. Sanwal).

https://doi.org/10.1016/j.bspc.2024.106472
Received 18 September 2023; Received in revised form 5 March 2024; Accepted 15 May 2024

BiomedicalSignalProcessingandControl95(2024)106472Availableonline24May20241746-8094/©2024ElsevierLtd.Allrightsarereserved,includingthosefortextanddatamining,AItraining,andsimilartechnologies.A. Ozcan et al.

networks (CNN), one of the deep learning methods, are used on image
data. CNN models are also a very efficient approach that can be used on
health image data. In this study, it was aimed to segment the thyroid
nodules in the image with U-Net, which is a CNN-based segmentation
network, using a dataset consisting of thyroid ultrasound images and
masks.

Thyroid nodules are abnormal lumps or masses of different struc-
tures and sizes that occur within the thyroid tissue. Thyroid nodule is a
condition that is usually seen in advanced ages. Although most of these
nodules are harmless and benign, they also carry various health risks.
These risks include pressure on the trachea due to excessive enlarge-
ment, hyperthyroidism caused by excessive hormone production as a
result of autonomous work, and cancerization. For all these reasons,
an accurate diagnosis of a thyroid nodule in the early stages is an
important issue.

Considering its success in the field of health, the use of computer de-
cision support systems in the detection of thyroid nodules can produce
effective results. Recently, it is seen that convolutional neural networks
have been used more frequently in these systems.

Because of their powerful feature extraction capabilities and capac-
ity for adaptive learning, convolutional neural networks (CNNs) are an
excellent choice for segmenting medical images. The application of seg-
mentation models based on full convolutional neural networks (FCNs),
as proposed by [1], has been shown to yield substantial enhancements
in the outcomes of medical picture segmentation. However, it is crucial
to acknowledge that FCNs, although efficient, may occasionally provide
ambiguous boundaries in their segmentation results due to the upscal-
ing procedure, resulting in a reduction of precise high-level semantic
details.

In the literature U-NET architecture is known for its superiority in
the image classification tasks [2]. It is renowned for its capacity to use
skip links to combine semantic and geographical information. Skip con-
nections enable the U-Net to learn both low-level texture information
and high-level semantic properties. This is crucial for medical picture
segmentation because it enables the model to recognize items in the
image properly while still maintaining their spatial connections [3].
Numerous elements contribute to the U-Net architecture’s success.
First, the model can learn both high-level and low-level characteristics
because of the usage of skip connections. Second, the symmetry of the
U-Net architecture facilitates training and generalization. Third, the
U-Net design is rather straightforward deploy.

By adding additional features, several academics have attempted to
enhance the U-Net design. To gain more discriminative characteristics,
U-Net++ [4] employs a hierarchical design and dense skip connections.
Attention techniques are used by U-Net [5] and Channel U-Net [6]
to improve the discriminative features obtained from the encoder and
decoder, respectively. An attention-guided upsampling module is sug-
gested by AUNet [7] to enhance the skip connection process, which
eliminates extraneous spatial information and closes the semantic gap.
In the processing of medical images nowadays, U-shaped models
are frequently employed [8–12]. The inclusion of skip connections is
crucial to their success, as it facilitates the integration of lower-level
feature maps obtained from the encoder, as discussed by [4], with
higher-level feature maps generated by the decoder. The recollection
of accurate information regarding target objects is facilitated by this
distinctive combination, even in the presence of complex backgrounds,
as elucidated by [13].

However, the CNN-derived UNet model has trouble capturing global
contextual variables. This is due to the restrictions of the convolution
process it employs [14]. The size of the kernel affects how localized the
focus is, and a convolution kernel in the UNet model can only focus on
a tiny local region. The lower and middle layers still struggle to capture
global features and are restricted to localized locations, despite the
UNet model’s ability to extend the reach of the convolution kernel by
adding more convolution layers, enabling higher layers to concentrate
on global features. The Transformer model works effectively when

taking into account information from a broad context. The Transformer
is being used as an encoder in research on medical picture segmentation
as a consequence.

In comparison to CNNs, Transformers have a distinctive capability
to efficiently gather comprehensive contextual information at a global
level, while also accurately identifying detailed local features. The
increasing significance of Transformers in the domain of NLP has
motivated scholars to investigate their potential utilization in the field
of computer vision. The Vision Transformer (ViT) is an architectural
breakthrough in the field, as evidenced by the work of [15], as it
only utilizes self-attention processes. The Vision Transformer (ViT) has
demonstrated exceptional performance in image identification tasks,
surpassing current state-of-the-art approaches. Subsequently, Trans-
formers have consistently demonstrated their exceptional skills in a
range of computer vision applications.

In order to leverage the benefits of global context modeling and
in-depth knowledge acquisition, scholars have embarked on the inte-
gration of U-Net and Transformer models. The integration described
in this context improves the functionality of the encoder by combining
the local characteristics obtained from the CNN module with the global
dependencies obtained from the Transformer module. The efficacy of
this methodology has attracted considerable interest, as evidenced by
many extensive investigations, as cited in [14].

Vision transformers have rapidly gained popularity as they enable
to model the context of images by establishing long-term relationships.
Nevertheless, the transformers do not apply convolution and only
use the global attention mechanisms since they are computationally
expensive which is not suitable for medical image processing tasks.
Transformers have issues in acquiring fine details of medical images,
which most of the approaches of today seem to ignore. Considering a
to-state discriminant data mining, optimization allows getting the most
of the information. To solve this, some experiments have combined
attributes of convolutional neural networks (CNN) and transformers
to capture both spatial and global features while using fewer param-
eters when being applied to medical image processing. It is the latest
discovery that the consideration of the frame of the whole medical
image is more clarified when applying the Transformer in models
like TransUnet [14] and TransAttUnet [16]. This assists in detecting
lesions that express their form and have more relevant and specific
characteristics, thus leading to more precise and extensive findings.

Generally, there are many approaches to thyroid ultrasound image
segmentation, but there is no one-size-fits-all model. As a result, it is
crucial to apply the best method for the unique situation and condition.
There are many ways the application can be employed depending on
sample size, time cost, accuracy, autonomy and model size.

This study is motivated by two points. Firstly, it is very hard
to tackle the blurred boundaries of ultrasound images. Secondly, the
classical UNet architecture has the deficiency of small object sensibility.
In order to find small targets more precisely, multi-scale representation
and contextual information are the main aspects of this paper. Our main
goal is to extract data from pictures to improve model’s localization
and, at the end, to achieve better lesion segmentations.

In this paper, we present Enhanced-TransUNet, a novel segmenta-
tion model created especially for the detection of thyroid nodules. Four
major contributions are made in this paper:

(i) To properly separate thyroid nodules in ultrasound pictures,
we provide a novel segmentation model called Enhanced-Tran-
sUNet.

(ii) Integrate vision transformers with UNet structure to increase its

efficiency on segmentation problems.

(iii) When compared to current state-of-the-art techniques for seg-
menting thyroid nodules, Enhanced-TransUNet shows promising
segmentation accuracy and works well on image segmentation.
(iv) We present a thorough assessment of the proposed model TN3K
data set, demonstrating its efficacy through both qualitative
analysis and numerical measures.

BiomedicalSignalProcessingandControl95(2024)1064722A. Ozcan et al.

The subsequent parts of this paper are organized in the following
structural arrangement: In Section 2, a comprehensive review of the
relevant literature is presented. Sections 3 and 4 provide an in-depth
analysis of the process, including a thorough and detailed explana-
tion. Sections 5 and 6 are devoted to a comprehensive analysis of
the experimental findings, whilst Section 7 enlightens the practical
implications and future scope of the study. Finally Section 8 constitutes
the concluding section of this work.

2. Related work

The literature review highlights various studies for segmentation
techniques, concentrating specifically on the medical field, and net-
works like U-Net and SegNet are frequently used for this purpose.
The importance of segmentation in health image analysis has been
acknowledged widely in the research area, especially for detecting
thyroid nodules. Accurate, manual measurements by specialists are
time-consuming. This has driven research into autonomous segmenta-
tion systems for health images. Notable among these is the Transformer
U-Net proposed by Yan et al. [17], which merges convolutional lay-
ers (feature), and transformers’ long-sequence modeling equipment. It
promises parametric compactness and conservation of GPU memory.
Maji et al. [18] suggested an early generator design with custom
loss functions. They also implemented attention gates to the decoders
to privilege learning features and design better mapping. Further-
more, Wang et al. [19] investigated the use of Vision Transformer
(ViT) in semantic segmentation for medical images. The methodology
employed by the researchers includes the application of sophisticated
Semi-Supervised Learning (SSL) methodologies, including MixUp-based
interpolation consistency training and the incorporation of adversarial
training. Furthermore, Sagar [20] proposed a Vision Transformer for
biomedical image segmentation. The encoder and decoder components
of the network use convolutions of varying sizes (1 × 1, 3 × 3, and
5 × 5) to split the input feature maps in which features are merged
using the concatenation operator and then fed into three transformer
blocks with attention mechanisms. Skip connections are used to connect
the transformer blocks in the encoder and decoder sections.

Azad et al. [21] have introduced a Trans-Norm framework that
is based on the standard UNET models encoder and skip connec-
tions. To fuse features from the expanding and contracting routes,
strong skip connections are used for segmentation. Liu et al. [22] pre-
sented a TransUNet+ framework for medical image segmentation that
uses a modified skip connection including an enhancement module,
which boosts the skip features by employing the transformer block’s
score matrix. This modification leads to improved global attention.
IB-TransUNet Li et al. [23] integrates Transformer and information
bottlenecks into the UNet paradigm. This framework can extract crucial
contextual data from a wider region resulting in better accuracy.

Further, Vadhiraj et al. [24] conducted research to identify benign
or malignant thyroid nodules. It uses a median filter and image bi-
narization to preprocess and segment the images, and the grey-level
co-occurrence matrix (GLCM) is utilized to extract specific features
from the ultrasound images which results in better accuracy. Nguyen
et al. [25] used enhancement segmentation networks to improve the
accuracy. Tao et al. [26] utilized a context-attention module based
on transformers to tackle the problem of low-clarity images around
the edges. The proposed method can gather more comprehensive as-
sociative information for the network, helping to capture the edge
details of the nodule contour. Moreover, Gong et al. [27] proposed
Thyroid Region Prior Guided Feature Enhancement Network (TRFE+)
to correctly segment thyroid nodules where the network has insufficient
prior knowledge about the particular location of the thyroid gland. This
method utilizes a normalization method that considers the channel size
as well as an adaptive module to improve attributes connected to the
gland area.

Convolutional operations are pivotal in computer vision problems
that offer contextual understanding and resilience in changing postures.
UNet has emerged as a promising segmentation method that employs
skip connections to capture long-range relationships to preserve the
information which is a prominent problem in CNN models [14]. The
problem arises in the convolutional process which fundamentally pri-
oritizes localized regions limiting its ability to capture global features
effectively. Despite the considerable achievements of the U-Net archi-
tecture, there exists an opportunity for enhancing the performance
of segmentation. The lack of enough attention given to the semantic
gap between the encoding and decoding stages is responsible for this
phenomenon. The presence of a semantic gap poses a challenge to
the seamless integration of features, which is crucial for successful
object identification. Deep-level characteristics are essential for this
integration, whereas low-level traits are particularly important for edge
segmentation. Identifying these efficacious characteristics, despite the
inherent difficulties, results in notable progress, as expounded upon
by [28].

Transformers were first utilized to create text-based models, and as
a result of their success, they are also employed for image processing
tasks [14]. The input to Transformer models (comprising different
blocks) is often a series of vectors that are embeddings of input tokens.
Each block consists of two primary parts: (1) a multi-head self-attention
layer that uses dot-product attention to acquire data from various
tokens in the sequence. This aids the model’s comprehension of the
connections and interdependence among the various input components.
(2) an MLP, or token-wise feed-forward layer, which treats each token
separately and performs modifications. To provide reliable and efficient
processing of the input sequence, this layer combines layer normaliza-
tion and residual connections. The basic architecture of the Transformer
is a feed-forward module that converts features into a latent space and
a self-attention module that records long-range relationships. The input
data in the Transformer technique consists of tokenized segments of the
picture, which are derived from feature maps of a convolutional neural
network. This strategy is elaborated by [29]. The decoder assumes a
critical function in enhancing the resolution of the encoded characteris-
tics and integrating them with the high-resolution CNN feature maps to
get accurate localization. In contrast, Transformers employ a methodol-
ogy wherein they examine data as 1D sequences and give precedence to
the aggregation of global context across all phases. The prioritization
of global context results in the production of low-resolution features
that exhibit a deficiency in exact localization details. Unfortunately, the
act of only augmenting the resolution by upsampling does not possess
the capability to restore the missing data, hence leading to fragmented
outputs that exhibit a deficiency in intricate particulars. As argued
by [14], the exclusive reliance on the Transformer mechanism leads
to unsatisfactory outcomes.

Transformers need a large amount of data to pre-train, which might
be problematic for datasets with less data. Vision Transformers (ViTs)
can now perform effectively on limited datasets [28] as [30] introduced
an effective training technique and knowledge distillation. Transform-
ers served as the basis for ViTs, however, the picture pre-processing
layer is significantly different. The photos are first divided into a
number of separate, non-overlapping sections. Then, each patch is
subjected to a learned linear projection. A series of tokens are produced
as a consequence, which are supplied to the Transformer. To categorize
the picture, the Transformer computes global information between each
token [15]. The number of filters used in the procedure, which uses
a 2D convolution, defines the hidden size of the sequence fed to the
Transformer.

Trans-UNET is a novel paradigm that combines transformers with
the U-NET architecture [14]. By utilizing skip connections between
appropriate layers, the U-NET design is renowned for its capacity to
enhance local features in feature maps. TransUNet is the first effective
attempt to segment medical imaging using the Transformer, a potent
neural network design. The Transformer takes the input as a collection

BiomedicalSignalProcessingandControl95(2024)1064723A. Ozcan et al.

Table 1
An overview of the medical image segmentation methods.

Study

Method

Strengths

Weaknesses

Proposed model

[2]

[31]

[4]

[32]

[5]

[33]

[14]

[34]

[35]

[36]

Enhanced UNet with
transformers
UNet

Skip connections Vision transformers Better IoU

Easy to implement and produces high accuracy

Residual UNet

UNet++

UNet with
Transformers
Attention UNet

UNet 3+

TransUNet

SGUNet

H-TUNet

SK-Unet++

More easy to train than UNet and also can increase
the depth of UNet
Better segmentation accuracy using a nested
architecture
Uses transformer block to model the long-range
contextual information of input images
Associates the information of salient maps with
feature maps
Improves the segmentation performance of Unet and
Unet++ with full-scale skip connections
Addition of transformers retaining higher-resolution
feature maps capturing distant spatial interactions
utilization of skip connections
Utilization of encoder–decoder network pixel-wise
semantic map for high-level semantic capturing
Improved accuracy
Combination of 2D and 3D Transformer UNets
Integration of multi-scale cross-attention transformer
(MSCAT) intra-frame feature extraction and
inter-frame feature aggregation
Usage of the selective kernel (SK) attention
mechanisms Replacement of original UNet++ encoder
blocks with fine-tuned SK convolution blocks Usage of
skip connections

Require large amounts of computational resources
Longer training time
Optimal depth of the network architecture is hard to
define
Optimal depth of the network architecture is hard to
define
Longer training time due to complex network
architecture
Longer training time due to complex network
architecture
Salient map is learned with complex method

Longer training time due to complex network
architecture
Potential decrease in segmentation accuracy
complexity and computational cost

High noise and blurry nodule boundaries Dependence
on the quality of image

Loss of low-level features during feature encoding
Weak representation of contextual features

Enhanced segmentation accuracy Better performance

of data and can produce feature maps that are smaller than those in the
original picture, which could lower segmentation accuracy. TransUNet
uses a combination of CNN and Transformer’s encoding strengths to
get over this problem. By aiding in the retention of higher-resolution
feature maps, the CNN enables the decoder to do more precise seg-
mentation through skip connections. The Transformer, on the other
hand, enables the model to focus more on capturing distant spatial
interactions. The skip connections are essential to TransUNet’s success.
In order to facilitate efficient information flow throughout various
phases of the model’s design, they mix high-level feature maps from
the decoder with low-level feature maps from the encoder [16,22].

Table 1 is a compilation of noteworthy research that centers on
developing approaches in the field of machine learning. Despite the
notable success of UNet-based network designs in diverse medical pic-
ture segmentation tasks, there persists a constraint in attaining optimal
segmentation performance. Furthermore, it is of utmost importance in
the field of medical image processing to ensure the constant provi-
sion of high-performance outcomes. This work presents the Enhanced-
TransUNet as a proposed approach to tackle the issues associated with
medical picture segmentation.

3. Methodology

In this section, we introduce our proposed effective model called
Enhanced-TransUNet for thyroid nodule image segmentation. Enhan-
ced-TransUNet architecture is a hybrid approach which was developed
to perform the segmentation task of the thyroid nodules with the U-Net
network by utilizing the power of transformers. The main motivation of
the method is based on coding the global context of the image patches,
as well as using low-level CNN features through UNet architecture.

3.1. Transformers and image segmentation

In conventional CNN techniques, the algorithm first encodes the
pictures into high-level features and then decodes them to restore
the original spatial resolution. These processes show that CNN mod-
els are architectures that have complex structures and require high
performance as major drawbacks. Transformers are used to incorpo-
rate self-attention processes into the encoding stage, which helps to

overcome the drawbacks of this approach. Segmentation in computer
vision is the division of an image into several segments or regions, each
of which represents a distinct item or area of the scene. Additionally,
transformer-based models have been modified for use in image segmentation
tasks.

Transformers offer a promising infrastructure for image segmenta-
tion with their powerful classification capabilities. There are four dif-
ferent basic components in the Transformer-based image segmentation
task.

• Patch Embeddings: Instead of processing the entire image at
once, the image is divided into smaller patches, each of which
is treated as a token. These patches are then embedded and
processed by the transformer model.

• Positional Encoding: The positional encoding is added to the
information about each

patch embeddings to provide spatial
patch’s location in the image.

• Self-Attention Mechanism: The transformer model employs a
self-attention mechanism to capture global dependencies between
different patches in the image.

• Decoder for Segmentation: A decoder can be added to the
transformer architecture to produce segmentation masks for each
patch, indicating the object or scene segment that the patch
belongs to.

An attention function generates an output based on a query and
key–value pairs. This procedure represents the query, keys, values,
and output as vectors. The Attention mechanism uses the following
equation to calculate matrices.

𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝑄, 𝐾, 𝑉 ) = 𝑠𝑜𝑓 𝑡𝑚𝑎𝑥(

𝑄𝐾 𝑇
√𝑑𝑘

)𝑉

(1)

In this equation, Q represents a set of queries, while K and V
√𝑑𝑘)
correspond to the key and value parameters, respectively. The 1∕(
is scaling factor. For each of these transformed versions of queries,
keys, and values, the attention function is applied simultaneously,
generating output values of dimensionality 𝑑𝑣. These outputs are then
combined and projected once more, ultimately producing the final set
of values. Multi-head attention (MHA) enables the model to collectively

BiomedicalSignalProcessingandControl95(2024)1064724A. Ozcan et al.

Table 2
Variable notation and definition table.

Variable name

Notation

Definition

Picture
Size
Channel
Patch
Dimension
Weights
Features

𝑥
𝐻 × 𝑊
𝐶
𝑃
𝐷
𝑊𝑝𝑎𝑡𝑐ℎ
𝐹𝑖𝑛, 𝐹𝑜𝑢𝑡

A picture with C channel
Height and Weight
Total number of channels
Resolution of patches
Latent vector size
Weight matrix for patches
Input and Output features

focus on details from various representation dimensions across different
positions where ℎ𝑒𝑎𝑑𝑖 = 𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝑄𝑊 𝑄
𝑖

, 𝐾𝑊 𝐾
𝑖

, 𝑉 𝑊 𝑉

𝑖 ).

𝑀𝐻𝐴(𝑄, 𝐾, 𝑉 ) = 𝐶𝑜𝑛𝑐𝑎𝑡(ℎ𝑒𝑎𝑑1, ℎ𝑒𝑎𝑑2, … , ℎ𝑒𝑎𝑑ℎ)𝑊 𝑂
and 𝑉 𝑊 𝑉

The 𝑄𝑊 𝑄
𝑖

, 𝐾𝑊 𝐾
𝑖

𝑖 values in the equation are the param-

(2)

eter matrices corresponding to the projections.

3.2. Proposed enhanced TransUNet model

This section presents the details of the proposed hybrid TransUNet
method. The Table 2 below gives the variables, notations and defini-
tions used within the scope of the proposed method.

Let 𝑥 ∈ 𝑅𝐻𝑊 𝐶 represent a picture with 𝐻 × 𝑊 and 𝐶 channels
providing the spatial resolution. The goal of picture segmentation is to
forecast a pixel-wise label map with dimensions 𝐻 × 𝑊 .

The standard Transformer model commonly functions on a one-
dimensional sequence of token embeddings. However, in the context
of 2D pictures, it becomes imperative to employ a transformation. To
adapt the model, the images are reshaped from 𝑥 ∈ 𝑅𝐻𝑊 𝐶 into a
𝑝 ∈ 𝑅𝑃 2.𝐶 , 𝑖 = 1, … , 𝑛. Here, 𝐶 repre-
series of flattened 2D patches 𝑥𝑖
sents the total number of channels, 𝑃 signifies the resolution of each
individual image patch (𝑃 , 𝑃 ) and 𝑊 corresponds to the resolution of
the original image (𝐻, 𝑊 ), the total number of patches are given by
𝑛 = 𝐻𝑊 ∕𝑃 2 which also serves as an effective input sequence length
for the Transformers.

The patches undergo a process of flattening and are subsequently
turned into a D-dimensional space by the utilization of a trainable linear
projection, as described in (3). The process of converting input data into
patch embeddings, which guarantees a consistent latent vector size (D)
throughout the layers of the Transformer model, is commonly known
as patch embedding.

𝑧0 = [𝑥1

𝑝𝐸; 𝑥2

𝑝𝐸; ...; 𝑥𝑛

𝑝] + 𝐸𝑝𝑜𝑠

(3)

A transformer block consists Multihead Self Attention (MSA) and
Multi-Layer Perceptron (MLP) blocks which are shown by Eqs. (4) and
(5). Consequently, the output of the 𝑙th layer is written as follows:

𝑧′
𝑙 = 𝑀𝑆𝐴(𝐿𝑁(𝑧𝑙−1)) + 𝑧𝑙−1

𝑧𝑙 = 𝑀𝐿𝑃 (𝐿𝑁(𝑧𝑙)) + 𝑧𝑙

(4)

(5)

The encoded picture representation is indicated by 𝑧𝑙 and the layer

normalization operator is denoted by 𝐿𝑁(∙).

A straightforward approach is to upscale the encoded feature repre-
sentation 𝑧𝐿 ∈ R𝐻𝑊 ∕𝑃 2×𝐷 to the original resolution for generating the
dense output. To maintain spatial integrity, the size of the encoded
feature needs to be initially reshaped from 𝐻𝑊 ∕𝑃 2 to 𝐻∕𝑃 × 𝑊 ∕𝑃 .
A 1 × 1 convolution has been employed to decrease the channel size
of the reshaped feature to several classes. Subsequently, the feature
map is directly bilinearly upsampled to the original resolution 𝐻 × 𝑊
to predict the final segmentation result. Using a Transformer with
basic upsampling already achieves decent performance. However, this
method does not fully leverage the potential of Transformers for seg-
mentation because the downsampled size (𝐻∕𝑃 × 𝑊 ∕𝑃 ) is typically
much smaller than the original image resolution (𝐻 × 𝑊 ), leading

Fig. 1. Proposed enhanced-TransUNet encoder module.

to a loss of fine-grained details. Hence, to address this loss of infor-
mation, TransUNet adopts a hybrid CNN-Transformer architecture as
the encoder and integrates a cascaded upsampler to ensure accurate
localization.

Based on the usage of transformers, the image is converted into
a series of smoothed image patches of equal size in the transformer
encoder block. The vectorized patches are then put into a step called
patch placement, where they are trained into a D-dimensional layout
space. The Fig. 1 below shows the construction of the transformer
encoder block.

To further enhance the connections, an enhancement module is
developed to strengthen the skip features. An enhancement module
for improving the understanding of column vector relations has been
created based on the column vector analysis. This module aims to
capture the relationships within the column vectors. The decoder fea-
tures, which come into play after the transformer encoder, establish
connections over long-ranges. The process can be visualized in Fig. 2.
Initially, the column vector generates patch weights, which are then
arranged into a matrix.

In the MSA phase of the Transformer architecture, the weight matri-
ces produced by the score matrices are aggregated to create a distinct
weight matrix that is particular to each layer of the transformer. There
are a total of 𝑛 weight matrices, with each matrix corresponding to a
transformer layer. The suggested methodology involves combining the
separate weight matrices to obtain the final weight matrix. The process
of merging in this context entails the utilization of the score matrix 𝑆𝑖
from the transformer layer, in combination with the weight assigned
to each patch, represented as 𝑊 . The function 𝑓 (⋅) represents the
mathematical operation done to the column vectors. The mathematical
expression guiding the computation of the weight patch is presented
in Eq. (6).

𝑊𝑝𝑎𝑡𝑐ℎ =

𝑛
∑

𝑖=1

𝑓 (𝑆𝑖)

(6)

The weight matrix is resized to match the dimensions of the skip fea-
tures. Subsequently, the weight matrix is used to enhance each encoder
feature, and the resulting skip features are passed on to the decoder,
𝐹𝑜𝑢𝑡 = 𝐹𝑖𝑛∙𝑢𝑝𝑠(𝑊𝑝𝑎𝑡𝑐ℎ). Before and after going through the enhancement
module, the features are referred to as 𝐹𝑖𝑛 and 𝐹𝑜𝑢𝑡, respectively. The
weight matrix is denoted as 𝑊𝑝𝑎𝑡𝑐ℎ, and the upsampling operation is
represented by 𝑢𝑝𝑠(⋅).

The second section uses CNN-based UNet for upsampling. As a
result, the transformer and UNet work together to generate a hybrid
encoder. The method’s cascaded upsampler (CUP) extracts the hidden
features for the final segmentation mask. After tweaking the hidden
feature 𝑧𝐿 ∈ 𝑅((𝐻𝑊 )∕𝑃 2)𝐷 × × to fit the form of (𝐻∕𝑃 ) × (𝑊 ∕𝑃 ) × 𝐷,
we generate CUP by combining numerous upsampling blocks to obtain
full resolution from (𝐻∕𝑃 ) × (𝑊 ∕𝑃 ) to 𝐻 × 𝑊 . Each block includes a
2× upsampling operation, a 3 × 3 convolutional layer, and ultimately
a ReLU layer.The decoder module utilizes a cascaded upsampler to
perform multi-level upsampling and decoding operations to generate
the segmentation output. The decoder block, as illustrated in Fig. 3,

BiomedicalSignalProcessingandControl95(2024)1064725A. Ozcan et al.

Fig. 2. Proposed enhanced-transUNet approach for thyroid nodule segmentation.

Table 3
Properties of transformer module used in Vit-L16.

Model

Layers

Hidden size

MLP Size

Heads

Params

Vit-Large/16

24

1024

4096

16

307M

with matching dimensions are specifically enhanced by skip connec-
tions throughout the first three stages when they are concatenated
across feature channels to improve the overall representation. In order
to separate foregrounds from backgrounds, the final feature map is
upsampled.

Fig. 3. Proposed enhanced-transUNet decoder module.

4. Experimental setup

comprises a 2× upsampling operation, a concatenation operation that
combines features from the encoder, and a convolution operation. Upon
completing a decoder block, the feature’s length and width are doubled,
while the number of channels is halved. When all three decoder blocks
are applied consecutively, the feature’s width and length are reduced
to half of the original picture size. Ultimately, the segmentation head
generates the final segmentation result by combining a linear layer with
an upsampling layer.

In the proposed approach, the thyroid image data is given to the
encoder phase first. At this stage, the CNN encoder transmits the data
patches it subsamples to the transformer encoder via linear projection.
The transformer encoder extracts the hidden features from the data it
receives and transmits it to the decoder stage. On the other hand, the
features taken from the subsampling layers of the CNN encoder are im-
proved by processing the weight matrices in the designed enhancement
module and transmitting them to the decoder. On the decoder side,
both the input transformer encoder features and the enhanced CNN
encoder layer features are used as inputs at each stage of upsampling.
In the segmentation head layer, the final output is produced.

We use the Vit-L/16 model, a 16 × 16 input patch size ‘‘Large’’
variation of the visual transformer module. Models with smaller patches
require more processing power, as the Transformer’s sequence length is
inversely proportional to the square of the patch size. The underlying
CNNs employed ResNet architecture, however normalizing layers were
updated by adopting Group normalizing as recommended by [37]
and standardized convolutions in place of Batch Normalization layers,
which were initially introduced. Kolesnikov et al. [38] found that these
adjustments enhanced the capacity to transfer learning (see Table 3).

Then, segmentation tokens go via a cascade-based upsampling pro-
cedure after being subjected to n successive Transformer layers. The
token sizes are multiplied by four using bilinear interpolation and two
convolutional neural networks. The ResNet50 encoder’s feature maps

The present section commences by presenting a comprehensive
review of the datasets utilized, explaining the assessment criteria ap-
plied, and then providing an in-depth discussion of the implementation
aspects. Following this, a thorough examination is conducted using
advanced approaches to verify the effectiveness of each component
inside the suggested architectural framework.

4.1. Dataset

To the best of our current understanding, the sole thyroid nodule
dataset that is openly available to the public without any usage limita-
tions is commonly known as DDTI, which was made available by [39].
Nevertheless, it is important to acknowledge that DDTI does have
several limitations, namely in terms of its relatively small dataset size,
which comprises just 637 images together with corresponding pixel-
wise lesion masks. The scale in question exhibits several limitations in
its applicability for the purposes of training and testing deep learning
models. In addition, it should be noted that the DDTI method does not
adequately account for the frequently encountered situation of multi-
nodules, which is a commonly observed phenomenon in ultrasonic
thyroid examinations.

In order to further the progress of research in the field of computer-
aided diagnosis for automated identification of thyroid nodules, a
significant dataset of ultrasound thyroid pictures has been integrated.
This dataset, referred to as TN3K, comprises a huge collection of
real-world scenarios. The dataset utilized in this study, obtained from
Zhujiang Hospital, South Medical University [27], presents significant
challenges in the task of thyroid nodule segmentation. The dataset
consists of a comprehensive collection of 3493 ultrasound pictures,
with each image accompanied by pixel-wise annotations. The TN3K
dataset consists of a total of 3493 pictures, with 2879 photos designated
for training and the remaining 614 images used for testing.

BiomedicalSignalProcessingandControl95(2024)1064726A. Ozcan et al.

4.2. Implementation details

The execution of the suggested approach is implemented using the
PyTorch framework. The experimental configuration utilized a single
RTX3060 VENTUS 2X OC GPU equipped with 12 GB of RAM. The
Adam optimizer [40] is utilized for the purpose of training the model,
with a consistent batch size of 16. The learning rate is initialized
at 10−5 and follows a linear decrease, eventually reaching zero after
40,000 iterations. It is worth mentioning that the initialization of
our model entails pre-training the ResNet50 and Transformer layers
using the ImageNet dataset [41]. In the empirical configuration of
hyperparameters, the values of 𝜆𝐶 , 𝜆𝐿, and 𝜆𝐴 were set to 0.25, 5.0,
and 1.0, respectively. These hyperparameters play a crucial role in
determining particular elements of our model’s performance. In order
to achieve the most efficient convergence, the parameter 𝜆𝐷 follows
an exponential ramp-up technique over a period of 40 iterations. The
parameter k is allocated a value of 1500, and our model architecture
includes 24 Transformer layers, a move intended to improve feature
extraction. Patch sizes are commonly denoted as 16 × 16 in academic
literature. In the training phase, data augmentation techniques are
employed to enhance the dataset by randomly applying horizontal and
vertical picture flips. All algorithms run for 50 epochs. The Enhanced-
TransUNet model is optimized by employing the Dice loss function,
which is supplemented with a thyroid nodule region mask for oversight.
The careful arrangement and systematic training routine adhere to
well-established academic conventions within the discipline.

4.3. Evaluation metrics

In our study, we employed a comprehensive set of seven metrics to
evaluate the segmentation performance. These metrics include Inter-
section Over Union (IoU), dice coefficient (DICE), Specificity, Precision
(PR), Accuracy, F1-score, and Area Under the Receiver Operating Char-
acteristic Curve (AUC). Notably, the DICE coefficient, as presented
in Eq. (7), stands as a widely acknowledged similarity measurement
method extensively utilized for object segmentation tasks, as referenced
by [42].

DICE = 2 ∗ TP∕(FP + FN + 2 ∗ TP)

(7)

An increased DICE score indicates a higher level of similarity, hence
suggesting improved success in segmentation. To ensure a comprehen-
sive and rigorous evaluation of the segmentation performance of our
proposed technique, we have carefully selected the following metrics:

• IoU (Intersection Over Union) = TP/(FP + FN)
• Recall = TP/(TP + FN)
• PR (Precision) = TP/(TP + FP)
• Accuracy = (TN + TP)/(TN + TP + FN + FP)
• F1-score = (2 ∗ PR ∗ RE)/(PR + RE)
• The Area Under the (ROC) Curve, denoted as AUC, is calculated
by evaluating the Intersection over Union (IoU) score for the
segmentation results acquired from all five folds.

• The HD95 measure is utilized to evaluate the accuracy of seg-
mentation borders. It involves calculating the greatest distance
between the predicted boundaries and the ground truth, and then
selecting the top 95% of these distances.

The abbreviations TP, FP, TN, and FN represent the terms true
positive, false positive, true negative, and false negative, respectively.
The F1-score is defined as the harmonic mean of accuracy and recall.

Table 4
Comparisons of our proposed segmentation model against with the state-of-the-art
models on the TN3K testset. The best result is shown in bold.

TN3K

AUC

F1-score

IoU

Dice

HD95

𝑝-value

Enhanced-TransUNet
UNet
SGUNet
FCN
SegNet
Deeplabv3+
CPFNet
Attention UNet
Attention R2 UNet

92.06
87.17
89.39
88.98
88.79
89.36
91.78
91.73
91.75

80.55
75.30
76.57
77.07
76.46
75.35
80.65
79.18
77.68

70.87
64.67
65.83
66.16
65.87
64.86
70.45
69.38
67.37

82.92
78.55
79.39
79.99
79.42
78.68
82.67
81.92
80.50

13.19
18.39
17.96
17.06
16.61
17.45
13.22
15.67
16.20

< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001

Table 5
Comparisons of our proposed segmentation model against with the state-of-the-art
models on the DDTI testset. The best result is shown in bold.

DDTI

AUC

F1-score

IoU

Dice

HD95

𝑝-value

Enhanced-TransUNet
UNet
SGUNet
FCN
SegNet
Deeplabv3+
CPFNet
Attention UNet
Attention R2 UNet

97.79
93.98
93.26
94.02
97.68
96.70
98.11
96.46
93.44

95.41
90.61
89.47
89.22
93.68
93.05
96.60
95.00
75.40

91.29
83.20
81.40
81.03
88.27
87.25
93.45
91.20
63.46

95.45
90.83
89.75
89.52
93.76
93.20
96.61
95.40
77.65

1.09
5.19
5.77
6.60
2.41
2.75
0.43
1.72
23.42

< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001
< 0.001

5. Experimental results and comparison with the state-of-the-art
methods

The approach employed in this study is subjected to a thorough
examination using the TN3K and DDTI test datasets. The outcomes
of this evaluation are reported in Tables 4 and 5. It is important to
acknowledge that all models are implemented in their original settings
as given by the authors. By conducting thorough comparisons with
cutting-edge segmentation approaches, we demonstrate the exceptional
performance of our Enhanced-TransUNet model.

To provide context, FCN and SegNet utilize the VGG architecture,
which has been pretrained on the ImageNet dataset [43]. On the other
hand, Deeplabv3+ and CPFNet are equipped with the ResNet backbone,
which has also been pretrained on ImageNet [44]. Furthermore, in
order to enhance the process of comparing performance, we incorporate
three models: basic UNet, Attention UNet, and Attention R2 UNet, as
mentioned in the work by [45].

The statistical significance of the comparisons is assessed by cal-
culating p-values using t-tests. This analysis focuses on the differences
in IoU between the proposed Enhanced-TransUNet model and the
alternative models. A 𝑝-value below the threshold of 0.05 indicates a
significant performance advantage in support of our suggested strategy
compared to the competing models.

The proposed technique demonstrates a significant enhancement
compared to the fundamental UNet design, as evidenced by a 6.20%
increase in the Jaccard score on the TN3K test set. Moreover, it may
be regarded as a prominent leader in comparison to the alternative
algorithms that have been presented. It is worth mentioning that our
approach has superior performance compared to other advanced meth-
ods that utilize robust ImageNet pretrained backbones, owing to the
careful design of our learning framework. It is noteworthy to notice that
our technique exhibits a little worse performance in terms of accuracy
and F1-score compared to CPFNet, while the difference is negligible.
Also the performance of the proposed model on TN3K dataset can be
seen at 4 and 5.

In Table 5, performance comparison of the algorithms for DDTI data

set is given.

As it can be seen from the table we only used the DDTI dataset,
in which 405 of the images are used for training purpose, 99 for

BiomedicalSignalProcessingandControl95(2024)1064727A. Ozcan et al.

Fig. 4. ROC curve of the models for TN3K test set.

Fig. 6. ROC curve of the models for DDTI test set.

Fig. 5. Recall and accuracy values of the models for TN3K test set.

Fig. 7. Recall and accuracy values of the models for DDTI test set.

validation, 129 for test, and all of them are randomly assigned. As being
a very small dataset, with the complex nature of the transformers, our
proposed algorithm comes in second place just a little behind CPFNet.
Performance of the proposed model on DDTI dataset can be seen at 6
and 7.

6. Discussion

The visual representation of the qualitative comparison findings is
shown in Figs. 8 and 9. The performance of the basic UNet model is no-
ticeably inferior, mostly due to its limited prior information concerning
the thyroid area. On the contrary, it becomes evident that alternative
models discussed in the existing literature typically exhibit superior
performance compared to UNet within this particular situation.

To provide a comprehensive evaluation of segmentation perfor-
mance utilizing ground truth photos, we give a tabular representation
below. This analysis encompasses established approaches from exist-
ing literature as well as our proposed methodology. All evaluations
are conducted using the TN3K dataset. The table has columns that
depict the original picture and the ground truth image in the first
and second columns, respectively. Subsequently, the table showcases
images displaying segmentations accomplished by different techniques
outlined in the existing literature, spanning from the third to the tenth
columns. The segmentation results achieved by our suggested approach
are displayed in the last column.

The majority of recently developed methodologies exhibit superior
performance in comparison to the UNet. Nevertheless, there are still

errors observed in their identification of the non-nodule region as the
thyroid nodule, and in certain instances, they have difficulties in accu-
rately segmenting all the nodules. In instances where several nodules
are present, the majority of algorithms exhibit suboptimal predictive
performance, occasionally failing to detect the second nodule. As a
result of the combination of Vit-Large/16 transformer and ResNet50
CNN models developed in the proposed method, it can be stated that it
produces segmentation results close to ground truth reference images.
In contrast, the proposed modified technique showcases improved
precision in its outcomes, thereby reducing the occurrence of misclas-
sified areas that are not thyroid nodules.

In the present work, we provide a new model that utilizes thyroid
nodule images with separate labels to improve the accuracy of thyroid
nodule segmentation. This approach has ensured significant impor-
tance, especially when considering the inherent difficulties related to
the annotation of medical images. The improved system effectively
utilizes a significant pool of annotated data, utilizing a common core
structure and independent decoding components. Automated segmenta-
tion of thyroid nodules plays a crucial role in both streamlining clinical
operations and facilitating thyroid nodule identification. Various fac-
tors, including dimensions, morphology, and the quantity of nodules,
exhibit statistical importance when assessing the grading of thyroid
nodules.

7. Practical implications and future scope of the work

Numerous diagnostic imaging techniques which include computed
tomography, magnetic resonance imaging, ultrasound, and radionu-
clide imaging are some of those used to investigate thyroid disorders.

BiomedicalSignalProcessingandControl95(2024)1064728A. Ozcan et al.

Fig. 8. Performance comparison of the models for TN3K test set.

Amongst these imaging modalities, mainly ultrasound is usually em-
ployed in the diagnosis of thyroid diseases, for this imaging technique
is real-time, inexpensive, non-invasive, and non-radioactive. However,
low image quality and speckle artifacts of ultrasound images distort
the optical properties of the tissues and result in the ultrasound image
being homogeneous and inhomogeneous. In clinical diagnostics, the
clinician has to utilize their experience in image interpretation. Besides,
one has a lengthy learning curve in an ultrasound examination and

subjective factors are difficult to remove in the diagnostic process. The
ultrasound images of the thyroid nodules may variably contain large
and small areas as well as perform poorly due to spots and echoes. This
noise, however, harms the quality of the image, and the problem of an
accurate determination is very important for young doctors: to find the
fuzzy boundary between the thyroid parenchyma and nodules.

The extraction of the thyroid region of ultrasound images with
conventional hand-crafted features in the feature-based method is very

BiomedicalSignalProcessingandControl95(2024)1064729A. Ozcan et al.

Fig. 9. Performance comparison of the models for DDTI test images.

difficult because of the low contrast and fuzzy environment. This issue
is mainly addressed by deep learning algorithms which perform better
than other approaches. However, the current deep learning methods
have some disadvantages. They are unable to fully satisfy all the
requirements, and the performance is currently too poor to be fully con-
vincing. The architectural flexibility of UNet and its learning techniques
have an impact on the correct multi-scale clinical analysis classifying
the thyroid. The initial design still has the encoder–decoder structure
inside which may lead to low-level features being lost further when
exploring the high-level features which consequently causes confusion
between thyroid structures and structures relevant. In addition, the
encoder–decoder structure is also responsible for incorrect recognition
of anatomical areas close to the thyroid boundary.

U-Net’s poor extraction of high-resolution information will lead to
its weak extraction of small targets and edges, which can be mitigated
by the introduced attention block. The detection and segmentation of
edges and small details becomes the key issue for the successful per-
formance of this task. Because of the invasiveness of nodules, acoustic
shadows, and the poor image resolution produced by old ultrasound de-
vices, the risk of damaging some image edges during the segmentation
process is relatively high. Furthermore, the small nodules are located in
some images and low-resolution shallow information extraction layers
have their segmentation effect confined.

Our study approaches were chosen to harness the unsurpassed abil-
ities of the transformers and UNet segmentation networks. The intro-
duction of automated segmentation can relieve doctors from the heavy
and time-consuming workload of manual segmentation, which can
increase the accuracy, speed, and thus overall efficiency of detecting
abnormalities.

Our proposed approach is not limited to thyroid image segmentation
systems but can be applied to the segmentation and modeling of
different medical images (thorax, thyroid kidney, etc.) that are perfect
for anatomical or surgical planning.

One of the deficiencies in thyroid ultrasound image segmentation
studies lies in the current research area. Abnormal tissues may appear
in different areas, seemingly different sizes, and associated with dif-
ferent textures, therefore deciding their delineation often involves new
questions. Furthermore, the lack of a well-designed thyroid ultrasound
dataset and adequate evaluation metrics slows down research on the
diagnosis of thyroid diseases. In the future, there may be a convenient
adjoining of research works to interpolate the shortcomings in current
ultrasound image segmentation in the thyroid.

The next step would be to delve deeper into this particular issue
and conduct further research to determine the prospect of engineering
other deep learning models capable of doing for medical imaging. As
the other one, the accuracy of the classification of deep nets requires
performing different imaging modalities. However, the limited samples

BiomedicalSignalProcessingandControl95(2024)10647210A. Ozcan et al.

that are taken from a predetermined dataset is another reason to ques-
tion this study. Hence for next studies; a real-life case can be applied.
To summarize, this interactive character of interdisciplinary research is
what makes it such a powerful tool to determine crucial biomarkers and
use them with confidence for artificial intelligence-based diagnostics,
allowing doctors to use them in their clinical practice. The following
sentence should be noted as well, as we anticipate future work in hos-
pitals to improve our method, which will be based on the real clinical
environment, and thus eventually it will become fully automatic and
more precise.

Moving forward, we will try to use the current results to conduct an
empirical study seeking different loss functions that could model area
and border information. In addition, we try to train the deep learning
models for different diseases, which will serve as tools on mobile and
clinical devices. Our goal is to realize that by using knowledge distil-
lation, our models can be trained without huge complexity, number of
parameters, and memory footprint.

In the future, we are ready to study different algorithms to cut the
processing time while keeping the accurate segmentation. Moreover,
we aim to investigate ways to cut back the training period of our
networks through the usage of other strategies.

8. Conclusion

The development of accurate and automated segmentation in the
field of medical imaging is an essential requirement for clinical diag-
nosis and comprehensive analysis. In the present study, we propose
a unique framework called Enhanced-Transunet, which enhances skip
characteristics through a reconfigured skip connection. The suggested
methodology incorporates the score matrix and skip connection, result-
ing in an increased efficacy of skip features and thus improving the
overall performance of segmentation.

The empirical evaluations done on various datasets provide clear
evidence of the improved performance of Enhanced-TransUNet com-
pared to existing state-of-the-art models. Significantly, our tests reveal
a noticeable difference in performance between the two datasets used.
This shows that ViT models stand out in terms of model size and
provide greater scalability, especially when trained on large data sets.
In our comprehensive assessment, we utilize a variety of indica-
tors as performance metrics to examine the segmentation Intersection
over Union (IoU) of our approach in relation to alternative methods.
The aforementioned evaluations clearly demonstrate the competitive
performance of our suggested method.

CRediT authorship contribution statement

Alper Ozcan: Software, Supervision, Writing – original draft. Ömür
Tosun: Conceptualization, Software, Methodology, Writing – original
draft. Emrah Donmez: Validation, Visualization, Writing – review &
editing. Muhammad Sanwal: Data curation, Formal analysis.

Declaration of competing interest

The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.

Data availability

Data will be made available on request.

References

[1] J. Long, E. Shelhamer, T. Darrell, Fully convolutional networks for semantic
segmentation, 2014, CoRR, arXiv:1411.4038, URL http://arxiv.org/abs/1411.
4038.

[2] O. Ronneberger, P. Fischer, T. Brox, U-net: Convolutional networks for biomed-
ical image segmentation, in: N. Navab, J. Hornegger, W.M. Wells, A.F. Frangi
(Eds.), Medical Image Computing and Computer-Assisted Intervention – MICCAI
2015, Springer International Publishing, 2015, pp. 234–241.

[3] M.D. Zeiler, D. Krishnan, G.W. Taylor, R. Fergus, Deconvolutional networks,
in: 2010 IEEE Computer Society Conference on Computer Vision and Pat-
tern Recognition, 2010, pp. 2528–2535, http://dx.doi.org/10.1109/CVPR.2010.
5539957.

[4] Z. Zhou, M.M.R. Siddiquee, N. Tajbakhsh, J. Liang, Unet++: A nested U-net
architecture for medical image segmentation, in: Deep Learning in Medical Image
Analysis and Multimodal Learning for Clinical Decision Support, Springer, 2018,
http://dx.doi.org/10.1007/978-3-030-00889-5_1.

[5] O. Oktay, J. Schlemper, L.L. Folgoc, M.C.H. Lee, M.P. Heinrich, K. Misawa,
K. Mori, S.G. McDonagh, N.Y. Hammerla, B. Kainz, B. Glocker, D. Rueckert,
Attention U-net: Learning where to look for the pancreas, 2018, CoRR, arXiv:
1804.03999, URL http://arxiv.org/abs/1804.03999.

[6] Y. Chen, K. Wang, X. Liao, Y. Qian, Q. Wang, Z. Yuan, P.-A. Heng, Channel-
unet: A spatial channel-wise convolutional neural network for liver and tumors
segmentation, Front. Genet. 10 (2019) http://dx.doi.org/10.3389/fgene.2019.
01110, URL https://www.frontiersin.org/articles/10.3389/fgene.2019.01110.
[7] H. Sun, C. Li, B. Liu, S. Wang, AUNet: Breast mass segmentation of whole
mammograms, 2018, CoRR, arXiv:1810.10151, URL http://arxiv.org/abs/1810.
10151.

[8] G. Litjens, T. Kooi, B.E. Bejnordi, A.A.A. Setio, F. Ciompi, M. Ghafoorian,
J.A. van der Laak, B. van Ginneken, C.I. Sánchez, A survey on deep learning
in medical image analysis, Med. Image Anal. 42 (2017) 60–88, http://dx.doi.
org/10.1016/j.media.2017.07.005, URL https://www.sciencedirect.com/science/
article/pii/S1361841517301135.

[9] N. Tajbakhsh, L. Jeyaseelan, Q. Li, J.N. Chiang, Z. Wu, X. Ding, Embracing
image

imperfect datasets: A review of deep learning solutions for medical
segmentation, Med. Image Anal. 63 (2020) 101693.

[10] D. Shen, G. Wu, H.-I. Suk, Deep learning in medical image analysis, Annu. Rev.
Biomed. Eng. 19 (2017) 221248, http://dx.doi.org/10.1007/978-3-030-33128-
3_1.

[11] G. Chartrand, P.M. Cheng, E. Vorontsov, M. Drozdzal, S. Turcotte, C.J. Pal, S.
Kadoury, A. Tang, Deep learning: A primer for radiologists, Radiographics 37
(7) (2017) 21132131, http://dx.doi.org/10.1148/rg.2017170077.

[12] T. Falk, D. Mai, R. Bensch, Ö. Çiçek, A. Abdulkadir, Y. Marrakchi, A. Böhm,
J. Deubner, Z. Jäckel, K. Seiwald, A. Dovzhenko, O. Tietz, C.D. Bosco, S.
Walsh, D. Saltukoglu, T.L. Tay, M. Prinz, K. Palme, M. Simons, I. Diester, T.
Brox, O. Ronneberger, U-Net: Deep learning for cell counting, detection, and
morphometry, Nature Methods 16 (1) (2019) 6770, http://dx.doi.org/10.1038/
s41592-018-0261-2.

[13] M. Drozdzal, E. Vorontsov, G. Chartrand, S. Kadoury, C. Pal, The importance of
skip connections in biomedical image segmentation, in: Deep Learning and Data
Labeling for Medical Applications, Springer, 2016, http://dx.doi.org/10.1007/
978-3-319-46976-8_19.

[14] J. Chen, Y. Lu, Q. Yu, X. Luo, E. Adeli, Y. Wang, L. Lu, A.L. Yuille, Y. Zhou,
TransUNet: Transformers make strong encoders for medical image segmentation,
2021, arXiv:2102.04306.

[15] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner,
M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, N. Houlsby, An
image is worth 16x16 words: Transformers for image recognition at scale, 2021,
arXiv:2010.11929.

[16] B. Chen, Y. Liu, Z. Zhang, G. Lu, A.W.K. Kong, TransAttUnet: Multi-level
attention-guided U-net with transformer for medical image segmentation, 2022,
arXiv:2107.05274.

[17] X. Yan, H. Tang, S. Sun, H. Ma, D. Kong, X. Xie, AFTer-UNet: Axial fusion
transformer unet for medical image segmentation, 2021, arXiv:2110.10403.
[18] D. Maji, P. Sigedar, M. Singh, Attention res-unet with guided decoder for
semantic segmentation of brain tumors, Biomed. Signal Process. Control 71
(2022) 103077, http://dx.doi.org/10.1016/j.bspc.2021.103077, URL https://
www.sciencedirect.com/science/article/pii/S1746809421006741.
[19] Z. Wang, C. Zhao, Z. Ni, Adversarial vision transformer for medical

image

semantic segmentation with limited annotations, 2022, p. 13.

[20] A. Sagar, ViTBIS: Vision Transformer for Biomedical

Image Segmentation,
Springer-Verlag, Berlin, Heidelberg, 2021, pp. 34–45, http://dx.doi.org/10.1007/
978-3-030-90874-4_4.

[21] R. Azad, M.T. AL-Antary, M. Heidari, D. Merhof, TransNorm: Transformer
provides a strong spatial normalization mechanism for a deep segmentation
model, 2022, arXiv:2207.13415.

[22] Y. Liu, H. Wang, Z. Chen, K. Huangliang, H. Zhang, TransUNet+: Redesign-
ing the skip connection to enhance features in medical image segmentation,
Knowl.-Based Syst. 256 (2022) 109859, http://dx.doi.org/10.1016/j.knosys.
2022.109859.

BiomedicalSignalProcessingandControl95(2024)10647211A. Ozcan et al.

[23] G. Li, D. Jin, Q. Yu, M. Qi, IB-TransUNet: Combining information bottleneck
and transformer for medical image segmentation, J. King Saud Univ. Comput.
Inf. Sci. 35 (3) (2023) 249–258, http://dx.doi.org/10.1016/j.jksuci.2023.02.012,
URL https://www.sciencedirect.com/science/article/pii/S1319157823000411.

[24] V.V. Vadhiraj, A. Simpkin, J. O’Connell, N. Singh Ospina, S. Maraka,
D.T. O’Keeffe, Ultrasound image classification of thyroid nodules using ma-
chine learning techniques, Medicina 57 (6) (2021) http://dx.doi.org/10.3390/
medicina57060527, URL https://www.mdpi.com/1648-9144/57/6/527.

[25] D.T. Nguyen, J. Choi, K.R. Park, Thyroid nodule segmentation in ultrasound
image based on information fusion of suggestion and enhancement networks,
Mathematics 10 (19) (2022) http://dx.doi.org/10.3390/math10193484, URL
https://www.mdpi.com/2227-7390/10/19/3484.

[26] Z. Tao, H. Dang, Y. Shi, W. Wang, X. Wang, S. Ren, Local and context-attention
adaptive LCA-net for thyroid nodule segmentation in ultrasound images, Sensors
22 (16) (2022) http://dx.doi.org/10.3390/s22165984, URL https://www.mdpi.
com/1424-8220/22/16/5984.

[27] H. Gong, J. Chen, G. Chen, H. Li, G. Li, F. Chen, Thyroid region prior guided
attention for ultrasound segmentation of thyroid nodules, Comput. Biol. Med.
155 (2023) 106389, http://dx.doi.org/10.1016/j.compbiomed.2022.106389, URL
https://www.sciencedirect.com/science/article/pii/S0010482522010976.
[28] J. Zhang, Q. Qin, Q. Ye, T. Ruan, ST-Unet: Swin transformer boosted
image segmenta-
U-Net with cross-layer feature enhancement
tion, Comput. Biol. Med. 153 (2023) 106516, http://dx.doi.org/10.1016/j.
compbiomed.2022.106516, URL https://www.sciencedirect.com/science/article/
pii/S0010482522012240.

for medical

[29] S. Guo, S. Sheng, Z. Lai, S. Chen, Trans-u: Transformer enhanced U-net for
medical image segmentation, in: 2022 3rd International Conference on Computer
Vision,
Image and Deep Learning & International Conference on Computer
Engineering and Applications (CVIDL & ICCEA), 2022, pp. 628–631, http://dx.
doi.org/10.1109/CVIDLICCEA56201.2022.9824530.

[30] H. Touvron, M. Cord, M. Douze, F. Massa, A. Sablayrolles, H. Jégou, Training
data-efficient image transformers & distillation through attention, 2021, arXiv:
2012.12877.

[31] A. Khanna, N.D. Londhe, S. Gupta, A. Semwal, A deep residual U-net convolu-
tional neural network for automated lung segmentation in computed tomography
images, Biocybern. Biomed. Eng. 40 (3) (2020) 1314–1327, http://dx.doi.org/
10.1016/j.bbe.2020.07.007, URL https://www.sciencedirect.com/science/article/
pii/S0208521620300887.

[32] A. Lin, B. Chen, J. Xu, Z. Zhang, G. Lu, DS-TransUNet:Dual swin transformer

U-net for medical image segmentation, 2021, arXiv:2106.06716.

[33] H. Huang, L. Lin, R. Tong, H. Hu, Q. Zhang, Y. Iwamoto, X. Han, Y.-W. Chen,
J. Wu, UNet 3+: A full-scale connected unet for medical image segmentation,
2020, arXiv:2004.08790.

[34] H. Pan, Q. Zhou, L.J. Latecki, Sgunet: Semantic guided unet for thyroid nodule
in: 2021 IEEE 18th International Symposium on Biomedical

segmentation,
Imaging, ISBI, IEEE, 2021, pp. 630–634.

[35] J. Chi, Z. Li, Z. Sun, X. Yu, H. Wang, Hybrid transformer unet for thyroid

segmentation from ultrasound scans, Comput. Biol. Med. 153 (2023) 106453.

[36] H. Dai, W. Xie, E. Xia, SK-Unet++: An improved Unet++ network with adaptive
receptive fields for automatic segmentation of ultrasound thyroid nodule images,
Med. Phys. (2023).

[37] Y. Wu, K. He, Group normalization, 2018, arXiv:1803.08494.
[38] A. Kolesnikov, L. Beyer, X. Zhai, J. Puigcerver, J. Yung, S. Gelly, N. Houlsby, Big
transfer (BiT): General visual representation learning, 2020, arXiv:1912.11370.
[39] L. Pedraza, C. Vargas, F. Narváez, O. Durán, E. Muñoz, E. Romero, An open
access thyroid ultrasound image database,
in: E. Romero, N. Lepore (Eds.),
10th International Symposium on Medical Information Processing and Analysis,
Vol. 9287, International Society for Optics and Photonics, 2015, p. 92870W,
http://dx.doi.org/10.1117/12.2073532.

[40] D.P. Kingma, J. Ba, Adam: A method for stochastic optimization, 2017, arXiv:

1412.6980.

[41] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, F.-F. Li, ImageNet: A large-
scale hierarchical image database, in: IEEE Conference on Computer Vision and
Pattern Recognition, 2009, pp. 248–255, http://dx.doi.org/10.1109/CVPR.2009.
5206848.

[42] A. Vakanski, M. Xian, P.E. Freer, Attention-enriched deep learning model for
breast tumor segmentation in ultrasound images, Ultrasound Med. Biol. 46 (10)
(2020) 2819–2833, http://dx.doi.org/10.1016/j.ultrasmedbio.2020.06.015, URL
https://www.sciencedirect.com/science/article/pii/S0301562920302878.
[43] K. Simonyan, A. Zisserman, Very deep convolutional networks for large-scale
image recognition, in: 3rd International Conference on Learning Representations
(ICLR 2015), Computational and Biological Learning Society, 2015, pp. 1–14.

[44] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition,
in: 2016 IEEE Conference on Computer Vision and Pattern Recognition, CVPR,
2016, pp. 770–778, http://dx.doi.org/10.1109/CVPR.2016.90.

[45] M.Z. Alom, M. Hasan, C. Yakopcic, T.M. Taha, V.K. Asari, Recurrent residual
image
convolutional neural network based on U-Net (R2U-net) for medical
segmentation, 2018, CoRR, arXiv:1802.06955, URL http://arxiv.org/abs/1802.
06955.

BiomedicalSignalProcessingandControl95(2024)10647212