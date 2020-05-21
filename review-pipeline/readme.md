# Topic Identification Pipeline for short texts

### Target text corpus:
 - Reviews
 - Customer complaints
 - Call trnscripts

 This directory will contain base implementation of a topic identification model with attention to context. This will be based on _LDA_ probablisitic topic assignment and pretrained sentence embedding from _BERT_ [1]. 

## Motivation for this pipeline

The nature of Twimintel and the diverse dataset twimintel evnatually will process pushes us to the problem of choosing correct type of approcahes. _This branch will deal with different kind of pipelines and alogorithms used in twimintel_.

As we can see [2] different type of text require us to take different approach to get correct topic out of our pipeline. This branch outlines the first draft of it.

## Motivation

One of the primary data to glean insight from is product reviews. There can be different types of reviews that can include from ecommerce product reviews in sites like amazon.in to digital reviews in steam and also in Zomato.
Most platforms have barely a satisfying categorization system for the reviews when it comes to what the reviewers are really talking about.

This pipeline will provide a topic identification procedure thats combines both bag-of-words and contextual information to explore potential __semantically meaningful__ categories out of the reviews.

## Dataset

#1 :  Steam review dataset for games: https://www.dl.dropboxusercontent.com/s/lp7f9h74ebwnf97/steam_reviews.csv?dl=0

## Architecture 

- Prepare the dataset for consumption using a set of RegEx to normalize the data
- Use EDA to get insight about data distribution and structure
- Implement topic identification models
- Deploy in docker / aws / etc

![Arch](images/datapipe.png)


## Methods

Common methods for topic classification includes using LDA (latent Dirichlet allocation) as a hierarchical Bayesian model.

+ Latent Dirichlet Allocation

+ Embedding + Clustering

For our text we will have the following limitation with LDA
- if the text corpus is small, LDA struggles to find proper topics in short text
- the review texts might noy have similar topic making it hard for LDA to classify them
- LDA is word frequency based. Whereas our reviews are mostly context based. LDA has no way of preserving context

Or we can use sentence embedding models like BERT. BERT will embed the text into a vector space to capture contextual meaning. 

## Our Architecture

We will leverage both bag pf words (LDA) and contextual informtion (BERT). The model looks like below

![Model](images/model.png)

The model leverages both bag-of-words and contextual information by including both the LDA topic probabilities and the sentence embeddings.

Here we 

+ take the information from LDA probabilistic topic assignment (`v_1`) and sentence embeddings (`v_2`)
+ concatenate `\lambda * v_1` and `v_2` to get `v_{full}`
+ learn the latent space representation `v_{latent}` of by autoencoder
+ implement clustering on the latent space representations.

## Result and Evluation

DONE.
Need to write

## Model Deep Dive 

WIP. Need to write

## Future Work

Evaluate if using _Roberta_ produces and impprovement over Bert.

 [1]: https://arxiv.org/abs/1810.04805
 [2]: https://www.researchgate.net/publication/335339697_A_Detailed_Survey_on_Topic_Modeling_for_Document_and_Short_Text_Data