WPct_estimators =read.csv("win_estimators.csv")
summary(WPct_estimators)

plot(WPct_estimators$WPct, WPct_estimators$Soolman_WPct)
plot(WPct_estimators$WPct, WPct_estimators$Soolman_WPct, xlab="winning percentage", 
     ylab = "Soolman Winning percentage", pch=23, col='red')

head(WPct_estimators)
tail(WPct_estimators)

#estimators = WPct_estimators[c("WPct", "Cook_WPct", "Soolman_WPct", "Kross_WPct",
#                               "Smyth_WPct", "BJames_Pythag_WPct", "BJames_Pythag_WPctII")]
estimators <- win_estimators[c('RperG', 'RAperG', 'WPct','Cook_WPct',  'Soolman_WPct',  'Kross_WPct', 'Smyth_WPct', 'BJames_Pythag_WPct', 'BJames_Pythag_WPctII')]

splom(estimators, xlab="win_estimators")

wpct_95th_pct = quantile(estimators$WPct, .95)
top_winners = estimators[estimators$WPct >= wpct_95th_pct,]
summary(top_winners)
mean(top_winners$WPct)
sd(top_winners$WPct)
splom(top_winners, xlab= "Top 5th percentile WPct")

wpct_5th_pct = quantile(estimators$WPct, .05)
worst_winners = estimators[estimators$WPct <= wpct_5th_pct, ]
summary(worst_winners)
mean(worst_winners$WPct)
sd(worst_winners$WPct)
splom(worst_winners, xlab="Bottm 5th percentile WPct")

estimators_1960s = WPct_estimators[WPct_estimators$yearID >= 1960 & WPct_estimators$yearID < 1970,]
summary(estimators_1960s)

estimators_2000s = WPct_estimators[WPct_estimators$yearID >= 2000 & WPct_estimators$yearID < 2010,]
