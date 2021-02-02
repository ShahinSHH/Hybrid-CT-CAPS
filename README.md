# Hybrid-CT-CAPS

Recently, we have proposed a fully-automated framework
based on Capsule Networks, referred to as the <a href="https://github.com/ShahinSHH/CT-CAPS">CT-CAPS</a>, to distinguish
COVID-19 infection from normal and Community Acquired
Pneumonia (CAP) cases using chest Computed Tomography (CT)
scans which is published at the <a href="https://2021.ieeeicassp.org">IEEE ICASSP 2021</a>.
In our next attemp to incerease the accuracy, validity, and explainability of the results, we have augmented the CT-CAPS model with a wide range of clinical/demographic data, including <b>patients’ gender, age, weight and symptoms</b>. More specifically,
we proposed a <b>Hybrid Deep Learning Model</b> that utilizes both clinical/
demographic data and CT scans to classify COVID-19 and
non-COVID cases using a Random Forest Classifier. The proposed
hybrid model specifies the most important predictive factors increasing
the explainability of the model. The experimental results
show that the proposed hybrid model improves the CT-CAPS performance,
achieving <b>accuracy of 90.8%, sensitivity of 94.5% and
specificity of 86.0%</b>.
