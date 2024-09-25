from ML.TextPreprocessing import preprocess, text_to_sequence
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


model = load_model('A:\\Users\Artem\PycharmProjects\kafkaTest\ML\\best_LSTM_V4_model.keras')  # model_telecom_84_per_cent.keras
classes = {1: "positive", 0: "negative"}


def pipeline(text):
    preprocessed_text = preprocess(text)
    print(preprocessed_text)
    sequence = text_to_sequence(preprocessed_text)
    print(sequence)
    vectorized_text = pad_sequences([sequence], maxlen=200)
    print(vectorized_text)
    prediction = model.predict(vectorized_text)
    print(prediction)
    result = {'label': classes[round((prediction[0][0]))], 'score': prediction[0][0]}
    return result

