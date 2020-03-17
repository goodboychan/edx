# Author : Chanseok Kang
# Contents : MIT 15.071x, The Analytics Edge

# Read CSV file
USDA = read.csv('dataset/USDA.csv')

# Describe structure
str(USDA)

# Statistical Summary
summary(USDA)

# Access variable
USDA$Sodium

# To get max value
which.max(USDA$Sodium)

# Columns names in USDA
names(USDA)
USDA$Description[265]

# Create New DataFrame
HighSodium <- subset(USDA, Sodium > 10000)

# number of rows in highSodium
nrow(HighSodium)

HighSodium$Description

# Search Text in DataFrame
match("CAVIAR", USDA$Description)
USDA$Sodium[4154]

# Combined
USDA$Sodium[match("CAVIAR", USDA$Description)]

# Summary of specific dataframe
summary(USDA$Sodium)

# Standard Deviation of Sodium level (Remove NA Values)
sd(USDA$Sodium, na.rm=TRUE)

# Plot 
plot(USDA$Protein, USDA$TotalFat)

# Plot with label modification
plot(USDA$Protein, USDA$TotalFat, xlab='Protein', ylab='Fat', main='Protein vs Fat')

# Histogram
hist(USDA$VitaminC, xlab = 'Vitamin C (mg)', main='Histogram of Vitamin C Levels')

# histogram with xlim
hist(USDA$VitaminC, xlab = 'Vitamin C (mg)', main='Histogram of Vitamin C Levels', xlim=c(0, 100))

# Histogram with breaks
hist(USDA$VitaminC, xlab = 'Vitamin C (mg)', main='Histogram of Vitamin C Levels', xlim=c(0, 100), breaks=100)
hist(USDA$VitaminC, xlab = 'Vitamin C (mg)', main='Histogram of Vitamin C Levels', xlim=c(0, 100), breaks=2000)

# Boxplot
boxplot(USDA$Sugar, main='Boxplot of Sugar Levels', ylab='Sugar (g)')
