# ID3 algorithm

The following code is used for finding the most important node(attribute) for a given dataset, using entorpy average information and information gain

## formula for entropy :

![entropyformula](https://user-images.githubusercontent.com/76522728/209316854-c37c0772-4b2d-4dd7-9ddd-5b03a57e1063.jpg)

## formula for information gain :
![inforgainform](https://user-images.githubusercontent.com/76522728/209316943-cbbb5967-a742-4bf7-8368-7ae7934b9f83.jpg)


the attribute with the most information gain will be selected as the next node

Once the node has been it selected it will act as the data set for selecting the next attribute and the process goes on until the tree is complete 
