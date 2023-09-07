# Hateful Speech Detection using BERT

A ML project that uses Huggingface's BERT model to classify sentences as being hateful or not.

## Project Description

Online safeguards against hate speech are limited and falling behind communities that bully and produce hateful content online. Through the use of code words and insinuations, hateful commenters are evading platforms' content barriers with increasing ease. This approach therefore seeks to cast a wider net to detect comments linked to hateful topics instead of laser targetting hate speech comments themselves.

## Features
- Uses BERT from Huggingface's Transformers library
- Uses Tensorflow
- Works as a binary classifier

## Data

This project uses data taken from the reddit dumps, trimmed to 1000 lines of text. For this particular project two known hateful subreddits were chosen to obtain hateful speech comments, and one known moderated "pacificst" subreddit was chosen to obtain regular sentences.

Each line contains represents the text content of a distinct post.

## Limitations and Improvements

This method is limited in various ways.
- The model relies on the creator's preconceptions of what is hateful speech or not.
- The model casts a wide net, and flags comments that are not directly hatespeech, but are linked to hateful topics and chats. I expect the model to produce a lot of qualitative false positives, since not every single comment in hateful subreddits is necessarily hateful or hate speech and we must expect some comments from the non hate speech dataset to be hateful or contain hate speech.
- There are ethical implications of this type of content filtering, since the model targets patterns of speech common within a certain online community rather than labelled hate speech, it will be inaccurate and require more stringent human oversight than supervised approaches. This may be improved upon by fine tuning on labelled datasets.
- Future versions of this model, may include a multi class classifier to determine varying levels of hatefulness.

### Notes

This is a cleaner version of a previous implementation, check out https://github.com/nik-hz/nlp_reddit_hate_speech for more util scripts and a Git Large File link to the datasets.
