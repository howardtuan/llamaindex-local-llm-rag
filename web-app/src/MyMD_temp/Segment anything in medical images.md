Article

https://doi.org/10.1038/s41467-024-44824-z

Segment anything in medical images

Received: 24 October 2023

Accepted: 5 January 2024

Check for updates

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

Jun Ma1,2,3, Yuting He4, Feifei Li
Bo Wang 1,2,3,7,8

1, Lin Han5, Chenyu You 6 &

Medical image segmentation is a critical component in clinical practice, facil-
itating accurate diagnosis, treatment planning, and disease monitoring.
However, existing methods, often tailored to speciﬁc modalities or disease
types, lack generalizability across the diverse spectrum of medical image
segmentation tasks. Here we present MedSAM, a foundation model designed
for bridging this gap by enabling universal medical image segmentation. The
model is developed on a large-scale medical image dataset with 1,570,263
image-mask pairs, covering 10 imaging modalities and over 30 cancer types.
We conduct a comprehensive evaluation on 86 internal validation tasks and 60
external validation tasks, demonstrating better accuracy and robustness than
modality-wise specialist models. By delivering accurate and efﬁcient seg-
mentation across a wide spectrum of tasks, MedSAM holds signiﬁcant
potential to expedite the evolution of diagnostic tools and the personalization
of treatment plans.

treatment planning,

Segmentation is a fundamental task in medical imaging analysis, which
involves identifying and delineating regions of interest (ROI) in various
medical images, such as organs, lesions, and tissues1. Accurate seg-
mentation is essential for many clinical applications, including disease
diagnosis,
and monitoring of disease
progression2,3. Manual segmentation has long been the gold standard
for delineating anatomical structures and pathological regions, but
this process is time-consuming, labor-intensive, and often requires a
high degree of expertise. Semi- or fully automatic segmentation
methods can signiﬁcantly reduce the time and labor required, increase
consistency, and enable the analysis of large-scale datasets4.

Deep learning-based models have shown great promise in medical
image segmentation due to their ability to learn intricate image fea-
tures and deliver accurate segmentation results across a diverse range
of tasks, from segmenting speciﬁc anatomical structures to identifying
pathological regions5. However, a signiﬁcant limitation of many cur-
rent medical image segmentation models is their task-speciﬁc nature.
These models are typically designed and trained for a speciﬁc seg-
mentation task, and their performance can degrade signiﬁcantly when
applied to new tasks or different types of imaging data6. This lack of
generality poses a substantial obstacle to the wider application of
these models in clinical practice. In contrast, recent advances in the

ﬁeld of natural image segmentation have witnessed the emergence of
segmentation foundation models, such as segment anything model
(SAM)7 and Segment Everything Everywhere with Multi-modal
prompts all at once8, showcasing remarkable versatility and perfor-
mance across various segmentation tasks.

There is a growing demand for universal models in medical image
segmentation: models that can be trained once and then applied to a
wide range of segmentation tasks. Such models would not only exhibit
heightened versatility in terms of model capacity but also potentially
lead to more consistent results across different tasks. However, the
applicability of the segmentation foundation models (e.g., SAM7) to
medical image segmentation remains limited due to the signiﬁcant
differences between natural images and medical images. Essentially,
SAM is a promptable segmentation method that requires points or
bounding boxes to specify the segmentation targets. This resembles
conventional interactive segmentation methods4,9–11 but SAM has bet-
ter generalization ability, while existing deep learning-based inter-
active segmentation methods focus mainly on limited tasks and image
modalities.

Many studies have applied the out-of-the-box SAM models to
typical medical image segmentation tasks12–17 and other challenging
scenarios18–21. For example, the concurrent studies22,23 conducted a

1Peter Munk Cardiac Centre, University Health Network, Toronto, ON, Canada. 2Department of Laboratory Medicine and Pathobiology, University of Toronto,
Toronto, ON, Canada. 3Vector Institute, Toronto, ON, Canada. 4Department of Computer Science, Western University, London, ON, Canada. 5Tandon School
of Engineering, New York University, New York, NY, USA. 6Department of Electrical Engineering, Yale University, New Haven, CT, USA. 7Department of
Computer Science, University of Toronto, Toronto, ON, Canada. 8UHN AI Hub, Toronto, ON, Canada.

e-mail: bowang@vectorinstitute.ai

Nature Communications |

 (2024) 15:654

1

Article

https://doi.org/10.1038/s41467-024-44824-z

comprehensive assessment of SAM across a diverse array of medical
images, underscoring that SAM achieved satisfactory segmentation
outcomes primarily on targets characterized by distinct boundaries.
However, the model exhibited substantial limitations in segmenting
typical medical targets with weak boundaries or low contrast. In con-
gruence with these observations, we further introduce MedSAM, a
reﬁned foundation model that signiﬁcantly enhances the segmenta-
tion performance of SAM on medical images. MedSAM accomplishes
this by ﬁne-tuning SAM on an unprecedented dataset with more than
one million medical image-mask pairs.

imaging modalities. Experimental

We thoroughly evaluate MedSAM through comprehensive
experiments on 86 internal validation tasks and 60 external validation
tasks, spanning a variety of anatomical structures, pathological con-
ditions, and medical
results
demonstrate that MedSAM consistently outperforms the state-of-the-
art (SOTA) segmentation foundation model7, while achieving perfor-
mance on par with, or even surpassing specialist models1,24 that were
trained on the images from the same modality. These results highlight
the potential of MedSAM as a new paradigm for versatile medical
image segmentation.

Results
MedSAM: a foundation model for promptable medical image
segmentation
MedSAM aims to fulﬁll the role of a foundation model for universal
medical image segmentation. A crucial aspect of constructing such a
model is the capacity to accommodate a wide range of variations in
imaging conditions, anatomical structures, and pathological condi-
tions. To address this challenge, we curated a diverse and large-scale

