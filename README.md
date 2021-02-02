# Hybrid-CT-CAPS

Recently, we have proposed a fully-automated framework
based on Capsule Networks, referred to as the <a href="https://github.com/ShahinSHH/CT-CAPS">CT-CAPS</a>, to distinguish
COVID-19 infection from normal and Community Acquired
Pneumonia (CAP) cases using chest Computed Tomography (CT)
scans which is published at the <a href="https://2021.ieeeicassp.org">IEEE ICASSP 2021</a>.
In our next attemp to increase the accuracy,validity, and explainability of the results, we have augmented the CT-CAPS model with a wide range of clinical/demographic data, including <b>patients’ gender, age, weight and symptoms</b>. More specifically,
we proposed a <b>Hybrid Deep Learning Model</b> that utilizes both clinical/
demographic data and CT scans to classify COVID-19 and
non-COVID cases using a Random Forest Classifier. The proposed
hybrid model specifies the most important predictive factors increasing
the explainability of the model. The experimental results
show that the proposed hybrid model improves the CT-CAPS performance,
achieving <b>accuracy of 90.8%, sensitivity of 94.5% and
specificity of 86.0%</b>.

## Code and Data
<ul>
 <li><b>Hybrid_CT_Data_Numeric.csv : </b>The Clinical data and the corresponding probability scores created by the CT-CAPS model are included in this CSV file .</li>
<li><b>clinical_data_COVID_CT_MD.csv : </b> The raw clinical data before filling the missing values and numerization are also available in this file.
The missing weights are filled with the average weights associated with the patient's gender. For 2 patients for which the symptom indications are not available, the corresponding columns are filled with 0. </li>

<li> <b>RF.py : </b> Implementation of the Random Forest model proposed in this study to integrate clinical data and the probability scores created by the CT-CAPS framework
</li>
<li><b>CT Scan Dataset :</b> In this study, processing the CT scans from the first step is not required, as all the CT-CAPS outputs are provided. However, if you're interested in the source of the data, the chest CT scans used in this study, are accessible through <a href="https://github.com/ShahinSHH/COVID-CT-MD">https://github.com/ShahinSHH/COVID-CT-MD</a>. </li>
</ul>

<img src="https://github.com/ShahinSHH/Hybrid-CT-CAPS/blob/main/pipeline.png" width="600" height="400" />


## Sample Decision Tree
In order to visualize the decision making procedure occurring
inside the RF classifiers, the internal structure of one of the
decision trees created by the proposed hybrid model is presented below. In this figure, the nodes and branches correspond to the split functions,
features, and thresholding values.

<img src="https://github.com/ShahinSHH/Hybrid-CT-CAPS/blob/main/tree.png" width="400" height="600" />


