from pymorphy3 import MorphAnalyzer
import pandas as pd


morph = MorphAnalyzer()
df = pd.read_csv('./word_forms/word_forms.tsv', sep='\t')

df = df[df.Number >= 1000]
df['tags'] = df['1gram'].apply(lambda x: morph.parse(str(x))[0].tag)

input_words = input('input ur sentence: ').split()

output_string = ''
for word in input_words:
    tags = morph.parse(word)[0].tag

    if 'PREP' in tags or 'CONJ' in tags or 'PRCL' in tags:
        output_string += word + ' '
        continue

    output_string += df[
        (df.tags == tags) &
        (df['1gram'] != word.lower())
    ]['1gram'].iloc[0] + ' '

print(output_string[:-1])
