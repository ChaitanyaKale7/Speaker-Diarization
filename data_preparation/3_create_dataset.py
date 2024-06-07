from datasets import Dataset

import pandas as pd

from datasets import Audio

import gc

## we will load the both of the data here.

train_df = pd.read_csv('modified_train.csv')

test_df = pd.read_csv('modified_test.csv')

## we will rename the columns as “audio”, “sentence”.

train_df.columns = ['audio', 'sentence']

test_df.columns = ['audio', 'sentence']

#Now we will create the dataset using the class methods Dataset.from_pandas() and cast the audio to an Audio datatype. For example:

train_dataset = Dataset.from_pandas(train_df)

test_dataset = Dataset.from_pandas(test_df)

#We will create arrays of each audio file and append those values as a column in the above datasets. To do this we will use the cast_column function from Dataset. We will also use sampling_rate as an argument so if there is any file we missed in preprocessing step.

train_dataset = train_dataset.cast_column('audio', Audio(sampling_rate=16000))

test_dataset = test_dataset.cast_column('audio', Audio(sampling_rate=16000))























