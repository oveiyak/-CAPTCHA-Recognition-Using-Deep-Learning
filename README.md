# CAPTCHA Recognition Using Deep Learning

## Project Overview

This project explores automated CAPTCHA recognition using deep learning and Optical Character Recognition (OCR).

It implements a Convolutional Recurrent Neural Network (CRNN) architecture combining CNN and Bidirectional LSTM layers to recognise character sequences from CAPTCHA images.

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- CNN
- Bidirectional LSTM
- Connectionist Temporal Classification (CTC) Loss

## Model Architecture

The recognition pipeline consists of:

1. **Image Preprocessing:** CAPTCHA images are loaded, converted into model-compatible inputs and preprocessed.
2. **Feature Extraction:** CNN layers extract visual features from CAPTCHA images.
3. **Sequence Learning:** Bidirectional LSTM layers learn sequential character patterns.
4. **Sequence Prediction:** CTC loss enables sequence learning without requiring character-level segmentation.
5. **Decoding:** CTC decoding converts model predictions into readable CAPTCHA text.

## Repository Structure

- `notebooks/` – Model development, training and inference notebooks.
- `src/` – Supporting Python scripts.
- `docs/` – Project documentation and inference analysis.

## Dataset

The model uses CAPTCHA images and their corresponding labels.

The dataset is not included in this repository. You will need to configure the dataset directory before running the notebooks.

## Running the Project

1. Clone this repository.
2. Install the required Python packages.
3. Configure the CAPTCHA dataset directory.
4. Open the notebooks using Jupyter Notebook or Google Colab.
5. Execute the preprocessing, training and prediction steps.

## Project Status

Academic deep learning project involving CAPTCHA recognition, model training and inference.
