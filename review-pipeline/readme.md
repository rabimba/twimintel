# Topic Identification Pipeline for short texts

### Target text corpus:
 - Reviews
 - Customer complaints
 - Call trnscripts

 This directory will contain base implementation of a topic identification model with attention to context. This will be based on _LDA_ probablisitic topic assignment and pretrained sentence embedding from _BERT_ [1]. 

### Motivation for this pipeline

The nature of Twimintel and the diverse dataset twimintel evnatually will process pushes us to the problem of choosing correct type of approcahes. _This branch will deal with different kind of pipelines and alogorithms used in twimintel_.

As we can see [2] different type of text require us to take different approach to get correct topic out of our pipeline. This branch outlines the first draft of it.

## Motivation

Product reviews are important as influencing people's choices especially for online shopping. We usually have dreadfully huge numbers of reviews for whatever products. However, many platforms have barely a satisfying categorization system for the reviews when it comes to what the reviewers are really talking about. Steam, for example, has a very carefully designed system where people can do a lot of things, but still there is no such access to categorizing the reviews by their semantic meanings.

![Steam review logo](./docs/images/steam_review.jpeg)

Therefore, we provide a topic identification procedure thats combines both bag-of-words and contextual information to explore potential __semantically meaningful__ categories out of the oceans of steam reviews.





 [1]: https://arxiv.org/abs/1810.04805
 [2]: https://www.researchgate.net/publication/335339697_A_Detailed_Survey_on_Topic_Modeling_for_Document_and_Short_Text_Data