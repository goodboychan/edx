rm(list=ls())
library("utils")
library("tidyverse")
library(stringr)
# Set your own working directory here
setwd("/Users/elizabethcao/Downloads/Gender_Stats_csv")
# Question 1
gender_data<-as_tibble(read.csv("Gender_StatsData.csv"))
# Question 2
#You can do this by inspection.
head(gender_data)
# Question 3
teenager_fr<-filter(gender_data,Indicator.Code=="SP.ADO.TFRT")
# Question 4
rm(gender_data)
# Question 6
round(mean(teenager_fr$X1960, na.rm = TRUE),2)
round(sd(teenager_fr$X1960, na.rm = TRUE),2)
# Question 7
round(mean(teenager_fr$X2000, na.rm = TRUE),2)
round(sd(teenager_fr$X2000, na.rm = TRUE),2)
# Question 9
byincomelevel<- filter(teenager_fr,Country.Code%in%c("LIC","MIC","HIC","WLD"))
# Question 10
plotdata_bygroupyear<-gather(byincomelevel,Year,FertilityRate,X1960:X2015) %>%
  select(Year, Country.Name,Country.Code, FertilityRate)
# Question 11
plotdata_byyear<-select(plotdata_bygroupyear,Country.Code,Year,FertilityRate)%>%
  spread(Country.Code,FertilityRate)
# Question 12
#Let's enter the code as if this statement were TRUE
plotdata_bygroupyear<-gather(byincomelevel,Year,FertilityRate,X1960:X2015) %>%
  select(Year, Country.Name,Country.Code, FertilityRate) #from Question 10
plotdata_byyear<-spread(plotdata_bygroupyear,Country.Code,FertilityRate)
#Let's enter the code as if this statement were FALSE
plotdata_bygroupyear<-gather(byincomelevel,Year,FertilityRate,X1960:X2015) %>%
  select(Year, Country.Name,Country.Code, FertilityRate)
plotdata_byyear<-select(plotdata_bygroupyear,Country.Code,Year,FertilityRate)%>%
  spread(Country.Code,FertilityRate)
#We see from this that the answer to Question 12 is FALSE: using select() is not redundant
# Question 13
ggplot (plotdata_bygroupyear, aes(x=Year,y=FertilityRate, group=Country.Code,colour=Country.Code)) +
  geom_line(  )+
  labs(title='Fertility Rate by Country-Income-Level over Time')
plotdata_bygroupyear<-mutate(plotdata_bygroupyear,Year=as.numeric(str_sub(Year,-4)))

#Question 18
histdata_twoyears <- select(teenager_fr, Country.Name, Country.Code, Indicator.Name, Indicator.Code, X1960,X2000)

histdata_twoyears <- gather(teenager_fr, Year, FertilityRate, X1960, X2000) %>%
  select(Year, Country.Name, Country.Code, FertilityRate)

histdata_twoyears <- filter(histdata_twoyears,!is.na(FertilityRate))

ggplot(histdata_twoyears, aes(x=FertilityRate)) + 
  geom_histogram(data=subset(histdata_twoyears, Year=="X1960"), 
                 color="darkred", fill="red", alpha=0.2) + 
  geom_histogram(data=subset(histdata_twoyears, Year=="X2000"), 
                 color="darkblue", fill="blue", alpha=0.2) 
ggsave("hist.png")

#Question 20
ggplot(histdata_twoyears, aes(x=FertilityRate, group=Year, color=Year, alpha=0.2)) +        geom_histogram(aes(y=..density..)) +
  geom_density(data=subset(histdata_twoyears, Year=="X1960"), color="darkred", fill="red", alpha=0.2, bw=5)+ 
  geom_density(data=subset(histdata_twoyears, Year=="X2000"), color="darkblue", fill="blue", alpha=0.2, bw=5)

#Part 2
#Question 2
rm(list=ls())
library("utils")
#install.packages('plot3D')
library(plot3D)
setwd()

#Creating the vector x and y
M <- mesh(seq(0,1,length=100), seq(0,1,length=100))
x<-M$x
y<-M$y
z<-6/5*(M$x+M$y^2)

#Plotting this pdf
persp3D(x, y, z, xlab='X variable', ylab= 'Y variable', xlim = c(0,1), main= "Plotting joint pdf')")

#Question 11
#Calculating cdf
x <- seq(0, 1, length=1000)
y <- seq(0, 1, length=1000)
cdfy <- 6/5 * (1/2*y+y^3/3)
cdfx <- 6/5*(1/3*x+x^2/2)

#Plotting cdf
pdf("cumulative.pdf")
plot(x, cdfx, type = "l", col="blue", xlab=" ", ylab = "Cumulative Probability", xlim=c(0,1), main="CDF plot")
lines(y, cdfy, lty=2, col="red", lwd=2)
legend("bottomright", ncol=1, legend = c("X", "Y"), lty=c(1,2), col=c("blue", "red"))
dev.off