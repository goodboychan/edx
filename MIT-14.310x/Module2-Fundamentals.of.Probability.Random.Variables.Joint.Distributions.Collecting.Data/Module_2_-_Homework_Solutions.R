rm(list = ls())

#rbinom(n, size, prob)
#where n refers to number of observations, size refers to number of trials, 
#and prob refers to probability of success on each trial
successes<-rbinom(1000, 8, 0.2)

#Question 9&10
hist(successes)

#Question 12
#probability of getting exactly 7 heads on 10 flips
#dbinom(x, size, prob, log = FALSE)
#pbinom(q, size, prob, lower.tail = TRUE, log.p = FALSE)
#Part A
dbinom(7,10,0.65)
#Part B
pbinom(7,10,0.65)
#Part C
1-pbinom(5,10,0.65)

#Question 14
binom_draws <- as_tibble(data.frame(successes))

estimated_pf <- binom_draws %>%
  group_by(successes) %>%
  summarize(n=n()) %>%
  mutate(freq=n/sum(n))

ggplot(estimated_pf, aes(x=successes, y=freq)) +
  geom_col() +
  ylab("Estimated Density")

#Question 15
#Create a tibble with x and the analytical probability densities.
my_binom<-as_tibble(list(x=0:n, prob=dbinom(0:n, n, p)))

#Plot the computed theoretical density.
ggplot(my_binom, aes(x=x, y=prob)) + geom_col() +
  ylab("Analytical Density")

calculated_cdf <- my_binom %>%
  mutate(cdf=cumsum(prob))

#Plot the computed cdf
ggplot(calculated_cdf, aes(x=x, y=cdf)) + geom_step() + 
  ylab("CDF")