medical image segmentation dataset with 1,570,263 medical image-
mask pairs, covering 10 imaging modalities, over 30 cancer types, and
a multitude of
imaging protocols (Fig. 1 and Supplementary
Tables 1–4). This large-scale dataset allows MedSAM to learn a rich
representation of medical images, capturing a broad spectrum of
anatomies and lesions across different modalities. Figure 2a provides
an overview of the distribution of images across different medical
imaging modalities in the dataset, ranked by their total numbers. It is
evident that computed tomography (CT), magnetic resonance ima-
ging (MRI), and endoscopy are the dominant modalities, reﬂecting
their ubiquity in clinical practice. CT and MRI images provide detailed
cross-sectional views of 3D body structures, making them indis-
pensable for non-invasive diagnostic imaging. Endoscopy, albeit more
invasive, enables direct visual inspection of organ interiors, proving
invaluable for diagnosing gastrointestinal and urological conditions.
Despite the prevalence of these modalities, others such as ultrasound,
pathology, fundus, dermoscopy, mammography, and optical coher-
ence tomography (OCT) also hold signiﬁcant roles in clinical practice.
The diversity of these modalities and their corresponding segmenta-
tion targets underscores the necessity for universal and effective
segmentation models capable of handling the unique characteristics
associated with each modality.

Another critical consideration is the selection of the appropriate
segmentation prompt and network architecture. While the concept of
fully automatic segmentation foundation models is enticing, it is
fraught with challenges that make it impractical. One of the primary
challenges is the variability inherent in segmentation tasks. For
example, given a liver cancer CT image, the segmentation task can vary
depending on the speciﬁc clinical scenario. One clinician might be

Fig. 1 | MedSAM is trained on a large-scale dataset that can handle diverse segmentation tasks. The dataset covers a variety of anatomical structures, pathological
conditions, and medical imaging modalities. The magenta contours and mask overlays denote the expert annotations and MedSAM segmentation results, respectively.

Nature Communications |

 (2024) 15:654

2

Article

a

b

https://doi.org/10.1038/s41467-024-44824-z

Image
encoder

Mask decoder

Prompt encoder

Input Image

Image
embedding

Segmentation

Bounding box prompts

Fig. 2 | Overview of the modality distribution in the dataset and the network architecture. a The number of medical image-mask pairs in each modality. b MedSAM is a
promptable segmentation method where users can use bounding boxes to specify the segmentation targets. Source data are provided as a Source Data ﬁle.

interested in segmenting the liver tumor, while another might need to
segment the entire liver and surrounding organs. Additionally, the
variability in imaging modalities presents another challenge. Mod-
alities such as CT and MR generate 3D images, whereas others like
X-ray and ultrasound yield 2D images. These variabilities in task deﬁ-
nition and imaging modalities complicate the design of a fully auto-
matic model capable of accurately anticipating and addressing the
diverse requirements of different users.

Considering these challenges, we argue that a more practical
approach is to develop a promptable 2D segmentation model. The
model can be easily adapted to speciﬁc tasks based on user-provided
prompts, offering enhanced ﬂexibility and adaptability. It is also able
to handle both 2D and 3D images by processing 3D images as a series
of 2D slices. Typical user prompts include points and bounding boxes
and we show some segmentation examples with the different prompts
in Supplementary Fig. 1. It can be found that bounding boxes provide a
more unambiguous spatial context for the region of interest, enabling
the algorithm to more precisely discern the target area. This stands in
contrast to point-based prompts, which can introduce ambiguity,
particularly when proximate structures resemble each other. More-
over, drawing a bounding box is efﬁcient, especially in scenarios
involving multi-object segmentation. We follow the network archi-
tecture in SAM7, including an image encoder, a prompt encoder, and a
mask decoder (Fig. 2b). The image encoder25 maps the input image
into a high-dimensional image embedding space. The prompt encoder
transforms the user-drawn bounding boxes into feature representa-
tions via positional encoding26. Finally, the mask decoder fuses the
features using cross-attention27
image embedding and prompt
(Methods).

Quantitative and qualitative analysis
We evaluated MedSAM through both internal validation and external
validation. Speciﬁcally, we compared it to the SOTA segmentation
foundation model SAM7 as well as modality-wise specialist U-Net1 and
DeepLabV3+24 models. Each specialized model was trained on images
from the corresponding modality, resulting in 10 dedicated specialist
models for each method. During inference, these specialist models
were used to segment the images from corresponding modalities,
while SAM and MedSAM were employed for segmenting images across
all modalities (Methods). The internal validation contained 86 seg-
mentation tasks (Supplementary Tables 5–8 and Fig. 2), and Fig. 3a
shows the median dice similarity coefﬁcient (DSC) score of these tasks
for the four methods. Overall, SAM obtained the lowest performance
on most segmentation tasks although it performed promisingly on
some RGB image segmentation tasks, such as polyp (DSC: 91.3%,
interquartile range (IQR): 81.2–95.1%) segmentation in endoscopy
images. This could be attributed to SAM’s training on a variety of RGB
images, and the fact that many targets in these images are relatively
straightforward to segment due to their distinct appearances. The
other three models outperformed SAM by a large margin and MedSAM

has a narrower distribution of DSC scores of the 86 interval validation
tasks than the two groups of specialist models, reﬂecting the robust-
ness of MedSAM across different tasks. We further connected the DSC
scores corresponding to the same task of the four models with the
podium plot Fig. 3b, which is complementary to the box plot. In the
upper part, each colored dot denotes the median DSC achieved with
the respective method on one task. Dots corresponding to identical
test cases are connected by a line. In the lower part, the frequency of
achieved ranks for each method is presented with bar charts. It can be
found that MedSAM ranked in ﬁrst place on most tasks, surpassing the
performance of the U-Net and DeepLabV3+ specialist models that have
a high frequency of ranks with second and third places, respectively, In
contrast, SAM ranked last place in almost all tasks. Figure 3c (and
Supplementary Fig. 9) visualizes some randomly selected segmenta-
tion examples where MedSAM obtained a median DSC score, including
liver tumor in CT images, brain tumor in MR images, breast tumor in
ultrasound images, and polyp in endoscopy images. SAM struggles
with targets of weak boundaries, which is prone to under or over-
segmentation errors. In contrast, MedSAM can accurately segment a
wide range of targets across various imaging conditions, which
achieves comparable of even better than the specialist U-Net and
DeepLabV3+ models.

