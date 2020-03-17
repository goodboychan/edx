# works in RStudio
BJamesData <- read.csv(file.choose())
View(BJamesData)

# scatterplot of the data
plot(BJamesData$RunsRatio, BJamesData$WinRatio, main="Runs Ratio vs. Win Ratio")

#adding log(x) versions to our data frame
BJamesData$WinRatio_log <- with(BJamesData, log(WinRatio))
BJamesData$RunRatio_log <- with(BJamesData, log(RunsRatio))

# scatterplot of the data
plot(BJamesData$RunRatio_log, BJamesData$WinRatio_log, main="Log RR vs. Log WR")

#regression with intercept
BJames_exponent1 <-
  lm(BJamesData$WinRatio_log ~ BJamesData$RunRatio_log)
BJames_exponent1

# Coefficients:
#   (Intercept)  BJamesData$RunRatio_log  
# -0.001123                 1.862782  

#regression without intercept
BJames_exponent2 <-
  lm(BJamesData$WinRatio_log ~ BJamesData$RunRatio_log + 0)
BJames_exponent2

# Coefficients:
#   BJamesData$RunRatio_log  
# 1.863