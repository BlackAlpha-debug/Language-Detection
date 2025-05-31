Sure! Here's a clean, professional version of the `README.md` file **without emojis**:

---

# Language Recognition Classifier

This project applies Natural Language Processing (NLP) and Machine Learning techniques to classify the **language** of a given text input. Two classifiers are used for comparison: **Decision Tree** and **Multinomial Naive Bayes**.

## Dataset

The dataset used is a CSV file with the following relevant columns:

* `Text`: The text input in different languages.
* `language`: The corresponding language label.

### Example

| Text                | Language |
| ------------------- | -------- |
| Hello, how are you? | English  |
| 你好吗                 | Chinese  |
| comment allez-vous  | French   |

## Requirements

Install the required Python libraries using:

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn
```

## Preprocessing Steps

1. URLs and numbers are removed using regular expressions.
2. Lowercasing is applied to all text except for languages such as Arabic, Urdu, Hindi, and German.
3. Duplicates are removed and the DataFrame index is reset.
4. The text is transformed into numerical features using `TfidfVectorizer`.

## Model Training

Two models are trained and evaluated:

### Decision Tree Classifier

* Criterion: Entropy
* Suitable for interpretability and handling categorical data

### Multinomial Naive Bayes

* Commonly used for text classification
* Performs well with sparse feature sets like TF-IDF vectors

## Evaluation Metrics

The following metrics are used to evaluate the models:

* Accuracy
* Precision (weighted)
* Recall (weighted)
* F1 Score (weighted)

Results are visualized using a Seaborn heatmap for easy comparison.

## Sample Predictions

The following are example predictions using the trained Multinomial Naive Bayes classifier:

```python
predict("你好吗")               # Expected: Chinese
predict("नमस्ते, आप कैसे हैं")   # Expected: Hindi
predict("broo what")           # Expected: English
predict("comment allez-vous")  # Expected: French
predict("兄弟")                 # Expected: Chinese
```

## File Structure

```
.
├── language_recognition.ipynb
├── Language recognition dataset.csv
├── README.md
```

## How to Run

1. Load and clean the dataset.
2. Vectorize text using TF-IDF.
3. Train both models on the training set.
4. Evaluate on the test set using classification metrics.
5. Use the `predict()` function to classify new text samples.

## Author

This project was developed for educational purposes to demonstrate basic language detection using scikit-learn.

---

Would you like this content exported as a `.md` file?