The external validation included 60 segmentation tasks, all of
which either were from new datasets or involved unseen segmen-
tation targets (Supplementary Tables 9–11 and Figs. 10–12). Fig-
ure 4a, b show the task-wise median DSC score distribution and their
correspondence of the 60 tasks, respectively. Although SAM con-
tinued exhibiting lower performance on most CT and MR segmen-
tation tasks,
the specialist models no longer consistently
outperformed SAM (e.g., right kidney segmentation in MR T1-
weighted images: 90.1%, 85.3%, 86.4% for SAM, U-Net, and Dee-
pLabV3+, respectively). This indicates the limited generalization
ability of such specialist models on unseen targets. In contrast,
MedSAM consistently delivers superior performance. For example,
MedSAM obtained median DSC scores of 87.8% (IQR: 85.0-91.4%) on
the nasopharynx cancer segmentation task, demonstrating 52.3%,
15.5%, and 22.7 improvements over SAM, the specialist U-Net, and
DeepLabV3+, respectively. Signiﬁcantly, MedSAM also achieved
better performance in some unseen modalities (e.g., abdomen T1
Inphase and Outphase), surpassing SAM and the specialist models
with improvements by up to 10%. Figure 4c presents four randomly
selected segmentation examples for qualitative evaluation, reveal-
ing that while all the methods have the ability to handle simple
segmentation targets, MedSAM performs better at segmenting
challenging targets with indistinguishable boundaries, such as cer-
vical cancer in MR images (more examples are presented in Sup-
plementary Fig. 13). Furthermore, we evaluated MedSAM on the
multiple myeloma plasma cell dataset, which represents a distinct
modality and task in contrast to all previously leveraged validation
tasks. Although this task had never been seen during training,

Nature Communications |

 (2024) 15:654

3

Article

https://doi.org/10.1038/s41467-024-44824-z

b

a

c

SAM

U-Net

DeepLabV3+

MedSAM

SAM

U-Net

DeepLabV3+

MedSAM

Fig. 3 | Quantitative and qualitative evaluation results on the internal
validation set. a Performance distribution of 86 internal validation tasks in terms
of median dice similarity coefﬁcient (DSC) score. The center line within the box
represents the median value, with the bottom and top bounds of the box deli-
neating the 25th and 75th percentiles, respectively. Whiskers are chosen to show
the 1.5 of the interquartile range. Up-triangles denote the minima and down-
triangles denote the maxima. b Podium plots for visualizing the performance
correspondence of 86 internal validation tasks. Upper part: each colored dot
denotes the median DSC achieved with the respective method on one task. Dots

corresponding to identical tasks are connected by a line. Lower part: bar charts
represent the frequency of achieved ranks for each method. MedSAM ranks in the
ﬁrst place on most tasks. c Visualized segmentation examples on the internal
validation set. The four examples are liver cancer, brain cancer, breast cancer, and
polyp in computed tomography (CT), (Magnetic Resonance Imaging) MRI, ultra-
sound, and endoscopy images, respectively. Blue: bounding box prompts; Yellow:
segmentation results. Magenta: expert annotations. Source data are provided as a
Source Data ﬁle.

b

a

c

SAM

U-Net

DeepLabV3+

MedSAM

SAM

U-Net

DeepLabV3+

MedSAM

Fig. 4 | Quantitative and qualitative evaluation results on the external
validation set. a Performance distribution of 60 external validation tasks in terms
of median dice similarity coefﬁcient (DSC) score. The center line within the box
represents the median value, with the bottom and top bounds of the box deli-
neating the 25th and 75th percentiles, respectively. Whiskers are chosen to show
the 1.5 of the interquartile range. Up-triangles denote the minima and down-
triangles denote the maxima. b Podium plots for visualizing the performance
correspondence of 60 external validation tasks. Upper part: each colored dot

denotes the median DSC achieved with the respective method on one task. Dots
corresponding to identical tasks are connected by a line. Lower part: bar charts
represent the frequency of achieved ranks for each method. MedSAM ranks in the
ﬁrst place on most tasks. c Visualized segmentation examples on the external
validation set. The four examples are the lymph node, cervical cancer, fetal head,
and polyp in CT, MR, ultrasound, and endoscopy images, respectively. Source data
are provided as a Source Data ﬁle.

Nature Communications |

 (2024) 15:654

4

Article

https://doi.org/10.1038/s41467-024-44824-z

MedSAM still exhibited superior performance compared to the SAM
(Supplementary Fig. 14), highlighting its remarkable generalization
ability.

The effect of training dataset size
We also investigated the effect of varying dataset sizes on MedSAM’s
performance because the training dataset size has been proven to be
pivotal in model performance28. We additionally trained MedSAM on
two different dataset sizes: 10,000 (10K) and 100,000 (100K) images
and their performances were compared with the default MedSAM
model. The 10K and 100K training images were uniformly sampled
from the whole training set, to maintain data diversity. As shown in
(Fig. 5a) (Supplementary Tables 12–14), the performance adhered to
the scaling rule, where increasing the number of training images sig-
niﬁcantly improved the performance in both internal and external
validation sets.

