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
