# Read Data
wine = read.csv('dataset/wine.csv')

# Structure of Data
str(wine)

# Summary of Data
summary(wine)

# Build one-variable linear regression model
model1 = lm(Price ~ AGST, data=wine)
summary(model1)

# SSE
model1$residuals
SSE = sum(model1$residuals^2)
SSE

# Build another lm model
model2 = lm(Price ~ AGST + HarvestRain, data=wine)
summary(model2)

# SSE
SSE = sum(model2$residuals^2)
SSE

# Build all linear model
model3 = lm(Price ~ AGST + HarvestRain + WinterRain + Age + FrancePop, data=wine)
summary(model3)

# SSE
SSE = sum(model3$residuals^2)
SSE

# For the question
modelq = lm(Price ~ HarvestRain + WinterRain, data=wine)
summary(modelq)

# Build model based on signif. Code of variable
model4 = lm(Price ~ AGST + HarvestRain + WinterRain + Age, data=wine)
summary(model4)

# For the question
modelq1 = lm(Price ~ HarvestRain + WinterRain, data=wine)
summary(modelq1)

# Correlation
cor(wine$WinterRain, wine$Price)
cor(wine$Age, wine$FrancePop)
cor(wine)

# New Model
model5 = lm(Price ~ AGST + HarvestRain + WinterRain, data=wine)
summary(model5)

# For the question
cor(wine$HarvestRain, wine$WinterRain)

# Data for test
wineTest = read.csv('dataset/wine_test.csv')
str(wineTest)

# Prediction
predictTest = predict(model4, newdata=wineTest)
predictTest

# SSE
SSE = sum((wineTest$Price - predictTest)^2)
# SST
SST = sum((wineTest$Price - mean(wine$Price))^2)

# R^2
1 - SSE/SST