MedSAM can improve the annotation efﬁciency
Furthermore, we conducted a human annotation study to assess the
time cost of two pipelines (Methods). For the ﬁrst pipeline, two human
experts manually annotate 3D adrenal tumors in a slice-by-slice way. For
the second pipeline, the experts ﬁrst drew the long and short tumor axes
with the linear marker (initial marker) every 3-10 slices, which is a com-
mon practice in tumor response evaluation. Then, MedSAM was used to
segment the tumors based on these sparse linear annotations. Finally,
the expert manually revised the segmentation results until they were
satisﬁed. We quantitatively compared the annotation time cost between
the two pipelines (Fig. 5b). The results demonstrate that with the assis-
tance of MedSAM, the annotation time is substantially reduced by
82.37% and 82.95% for the two experts, respectively.

Discussion
We introduce MedSAM, a deep learning-powered foundation model
designed for the segmentation of a wide array of anatomical structures
and lesions across diverse medical imaging modalities. MedSAM is
trained on a meticulously assembled large-scale dataset comprised of
over one million medical image-mask pairs. Its promptable conﬁg-
uration strikes an optimal balance between automation and customi-
zation, rendering MedSAM a versatile tool for universal medical image
segmentation.

Through comprehensive evaluations encompassing both internal
and external validation, MedSAM has demonstrated substantial cap-
abilities in segmenting a diverse array of targets and robust general-
ization abilities to manage new data and tasks. Its performance not
only signiﬁcantly exceeds that of existing the state-of-the-art seg-
mentation foundation model, but also rivals or even surpasses spe-
cialist models. By providing precise delineation of anatomical
structures and pathological regions, MedSAM facilitates the compu-
tation of various quantitative measures that serve as biomarkers. For

instance, in the ﬁeld of oncology, MedSAM could play a crucial role in
accelerating the 3D tumor annotation process, enabling subsequent
calculations of tumor volume, which is a critical biomarker29 for
assessing disease progression and response to treatment. Additionally,
MedSAM provides a successful paradigm for adapting natural image
foundation models to new domains, which can be further extended to
biological image segmentation30, such as cell segmentation in light
microscopy images31 and organelle segmentation in electron micro-
scopy images32.

While MedSAM boasts strong capabilities, it does present certain
limitations. One such limitation is the modality imbalance in the
training set, with CT, MRI, and endoscopy images dominating the
dataset. This could potentially impact the model’s performance on
less-represented modalities, such as mammography. Another limita-
tion is its difﬁculty in the segmentation of vessel-like branching
structures because the bounding box prompt can be ambiguous in this
setting. For example, arteries and veins share the same bounding box
in eye fundus images. However, these limitations do not diminish
MedSAM’s utility. Since MedSAM has learned rich and representative
medical image features from the large-scale training set, it can be ﬁne-
tuned to effectively segment new tasks from less-represented mod-
alities or intricate structures like vessels.

In conclusion, this study highlights the feasibility of constructing a
single foundation model capable of managing a multitude of seg-
mentation tasks, thereby eliminating the need for task-speciﬁc models.
MedSAM, as the inaugural foundation model in medical image seg-
mentation, holds great potential to accelerate the advancement of new
diagnostic and therapeutic tools, and ultimately contribute to
improved patient care33.

Methods
Dataset curation and pre-processing
We curated a comprehensive dataset by collating images from publicly
available medical image segmentation datasets, which were obtained
from various sources across the internet, including the Cancer Imaging
Archive (TCIA)34, Kaggle, Grand-Challenge, Scientiﬁc Data, CodaLab,
and segmentation challenges in the Medical Image Computing and
Computer Assisted Intervention Society (MICCAI). All the datasets
provided segmentation annotations by human experts, which have
been widely used in existing literature (Supplementary Table 1–4). We
incorporated these annotations directly for both model development
and validation.

The original 3D datasets consisted of computed tomography (CT)
and magnetic resonance (MR) images in DICOM, nrrd, or mhd formats.
To ensure uniformity and compatibility with developing medical
image deep learning models, we converted the images to the widely
used NifTI format. Additionally, grayscale images (such as X-Ray and
Ultrasound) as well as RGB images (including endoscopy, dermoscopy,
fundus, and pathology images), were converted to the png format.

Fig. 5 | The effect of training dataset size and a user study of tumor annotation
efﬁciency. a Scaling up the training image size to one million can signiﬁcantly
improve the model performance on both internal and external validation sets.

b MedSAM can be used to substantially reduce the annotation time cost. Source
data are provided as a Source Data ﬁle.

Nature Communications |

 (2024) 15:654

5

Article

https://doi.org/10.1038/s41467-024-44824-z

Several exclusive criteria are applied to improve the dataset quality
and consistency, including incomplete images and segmentation tar-
gets with branching structures,
inaccurate annotations, and tiny
volumes. Notably, image intensities varied signiﬁcantly across differ-
ent modalities. For instance, CT images had intensity values ranging
from -2000 to 2000, while MR images exhibited a range of 0 to 3000.
In endoscopy and ultrasound images, intensity values typically span-
ned from 0 to 255. To facilitate stable training, we performed intensity
normalization across all
images, ensuring they shared the same
intensity range.

For CT images, we initially normalized the Hounsﬁeld units using
typical window width and level values. The employed window width
and level values for soft tissues, lung, and brain are (W:400, L:40),
(W:1500, L:-160), and (W:80, L:40), respectively. Subsequently, the
intensity values were rescaled to the range of [0, 255]. For MR, X-ray,
ultrasound, mammography, and optical coherence tomography (OCT)
images, we clipped the intensity values to the range between the 0.5th
and 99.5th percentiles before rescaling them to the range of [0, 255].
Regarding RGB images (e.g., endoscopy, dermoscopy, fundus, and
pathology images), if they were already within the expected intensity
range of [0, 255], their intensities remained unchanged. However, if
they fell outside this range, we utilized max-min normalization to
rescale the intensity values to [0, 255]. Finally, to meet the model’s
input requirements, all images were resized to a uniform size of
1024 × 1024 × 3. In the case of whole-slide pathology images, patches
were extracted using a sliding window approach without overlaps. The
patches located on boundaries were padded to this size with 0. As for
3D CT and MR images, each 2D slice was resized to 1024 × 1024, and
the channel was repeated three times to maintain consistency. The
remaining 2D images were directly resized to 1024 × 1024 × 3. Bi-cubic
interpolation was used for resizing images, while nearest-neighbor
interpolation was applied for resizing masks to preserve their precise
boundaries and avoid introducing unwanted artifacts. These standar-
dization procedures ensured uniformity and compatibility across all
images and facilitated seamless integration into the subsequent stages
of the model training and evaluation pipeline.

