from Pbo import NLP
from sklearn.model_selection import KFold
import numpy as np
import tensorflow as tf

class Train():
    def train(nlp = NLP()):

        # membaca dataset dan menamilkan 5 teratas dataset
        data_training = nlp.read_excel("DataMix.xlsx")
        data_training.head()
        data_training.info()
        data_training.LabelTeks.value_counts()

        x = data_training['text'].values
        y = data_training['LabelTeks'].values

        nlp.add_to_vocab(x)

        x = nlp.pra_process(x)
        x = nlp.add_padding(x)
        print('shape of data tensor:', x.shape)
        print('shape of data tensor:', x)

        y = nlp.convert_string_to_label(y)
        print('Shape of label tensor :', y.shape)

        # Define per-fold score containers
        acc_per_fold = []
        loss_per_fold = []

        kfold = KFold(n_splits=10, random_state=7, shuffle=True)

        fold_no = 1
        for train, val in kfold.split(x, y):
            # arsitektur model dan melatih data train menjadi model
            model = nlp.generate_model()
            # model.summary()

            checkpoint = tf.keras.callbacks.ModelCheckpoint('model_'+str(fold_no)+'.h5',
                                                            monitor='val_accuracy', verbose=1,
                                                            save_best_only=True, mode='max')
            callback_list = [checkpoint]
            # Generate a print
            print('------------------------------------------------------------------------')
            print(f'Training for fold {fold_no} ...')
            history = nlp.training(model, x[train], y[train], x[val], y[val], callback_list)

            model.load_weights('model_'+str(fold_no)+'.h5')
            # Generate generalization metrics
            scores = nlp.evaluate(model, x[val], y[val])
            print(f'Score for fold {fold_no}: {model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1] * 100}%')
            acc_per_fold.append(scores[1] * 100)
            loss_per_fold.append(scores[0])


            # Increase fold number
            fold_no = fold_no + 1

        # == Provide average scores ==
        print('------------------------------------------------------------------------')
        print('Score per fold')
        for i in range(0, len(acc_per_fold)):
          print('------------------------------------------------------------------------')
          print(f'> Fold {i+1} - Loss: {loss_per_fold[i]} - Accuracy: {acc_per_fold[i]}%')
        print('------------------------------------------------------------------------')
        print('Average scores for all folds:')
        print(f'> Accuracy: {np.mean(acc_per_fold)} (+- {np.std(acc_per_fold)})')
        print(f'> Loss: {np.mean(loss_per_fold)}')
        print('------------------------------------------------------------------------')

Train.train(NLP())