load('wordCount.mat')
%testing
columnSum = sum(M,1);
lineSum = sum(M,2);

normA = repmat(columnSum, [size(M,1) 1]); 

normData = M./normA;
normData(isnan(normData)) = 0 ;


sizes = size(normData);
bigMat = (normData> 0.5);
nBigInCol = sum(bigMat);
BigcolIdx = nBigInCol ~= 1; 

matFixed = M(:, BigcolIdx);

normB = repmat(lineSum, [1 size(matFixed,2)]); 

normData2 = matFixed./normB;
normData2(isnan(matFixed)) = 0 ;

%CLEANING

[COEFF,SCORE] = princomp(normData2);

nPC = 2;
IDX = kmeans(SCORE(:,1:5), 5);
scatter3(SCORE(:,1),SCORE(:,2),SCORE(:,3),20,IDX, 'filled');

save 'matlabData'