Network architecture
The network utilized in this study was built on transformer
architecture27, which has demonstrated remarkable effectiveness in
various domains such as natural language processing and image
recognition tasks25. Speciﬁcally, the network incorporated a vision
transformer (ViT)-based image encoder responsible for extracting
image features, a prompt encoder for integrating user interactions
(bounding boxes), and a mask decoder that generated segmentation
results and conﬁdence scores using the image embedding, prompt
embedding, and output token.

To strike a balance between segmentation performance and com-
putational efﬁciency, we employed the base ViT model as the image
encoder since extensive evaluation indicated that larger ViT models,
such as ViT Large and ViT Huge, offered only marginal improvements in
accuracy7 while signiﬁcantly increasing computational demands. Speci-
ﬁcally, the base ViT model consists of 12 transformer layers27, with each
block comprising a multi-head self-attention block and a Multilayer
Perceptron (MLP) block incorporating layer normalization35. Pre-training
was performed using masked auto-encoder modeling36, followed by
fully supervised training on the SAM dataset7. The input image
(1024 × 1024 × 3) was reshaped into a sequence of ﬂattened 2D patches
with the size 16 × 16 × 3, yielding a feature size in image embedding of
64 × 64 after passing through the image encoder, which is 16 × down-
scaled. The prompt encoders mapped the corner point of the bounding
box prompt to 256-dimensional vectorial embeddings26. In particular,
each bounding box was represented by an embedding pair of the top-
left corner point and the bottom-right corner point. To facilitate real-
time user interactions once the image embedding had been computed, a

lightweight mask decoder architecture was employed. It consists of two
transformer layers27 for fusing the image embedding and prompt
encoding, and two transposed convolutional layers to enhance the
embedding resolution to 256 × 256. Subsequently, the embedding
underwent sigmoid activation, followed by bi-linear interpolations to
match the input size.

Training protocol and experimental setting
During data pre-processing, we obtained 1,570,263 medical image-
mask pairs for model development and validation. For internal vali-
dation, we randomly split the dataset into 80%, 10%, and 10% as
training, tuning, and validation, respectively. Speciﬁcally, for mod-
alities where within-scan continuity exists, such as CT and MRI, and
modalities where continuity exists between consecutive frames, we
performed the data splitting at the 3D scan and the video level
respectively, by which any potential data leak was prevented. For
pathology images, recognizing the signiﬁcance of slide-level cohe-
siveness, we ﬁrst separated the whole-slide images into distinct slide-
based sets. Then, each slide was divided into small patches with a ﬁxed
size of 1024 × 1024. This setup allowed us to monitor the model’s
performance on the tuning set and adjust its parameters during
training to prevent overﬁtting. For the external validation, all datasets
were held out and did not appear during model training. These data-
sets provide a stringent test of the model’s generalization ability, as
they represent new patients, imaging conditions, and potentially new
segmentation tasks that the model has not encountered before. By
evaluating the performance of MedSAM on these unseen datasets, we
can gain a realistic understanding of how MedSAM is likely to perform
in real-world clinical settings, where it will need to handle a wide range
of variability and unpredictability in the data. The training and vali-
dation are independent.

The model was initialized with the pre-trained SAM model with
the ViT-Base model. We ﬁxed the prompt encoder since it can already
encode the bounding box prompt. All the trainable parameters in the
image encoder and mask decoder were updated during training.
Speciﬁcally, the number of trainable parameters for the image encoder
and mask decoder are 89,670,912 and 4,058,340, respectively. The
bounding box prompt was simulated from the expert annotations with
a random perturbation of 0-20 pixels. The loss function is the
unweighted sum between dice loss and cross-entropy loss, which has
been proven to be robust in various segmentation tasks1. The network
was optimized by AdamW37 optimizer (β1 = 0.9, β2 = 0.999) with an
initial learning rate of 1e-4 and a weight decay of 0.01. The global batch
size was 160 and data augmentation was not used. The model was
trained on 20 A100 (80G) GPUs with 150 epochs and the last check-
point was selected as the ﬁnal model.

Furthermore, to thoroughly evaluate the performance of Med-
SAM, we conducted comparative analyses against both the state-of-
the-art segmentation foundation model SAM7 and specialist models
(i.e., U-Net1 and DeepLabV3+24). The training images contained 10
modalities: CT, MR, chest X-ray (CXR), dermoscopy, endoscopy,
ultrasound, mammography, OCT, and pathology, and we trained the
U-Net and DeepLabV3+ specialist models for each modality. There
were 20 specialist models in total and the number of corresponding
training images was presented in Supplementary Table 5. We
employed the nnU-Net to conduct all U-Net experiments, which can
automatically conﬁgure the network architecture based on the dataset
properties. In order to incorporate the bounding box prompt into the
model, we transformed the bounding box into a binary mask and
concatenated it with the image as the model input. This function was
originally supported by nnU-Net in the cascaded pipeline, which has
demonstrated increased performance in many segmentation tasks by
using the binary mask as an additional channel to specify the target
location. The training settings followed the default conﬁgurations of
2D nnU-Net. Each model was trained on one A100 GPU with 1000

Nature Communications |

 (2024) 15:654

6

Article

https://doi.org/10.1038/s41467-024-44824-z

