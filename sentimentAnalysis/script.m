clc
clear


%% open votes file 
votes_set = csvread('votes.csv');

% add +1 to up and down votes
votes_set = votes_set + 1;


%% open text file
text_id = fopen('features.csv');
text_set = textscan(text_id, '%s');

%% variable to be predicted -> UP/DOWN ratio

%% try at least one statistical method
% K-nearest-neighbour (KNN) classifier
% compare article with all the others
% K is the number of top related articles
% prediction is the average of ratio of the K articles

%%
% As a baseline to compare with you can use e.g. the average of 
% the vote ratio over the collection