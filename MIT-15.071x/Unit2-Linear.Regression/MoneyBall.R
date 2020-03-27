# Read Data
baseball = read.csv('./dataset/baseball.csv')

# Structure of Data
str(baseball)

# Subset the data
moneyball = subset(baseball, Year < 2002)
str(moneyball)

# Create new variable to show difference between RS and RA
moneyball$RD = moneyball$RS - moneyball$RA
str(moneyball)

# Visualize linear relationship
plot(moneyball$RD, moneyball$W)

# Create lm model
WinsReg = lm(W ~ RD, data=moneyball)
summary(WinsReg)

# for the question
(713 - 614)*0.105766 + 80.881375

RunsReg = lm(RS ~ OBP + SLG + BA, data=moneyball)
summary(RunsReg)

# To reduce multi-collinearity, remove BA
RunsReg = lm(RS ~ OBP + SLG, data=moneyball)
summary(RunsReg)

RunaReg = lm(RA ~ OOBP + OSLG, data=moneyball)
summary(RunaReg)

# For the question 1
-804.63 + 2737.77 * 0.311 + 1584.91 * 0.405

# For the question 2
-837.38 + 2913.60 * 0.297 + 1514.29 * 0.370