epochs and the last checkpoint was used as the ﬁnal model. The
DeepLabV3+ specialist models used ResNet5038 as the encoder. Similar
to ref. 3, the input images were resized to 224 × 224 × 3. The bounding
box was transformed into a binary mask as an additional input channel
to provide the object location prompt. Segmentation Models Pytorch
(0.3.3)39 was used to perform training and inference for all the
modality-wise specialist DeepLabV3 + models. Each modality-wise
model was trained on one A100 GPU with 500 epochs and the last
checkpoint was used as the ﬁnal model. During the inference phase,
SAM and MedSAM were used to perform segmentation across all
modalities with a single model. In contrast, the U-Net and DeepLabV3+
specialist models were used to individually segment the respective
corresponding modalities.

A task-speciﬁc segmentation model might outperform a modality-
based one for certain applications. Since U-Net obtained better per-
formance than DeepLabV3+ on most tasks, we further conducted a
comparison study by training task-speciﬁc U-Net models on four
representative tasks, including liver cancer segmentation in CT scans,
abdominal organ segmentation in MR scans, nerve cancer segmenta-
tion in ultrasound, and polyp segmentation in endoscopy images. The
experiments included both internal validation and external validation.
For internal validation, we adhered to the default data splits, using
them to train the task-speciﬁc U-Net models and then evaluate their
performance on the corresponding validation set. For external vali-
dation, the trained U-Net models were evaluated on new datasets from
the same modality or segmentation targets. In all these experiments,
MedSAM was directly applied to the validation sets without additional
ﬁne-tuning. As shown in Supplementary Fig. 15, while task-speciﬁc U-
Net models often achieved great results on internal validation sets,
their performance diminished signiﬁcantly for external sets. In con-
trast, MedSAM maintained consistent performance across both inter-
nal and external validation sets. This underscores MedSAM’s superior
generalization ability, making it a versatile tool in a variety of medical
image segmentation tasks.

Loss function
We used the unweighted sum between cross-entropy loss and dice
loss40 as the ﬁnal loss function since it has been proven to be robust
across different medical image segmentation tasks41. Speciﬁcally, let
S, G denote the segmentation result and ground truth, respectively.
si, gi denotes the predicted segmentation and ground truth of voxel i,
respectively. N is the number of voxels in the image I. Binary cross-
entropy loss is deﬁned by

LBCE = (cid:1)

1
N

XN

(cid:2)

i = 1

(cid:3)
gi log si + ð1 (cid:1) giÞ logð1 (cid:1) siÞ

,

and dice loss is deﬁned by

LDice = 1 (cid:1)

The ﬁnal loss L is deﬁned by

P

P
N

2
i = 1 ðgiÞ2 +

N
i = 1 gisi
P
N

i = 1 ðsiÞ2

:

L = LBCE + LDice

:

ð1Þ

ð2Þ

ð3Þ

Human annotation study
The objective of the human annotation study was to quantitatively
evaluate how MedSAM can reduce the annotation time cost. Speciﬁ-
cally, we used the recent adrenocortical carcinoma CT dataset34,42,43,
where the segmentation target, adrenal tumor, was neither part of the
training nor of the existing validation sets. We randomly sampled 10
cases, comprising a total of 733 tumor slices requiring annotations.
Two human experts participated in this study, both of whom are

experienced radiologists with 8 and 6 years of clinical practice in
abdominal diseases, respectively. Each expert generated two groups of
annotations, one with the assistance of MedSAM and one without.

In the ﬁrst group, the experts manually annotated the 3D adrenal
tumor in a slice-by-slice manner. Annotations by the two experts were
conducted independently, with no collaborative discussions, and the
time taken for each case was recorded. In the second group, annota-
tions were generated after one week of cooling period. The experts
independently drew the long and short tumor axes as initial markers,
which is a common practice in tumor response evaluation. This pro-
cess was executed every 3-10 slices from the top slice to the bottom
slice of the tumor. Then, we applied MedSAM to segment the tumors
based on these sparse linear annotations, including three steps.

(cid:129)

(cid:129)

(cid:129)

Step 1. For each annotated slice, a rectangle binary mask was
generated based on the linear label that can completely cover
the linear label.
Step 2. For the unlabeled slices, the rectangle binary masks were
created through interpolation of the surrounding labeled slices.
Step 3. We transformed the binary masks into bounding boxes
and then fed them along with the images into MedSAM to gen-
erate segmentation results.

All these steps were conducted in an automatic way and the model
running time was recorded for each case. Finally, human experts
manually reﬁned the segmentation results until they met their satis-
faction. To summarize, the time cost of the second group of annota-
tions contained three parts: initial markers, MedSAM inference, and
reﬁnement. All the manual annotation processes were based on ITK-
SNAP44, an open-source software designed for medical image visuali-
zation and annotation.

Evaluation metrics
We followed the recommendations in Metrics Reloaded45 and used the
dice similarity coefﬁcient and normalized surface distance (NSD) to
quantitatively evaluate the segmentation results. DSC is a region-based
segmentation metric, aiming to evaluate the region overlap between
expert annotation masks and segmentation results, which is deﬁned by

DSCðG, SÞ =

2jG \ Sj
jGj + jSj

,

NSD46 is a boundary-based metric, aiming to evaluate the boundary
consensus between expert annotation masks and segmentation results
at a given tolerance, which is deﬁned by

NSDðG, SÞ =

j∂G \ BðτÞ

∂S j + j∂S \ BðτÞ
∂Gj
j∂Gj + j∂Sj

,

∂G = fx 2 R3 j 9~x 2 ∂G, jjx (cid:1) ~xjj ≤ τg, BðτÞ

where BðτÞ
∂S = fx 2 R3 j 9~x 2 ∂S, jjx (cid:1)
~xjj ≤ τg denote the border region of the expert annotation mask and
the segmentation surface at tolerance τ, respectively. In this paper, we
set the tolerance τ as 2.

Statistical analysis
To statistically analyze and compare the performance of the afore-
mentioned four methods (MedSAM, SAM, U-Net, and DeepLabV3+
specialist models), we employed the Wilcoxon signed-rank test. This
non-parametric test is well-suited for comparing paired samples and is
particularly useful when the data does not meet the assumptions of
normal distribution. This analysis allowed us to determine if any
method demonstrated statistically superior segmentation perfor-
mance compared to the others, providing valuable insights into the
comparative effectiveness of the evaluated methods. The Wilcoxon
signed-rank test results are marked on the DSC and NSD score tables
(Supplementary Table 6–11).

Nature Communications |

 (2024) 15:654

7

Article

https://doi.org/10.1038/s41467-024-44824-z

Software utilized
All code was implemented in Python (3.10) using Pytorch (2.0) as the
base deep learning framework. We also used several Python packages
including connected-
for data analysis and results visualization,
components-3d (3.10.3), SimpleITK (2.2.1), nibabel (5.1.0), torchvision
(0.15.2), numpy (1.24.3), scikit-image (0.20.0), scipy (1.10.1), and pan-
das (2.0.2), matplotlib (3.7.1), opencv-python (4.8.0), ChallengeR
(1.0.5), and plotly (5.15.0). Biorender was used to create Fig. 1.

Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.

Data availability
The training and validating datasets used in this study are available in
the public domain and can be downloaded via the links provided in
Supplementary Tables 16 and 17. Source data are provided with this
paper in the Source Data ﬁle. We conﬁrmed that All the image datasets
in this study are publicly accessible and permitted for research pur-
poses. Source data are provided in this paper.

Code availability
The training script, inference script, and trained model have been
publicly available at https://github.com/bowang-lab/MedSAM. A per-
manent version is released on Zenodo47.

References
1.

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J. & Maier-Hein, K. H.
nnU-Net: a self-conﬁguring method for deep learning-based bio-
medical image segmentation. Nat. Method. 18, 203–211 (2021).
2. De Fauw, J. Clinically applicable deep learning for diagnosis and
referral in retinal disease. Nat. Med. 24, 1342–1350 (2018).

3. Ouyang, D. Video-based AI for beat-to-beat assessment of cardiac

function. Nature 580, 252–256 (2020).

4. Wang, G. Deepigeos: a deep interactive geodesic framework for

medical image segmentation. In IEEE Transactions on Pattern Ana-
lysis and Machine Intelligence 41, 1559–1572 (IEEE, 2018).

5. Antonelli, M. The medical segmentation decathlon. Nat. Commun.

13, 4128 (2022).

7.

6. Minaee, S. Image segmentation using deep learning: A survey. In
IEEE Transactions on Pattern Analysis and Machine Intelligence 44,
3523–3542 (IEEE, 2021).
Kirillov, A. et al. Segment anything. In IEEE International Conference
on Computer Vision. 4015–4026 (IEEE, 2023).
Zou, X. et al. Segment everything everywhere all at once. In
Advances in Neural Information Processing Systems (MIT
Press, 2023).

8.

15. Roy, S. et al. SAM.MD: zero-shot medical image segmentation

capabilities of the segment anything model. Preprint at https://
arxiv.org/abs/2304.05396 (2023).

16. Zhou, T., Zhang, Y., Zhou, Y., Wu, Y. & Gong, C. Can SAM segment
polyps? Preprint at https://arxiv.org/abs/2304.07583 (2023).
17. Mohapatra, S., Gosai, A., Schlaug, G. Sam vs bet: a comparative

study for brain extraction and segmentation of magnetic resonance
images using deep learning. Preprint at https://arxiv.org/abs/2304.
04738 (2023).

18. Chen, J., Bai, X. Learning to" segment anything" in thermal infrared

images through knowledge distillation with a large scale dataset
SATIR. Preprint at https://arxiv.org/abs/2304.07969 (2023).
19. Tang, L., Xiao, H., Li, B. Can SAM segment anything? when SAM

meets camouﬂaged object detection. Preprint at https://arxiv.org/
abs/2304.04709 (2023).

20. Ji, G.-P. et al. SAM struggles in concealed scenes–empirical study
on” segment anything”. Science China Information Sciences. 66,
226101 (2023).
Ji, W., Li, J., Bi, Q., Li, W., Cheng, L. Segment anything is not always
perfect: an investigation of SAM on different real-world applica-
tions. Preprint at https://arxiv.org/abs/2304.05750 (2023).
22. Mazurowski, M. A. Segment anything model for medical image

21.

analysis: an experimental study. Med. Image Anal. 89,
102918 (2023).

23. Huang, Y. et al. Segment anything model for medical images? Med.

Image Anal. 92, 103061 (2024).

24. Chen, L.-C., Zhu, Y., Papandreou, G., Schroff, F., Adam, H. Encoder-
decoder with atrous separable convolution for semantic image
segmentation. In Proc. European Conference on Computer Vision.
801–818 (IEEE, 2018).

25. Dosovitskiy, A. et al. An image is worth 16x16 words: transformers
for image recognition at scale. In: International Conference on
Learning Representations (OpenReview.net, 2020).

26. Tancik, M. Fourier features let networks learn high frequency
functions in low-dimensional domains. In Advances in Neural
Information Processing Systems 33, 7537–7547 (Curran Associates,
Inc., 2020).

27. Vaswani, A. et al. Attention is all you need. In Advances in Neural
Information Processing Systems, Vol. 30 (Curran Associates,
Inc., 2017).

28. He, B. Blinded, randomized trial of sonographer versus AI cardiac

function assessment. Nature 616, 520–524 (2023).

29. Eisenhauer, E. A. New response evaluation criteria in solid tumours:

revised recist guideline (version 1.1). Eur. J. Cancer 45,
228–247 (2009).

30. Ma, J. & Wang, B. Towards foundation models of biological image

segmentation. Nat. Method. 20, 953–955 (2023).

9. Wang, G. Interactive medical image segmentation using deep

31. Ma, J. et al. The multi-modality cell segmentation challenge:

learning with image-speciﬁc ﬁne tuning. In IEEE Transactions on
Medical Imaging 37, 1562–1573 (IEEE, 2018).

towards universal solutions. Preprint at https://arxiv.org/abs/2308.
05864 (2023).

10. Zhou, T. Volumetric memory network for interactive medical image

32. Xie, R., Pang, K., Bader, G.D., Wang, B. Maester: masked auto-

11.

segmentation. Med. Image Anal. 83, 102599 (2023).
Luo, X. Mideepseg: Minimally interactive segmentation of unseen
objects from medical images using deep learning. Med. Image Anal.
72, 102102 (2021).

12. Deng, R. et al. Segment anything model (SAM) for digital pathology:
assess zero-shot segmentation on whole slide imaging. Preprint at
https://arxiv.org/abs/2304.04155 (2023).

13. Hu, C., Li, X. When SAM meets medical images: an investigation of
segment anything model (SAM) on multi-phase liver tumor seg-
mentation. Preprint at https://arxiv.org/abs/2304.08506
(2023).

14. He, S., Bao, R., Li, J., Grant, P.E., Ou, Y. Accuracy of segment-

anything model (SAM) in medical image segmentation tasks. Pre-
print at https://doi.org/10.48550/arXiv.2304.09324 (2023).

encoder guided segmentation at pixel resolution for accurate, self-
supervised subcellular structure recognition. In IEEE Conference on
Computer Vision and Pattern Recognition. 3292–3301 (IEEE, 2023).
33. Bera, K., Braman, N., Gupta, A., Velcheti, V. & Madabhushi, A. Pre-
dicting cancer outcomes with radiomics and artiﬁcial intelligence in
radiology. Nat. Rev. Clin. Oncol. 19, 132–146 (2022).

34. Clark, K. The cancer imaging archive (TCIA): maintaining and

operating a public information repository. J. Digit. Imaging 26,
1045–1057 (2013).

35. Ba, J.L., Kiros, J.R., Hinton, G.E. Layer normalization. Preprint at

https://arxiv.org/abs/1607.06450 (2016).

36. He, K. et al. Masked autoencoders are scalable vision learners. In
Proc. IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 16000–16009 (IEEE, 2022).

Nature Communications |

 (2024) 15:654

8

Article

https://doi.org/10.1038/s41467-024-44824-z

37. Loshchilov, I., Hutter, F. Decoupled weight decay regularization. In
International Conference on Learning Representations (Open-
Review.net, 2019).

39.

38. He, K., Zhang, X., Ren, S., Sun, J. Deep residual learning for image
recognition. In Proc. IEEE Conference on Computer Vision and Pat-
tern Recognition. 770–778 (IEEE, 2016).
Iakubovskii, P. Segmentation models pytorch. GitHub https://
github.com/qubvel/segmentation_models.pytorch (2019).
40. Milletari, F., Navab, N., Ahmadi, S.-A. V-net: Fully convolutional
neural networks for volumetric medical image segmentation. In
International Conference on 3D Vision (3DV). 565–571
(IEEE, 2016).

41. Ma, J. Loss odyssey in medical image segmentation. Med. Image

Anal. 71, 102035 (2021).

42. Ahmed, A. Radiomic mapping model for prediction of Ki-67
expression in adrenocortical carcinoma. Clin. Radiol. 75,
479–17 (2020).

43. Moawad, A.W. et al. Voxel-level segmentation of pathologically-

Author contributions
Conceived and designed the experiments: J.M. Y.H., C.Y., B.W. Per-
formed the experiments: J.M. Y.H., F.L., L.H., C.Y. Analyzed the data: J.M.
Y.H., F.L., L.H., C.Y., B.W. Wrote the paper: J.M. Y.H., F.L., L.H., C.Y., B.W.
All authors have read and agreed to the published version of the
manuscript.

Competing interests
The authors declare no competing interests

Additional information
Supplementary information The online version contains
supplementary material available at
https://doi.org/10.1038/s41467-024-44824-z.

Correspondence and requests for materials should be addressed to Bo
Wang.

proven Adrenocortical carcinoma with Ki-67 expression (Adrenal-
ACC-Ki67-Seg) [data set]. https://doi.org/10.7937/1FPG-
VM46 (2023).

Peer review information Nature Communications thanks David Ouyang,
and the other, anonymous, reviewer(s) for their contribution to the peer
review of this work. A peer review ﬁle is available.

44. Yushkevich, P.A., Gao, Y., Gerig, G. Itk-snap: an interactive tool for

semi-automatic segmentation of multi-modality biomedical ima-
ges. In International Conference of the IEEE Engineering in Medicine
and Biology Society (EMBC). 3342–3345 (IEEE, 2016).

45. Maier-Hein, L. et al. Metrics reloaded: Pitfalls and recommendations
for image analysis validation. Preprint at https://arxiv.org/abs/
2206.01653 (2022).

46. DeepMind surface-distance. https://github.com/google-

deepmind/surface-distance (2018).

47. Ma, J. bowang-lab/MedSAM: v1.0.0. https://doi.org/10.5281/

zenodo.10452777 (2023).

Acknowledgements
This work was supported by the Natural Sciences and Engineering
Research Council of Canada (NSERC, RGPIN-2020-06189 and DGECR-
2020-00294) and CIFAR AI Chair programs. The authors of this paper
highly appreciate all the data owners for providing public medical
images to the community. We also thank Meta AI for making the source
code of segment anything publicly available to the community. This
research was enabled in part by computing resources provided by the
Digital Research Alliance of Canada.

Reprints and permissions information is available at
http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if
changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit http://creativecommons.org/
licenses/by/4.0/.

© The Author(s) 2024

Nature Communications |

 (2024) 15:654

9

